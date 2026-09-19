"""
@Author:xuyinglai
@Date:2026/7/21
@DESC:
"""
book_list = []
while True:
    print("*" * 50)
    print("欢迎来到图书管理系统")
    print("1.添加图书")
    print("2.根据id修改")
    print("3.根据id查询")
    print("4.查询所有图书")
    print("5.根据id删除某个图书")
    print("6.退出")
    print("*" * 50)
    num = input("请你输入编号:")

    # 1.添加图书
    if num == "1":
        b_id = input("请输入图书id:")
        #         判断id是否重复
        flag = False
        for book in book_list:
            if book["id"] == b_id:
                flag = True
                break
        if flag:
            print("该图书id已存在，添加失败!")
        else:
            name = input("请输入书名: ")
            author = input("请输入作者: ")
            price = input("请输入价格: ")
            new_book = {"id": b_id, "name": name, "author": author, "price": price}
            book_list.append(new_book)
            print("图书添加成功!")

            # 2.根据id修改图书
    elif num == "2":
        b_id = input("请输入要修改的图书id ")
        find = False
        for book in book_list:
            if book["id"] == b_id:
                find = True
                print("请输入新的信息: ")
                new_name = input("新书名: ")
                new_author = input("新作者: ")
                new_price = input("新价格: ")
                # 不为空才更新
                if new_name:
                    book["name"] = new_name
                if new_author:
                    book["author"] = new_author
                if new_price:
                    book["price"] = new_price
                print("图书修改完成!")
                break
        if not find:  # if find == False
            print("未找到该id的图书")


    # 3.根据id查询单本图书
    elif num == "3":
        b_id = input("qin")
        find = False
        for book in book_list:
            if book["id"] == b_id:
                find = True
                print("-" * 20)
                print(f"图书id:{book['id']}")
                print(f"书名:{book['name']}")
                print(f"作者:{book['author']}")
                print(f"价格:{book['price']}")
                print("-" * 20)
                break
        if not find:
            print("未找到该id的图书")
    # 4.查询全部图书
    elif num == "4":
        if len(book_list) == 0:
            print("暂无图书数据")
        else:
            print("========全部图书列表===========")
            for book in book_list:
                print(f"id:{book['id']}")

    # 5.根据id删除图书
    elif num == '5':
        b_id = input("请输入要删除的图书id: ")
        find = False
        for i in range(len(book_list)):
            if book_list[i]["id"] == b_id:
                find = True
                del book_list[i]
                print("图书删除成功! ")
                break
        if not find:
            print("未找到该id的图书")

    # 6.退出系统
    elif num == '6':
        print("系统已退出")
        break

    # 输入的编号非法时
    else:
        print("输入的数字有误")

    input("\n按回车返回主菜单————————")
