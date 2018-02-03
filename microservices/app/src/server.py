from src import app, mail

@app.route('/')
def home():
    return "Intercom Analysis - T12PF1"

@app.route('/mailconversations', methods=['POST'])
def mailconversations():
    if request.json is None:
        bad_request("JSON parameters expected")

    days = request.json.get("days", None)
    hours = request.json.get("hours", None)
    minutes = request.json.get("minutes", None)
    time_hour = request.json.get("time_hour", None)
    time_minute = request.json.get("time_minute", None)
    emailid = request.json.get("emailid", None)

    # get seconds at which the schedule needs to be triggered
    seconds = getseconds(time_hour, time_minute)

    #def daily_email():
    #    try:
    # configure intercom with your extended access token
    # edit intercomconfig.py with your token
    #intercom = configure_client()

    # get open conversations
    #open_convo = getconversations(intercom)

    # calculate open time acceptable as per user
    #open_time = calculate_open_time(minus_time(int(days), int(hours), int(minutes)))

    # get filtered conversations
    #filter_convo = filterconversations(open_convo, open_time)

    # get body and send email
    #send_email(getbody(filter_convo), emailid)
    return seconds

"""    except Exception as e:
            Error(500, str(e))
    daily_email()
    #schedule(seconds, daily_email)

    return OK()
"""

@app.route('/test')
def test():
    return current_app.send_static_file('test.html')
