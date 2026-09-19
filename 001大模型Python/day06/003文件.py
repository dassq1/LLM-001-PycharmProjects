"""
@Author:xuyinglai
@Date:2026/7/23
@DESC:自习
"""


def copyFile(source_file_path, dest_file_path):
    source_file = open(source_file_path, 'rb')
    content = source_file.read()

    dest_file = open(dest_file_path, 'wb')
    dest_file.write(content)

    source_file.close()
    dest_file.close()


copyFile("./demo1.png", "./demo2.png")
