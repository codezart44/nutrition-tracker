from flask import current_app, Blueprint, request

from nutrition.validate import validate_list_of
from nutrition.db.connection import get_connection
from nutrition.db.queries import (
    select_nutrient,
)

blueprint_nutrient = Blueprint("nutrient", __name__, url_prefix="/nutrients")

@blueprint_nutrient.post("")
def get_nutrients():
    payload = request.get_json() or {}
    nutrient_ids = validate_list_of(int, payload.get("nutrient_ids", []))

    with get_connection(current_app.config["DB_PATH"]) as con:
        result = select_nutrient(con, nutrient_ids)

    return result, 200
