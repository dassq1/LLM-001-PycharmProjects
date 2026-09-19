"""
@Author:xuyinglai
@Date:2026/8/12
@DESC:
0.mysql的联合查询方式有哪些

1.mysql的约束有哪些 分别有什么作用

2.什么是 脏读 幻读  不可重复读

3.什么是协程 ? 如何出让CPU的执行权

4.使用fastapi 定义三个接口
   1.可以接收两个路径参数 名字和年龄 并返回 名字和年龄
   2.接收请求参数 名字:默认值为zs 年龄 ,体重:可选参数 可以传递也可以不传
     有体重 返回 名字 年龄 体重
     没有 返回 名字 年龄
   3.接收请求体参数 书籍的名字 书籍的价格 书籍的作者 可以将信息封装为对象
    返回对象的信息
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/user/{name}/{age}")
async def get_user_path(name: str, age: int):
    return {"name": name, "age": age}


@app.get("/user/")
async def get_user_query(

        age: int,
        weight: float,
        name: str = "zs",
):
    if weight:
        return {"name": name, "age": age, "weight": weight}
    else:
        return {"name": name, "age": age}


class Book(BaseModel):
    name: str
    price: float
    author: str


@app.post("/books")
async def creat_book(book: Book):
    return {"name": book.name, "price": book.price, "author": book.author}
