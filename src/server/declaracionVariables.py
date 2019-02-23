import os

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

#BBDD
conn = sql.connect('database.db')
print("Opened database successfully")
#conn.execute('DROP TABLE IF EXISTS historia')
#conn.execute('DROP TABLE IF EXISTS mision')
conn.execute('CREATE TABLE IF NOT EXISTS historia (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_historia TEXT, idioma_historia TEXT, imagen_historia BLOB, latitud_historia INT, longitud_historia INT, zoom INT, descripcion_historia TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS mision (id INTEGER PRIMARY KEY AUTOINCREMENT, id_historia INTEGER, nombre_mision TEXT, icono_mision BLOB, latitud_mision INT, longitud_mision INT, interaccion TEXT, codigo_interaccion TEXT, precedentes TEXT, pista_audio BLOB, descripcion TEXT, FOREIGN KEY(id_historia) REFERENCES historia(id))')
print("Table created successfully")
conn.close()

# Metadata
server_info = {}
server_info['desarrollador'] = 'Juan Carlos Serrano Pérez'
server_info['email'] = 'juan.carlos.wow.95@gmail.com'
server_info['twitter'] = '@xenahort'
server_info['server_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-servidor'
server_info['app_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-Android'
