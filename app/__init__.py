from flask import Flask, request
import app.controller

def Server():
    controller = app.controller

    server = Flask(__name__)
    server.add_url_rule("/method/<method>", methods=["POST", "GET"], view_func=controller.methods)
    server.run(debug=True)