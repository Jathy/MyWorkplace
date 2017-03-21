# utf-8
# python 3.5

import threading as td
import time
from queue import Queue

def thread_job(l,q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)

def multiThreading():
    q = Queue()
    threads = []
    data = [[1,2,3],[4,5,6],[7,8,9],[11,12,13]]
    for i in range(4):
        t = td.Thread(target=thread_job, args=(data[i], q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name__ == '__main__':
    multiThreading()

