import numpy as np


def create_non_iid_clients(data, num_clients=4):
    shuffled_data = data.sample(frac=1, random_state=42)
    client_data = np.array_split(shuffled_data, num_clients)
    return client_data
