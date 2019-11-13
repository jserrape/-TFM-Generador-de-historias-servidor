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

import smtplib
from email.mime.text import MIMEText as text

from random import choice

# Flask initialisation
app = Flask(__name__)

#BBDD
conn = sql.connect('database.db')
print("Opened database successfully")
#conn.execute('DROP TABLE IF EXISTS historia')
#conn.execute('DROP TABLE IF EXISTS mision')
#conn.execute('DROP TABLE IF EXISTS usuario')
#conn.execute('DROP TABLE IF EXISTS pregunta')
#conn.execute('DROP TABLE IF EXISTS mision_usuario')
conn.execute('CREATE TABLE IF NOT EXISTS historia (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_historia TEXT, idioma_historia TEXT, imagen_historia BLOB, latitud_historia INT, longitud_historia INT, zoom INT, descripcion_historia TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS mision (id INTEGER PRIMARY KEY AUTOINCREMENT, id_historia INTEGER, nombre_mision TEXT, icono_mision BLOB, latitud_mision INT, longitud_mision INT, tipo_localizacion TEXT, codigo_localizacion TEXT, tipo_prueba TEXT, codigo_prueba TEXT, descripcion_inicial TEXT, imagen_inicial BLOB, descripcion_final TEXT, imagen_final BLOB, resumen TEXT, precedentes TEXT, final INTEGER, misiones_a_cancelar TEXT,bool_loc TEXT, FOREIGN KEY(id_historia) REFERENCES historia(id))')
conn.execute('CREATE TABLE IF NOT EXISTS usuario (email TEXT PRIMARY KEY, nombre TEXT, password TEXT, imagen BLOB, ruta TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS pregunta (id INTEGER PRIMARY KEY AUTOINCREMENT, codigo_prueba_mision TEXT, enunciado TEXT, respues_correcta TEXT, respues_incorrecta_1 TEXT, respues_incorrecta_2 TEXT, respues_incorrecta_3 TEXT, FOREIGN KEY(codigo_prueba_mision) REFERENCES mision(codigo_prueba))')
conn.execute('CREATE TABLE IF NOT EXISTS mision_usuario (email TEXT, id_historia INTEGER, id_mision INTEGER, fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP, primary key(email, id_historia, id_mision))')
conn.execute('CREATE TABLE IF NOT EXISTS sesion (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(email) REFERENCES usuario(email))')




#conn.execute('DROP TABLE IF EXISTS tarea')

#conn.execute('CREATE TABLE IF NOT EXISTS tarea (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, descripcion TEXT, repetible BOOLEAN, periodidad_dia TEXT, periodicidad_hora TEXT)')
#conn.execute('CREATE TABLE IF NOT EXISTS historial (id INTEGER PRIMARY KEY AUTOINCREMENT, id_tarea INTEGER, time timestamp, realizada )')

print("Table created successfully")
conn.close()




with sql.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("INSERT INTO tarea (nombre, descripcion, repetible, periodidad_dia, periodicidad_hora) VALUES (?,?,?,?,?)",('TArea de prueba 1', 'Pastilla del corazon', 'false', '','') )
    con.commit()

con.close()






# Información general
server_info = {}
server_info['desarrollador'] = 'Juan Carlos Serrano Pérez'
server_info['email'] = 'juan.carlos.wow.95@gmail.com'
server_info['twitter'] = '@xenahort'
server_info['server_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-servidor'
server_info['app_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-Android'

# Información de email
mail_info = {}
mail_info['email'] = 'mail'
mail_info['password'] = 'password'
