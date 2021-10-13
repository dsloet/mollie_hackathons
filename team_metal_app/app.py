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


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/predict")
async def predict():
    return {"message": "Go away"}
