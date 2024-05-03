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

@app.teardown_appcontext
def teardown(exception):
    storage.close()

if __name__ == "__main__":
  HOST = getenv('HBNB_API_HOST', '0.0.0.0')
  PORT = int(getenv('HBNB_API_PORT', 5000))
  app.run(hosts=HOST, port=PORT, threaded=True)
