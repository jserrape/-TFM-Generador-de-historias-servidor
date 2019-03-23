import os, sys
import base64

import zipfile

import qrcode

import sqlite3 as sql

import json

from flask import Flask, redirect
from flask import render_template
from flask import jsonify
from flask import request
from flask import abort
from flask import Response
from flask import send_from_directory

import hashlib

import requests

import MySQLdb

# Flask initialisation
app = Flask(__name__)

#BBDD
conn = sql.connect('database.db')
print("Opened database successfully")
#conn.execute('DROP TABLE IF EXISTS historia')
#conn.execute('DROP TABLE IF EXISTS mision')
#conn.execute('DROP TABLE IF EXISTS usuario')
conn.execute('CREATE TABLE IF NOT EXISTS historia (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_historia TEXT, idioma_historia TEXT, imagen_historia BLOB, latitud_historia INT, longitud_historia INT, zoom INT, descripcion_historia TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS mision (id INTEGER PRIMARY KEY AUTOINCREMENT, id_historia INTEGER, nombre_mision TEXT, icono_mision BLOB, latitud_mision INT, longitud_mision INT, interaccion TEXT, codigo_interaccion TEXT, precedentes TEXT, pista_audio BLOB, descripcion TEXT, FOREIGN KEY(id_historia) REFERENCES historia(id))')
conn.execute('CREATE TABLE IF NOT EXISTS usuario (email TEXT PRIMARY KEY, nombre TEXT, password TEXT, imagen BLOB, ruta TEXT)')
print("Table created successfully")
conn.close()

#Crear directorio qr
directorio = "qr"
try:
    os.stat(directorio)
except:
    os.mkdir(directorio)

# Metadata
server_info = {}
server_info['desarrollador'] = 'Juan Carlos Serrano Pérez'
server_info['email'] = 'juan.carlos.wow.95@gmail.com'
server_info['twitter'] = '@xenahort'
server_info['server_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-servidor'
server_info['app_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-Android'


#Creo la bbdd sql
query = """DROP TABLE IF EXISTS usuario"""
execute_query(query)
query = """CREATE TABLE usuario (
                email    CHAR(30) NOT NULL PRIMARY KEY,
                nombre     CHAR(30),
                password CHAR(60),
                imagen BLOB,
                ruta CHAR(30) )"""
execute_query(query)



def execute_query(query):
    db = MySQLdb.connect(host='us-cdbr-gcp-east-01.cleardb.net',
                         user='b761ae150766d3',
                         passwd='4bcf3d10',
                         db='gcp_ca2ad2566039a3f0f01c',
                         port=3306)
    cursor = db.cursor()

    try:
        cursor.execute(query)
    except Exception as error:
        cursor.close()
        db.close()
        raise error

    db.commit()
    result = cursor.fetchall()
    cursor.close()
    db.close()
