from flask import jsonify

def badRequest(message):
    return jsonify(code=400, message=message), 400
