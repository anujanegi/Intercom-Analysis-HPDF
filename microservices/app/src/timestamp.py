import time

def minus_time(days, hours, minutes):
    return ((days*86400) + (hours*3600) + (minutes*60))

def calculate_open_time(mentioned_time):
    return (int(time.time()) - int(mentioned_time))
