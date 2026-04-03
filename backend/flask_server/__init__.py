from flask import Flask, session
from flask_cors import CORS
from flask_session import Session

# import blueprints
from routes.test_api import test_blueprint
from routes.fetch_api import fetch_blueprint



def create_app() -> Flask:
    app = Flask(__file__)

    CORS(app=app)

    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app=app)

    # register blueprints
    app.register_blueprint(blueprint=test_blueprint)
    app.register_blueprint(blueprint=fetch_blueprint)

    # implement later on
    # app.register_error_handler()

    return app
