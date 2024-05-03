#!/usr/bin/python3
"""
Create Flask App
"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


def not_found(error):
    """Handles 404 error using JSON formatted responses"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
