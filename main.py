from stuff import *

base = {}

schedsave("odp.txt", base)
while 1:
    temp_exercise = Exercise(int(input()), input())
    if temp_exercise.valid():
        base[temp_exercise.number] = temp_exercise.query
        print("bangla")
    else:
        print("nie bangla")

