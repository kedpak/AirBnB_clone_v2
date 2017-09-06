#!/usr/bin/python3
"""
Script that starts a Flask web application.
/: display "Hello HBNB!"
/hbnb: display "HBNB"
"""

from flask import Flask
from flask import request


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def hello_route():
    return ("Hello HBNB!")


@app.route('/hbnb', methods=['GET'])
def hbnb_route():
    return ("HBNB")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
