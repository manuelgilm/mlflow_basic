import os
from random import random, randint
import mlflow
from mlflow.models import infer_signature
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier

import pandas as pd

if __name__ == "__main__":
    # make fake classification data
    X, y = make_classification(n_classes=2)
    X = pd.DataFrame(X, columns=[f"feature_{n+1}" for n in range(20)])
    y = pd.DataFrame(y, columns=["label"])

    x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=1)
    signature = infer_signature(model_input=x_train, model_output=y_train)
    # create a scikit learn model
    clf = DecisionTreeClassifier()
    clf.fit(x_train, y_train)
    # Log a scikit learn model
    mlflow.sklearn.log_model(clf,"sklearn_model",signature=signature)