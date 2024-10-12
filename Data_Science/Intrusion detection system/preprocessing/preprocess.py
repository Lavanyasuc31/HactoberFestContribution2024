import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(df):

    # Handle missing values
    missing_columns = ['Protocol', 'Timestamp', 'Fwd URG Flags', 'Bwd Header Len', 'ECE Flag Cnt', 'Subflow Bwd Byts', 'Init Fwd Win Byts', 'Fwd Act Data Pkts', 'Fwd Seg Size Min', 'Active Max']
    
    columns_to_drop = [col for col in missing_columns if col in df.columns]
    if columns_to_drop:
        df = df.drop(columns_to_drop, axis=1)

    # Handle infinite values
    df = df.replace([float('inf'), -float('inf')], pd.NA).dropna()

    # # If 'Label' exists, drop it (as it is the target to be predicted)
    # if 'Label' in df.columns:
    #     df = df.drop('Label', axis=1)

    # Normalize numerical features
    scaler = StandardScaler()
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    # Handle categorical values
    le = LabelEncoder()
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        df[col] = le.fit_transform(df[col].astype(str))

    return df
