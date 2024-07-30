from flask import Blueprint, jsonify

products_blueprint = Blueprint('products', __name__)

@products_blueprint.route('/', methods=['GET'], strict_slashes=False)
def get_products():
    products = [
        {
            "ProductID": 1,
            "ProductName": "Hat",
            "ProductPhotoURL": "http://example.com/hat.jpg",
            "ProductStatus": "Active"
        },
        {
            "ProductID": 2,
            "ProductName": "Shoes",
            "ProductPhotoURL": "http://example.com/shoes.jpg",
            "ProductStatus": "Active"
        }
    ]
    return jsonify(products)