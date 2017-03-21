# utf-8
# python 3.5

import threading as td
import time
import copy
from queue import Queue

def thread_job(l,q):
    res = sum(l)
    q.put(res)

def multiThreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = td.Thread(target=thread_job, args=(copy.copy(l), q), name='T%i'%i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(10000))
    time_star = time.time()
    normal(l*4)
    print('normal: ', time.time() - time_star)

    time_star = time.time()
    multiThreading(l)
    print('multiThreading: ', time.time()-time_star)

