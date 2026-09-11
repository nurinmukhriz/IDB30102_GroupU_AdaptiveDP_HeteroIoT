import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_dataset(file_path):
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    data = data.drop_duplicates()
    data = data.dropna()
    return data


def scale_features(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)
