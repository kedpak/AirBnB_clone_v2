#!/usr/bin/python3
"""
Script starts a flask web application.
Listens on 0.0.0.0. at port 5000
strict_slashes=False your route definition
"""

from flask import Flask
from flask import request


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def hello_route():
    return ("Hello HBNB!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
