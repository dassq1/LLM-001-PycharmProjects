"""
@Author:xuyinglai
@Date:2026/7/31
@DESC:
"""
import threading
import time

total_tickets = 100
lock = threading.Lock()


def sell_tickets(window_name):
    global total_tickets
    while True:
        with lock:
            if total_tickets > 0:
                time.sleep(0.1)
                total_tickets -= 1
                print(f"{window_name}售出1张票,剩余{total_tickets}张票")
            else:
                print("售完")
                break


if __name__ == "__main__":
    threads = []
    for i in range(1, 5):
        thread = threading.Thread(target=sell_tickets, args=(f"窗口{i}",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print("售完")
