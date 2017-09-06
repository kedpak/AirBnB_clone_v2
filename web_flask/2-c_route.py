#!/usr/bin/python3
"""
script that starts a Flask web application
/c/<text>: display "C " followed by the value of the text variable
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


@app.route('/c/<text>', methods=['GET'])
def c_route(text):
    return ('C %s' % text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
