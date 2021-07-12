# import libraries

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import iris

import pandas as pd
import numpy as np

from get_model_metrics import calc_metrics

# set configurations

RANDOM_SEED = 42

# load data

# Write code to load the data into a pandas data frame
df = None 

# Minimise the number of features without compromising the classification metrics

# define a function to select k_best features
def select_k_best_features(df: pd.DataFrame) -> list:
    # write your code here:
    relevant_feats = None
    # End of your code.
    return list(relevant_feats.index)

# Define a function that selects best features using the function
# above > trains a model > returns the model performance metrics.
def train_and_metrics_pipeline(df: pd.DataFrame):
    # write your code here

    relevant_feats = select_k_best_features(df)
    df = df[relevant_feats].copy()
    X = df.drop(columns=['label'])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, size=0.2, random_state=RANDOM_SEED)
    model = RandomForestClassifier(estimator='entropy', random_state=RANDOM_SEED)
    model.fit(X_train, y_train)

    metrics = calc_metrics(model, X_test, y_test)

    # End of your code
    return metrics


