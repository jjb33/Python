from multiprocessing import Pool
import multiprocessing
import os
import myfunct
import time
from myfunct import processnum

# def makeset(x):
    
#     s = set()
#     for x in range(1, x+1):
#         s.add(processnum(x))
#     return s

x = 1000000 #'How many values do you want multiprocessing to run through?'))
p = 1 #'How many processes do you want to use?'

# tstart = time.time()
# for i in range(1, x):
#     #print(f'Process ID is {os.getpid()}')
#     processnum(i)
# tstop = time.time()
# print(f'With no Pools, this took {(tstop - tstart)/60} minutes to complete with {x} values') 

if __name__ == '__main__':
    pool = Pool(processes=p)
    tstart = time.time()
    pool.map(processnum, range(1, 1+x))
    tstop = time.time()
    print(f'With {p} multiprocessing pools on {multiprocessing.cpu_count()} CPU cores, this took {(tstop - tstart)/60} minutes to complete with {x} values')
    

'''
RESULTS:
With 1 multiprocessing pools on 4 CPU cores, this took 0.17694028615951538 minutes to complete with 1000000 values
With 2 multiprocessing pools on 4 CPU cores, this took 0.10976528326670329 minutes to complete with 1000000 values
With 3 multiprocessing pools on 4 CPU cores, this took 0.0888615886370341  minutes to complete with 1000000 values
With 4 multiprocessing pools on 4 CPU cores, this took 0.07898440361022949 minutes to complete with 1000000 values
With 5 multiprocessing pools on 4 CPU cores, this took 0.08163272937138875 minutes to complete with 1000000 values




With no Pools, this took 0.38077909549077354 minutes to complete with 10000 values


With multiprocessing pools, this took 0.042066192626953124 minutes to complete with 10000 values
'''
