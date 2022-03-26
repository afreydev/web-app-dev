import functools
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.company import (
    get_companies,
    get_company,
    create_company,
    get_company_by_name,
    update_company,
    delete_company,
)

bp = Blueprint('companies', __name__, url_prefix='/companies')
CORS(bp)

@bp.route('/', methods=['GET'])
def list():
    retorno = get_companies()
    return jsonify(retorno)

@bp.route('/<int:company_id>', methods=['GET'])
def get(company_id):
    return jsonify(get_company(company_id))

@bp.route('/by_name/<company_name>', methods=['GET'])
def get_by_name(company_name):
    return jsonify(get_company_by_name(company_name))

@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    name = data['name']
    description = data['description']
    return jsonify(create_company(name, description))

@bp.route('/<int:company_id>', methods=['PUT'])
def update(company_id):
    data = request.get_json()
    name = data['name']
    description = data['description']
    return jsonify(update_company(name, description, company_id))

@bp.route('/<int:company_id>', methods=['DELETE'])
def delete(company_id):
    return jsonify(delete_company(company_id))
