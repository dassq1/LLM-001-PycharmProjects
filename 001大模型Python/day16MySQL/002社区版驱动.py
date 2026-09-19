"""
@Author:xuyinglai
@Date:2026/8/6
@DESC:pymysql
"""

import pymysql


def connect_test():
    conn_params = {
        "host": "localhost",  # 本地数据库写localhost，远程写服务器IP
        "port": 3306,  # MySQL默认端口3306
        "user": "root",  # 你的MySQL用户名
        "password": "12345",
        "database": "atguigu"  # 要连接的具体数据库
    }
    try:
        # 2. 建立数据库连接
        conn = pymysql.connect(**conn_params)
        print("pymsql获取连接成功", conn)
        return conn
    except:
        print("获取连接的时候发生了异常")


if __name__ == "__main__":
    connect_test()
