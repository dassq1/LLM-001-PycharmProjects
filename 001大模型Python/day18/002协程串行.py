"""
@Author:xuyinglai
@Date:2026/8/11
@DESC:
"""
import asyncio
import time


async def my_func(name, delay):
    print(f"任务{name}开始")
    await  asyncio.sleep(delay)
    print(f"任务{name}完成")
    return f"任务{name}结果"


async def main_sync():
    print("--------串行执行-------")
    await my_func("A", 1)
    await my_func("B", 2)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main_sync())
    print(f"串行耗时间:{time.time() - start_time}秒")
