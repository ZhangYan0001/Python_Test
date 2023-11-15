from ast import mod
from typing import List
from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class ModelName(str,Enum):
  alexnet = "alexnet"
  resnet = "rednet"
  lenet = "lenet"


class User(BaseModel):
  id:int
  name:str
  friends:List[str] = []


app = FastAPI()

@app.get("/items/{item_id}")
async def root(item_id:int):
  return {"item_id":item_id}


@app.get("/users/me")
async def read_me():
  return {"use_id":"the current user"}

@app.get("/users/{use_id}")
async def read_use_id(use_id:str):
  return {"use_id":use_id}


@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
  if model_name is ModelName.alexnet:
    return {"model_name":model_name,"message":"Deep Learning FTW"}
  
  if model_name is ModelName.lenet:
    return {"model_name":model_name,"message":"LeCNN all the images"}
  
  return {"model_name":model_name,"message":"Have some residuals"}