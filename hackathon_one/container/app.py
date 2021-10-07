from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


class Input(BaseModel):
    """Data model for post request form"""

    input1: str
    input2: int
    input3: float


@app.get("/")
def home():
    return {"message": "Hello world"}


@app.post("/predict")
def predict(params: Input):

    data_input = [[params.input1, params.input2, params.input3]]

    return {"message": data_input}
