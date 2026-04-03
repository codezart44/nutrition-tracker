from flask import Blueprint, session, request, make_response, jsonify
import json

test_blueprint = Blueprint(
    name='test',
    import_name=__name__,
    url_prefix='/test'
)

@test_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    response = jsonify({
        'message':'pong',
    }), 200
    return response

@test_blueprint.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    echo = data['content']
    response = jsonify({
        'content':echo
    }), 200
    return response
