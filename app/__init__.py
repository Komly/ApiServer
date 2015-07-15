from flask import Flask, request

def create_app():
    app = Flask(__name__)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/method')

    return app
