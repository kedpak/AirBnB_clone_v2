#!/usr/bin/python3
"""
Script that starts a Flask web application.
/number_odd_or_even/<n>: display a HTML page only if n is an integer
"""

from flask import Flask
from flask import render_template


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


@app.route('/', defaults={'text': 'Python is cool'})
@app.route('/python/<text>', methods=['GET'])
def python_route(text):
    return ('Python %s' % text.replace('_', ' '))


@app.route('/number/<int:n>', methods=['GET'])
def num_route(n):
    return ('%d is a number' % n)


@app.route('/number_template/<int:n>')
def template_route(n):
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>')
def odd_even_route(n):
    return (render_template('6-number_odd_or_even.html', n=n))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
