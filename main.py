from classes import Exercise
import re

base = {}
cont = True
pattern = "select \w* from \w* where \w.+?(?=order by)order by (asc|desc)" #query do poprawienia, zabawa z smss
while cont == True:

    temp_exercise = Exercise(12, 'costam')
    temp_exercise.number = int(input())
    temp_exercise.query = input()
    match = re.match(pattern, temp_exercise.query, re.M|re.I)
    if match:
        print(match.group())
        base[temp_exercise.number] = temp_exercise.query;
    if temp_exercise.query == 'dupa':
        cont = False
print(str(base))
