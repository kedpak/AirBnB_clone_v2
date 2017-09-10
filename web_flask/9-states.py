#!/usr/bin/python3
"""
fetch script that prints all states
fetches specific states based on input id
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', defaults={'id': ""}, methods=['GET'])
@app.route('/states/<id>')
def fetch_state(id):

    if id == "":
        state = storage.all('State').values()
        return (render_template('9-states.html', state=state, iden=id))
    else:
        try:
            state = storage.all('State').values()
            city_list = []
            city_id = []
            for i in state:
                if i.id == id:
                    state_name = i.name
                    for j in i.cities:
                        city_id.append(j.id)
                        city_list.append(j.name)
            return render_template('9-states.html', city_id=city_id,
                                   state_name=state_name, city_list=city_list)
        except:
            return render_template('9-states.html', city_id=None,
                                   state_name=None, city_list=None, iden=None)


@app.teardown_appcontext
def route_close(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
