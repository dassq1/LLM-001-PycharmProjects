"""
@Author:xuyinglai
@Date:2026/8/6
@DESC:
"""
from fastapi import FastAPI, Query, HTTPException
from typing import Optional

app=FastAPI(title="图书查询API")

@app.get("/books")
async def search_books(
        category:str=Query(default="Python开发",min_length=5,max_length=255,description="图书分类，默认为'Python'开发"),
        price:float=Query(...,ge=50,le=100,description="图书价格范围是[50,100]")
):


