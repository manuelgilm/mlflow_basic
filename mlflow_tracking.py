from random import randint
from mlflow.tracking import MlflowClient
import mlflow

if __name__ == "__main__":
    client = MlflowClient()
    experiment_name = "Default"
    #get experiment
    experiment = client.get_experiment_by_name(experiment_name)
    #get experiment id from experiment
    experiment_id = experiment.experiment_id
    with mlflow.start_run(experiment_id=experiment_id) as run:

        mlflow.log_param("param1",randint(0,100))
        mlflow.log_param("param2",randint(0,100))
        mlflow.log_param("param3",randint(0,100))
        mlflow.log_param("param4",randint(0,100))
