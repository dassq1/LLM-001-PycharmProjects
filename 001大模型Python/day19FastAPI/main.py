# """
# @Author:xuyinglai
# @Date:2026/8/11
# @DESC:
# """
# import uvicorn
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"hello": "world"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str):
#     return {"item_id": item_id, "q": q}
############################################################
from fastapi import FastAPI
from routers import user, item  # 导入子模块路由
import uvicorn

app = FastAPI(title="路由分发示例")

# 挂载用户路由：所有 /users 开头的请求由 user.router 处理
app.include_router(user.router)

# 挂载商品路由：所有 /items 开头的请求由 item.router 处理
app.include_router(item.router)


# 主应用自身也可以定义路由
@app.get("/")
def root():
    return {"message": "欢迎访问主页面"}


if __name__ == "__main__":
    # 直接在代码中启动uvicorn服务器
    uvicorn.run(
        app="main:app",  # 指定要运行的FastAPI应用实例
        host="127.0.0.1",  # 允许外部访问（本地可通过127.0.0.1或localhost访问）
        port=8888,  # 端口号
        reload=True  # 开发模式：代码修改后自动重启（生产环境需去掉）
    )
