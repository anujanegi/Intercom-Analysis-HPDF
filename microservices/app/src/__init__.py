from flask import Flask
from flask import json, jsonify, request, current_app
from flask_mail import Mail, Message
from intercom.client import Client
from intercomconfig import *
from conversation import *
from timestamp import *
from response_sender import *

app = Flask(__name__)
mail = Mail(app)

from .server import *
