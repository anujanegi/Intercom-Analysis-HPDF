from flask import jsonify

def bad_request(message):
    return jsonify(code=400, message=message), 400

def Error(code = None, message):
    if code is None:
        return jsonify(code=500, message=message), 500
    return jsonify(code=code, message=message), code

def OK():
    return jsonify(code=200, message="Email sent!"), 200
