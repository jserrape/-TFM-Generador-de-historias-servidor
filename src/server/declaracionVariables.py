import os

import json

from modelo.DAOHistoria import DAOHistoria

from modelo.Historia import Historia

from flask import Flask
from flask import send_from_directory
from flask import render_template
from flask import jsonify
from flask import request
from flask import abort
from flask import Response

import sqlite3

# Flask initialisation
app = Flask(__name__)

#BBDD https://www.python-course.eu/sql_python.php
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

# Metadata
server_info = {}
server_info['desarrollador'] = 'Juan Carlos Serrano Pérez'
server_info['email'] = 'juan.carlos.wow.95@gmail.com'
server_info['twitter'] = '@xenahort'
server_info['server_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-servidor'
server_info['app_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-Android'
