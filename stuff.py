import re
import unittest
import datetime

class Exercise: #klasa zadania

    def __init__(self, number, query):
        self.number = number
        self.query = query

    def valid(self):    #sprawdza poprawnosc zapytania
        match = re.match('select .*?(?=from)from .*?(?=where)where .*?(?=order by)order by( .*)?', self.query, re.I)
        if match:
            return True
        else:
            return False


class TestReg(unittest.TestCase): #testy metody sprawdzajacej poprawnosc zapytania

    def test1(self):
        self.assertEqual(Exercise(23, 'select x from hg where fdf like asd order by f asc').valid(), True)

    def test2(self):
        self.assertEqual(Exercise(5, 'select where hg from fdf like asd order by f asc').valid(), False)

    def test3(self):
        self.assertEqual(Exercise(2, 'select x from hg where fdf like asd ').valid(), False)

    def test4(self):
        self.assertEqual(Exercise(23, 'select from where order by').valid(), True)


def save(file, d):  #zapis do odp.txt
    with open(file, "w+") as f:
        for key, val in sorted(d.items()):
             f.write(str(key) + " " + val + "\n")


def inp(d):
    while 1:
        temp_exercise = Exercise(int(input()), input())     #wprowadzanie zadan
        if temp_exercise.valid():       #sprawdzenie poprwanosci zapytania
            d[temp_exercise.number] = temp_exercise.query   # zapis do slownika
        else:
            print('Niepoprawne zapytanie, odpowiedz nie zostanie zapisana')     #komunikat o bledzie


def timeleft(end, now):
    delta = (end.hour - start.hour)*60 + end.minute - start.minute
    return delta

def plan(): #plan zajec na WMI
    now = datetime.datetime.now().time()
    if now <= datetime.time(8, 15):
        return
    if (now >= datetime.time(8, 15) and now <= datetime.time(9, 45)):
        print(timeleft(datetime.time(9, 45), now), "minut do konca zajec")
        return
    if (now >= datetime.time(10, 0) and now <= datetime.time(11, 30)):
        print(timeleft(datetime.time(11, 30), now), "minut do konca zajec")
        return
    if (now >= datetime.time(11, 45) and now <= datetime.time(13, 15)):
        print(timeleft(datetime.time(13, 15), now), "minut do konca zajec")
        return
    if (now >= datetime.time(13, 45) and now <= datetime.time(15, 15):
        print(timeleft(datetime.time(15, 15), now), "minut do konca zajec")
        return
    if (now >= datetime.time(15, 30) and now <= datetime.time(17, 0)):
        print(timeleft(datetime.time(17, 0), now), "minut do konca zajec")
        return
    if (now >= datetime.time(17, 15) and now <= datetime.time(18, 45)):
        print(timeleft(datetime.time(18, 45), now), "minut do konca zajec")
        return
    if (now >= datetime.time(9, 45) and now <= datetime.time(10, 0)):
        print(timeleft(datetime.time(10, 0), now), "minut do konca przerwy")
        return
    if (now >= datetime.time(10, 30) and now <= datetime.time(10, 45)):
        print(timeleft(datetime.time(10, 45), now), "minut do konca przerwy")
        return
    if (now >= datetime.time(13, 15) and now <= datetime.time(13, 45)):
        print(timeleft(datetime.time(13, 45), now), "minut do konca przerwy")
        return
    if (now >= datetime.time(15, 15) and now <= datetime.time(15, 30)):
        print(timeleft(datetime.time(15, 30), now), "minut do konca przerwy")
        return
    if (now >= datetime.time(17, 0) and now <= datetime.time(17, 15)):
        print(timeleft(datetime.time(17, 15), now), "minut do konca przerwy")
