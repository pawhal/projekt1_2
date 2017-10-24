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





