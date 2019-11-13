import os, sys
import base64
import datetime


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


conn.execute('DROP TABLE IF EXISTS tarea')
conn.execute('DROP TABLE IF EXISTS historial')

conn.execute('CREATE TABLE IF NOT EXISTS tarea (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, descripcion TEXT, repetible BOOLEAN, periodidad_dia TEXT, periodicidad_hora TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS historial (id INTEGER PRIMARY KEY AUTOINCREMENT, id_tarea INTEGER, time TEXT, realizada TEXT)')

print("Table created successfully")
conn.close()



ahora = datetime.datetime.utcnow()
with sql.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("INSERT INTO tarea (nombre, descripcion, repetible, periodidad_dia, periodicidad_hora) VALUES (?,?,?,?,?)",('TArea de prueba 1', 'Pastilla del corazon e irte a la PUTTA cama.', 'false', '','') )
    cur.execute("INSERT INTO historial (id_tarea, time, realizada) VALUES (?,?,?)",(1, ahora + datetime.timedelta(days=1), 'null') )
    con.commit()
con.close()



