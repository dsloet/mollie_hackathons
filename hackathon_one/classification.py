# import libraries
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif

# from sklearn.datasets import iris

import pandas as pd
import numpy as np

from get_model_metrics import calc_metrics

# set configurations

RANDOM_SEED = 42


# Minimise the number of features without compromising the classification metrics

# define a function to select k_best features using ANOVA f-statistic
def select_k_best_features(df, X, y) -> list:
    # write your code here:
    # Split train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=RANDOM_SEED
    )

    # All features of dataset are float values. You normalize all features of the train and test dataset here.
    scaler = StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    selector = SelectKBest(f_classif, k=20)

    # Fit to scaled data, then transform it
    X_new = selector.fit_transform(X_train_scaled, y_train)

    # Print the results
    feature_idx = selector.get_support()
    for name, included in zip(df.drop("diagnosis_int", 1).columns, feature_idx):
        print("%s: %s" % (name, included))

    # Drop the target variable
    feature_names = df.drop(columns=["diagnosis_int"]).columns[feature_idx]

    return feature_names


# Define a function that selects best features using the function
# above > trains a model > returns the model performance metrics.
def train_and_metrics_pipeline(df, X, y):
    # write your code here

    relevant_feats = select_k_best_features(df, X, y)
    df = df[relevant_feats].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_SEED
    )

    scaler = StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestClassifier(criterion="entropy", random_state=RANDOM_SEED)
    model.fit(X_train_scaled, y_train)

    metrics = calc_metrics(model, X_test_scaled, y_test)
    print(metrics)
    # End of your code
    return metrics
