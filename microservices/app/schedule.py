import time
import atexit
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

def getseconds(hour, minute):
    x=datetime.today()
    delta_t = (((int(x.hour) - int(hour))*3600) + ((int(x.minute) - int(minute))*60))
    if (delta_t > 0):
        sec = 86400 - delta_t
    else:
        sec = 86400 - delta_t
    return sec

def schedule(sec, function):
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        func=function,
        trigger=IntervalTrigger(seconds=sec),
        id='send_email',
        name='Send email at the specified time by user',
        replace_existing=True)
