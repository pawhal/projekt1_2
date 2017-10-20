from stuff import *
from crontab import CronTab

cron = CronTab()
base = {}

saving = cron.new(command = 'python ./saving.py')
saving.minute.every(1)

while 1:
    inp(base)