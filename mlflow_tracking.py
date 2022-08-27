import os
from random import random, randint
import mlflow

if __name__ == "__main__":
    # Log a metric (key-value pair)
    mlflow.log_metric("metric_1", randint(0, 100))
