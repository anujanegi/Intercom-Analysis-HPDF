from flask import Flask, Blueprint, current_app, request, json

app = Flask(__name__)
api = Blueprint('api',__name__)

@api.before_request
def before_request():
    if request.json is None:
        return sender.badRequest("JSON parameters expected")
from .server import *
from .sender import *
