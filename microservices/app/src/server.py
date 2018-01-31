from src import app
from flask import json, jsonify, request, current_app
from flask_mail import Mail, Message
from intercom.client import Client
import intercomconfig
import conversation
import timestamp

mail = Mail(app)

def send_email(body, emailid):
    try:
        mail.connect()
    except Exception as e:
        return jsonify(code=500, message=str(e)), 500

    msg = Message(subject="Open conversations", body=body, sender="abc@example.com", recipients=[emailid])
    mail.send(msg)


@app.route('/')
def home():
    return "Intercom Analysis - T12PF1"

@app.route('/maillistofconversations', methods=['POST'])
def maillistofconversations():
    if request.json is None:
        return jsonify(code=400, message="JSON parameters expected"), 400

    days = request.json.get("days", None)
    hours = request.json.get("hours", None)
    minutes = request.json.get("minutes", None)
    time = request.json.get("time", None)
    emailid = request.json.get("emailid", None)

    #configure intercom with your extended access token
    #edit intercomconfig.py with your token
    try:
        intercom = configure_client()
    except Exception as e:
        return jsonify(code=500, message=str(e)), 500

    #get open conversations
    try:
        getconversations(intercom)
    except Exception as e:
        return jsonify(code=500, message=str(e)), 500


        #filter and find conversations open for X days from today by parameter created_at

        #send_email(message, emailid)
    return jsonify(code=200, message="Done"), 200

@app.route('/test')
def test():
    return current_app.send_static_file('test.html')
