from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
import warnings
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")
np.random.seed(42)
data = pd.read_csv("static/marketing_campaign.csv", sep="\t")

app = Flask(__name__)
data = data.dropna()
data["Dt_Customer"] = pd.to_datetime(data["Dt_Customer"],format='%d-%m-%Y')
dates = []
for i in data["Dt_Customer"]:
    i = i.date()
    dates.append(i)  
days = []
d1 = max(dates) #taking it to be the newest customer
for i in dates:
    delta = d1 - i
    days.append(delta)
data["Customer_For"] = days
data["Customer_For"] = pd.to_numeric(data["Customer_For"], errors="coerce")
#Feature Engineering
#Age of customer today 
data["Age"] = 2021-data["Year_Birth"]

#Total spendings on various items
data["Spent"] = data["MntWines"]+ data["MntFruits"]+ data["MntMeatProducts"]+ data["MntFishProducts"]+ data["MntSweetProducts"]+ data["MntGoldProds"]

#Deriving living situation by marital status"Alone"
data["Living_With"]=data["Marital_Status"].replace({"Married":"Partner", "Together":"Partner", "Absurd":"Alone", "Widow":"Alone", "YOLO":"Alone", "Divorced":"Alone", "Single":"Alone",})

#Feature indicating total children living in the household
data["Children"]=data["Kidhome"]+data["Teenhome"]

#Feature for total members in the householde
data["Family_Size"] = data["Living_With"].replace({"Alone": 1, "Partner":2})+ data["Children"]

#Feature pertaining parenthood
data["Is_Parent"] = np.where(data.Children> 0, 1, 0)

#Segmenting education levels in three groups
data["Education"]=data["Education"].replace({"Basic":"Undergraduate","2n Cycle":"Undergraduate", "Graduation":"Graduate", "Master":"Postgraduate", "PhD":"Postgraduate"})

#For clarity
data=data.rename(columns={"MntWines": "Wines","MntFruits":"Fruits","MntMeatProducts":"Meat","MntFishProducts":"Fish","MntSweetProducts":"Sweets","MntGoldProds":"Gold"})

#Dropping some of the redundant features
to_drop = ["Marital_Status", "Dt_Customer", "Z_CostContact", "Z_Revenue", "Year_Birth", "ID"]
data = data.drop(to_drop, axis=1)
data = data[(data["Age"]<90)]
data = data[(data["Income"]<600000)]
corrmat= data.corr(numeric_only=True)
s = (data.dtypes == 'object')
object_cols = list(s[s].index)
LE=LabelEncoder()
for i in object_cols:
    data[i]=data[[i]].apply(LE.fit_transform)
ds = data.copy()
# creating a subset of dataframe by dropping the features on deals accepted and promotions
cols_del = ['AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1','AcceptedCmp2', 'Complain', 'Response']
ds = ds.drop(cols_del, axis=1)
#Scaling
scaler = StandardScaler()
scaler.fit(ds)
scaled_ds = pd.DataFrame(scaler.transform(ds),columns= ds.columns )
pca = PCA(n_components=3)
pca.fit(scaled_ds)
PCA_ds = pd.DataFrame(pca.transform(scaled_ds), columns=(["col1","col2", "col3"]))
from sklearn.decomposition import PCA

# Set number of components to retain 90% of variance
pca = PCA(n_components=0.90)  # Retains enough components to explain 90% of the variance
pca.fit(scaled_ds)
PCA_ds = pd.DataFrame(pca.transform(scaled_ds))
AC = AgglomerativeClustering(n_clusters=4)
# fit model and predict clusters 
yhat_AC = AC.fit_predict(PCA_ds)
PCA_ds["Clusters"] = yhat_AC
#Adding the Clusters feature to the orignal dataframe.
data["Clusters"]= yhat_AC
data["Total_Promos"] = data["AcceptedCmp1"]+ data["AcceptedCmp2"]+ data["AcceptedCmp3"]+ data["AcceptedCmp4"]+ data["AcceptedCmp5"]
Personal = [ "Kidhome","Teenhome","Customer_For", "Age", "Children", "Family_Size", "Is_Parent", "Education","Living_With"]
# Cluster properties on the unscaled data
cluster_unscaled_centers = data.groupby("Clusters").mean()
# Cluster properties on the unscaled data
cluster_unscaled_centers = data.groupby("Clusters").mean()
# Function to name clusters based on data insights
def name_clusters(cluster_centers_unscaled):
    cluster_names = []
    cnt=0
    
    for i, row in cluster_centers_unscaled.iterrows():
        cluster_names.append([])
        if row['Spent'] > 600 and row['Income'] > 5000:
            cluster_names[cnt].append("High-Spender, Wealthy")
        if row['Spent'] < 500 and row['Income'] < 30000:
            cluster_names[cnt].append(" Low-Spender, Low-Income")
        if row['Is_Parent'] > 0.5 and row['Family_Size'] > 3:
            cluster_names[cnt].append(" Family_Oriented, Moderate Spender")
        if row['Is_Parent']>0.9 :
            cluster_names[cnt].append(" Has Many Chidren")
        
        
        cnt+=1
    
    return cluster_names

# Name clusters based on their representative points (unscaled data)
cluster_names = name_clusters(cluster_unscaled_centers)
# Define all required features
all_features = ['Education', 'Income', 'Kidhome', 'Teenhome', 'Recency', 'Wines', 'Fruits', 'Meat',
                'Fish', 'Sweets', 'Gold', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
                'NumStorePurchases', 'NumWebVisitsMonth', 'Customer_For', 'Age', 'Spent', 'Living_With',
                'Children', 'Family_Size', 'Is_Parent']

from sklearn.neighbors import NearestCentroid

def classify_new_customer(new_data, clustering_model, scaler, scaled_ds):
    # Fit the NearestCentroid classifier on the scaled data and clusters
    nc = NearestCentroid()
    nc.fit(scaled_ds, clustering_model.labels_)
    
    # Scale the new data with the same scaler used previously
    new_data_scaled = scaler.transform(new_data)
    
    # Predict the cluster for the new customer
    cluster = nc.predict(new_data_scaled)
    return cluster



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    # Redirect to result route with all query parameters from the form
    return redirect(url_for('result', **request.args))


@app.route('/result')
def result():
    # List of all expected features
    all_features = [
        'Education', 'Income', 'Kidhome', 'Teenhome', 'Recency', 'Wines', 'Fruits',
        'Meat', 'Fish', 'Sweets', 'Gold', 'NumDealsPurchases', 'NumWebPurchases',
        'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth', 'Customer_For',
        'Age', 'Spent', 'Living_With', 'Children', 'Family_Size', 'Is_Parent'
    ]
    
    # Retrieve and convert query parameters dynamically
    customer_data = {feature: int(request.args.get(feature, 0)) for feature in all_features}
    customer_segmentation = {
    "Group 1": {
        "description": "Definitely a parent, max 4 family members, at least 2. Many are single parents with teenagers at home, relatively older.",
        "characteristics": {
            "parent_status": "definitely a parent",
            "max_family_members": 4,
            "min_family_members": 2,
            "common_age": "older",
            "notable_traits": ["single parents", "teenagers at home"]
        }
    },
    "Group 2": {
        "description": "Definitely not a parent, max 2 family members, mostly couples, high income group, spans all ages.",
        "characteristics": {
            "parent_status": "definitely not a parent",
            "max_family_members": 2,
            "common_age": "all ages",
            "income": "high",
            "notable_traits": ["mostly couples"]
        }
    },
    "Group 3": {
        "description": "Majority are parents, max 3 family members, mostly one kid, typically not teenagers, relatively younger.",
        "characteristics": {
            "parent_status": "mostly parents",
            "max_family_members": 3,
            "common_age": "younger",
            "notable_traits": ["mostly one kid", "not teenagers"]
        }
    },
    "Group 4": {
        "description": "Definitely a parent, max 5 family members, at least 2, many have teenagers at home, relatively older, lower income group.",
        "characteristics": {
            "parent_status": "definitely a parent",
            "max_family_members": 5,
            "min_family_members": 2,
            "common_age": "older",
            "income": "low",
            "notable_traits": ["many have teenagers"]
        }
    }
}
    # Convert the dictionary into a Pandas DataFrame
    new_customer = pd.DataFrame([customer_data])

    # Call the classification function to classify the new customer
    new_customer_cluster = classify_new_customer(new_customer, AC, scaler, scaled_ds)

     # Get the cluster number
    cluster_number = new_customer_cluster[0]

    # Access the description and characteristics from the segmentation dictionary
    group_name = f"Group {cluster_number}"  # Adjust for 0-indexed to 1-indexed
    group_info = customer_segmentation[group_name]

    # Render the result page with the predicted cluster and its details
    return render_template('result.html', 
                           cluster_number=cluster_number + 1,
                           description=group_info['description'], 
                           characteristics=group_info['characteristics'])

@app.route('/visual')
def visualization_page():
    return render_template('visual.html')

if __name__ == '__main__':
    app.run(debug=True)

