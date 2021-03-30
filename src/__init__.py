from flask import Flask
from src.controller import process
from flask_cors import CORS, cross_origin

service = Flask(__name__)

cors = CORS(service, resources={r"/*": {"origins": "http://0.0.0.0:3007"}})

service.register_blueprint(process)