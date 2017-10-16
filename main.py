from stuff import *
import schedule
import time

base = {}

schedule.every().seconds.do(save, file = "odp.txt", dict = base)
schedule.every().seconds.do(inp, dict = base)


while 1:
    schedule.run_pending()
    time.sleep(1)