#!/usr/bin/python3
"""Create Flask app and app_views""""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def api_status():
    return jsonify({"status": "OK"})
