from stuff import *
from apscheduler.schedulers.background import BackgroundScheduler

base = {}   #slownik, w ktorym przechowywane beda poprawne zadania

sch = BackgroundScheduler()
sch.start()

sch.add_job(save, "cron", args = ("/home/paw/projekt1_2/odp.txt", base), second='*/30') #zapis zadan co 30 sekund
sch.add_job(plan, "cron", minute = '*/1', hour = '8-18', day_of_week = '0-4')   #informacja o zajeciach/przerwach (do zamodelowania)

unittest.main(exit = False)     #start testow
inp(base)       #petla do podawania numerow zadan i zapytan