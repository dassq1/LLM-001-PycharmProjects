"""
@Author:xuyinglai
@Date:2026/7/27
@DESC:书籍类: 封装 书籍的零散信息 id 书名 作者 价格
书籍管理类:
      对书籍的增 删 改 查
      实例属性 book_list=[]
      增加功能: 本质就是向 列表内添加一个书籍对象
      查询所有图书: 返回书籍列表
      根据id查询:
             遍历列表 获取图书的编号 判断和传入的编号是否一致
                     有 返回图书对象 没有 返回None
"""
class Book:
    def __init__(self,book_id,book_name,book_author,book_price):
        self.book_id=book_id
        self.book_name=book_name
        self.book_author=book_author
        self.book_price=book_price
    def