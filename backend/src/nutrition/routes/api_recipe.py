from flask import current_app, Blueprint, request

from nutrition.validate import validate_list_of, validate_equal_lengths
from nutrition.db.connection import get_connection
from nutrition.db.queries import (
    select_food_nutrient_total,
)

blueprint_recipe = Blueprint("recipe", __name__, url_prefix="/recipe")

@blueprint_recipe.post("/nutrients")
def get_recipe_nutrients():
    payload = request.get_json() or {}
    fdc_ids = validate_list_of( int,         payload.get("fdc_ids", []))
    amounts = validate_list_of((int, float), payload.get("amounts", []))
    fdc_ids, amounts = validate_equal_lengths(fdc_ids, amounts)

    with get_connection(current_app.config["DB_PATH"]) as con:
        result = select_food_nutrient_total(con, fdc_ids, amounts)

    return result, 200
