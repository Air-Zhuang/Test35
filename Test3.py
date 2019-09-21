from concurrent.futures import ThreadPoolExecutor,as_completed
import time

def x(a):
    time.sleep(1)
    return "结果:"+str(a)

pool=ThreadPoolExecutor(max_workers=2)

tasks=[pool.submit(x,i) for i in range(10)]


for each_task in as_completed(tasks):
    print(each_task.result())