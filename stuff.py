import re

class Exercise:
    def __init__(self, number, query):
        self.number = number
        self.query = query

    def valid(self):
        match = re.match('select.*?(?=from)from.*?(?=where)where.*?(?=order by)order by.*?', self.query,
                         re.I)  # re.I => ignore case
        if match:
            return True
        else:
            return False


def inp(dicti):
    while 1:
        temp_exercise = Exercise(int(input()), input())
        if temp_exercise.valid():
            dicti[temp_exercise.number] = temp_exercise.query
            print("bangla")
        else:
            print("nie bangla")