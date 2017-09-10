#!/usr/bin/python3
"""
script that starts a Flask web application.
Fetch data from storage and prints html associated
with data
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states', methods=['GET'])
def fetch_cities():
    """
    fetches state data from storage and renders
    """
    state = storage.all('State').values()
    return (render_template('8-cities_by_states.html', state=state))


@app.teardown_appcontext
def route_close(exception):
    """
    closes storage after fetch
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
