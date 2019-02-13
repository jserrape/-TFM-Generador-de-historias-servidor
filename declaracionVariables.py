import os

from flask import Flask
from flask import send_from_directory
from flask import render_template
from flask import jsonify
from flask import request
from flask import abort
from flask import Response


# Flask initialisation
app = Flask(__name__)

# HTML file directories
HTML_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'website', 'html')
CSS_DIR  = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'website', 'css')
IMG_DIR  = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'website', 'img')
