import re
import unittest

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

def plan():
    print(" x minut do konca zajec/przerwy") #do zamodelowania
