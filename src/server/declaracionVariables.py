import os

import sqlite3 as sql

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

#BBDD https://www.python-course.eu/sql_python.php
#https://www.tutorialspoint.com/flask/flask_sqlite.htm
conn = sql.connect('database.db')
print("Opened database successfully")
conn.execute('DROP TABLE historia')
conn.execute('CREATE TABLE IF NOT EXISTS historia (nombre_historia TEXT PRIMARY KEY, idioma_historia TEXT, imagen_historia BLOB, latitud_historia INT, longitud_historia INT, zoom INT, descripcion_historia TEXT)')
print("Table created successfully")
conn.close()

# Metadata
server_info = {}
server_info['desarrollador'] = 'Juan Carlos Serrano Pérez'
server_info['email'] = 'juan.carlos.wow.95@gmail.com'
server_info['twitter'] = '@xenahort'
server_info['server_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-servidor'
server_info['app_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-Android'
