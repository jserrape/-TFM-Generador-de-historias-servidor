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
UPLOAD_FOLDER_MISION_ICON = "./documentos/imagenes_misiones"
UPLOAD_FOLDER_MISION_AUDIO = "./documentos/audios_misiones"
app.config['UPLOAD_FOLDER_HISTORIA'] = UPLOAD_FOLDER_HISTORIA
app.config['UPLOAD_FOLDER_MISION_ICON'] = UPLOAD_FOLDER_MISION_ICON
app.config['UPLOAD_FOLDER_MISION_AUDIO'] = UPLOAD_FOLDER_MISION_AUDIO

#BBDD https://www.python-course.eu/sql_python.php
#https://www.tutorialspoint.com/flask/flask_sqlite.htm
conn = sql.connect('database.db')
print("Opened database successfully")
#conn.execute('DROP TABLE IF EXISTS historia')
#conn.execute('DROP TABLE IF EXISTS mision')
conn.execute('CREATE TABLE IF NOT EXISTS historia (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_historia TEXT, idioma_historia TEXT, imagen_historia TEXT, latitud_historia INT, longitud_historia INT, zoom INT, descripcion_historia TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS mision (id INTEGER PRIMARY KEY AUTOINCREMENT, id_historia INTEGER, nombre_mision TEXT, icono_mision TEXT, latitud_mision INT, longitud_mision INT, interaccion TEXT, codigo_interaccion TEXT, precedentes TEXT, pista_audio TEXT, descripcion TEXT, FOREIGN KEY(id_historia) REFERENCES historia(id))')
print("Table created successfully")
conn.close()

# Metadata
server_info = {}
server_info['desarrollador'] = 'Juan Carlos Serrano Pérez'
server_info['email'] = 'juan.carlos.wow.95@gmail.com'
server_info['twitter'] = '@xenahort'
server_info['server_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-servidor'
server_info['app_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-Android'
