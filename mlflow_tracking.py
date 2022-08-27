import os
from random import random, randint
import mlflow

if __name__ == "__main__":
    # Log a parameter (key-value pair)
    mlflow.log_param("param1", randint(0, 100))
    mlflow.log_param("param2", randint(0, 100))
    mlflow.log_param("param3", randint(0, 100))
    mlflow.log_param("param4", randint(0, 100))
