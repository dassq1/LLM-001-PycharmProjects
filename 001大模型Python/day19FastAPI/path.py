"""
@Author:xuyinglai
@Date:2026/8/11
@DESC:
"""
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"path": "Hello"}


@app.get("/path/{id}")
async def get_id(id: int):
    return {"path": id}


@app.get("/path/{name}/{age}")
async def get_item(name, age):
    return {"name": name, "age": age}
