import os
from random import random, randint
import mlflow

if __name__ == "__main__":
    # Log a parameter (key-value pair)
    mlflow.log_param("param1", randint(0, 100))
