import re
import time

class Exercise:

    def __init__(self, number, query):
        self.number = number
        self.query = query

    def valid(self):
        match = re.match('select \w.+?(?=from)from \w.+?(?=where)where \w.+?(?=order by)order by \w*', self.query,
                         re.I)  # re.I => ignore case
        if match:
            return True
        else:
            return False



def save(file, dict):
    with open(file, "w") as f:
        for key, val in sorted(dict.items()):
            f.write(str(key) + " " + val + "\n")

def schedsave(file, dict):
    while 1:
        save(file, dict)
        time.sleep(10.0 - time.time() % 10.0)
        #print("KEK")
