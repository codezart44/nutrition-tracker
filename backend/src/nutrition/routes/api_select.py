from flask import current_app, Blueprint, request, jsonify
from nutrition.db.connection import get_connection
from nutrition.db.queries import (
    select_food,
    select_nutrient,
    select_food_nutrient,
    select_food_nutrient_summed,
)

blueprint_select = Blueprint("select", __name__, url_prefix="/select")

@blueprint_select.post("/food")
def _select_food():
    payload = request.get_json() or {}
    fdc_ids = payload.get("fdc_ids", [])

    with get_connection(current_app.config["DB_PATH"]) as con:
        result = select_food(con, fdc_ids)

    return jsonify(result), 200
