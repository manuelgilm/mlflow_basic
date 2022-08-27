import os
from random import random, randint
import mlflow

if __name__ == "__main__":
    # Log different metrics (key-value pair)
    mlflow.log_metric("metric_1", randint(0, 100))
    mlflow.log_metric("metric_2", randint(0, 100))
    mlflow.log_metric("metric_3", randint(0, 100))
    mlflow.log_metric("metric_4", randint(0, 100))
