from stuff import *
from crontab import CronTab

cron = CronTab(user='paw')
base = {}

out = open("out.txt", "w")
cron.remove_all()
saving = cron.new(command = 'python3 ./saving.py >> out.txt')
saving.minute.every(1)
saving.enable()

s = cron.new(command = 'tail -f out.txt')
s.minute.every(1)
s.enable()


cron.write()
while 1:
    inp(base)