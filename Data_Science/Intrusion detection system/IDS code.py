#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.decomposition import PCA
import joblib
import shap
import xgboost as xgb
from sklearn.metrics import accuracy_score


# In[2]:


df = pd.read_csv(r"D:\IDS system\IDS dataset\02-14-2018.csv\02-14-2018.csv")


# In[3]:


df.head()


# In[4]:


df["Label"].value_counts()


# In[5]:


df.shape


# In[6]:


df.isna().sum()


# In[7]:


df.info()


# In[8]:


df.columns


# ## Handling categorical values

# In[9]:


# Assuming 'df' is your DataFrame and 'category_column' is a categorical column
label_encoder = LabelEncoder()
df['Label'] = label_encoder.fit_transform(df['Label'])


# In[10]:


# Convert the 'Timestamp' column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d/%m/%Y %H:%M:%S')

# Extract year, month, day, hour, minute, and second into separate columns
df['Year'] = df['Timestamp'].dt.year
df['Month'] = df['Timestamp'].dt.month
df['Day'] = df['Timestamp'].dt.day
df['Hour'] = df['Timestamp'].dt.hour
df['Minute'] = df['Timestamp'].dt.minute
df['Second'] = df['Timestamp'].dt.second


# In[11]:


df.drop(["Timestamp"],axis=1,inplace=True)


# ## Handling infinite values

# In[12]:


# Step 1: Check for infinite values
print("Checking for infinite values...")
print(df.isin([np.inf, -np.inf]).sum())


# In[13]:


# Step 2: Replace infinite values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)


# In[14]:


# Option 1: Drop rows with NaN values
df.dropna(inplace=True)


# ## Feature reduction

# In[15]:


df.head()


# ## Feature reduction

# In[16]:


# Define the features (X) and target variable (y)
X = df.drop(columns=['Label'])
y = df['Label']


# In[17]:


# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[18]:


# Apply PCA for dimensionality reduction
pca = PCA(n_components=0.95)  # Preserve 95% variance, or set a fixed number of components like n_components=30
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)


# In[19]:


# Train a model (RandomForestClassifier in this case)
model = RandomForestClassifier(random_state=42)  # Added random_state for reproducibility
model.fit(X_train_pca, y_train)


# In[20]:


y_pred = model.predict(X_test_pca)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")


# In[ ]:




