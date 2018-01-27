from src import app
import sender

@app.route("/")
def home():
    return "Intercom Analysis - T12PF1"

@api.route('/getconversation', methods=['POST'])
def getconversation():
    days = request.json.get("days", None)
    hours = request.json.get("hours", None)
    minutes = request.json.get("minutes", None)
    time = request.json.get("time", None)
    emailid = request.json.get("emailid", None)

    return days
