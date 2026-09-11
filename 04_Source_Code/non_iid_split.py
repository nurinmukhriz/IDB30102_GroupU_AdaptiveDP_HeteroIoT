import numpy as np


# Step 1: Shuffle the dataset
def shuffle_data(data):
    return data.sample(frac=1, random_state=42)


# Step 2: Split data among IoT clients
def create_non_iid_clients(data, num_clients=4):
    shuffled_data = shuffle_data(data)

    client_data = np.array_split(
        shuffled_data,
        num_clients
    )

    return client_data


# Step 3: Display client data distribution
def show_client_distribution(client_data):
    for i, client in enumerate(client_data):
        print(f"Client {i + 1}: {len(client)} samples")
