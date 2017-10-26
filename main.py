from stuff import *
from apscheduler.schedulers.background import BackgroundScheduler

base = {}

sch = BackgroundScheduler()
sch.start()

sch.add_job(save, "cron", args = ("/home/paw/projekt1_2/odp.txt", base), second='*/30')
sch.add_job(classes, "cron", minute = '*/1')
sch.add_job(breaks, "cron", minute = '*/1')

while 1:
    inp(base)
