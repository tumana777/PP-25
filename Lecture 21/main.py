import time
import threading

# def plan_project():
#     time.sleep(2)
#     print("Project planned")
#
# def start_project():
#     time.sleep(4)
#     print("Project started")
#
# def end_project():
#     time.sleep(3)
#     print("Project ended")
#
#
# time1 = time.perf_counter()
#
# thread1 = threading.Thread(target=plan_project)
# thread2 = threading.Thread(target=start_project)
# thread3 = threading.Thread(target=end_project)
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()

# plan_project()
# start_project()
# end_project()

# time2 = time.perf_counter()
#
#
# print(f"All tasks completed in {time2 - time1} seconds")


# def print_tasks(task_name):
#     print(f"Task: {task_name} started")
#     time.sleep(1)
# #
# t1 = time.perf_counter()
#
# thread_list = []
#
# for i in range(1, 11):
#     thread = threading.Thread(target=print_tasks, args=(i, ))
#     thread.start()
#     thread_list.append(thread)
#
# for thread in thread_list:
#     thread.join()
#
# t2 = time.perf_counter()
#
# print(f"All tasks completed in {t2 - t1} seconds")

# def print_tasks(task_name):
#     print(f"Task: {task_name} started")
#     time.sleep(1)
#
# from concurrent.futures import ThreadPoolExecutor
#
# thread_list = []
#
# t1 = time.perf_counter()
#
# with ThreadPoolExecutor(max_workers=4) as executor:
#     for i in range(1, 11):
#         thread = executor.submit(print_tasks, i)
#         thread_list.append(thread)
#
# t2 = time.perf_counter()
#
# print(f"All tasks completed in {t2 - t1} seconds")

# import queue
#
# task_queue = queue.Queue()
#
# def worker():
#     while True:
#         task = task_queue.get()
#
#         if task is None:
#             break
#
#         print("Processing", task)
#         time.sleep(1)
#         task_queue.task_done()
#
# num_threads = 5
#
# threads = []
#
# t1 = time.perf_counter()
#
# for _ in range(num_threads):
#     thread = threading.Thread(target=worker)
#     thread.start()
#     threads.append(thread)
#
# for i in range(10):
#     task_queue.put(i)
#
# for _ in range(num_threads):
#     task_queue.put(None)
#
# for thread in threads:
#     thread.join()
#
# t2 = time.perf_counter()
#
# print(f"All tasks completed in {t2 - t1} seconds")

