import time as t
import math

def delay(seconds):
    seconds = seconds*4
    sum = 0
    for i in range(math.ceil(seconds*1666334)):
        sum = sum + 1
t1 = t.perf_counter()
delay(5)
t2 = t.perf_counter()
print(t2-t1)