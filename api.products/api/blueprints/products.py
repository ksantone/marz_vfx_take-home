from flask import Blueprint, jsonify
from models import Products

products_blueprint = Blueprint('products', __name__)

@products_blueprint.route('/', methods=['GET'])
def get_products():
    try:
        products = Products.select().where(Products.ProductStatus == 'Active').dicts()
        products_list = list(products)
    except Exception as err:
        return jsonify({'message': str(err)}), 500
    return jsonify(products_list)