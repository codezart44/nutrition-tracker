from flask import Flask
from flask_cors import CORS
from nutrition.config import Config

from nutrition.routes.api_food import blueprint_food
from nutrition.routes.api_nutrient import blueprint_nutrient
from nutrition.routes.api_recipe import blueprint_recipe
from nutrition.errors import ValidationError, validation_error

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app=app)

    app.register_blueprint(blueprint=blueprint_food)
    app.register_blueprint(blueprint=blueprint_nutrient)
    app.register_blueprint(blueprint=blueprint_recipe)
    app.register_error_handler(ValidationError, validation_error)

    return app
