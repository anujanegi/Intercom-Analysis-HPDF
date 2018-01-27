from src import app
from flask import json, jsonify, request
@app.route("/")
def home():
    return "Intercom Analysis - T12PF1"

@app.route('/getconversation', methods=['POST'])
def getconversation():
    days = request.json.get("days", None)
    hours = request.json.get("hours", None)
    minutes = request.json.get("minutes", None)
    time = request.json.get("time", None)
    emailid = request.json.get("emailid", None)

    if request.json is None:
        return jsonify(code=400, message="JSON parameters expected"), 400


    return days
