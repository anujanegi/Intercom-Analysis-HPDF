from flask import jsonify

def bad_request(message):
    return jsonify(code=400, message=message), 400

def Error(message):
    return jsonify(code=500, message=message), 500

def OK():
    return jsonify(code=200, message="Email sent!"), 200
