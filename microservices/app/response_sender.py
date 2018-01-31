from flask import jsonify

def bad_request(message):
    return jsonify(code=400, message=message), 400

def Error(code, message):
    return jsonify(code=code, message=message), code

def OK():
    return jsonify(code=200, message="Email sent!"), 200
