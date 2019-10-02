
import random
import time
import os

def processnum(x):
    print(f'Process ID is {os.getpid()}')
    x = x * (random.randrange(1, 1000))
    x = x + (random.randrange(1, 5000))
    x = x / (random.randrange(1, 5000))
    x = x - (random.randrange(1, 5000))
    #print(x)