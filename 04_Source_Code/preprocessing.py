import pandas as pd
from sklearn.preprocessing import StandardScaler


# Step 1: Load dataset
def load_dataset(file_path):
    data = pd.read_csv(file_path)
    return data


# Step 2: Remove duplicate and missing data
def preprocess_data(data):
    data = data.drop_duplicates()
    data = data.dropna()
    return data


# Step 3: Scale numerical features
def scale_features(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)
