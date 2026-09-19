"""
@Author:xuyinglai
@Date:2026/8/6
@DESC:
"""
import pymysql


def get_connection():
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


def select_department(conn):
    my_cursor = conn.cursor()
    sql = "select * from t_department"
    row_number = my_cursor.execute(sql)
    rows = my_cursor.fetchall()
    # for i in rows:
    #     print(i)


def insert_data(conn):
    my_c = conn.cursor()
    sql = "insert into t_department values (10,'test','testtest')"
    my_c.execute(sql)
    # 提交事务
    conn.commit()
    my_c.close()


def delete_data(conn):
    my_c = conn.cursor()
    sql = "delete from t_department where did=10"
    my_c.execute(sql)
    # 提交事务
    conn.commit()
    my_c.close()


def update_data(conn):
    my_c = conn.cursor()
    sql = "update t_department set dname='dev' where did=10  "
    my_c.execute(sql)
    # 提交事务
    conn.commit()
    my_c.close()


if __name__ == "__main__":
    conn = get_connection()
    # select_department(conn)
    insert_data(conn)
    # delete_data(conn)
    update_data(conn)
    conn.close()
