from flask import Flask
from flask_cors import CORS
from nutrition.config import Config

from nutrition.routes.api_select import blueprint_select

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app=app)

    app.register_blueprint(blueprint=blueprint_select)
    # app.register_error_handler() FIXME

    return app
