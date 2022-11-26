#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import redis
import time

app = Flask(__name__)
CORS(app)

r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

initial_state = {
    'time': '0',
    'count': '0',
    'Google': '0',
    'Facebook': '0',
    'Microsoft': '0',
    'Amazon': '0'
}


@app.route('/v1/reset_state', methods=['GET'])
def reset_state():
    r.mset(initial_state)
    return jsonify({})


@app.route('/v1/get_state', methods=['GET'])
def get_state():
    tracker_states = {}
    for key in initial_state.keys():
        tracker_states[key] = r.get(key)
    tracker_states['time'] = int(time.time())
    return jsonify(tracker_states)


@app.route('/v1/set_state', methods=['GET'])
def set_state():
    name = request.args.get('name')
    r.set('count', int(r.get('count')) + 1)
    r.set(name, int(time.time()))
    return jsonify({})


if __name__ == "__main__":
    app.run(debug=True)
