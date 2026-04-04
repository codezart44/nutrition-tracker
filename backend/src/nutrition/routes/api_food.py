from flask import current_app, Blueprint, request

from nutrition.validate import validate_list_of
from nutrition.db.connection import get_connection
from nutrition.db.queries import (
    select_food,
    select_food_nutrient,
)

blueprint_food = Blueprint("food", __name__, url_prefix="/foods")

@blueprint_food.post("")
def get_foods():
    payload = request.get_json() or {}
    fdc_ids = validate_list_of(int, payload.get("fdc_ids", []))

    with get_connection(current_app.config["DB_PATH"]) as con:
        result = select_food(con, fdc_ids)

    return result, 200

@blueprint_food.post("/nutrients")
def get_foods_nutrients():
    payload = request.get_json() or {}
    fdc_ids = validate_list_of(int, payload.get("fdc_ids", []))

    with get_connection(current_app.config["DB_PATH"]) as con:
        result = select_food_nutrient(con, fdc_ids)

    return result, 200
