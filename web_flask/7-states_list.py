#!/usr/bin/python3
"""
script that starts a Flask web application.
uses storages for fetching data
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list', methods=['GET'])
def fetch_state():
    state = storage.all('State').values()
    return (render_template('7-states_list.html', state=state))


@app.teardown_appcontext
def route_close(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
