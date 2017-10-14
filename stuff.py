import re

class Exercise:
    exerciseCount = 0

    def __init__(self, number, query):
        self.number = number
        self.query = query
        Exercise.exerciseCount += 1

    def show(self):
        print (self.number,self.query)

    def valid(self):
        match = re.match("select \w.+?(?=from)from \w.+?(?=where)where \w.+?(?=order by)order by \w*", self.query, re.I)  # re.I => ignore case
        if match:
            return True
        else:
            return False