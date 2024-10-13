import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from preprocessing.preprocess import preprocess_data
from utils.helpers import rename_columns, change_order_rows

def train_model():
    # Load and preprocess the data
    df = pd.read_csv(r"D:\Intrusion detection system\IDS dataset\02-14-2018.csv\02-14-2018.csv")
    df = preprocess_data(df)

    # Split features and target
    X = df.drop('Label', axis=1)
    y = df['Label']

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")

    # Save the model
    joblib.dump(model, 'model/model.joblib')

if __name__ == "__main__":
    train_model()