import re

class Exercise:
    def __init__(self, number, query):
        self.number = number
        self.query = query

    def valid(self):
        match = re.match('select .*?(?=from)from .*?(?=where)where .*?(?=order by)order by( .*)?', self.query, re.I)
        if match:
            return True
        else:
            return False


def save(file, d):
    print(file)
    print(d)
    with open(file, "w+") as f:
        for key, val in sorted(d.items()):
             f.write(str(key) + " " + val + "\n")
    print("saved")


def inp(d):
    while 1:
        temp_exercise = Exercise(int(input()), input())
        if temp_exercise.valid():
            d[temp_exercise.number] = temp_exercise.query
            print("bangla")
        else:
            print("nie bangla")

def classes():
    print("minut do konca zajec")


def breaks():
    print("minut do konca przerwy")