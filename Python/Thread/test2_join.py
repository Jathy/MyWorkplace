# utf-8
# python 3.5

import threading as td
import time

def thread_job():
    print("%s start" %td.currentThread().getName())
    time.sleep(1)
    print("%s finished" %td.currentThread().getName())

def T2_job():
    print("%s start" %td.currentThread().getName())
    print("%s finished" %td.currentThread().getName())

def main():
    T1 = td.Thread(target=thread_job, name="T1")
    T2 = td.Thread(target=T2_job, name="T2")
    T1.start()
    T2.start()
    T1.join()
    # T2.join()
    print('all done!')

if __name__ == '__main__':
    main()

