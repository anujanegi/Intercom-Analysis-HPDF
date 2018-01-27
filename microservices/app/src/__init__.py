from flask import Flask, Blueprint, current_app, request, json, jsonify

app = Flask(__name__)
api = Blueprint('api',__name__)

@api.before_request
def before_request():
    if request.json is None:
        return jsonify(code=400, message="JSON parameters expected"), 400

from .server import *
