import datetime
from fastapi import FastAPI,Path,Query,HTTPException,Depends
from pydantic import BaseModel,Field
from fastapi.responses import HTMLResponse
app = FastAPI()
#
# @app.get("/")
# async def read_root():
#     return {"Hello": "World99999999999999999999900000000000000000000999999"}
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"HELLO {name}"}
#
# @app.get("/hello")
# async def get_hello():
#     return {"msg":"你好FASTAPI"}
#
# @app.get("/book/{id}")
# async def get_book(id:int=Path(...,gt=0,lt=101,description="书籍的id取值[1,100]")):
#     return {"id":id,"title":f"这是第{id}本书"}
#
# # 查找书籍作者，2-10，name
# @app.get("/author/{name}")
# async def get_name(name:str=Path(...,min_length=2,max_length=10)):
#     return {"msg":f"这是{name}的信息"}
#
# # 查询参数 查询新闻skip limit
# @app.get("/news/news_list")
# async def get_newslist(
#         skip:int=Query(0,description="跳过的记录数",lt=100),
#         limit:int=Query(10,description="返回的记录数")
#     ):
#     return {"skip":skip,"limit":limit}
# # 请求体参数 注册：用户名密码str
# class User(BaseModel):
#     username:str=Field(default="zhangsan",min_length=2,max_length=10,description="用户名长度要求2-10个字")
#     password:str=Field(min_length=3,max_length=10)
#
# @app.post("/register")
# async def register(user:User):
#     return user
# # 接口->响应HTML代码
# @app.get("/html",response_class=HTMLResponse)
# async def get_html():
#     return "<h1>这是一级标题</h1>"
# # 接口 返回一张图片内容
# from fastapi.responses import FileResponse
# @app.get("/files")
# async def get_file():
#     path="./files/噜噜1.png"
#     return FileResponse(path)
# # 定义一个新闻接口->id title content
# # class News(BaseModel):
# # #     id:int
# # #     title:str
# # #     content:str
# # # @app.get("/news/{id}",response_model=News)
# # # async def get_news(id:int):
# # #     return {
# # #         "id":id,
# # #         "title":f"这是第{id}本书",
# # #         "content":"这是一本好书"
# # #
# # #     }
#
#
#
# #   按id查询新闻1-6
# @app.get("/news/{id}")
# async def get_news(id: int):
#     id_list = [1, 2, 3, 4, 5, 6]
#     if id not in id_list:
#         raise HTTPException(status_code=404, detail="查找的新闻不存在")
#     return {"id": id}

# region
# @app.middleware("http")
# async def middleware1(request,call_next):
#     print("中间件1 start")
#     response=await call_next(request)
#     print("中间件1 end")
#     return response
# @app.middleware("http")
# async def middleware1(request,call_next):
#     print("中间件2 start")
#     response=await call_next(request)
#     print("中间件2 end")
#     return response
#
# @app.get("/")
# async def root():
#     return{"message":"hello world"}
#

#endregion
# ############################################
# region
# 分页参数逻辑共用 新闻列表和用户列表
@app.get("/")
async def root():
    return {"message":"Hello World"}
async def common_parameters(
        skip:int=Query(0,ge=0),
        limit:int=Query(10,le=60)
):
    return{"skip":skip,"limit":limit}

@app.get("/news/new_list")
async def get_news_list(common=Depends(common_parameters)):
    return common
@app.get("/user/user_list")
async def get_user_list(common=Depends(common_parameters)):
    return{"message":"Hello"}

# endregion
##############################################
# region
# 创建异步引擎
from datetime import datetime                      # Python 内置时间
from sqlalchemy import DateTime, func             # SQLAlchemy 的列类型和函数
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  # ORM 核心
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
ASYNC_DATABASE_URL="mysql+aiomysql://root:12345@localhost:3306/FastAPI?charset=utf-8"
async_engine=create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow=20
)
class Base(DeclarativeBase):
    create_time:Mapped[datetime]=mapped_column(DateTime,insert_default=func.now(),comment="创建时间")
    update_time:Mapped[datetime]=mapped_column(DateTime,insert_default=func.now(),comment="修改时间")


class Book(Base):
    pass
