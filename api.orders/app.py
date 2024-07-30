from flask import Flask
from api.blueprints.orders import orders_blueprint
from api.blueprints.products import products_blueprint
from api.models import db

_URL_PREFIX ='/api'
ORDERS_URL = f"{_URL_PREFIX}/orders"
PRODUCTS_URL = f"{_URL_PREFIX}/products"

app = Flask(__name__)

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

@app.route('/routes', methods=['GET'])
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.parse.unquote(f"{rule.endpoint:50s} {methods:20s} {rule}")
        output.append(line)
    return '<br>'.join(output)

app.register_blueprint(orders_blueprint, url_prefix=ORDERS_URL)
app.register_blueprint(products_blueprint, url_prefix=PRODUCTS_URL)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)