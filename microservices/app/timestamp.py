import time

def minus_time(days, hours, minutes):
    # time in seconds for user input
    return ((int(days)*86400) + (int(hours)*3600) + (int(minutes)*60))

def calculate_open_time(mentioned_time):
    # time block for conversations to be mailed
    return (int(time.time()) - int(mentioned_time))
