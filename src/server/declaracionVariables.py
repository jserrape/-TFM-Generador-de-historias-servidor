import os

import base64

import sqlite3 as sql

from werkzeug.utils import secure_filename

import json

from flask import Flask
from flask import send_from_directory
from flask import render_template
from flask import jsonify
from flask import request
from flask import abort
from flask import Response

# Flask initialisation
app = Flask(__name__)

UPLOAD_FOLDER_HISTORIA = "./documentos/imagenes_historias"
app.config['UPLOAD_FOLDER_HISTORIA'] = UPLOAD_FOLDER_HISTORIA

#BBDD https://www.python-course.eu/sql_python.php
#https://www.tutorialspoint.com/flask/flask_sqlite.htm
conn = sql.connect('database.db')
print("Opened database successfully")
conn.execute('DROP TABLE historia')
conn.execute('CREATE TABLE IF NOT EXISTS historia (nombre_historia TEXT PRIMARY KEY, idioma_historia TEXT, imagen_historia TEXT, latitud_historia INT, longitud_historia INT, zoom INT, descripcion_historia TEXT)')
#conn.execute('CREATE TABLE IF NOT EXISTS mision ()')
print("Table created successfully")
conn.close()

# Metadata
server_info = {}
server_info['desarrollador'] = 'Juan Carlos Serrano Pérez'
server_info['email'] = 'juan.carlos.wow.95@gmail.com'
server_info['twitter'] = '@xenahort'
server_info['server_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-servidor'
server_info['app_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-Android'
