from src import app
from flask import json, jsonify, request, current_app
from flask_mail import Mail, Message
from intercom.client import Client

mail = Mail(app)

def configure_client():
    intercom = Client(personal_access_token='extended_access_token')

def send_email(msg, emailid):
    try:
        mail.connect()
    except Exception as e:
        return jsonify(code=500, message=str(e)), 500

    msg = Message(subject="Open conversations", body=msg, sender="abc@example.com", recipients=[emailid])
    mail.send(msg)


@app.route('/')
def home():
    return "Intercom Analysis - T12PF1"

@app.route('/getconversation', methods=['POST'])
def getconversation():
    if request.json is None:
        return jsonify(code=400, message="JSON parameters expected"), 400

    days = request.json.get("days", None)
    hours = request.json.get("hours", None)
    minutes = request.json.get("minutes", None)
    time = request.json.get("time", None)
    emailid = request.json.get("emailid", None)

    try:
        configure_client()
    except Exception as e:
        return jsonify(code=500, message=str(e)), 500

    for convo in intercom.conversations.find_all(type='admin', id= id, open= true): #user or admin?
        #filter and find conversations open for X days from today by parameter created_at

        send_email(message, emailid)

    return jsonify(code=200, message="Done"), 200

@app.route('/test')
def test():
    return current_app.send_static_file('test.html')
