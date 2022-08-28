from mlflow.tracking import MlflowClient

if __name__ == "__main__":
    client = MlflowClient()
    experiment_name = "experiment_2"
    client.create_experiment(name=experiment_name)

