from stuff import *
import schedule
import time
from multiprocessing import Process, Manager


def save(file, d):
    print(file)
    print(base)
    with open(file, "w+") as f:
        for key, val in sorted(d.items()):
             f.write(str(key) + " " + val + "\n")
    print("saved")


def inp(base):
    while 1:
        temp_exercise = Exercise(int(input()), input())
        if temp_exercise.valid():
            base[temp_exercise.number] = temp_exercise.query
            print("bangla")
        else:
            print("nie bangla")


def f1(d):
    schedule.every(30).seconds.do(save, "/home/paw/projekt1_2/odp.txt", d)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=='__main__':
    manager = Manager()
    base = Manager().dict()
    p1 = Process(target=f1, args=(base,))
    p1.start()
    p1.join()
    while 1:
        inp(base)
