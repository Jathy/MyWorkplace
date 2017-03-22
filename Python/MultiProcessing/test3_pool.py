# utf-8
# python 3.5

import multiprocessing as mp

def job(x):
    return x * x

def multicore():
    pool = mp.Pool(processes=2)
    res = pool.map(job, range(100))
    print(res)
    
    multi_res = [pool.apply_async(job, (i,)) for i in range(100)]
    print([res.get() for res in (multi_res)])

if __name__ == "__main__":
    multicore()
