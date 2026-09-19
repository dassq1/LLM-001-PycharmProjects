"""
@Author:xuyinglai
@Date:2026/7/31
@DESC:

1.
  进程池 读取 5个文件 获取每一个文件的大小 并返回
  len(read())
  返回 python1.txt 字符数量是 xxx
  map

"""
import os.path
from multiprocessing import Pool


def count_file_chars(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        file_name = os.path.basename(file_path)
        return file_name, len(content)


if __name__ == '__main__':
    base_dir = r"C:\Users\23716\Desktop\PycharmProjects\大模型\day13\进程池\data"
    file_list = [f"{base_dir}/python{i}.txt" for i in range(1, 6)]
    with Pool(processes=5) as pool:
        result = pool.map(count_file_chars, file_list)

    for name, size in result:
        print(f"{name}的字符数量是{size}")
