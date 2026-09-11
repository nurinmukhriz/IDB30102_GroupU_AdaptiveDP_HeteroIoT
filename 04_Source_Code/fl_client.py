import flwr as fl


class IoTClient(fl.client.NumPyClient):

    def get_parameters(self, config):
        return []

    def fit(self, parameters, config):
        # Local model training will be implemented here.
        return parameters, 1, {}

    def evaluate(self, parameters, config):
        # Model evaluation will be implemented here.
        return 0.0, 1, {}
