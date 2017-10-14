from stuff import *

base = {}
odp = open("odp.txt", "r+", 0)
while True:

    temp_exercise = Exercise(int(input()), input())
    if temp_exercise.valid():
        temp_exercise.show()
        base[temp_exercise.number] = temp_exercise.query;
    if temp_exercise.query == 'q':
        break
print(str(base))
