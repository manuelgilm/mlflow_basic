import os
from random import random, randint
import mlflow

if __name__ == "__main__":
    # Log an artifact (output file)
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")
    mlflow.log_artifacts("outputs")