import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import pandas as pd


from classification import train_and_metrics_pipeline


df = pd.read_csv(
    "https://raw.githubusercontent.com/pkmklong/Breast-Cancer-Wisconsin-Diagnostic-DataSet/master/data.csv"
)
# Integer encode the target variable, diagnosis
df["diagnosis_int"] = (df["diagnosis"] == "M").astype("int")

# Drop the previous string column
df.drop(["diagnosis", "Unnamed: 32"], axis=1, inplace=True)

print(df.head())

# Split feature and target vectors
X = df.drop("diagnosis_int", 1)
y = df["diagnosis_int"]

train_and_metrics_pipeline(df, X, y)
