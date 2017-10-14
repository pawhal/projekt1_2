from stuff import *
from threading import Thread

base = {}

t2 = Thread(target = schedsave("odp.txt", base))
t1 = Thread(target = main)

t1.start()
t2.start()
t1.join()


#schedsave("odp.txt", base)
def main():
    while 1:
        temp_exercise = Exercise(int(input()), input())
        if temp_exercise.valid():
            base[temp_exercise.number] = temp_exercise.query
            print("bangla")
        else:
            print("nie bangla")

