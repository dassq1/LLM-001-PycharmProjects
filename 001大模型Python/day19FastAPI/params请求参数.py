"""
@Author:xuyinglai
@Date:2026/8/11
@DESC:
"""
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


# http://127.0.0.1:8000/params1?name=Zhangsan&age=999
@app.get("/params1")
def params1(name, age):
    return {"name": name, "age": age}


@app.get("/params3")
def params1(name: str, age: int, height: float):
    return {"name": name, "age": age, "height": height}


@app.get("/params4")
def params1(age: int, name="张三"):
    return {"name": name, "age": age}


class Person(BaseModel):
    name: str
    age: int
    height: float
    gender: str


@app.post("/param7")
def params7(person: Person):
    return {"name": person.name, "age": person.age, "height": person.height}


@app.get("/params8/{id}")
def params8(id: int, name: str, age=20):
    return {"name": name, "age": age, "id": id}


@app.get("/params9")
def params9(q: bool):
    return {"q": q}
