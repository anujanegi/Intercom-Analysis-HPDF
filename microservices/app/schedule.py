import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


def schedule(hour, minute, function):
    x=datetime.today()
    y=x.replace(day=x.day, hour=hour, minute=minute, second=0, microsecond=0)
    delta_t=y-x
    if (delta_t > 0):
        sec = 86400 - delta_t
    else:
        sec = 86400 - delta_t

    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        func=function,
        trigger=IntervalTrigger(seconds=sec),
        id='send_email',
        name='Send email at the specified time by user',
        replace_existing=True)
