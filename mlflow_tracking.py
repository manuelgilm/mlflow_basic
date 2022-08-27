import os
from random import random, randint
import mlflow

if __name__ == "__main__":
    # Log an artifact (output file)
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")
    with open("outputs/test1.txt", "w") as f:
        f.write("hello world from test 1!")
    with open("outputs/test2.txt", "w") as f:
        f.write("hello world from test 2!")                
    mlflow.log_artifacts("outputs")