# utf-8
# python 3.5

import multiprocessing as mp

value = mp.Value('d', 1)
array = mp.Array('i', [1,2,3])
