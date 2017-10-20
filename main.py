from stuff import *
import schedule
import time
from multiprocessing import Process

base = {}
def f1():

    schedule.every(10).seconds.do(save, file = "odp.txt", dicti = base)
    while 1:
        schedule.run_pending()
        time.sleep(1)

def f2():
    while 1:
        inp(base)

if __name__=='__main__':
     p1 = Process(target = f1)
     p1.start()
     inp(base)