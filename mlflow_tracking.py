import os
from random import random, randint
import mlflow

if __name__ == "__main__":
    # Log a parameter (key-value pair)
    mlflow.log_params({
        "param1": randint(0, 100),
        "param2": randint(0, 100),
        "param3": randint(0, 100),
        "param4": randint(0, 100),
    })
