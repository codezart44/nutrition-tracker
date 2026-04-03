from flask import Blueprint, request, jsonify
import sqlite3
import os
from pprint import pprint


db_path = os.path.dirname(os.path.dirname(__file__))+'/database/food.db'

fetch_blueprint = Blueprint(
    name='fetch',
    import_name=__name__,
    url_prefix='/fetch'
)

@fetch_blueprint.route('/all_items', methods=['GET'])
def fetch_all_items():
    try:
        sql_all = 'SELECT * FROM fndds_items'

        with sqlite3.connect(database=db_path) as con:
            cur = con.cursor()
            cur.execute(sql_all)
            items = cur.fetchall()
            cur.close()

        response = jsonify({
            'message': 'success',
            'content': {
                'items': items
            }
        }), 200
        return response
    
    except Exception:
        response = jsonify({
            'message': 'internal server error'
        }), 500
        return response


@fetch_blueprint.route('/item/<int:fdc_id>', methods=['GET'])
def fetch_item(fdc_id):
    try:
        sql_query = 'SELECT * FROM fndds_items WHERE fdc_id = ?'

        with sqlite3.connect(database=db_path) as con:
            cur = con.cursor()
            cur.execute(sql_query, (fdc_id,))
            item = cur.fetchone()
            cur.close()

        response = jsonify({
            'message': 'success',
            'content':{
                'item': item
            }
        }), 200

        return response    
    except Exception:
        response = jsonify({
            'message': 'internal server error'
        }), 500
        return response


@fetch_blueprint.route('/full_item/<int:fdc_id>', methods=['GET'])
def fetch_full_info(fdc_id):
    try:
        query_item = 'SELECT * FROM fndds_items WHERE fdc_id = ?'
        query_nutrients = 'SELECT * FROM fndds_nutrients WHERE fdc_id = ? ORDER BY nutrient_category'
        query_measures = 'SELECT * FROM fndds_measures WHERE fdc_id = ?'

        with sqlite3.connect(database=db_path) as con:
            cur = con.cursor()
            cur.execute(query_item, (fdc_id,))
            item = cur.fetchone()
            cur.execute(query_nutrients, (fdc_id,))
            nutrients = cur.fetchall()
            cur.execute(query_measures, (fdc_id,))
            measures = cur.fetchall()
            cur.close()

        response = jsonify({
            'message': 'success',
            'content':{
                'item': item,
                'nutrients': nutrients,
                'measures': measures
            }
        }), 200

        return response 
    except Exception:
        response = jsonify({
            'message': 'internal server error'
        }), 500
        return response


# @fetch_blueprint.route('/nutrients/<int:fdc_id>', methods=['GET'])
# def fetch_nutrients(fdc_id):
#     try:
#         sql_query = f"""
#         --sql
#         SELECT * FROM fndds_nutrients WHERE fdc_id = ?
#         ;
#         """
#         with sqlite3.connect(database=db_path) as con:
#             cur = con.cursor()
#             cur.execute(sql_query, fdc_id)
#             rows = cur.fetchall()
#             cur.close()

#         response = jsonify({
#             'message': 'success',
#             'content':rows
#         }), 200

#         return response    
#     except Exception:
#         response = jsonify({
#             'message': 'internal server error'
#         }), 500
#         return response


# @fetch_blueprint.route('/measures/<int:fdc_id>', methods=['GET'])
# def fetch_measures(fdc_id):
#     try:
#         sql_query = f"""
#         --sql
#         SELECT * FROM fndds_measures WHERE fdc_id = ?
#         ;
#         """
#         with sqlite3.connect(database=db_path) as con:
#             cur = con.cursor()
#             cur.execute(sql_query, fdc_id)
#             rows = cur.fetchall()
#             cur.close()

#         response = jsonify({
#             'message': 'success',
#             'content':rows
#         }), 200

#         return response 
#     except Exception:
#         response = jsonify({
#             'message': 'internal server error'
#         }), 500
#         return response