from mlflow.tracking import MlflowClient

if __name__ == "__main__":
    client = MlflowClient()
    experiment_name = "experiment_2"
    #get experiment
    experiment = client.get_experiment_by_name(experiment_name)
    #get experiment id from experiment
    experiment_id = experiment.experiment_id
    #delete experiment
    client.delete_experiment(experiment_id=experiment_id)

