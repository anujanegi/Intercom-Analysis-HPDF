from src import app, mail

@app.route('/')
def home():
    return "Intercom Analysis - T12PF1"

@app.route('/maillistofconversations', methods=['POST'])
def maillistofconversations():
    if request.json is None:
        bad_request("JSON parameters expected")

    days = request.json.get("days", None)
    hours = request.json.get("hours", None)
    minutes = request.json.get("minutes", None)
    time = request.json.get("time", None)
    emailid = request.json.get("emailid", None)

    try:
        # configure intercom with your extended access token
        # edit intercomconfig.py with your token
        intercom = configure_client()

        # get open conversations
        open_convo = getconversations(intercom)

        # calculate open time acceptable as per user
        open_time = calculate_open_time(minus_time(days, hours, minutes))

        # get filtered conversations
        filter_convo = filterconversations(open_convo, open_time)

        # get body and send email
        send_email(getbody(filter_convo), emailid)

    except Exception as e:
        Error(500, str(e))

    return OK()

@app.route('/test')
def test():
    return current_app.send_static_file('test.html')
