from flask import Flask
from flask import send_from_directory
from flask import jsonify
from flask import request
from flask import abort
from flask import Response


# Flask initialisation
app = Flask(__name__)
