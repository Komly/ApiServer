from flask import jsonify

def response(text):
    return jsonify(
        {
            "response":
                text
        }
        )