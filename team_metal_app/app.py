import pickle
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

infile = open("./model", "rb")
model = pickle.load(infile)
infile.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class Payload(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    radius_se: float
    perimeter_se: float
    area_se: float
    concave_points_se: float
    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float

@app.post("/predict")
async def predict(payload: Payload):
    return {"message": "Go away"}
