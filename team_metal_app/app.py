import pickle

from fastapi import FastAPI

app = FastAPI()

infile = open("./model", "rb")
model = pickle.load(infile)
infile.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}
