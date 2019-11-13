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

conn.execute('CREATE TABLE IF NOT EXISTS tarea (id INTEGER PRIMARY KEY, nombre TEXT, descripcion TEXT, repetible BOOLEAN, periodidad_dia TEXT, periodicidad_hora TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS historial (id INTEGER PRIMARY KEY AUTOINCREMENT, id_tarea INTEGER, time TEXT, realizada TEXT)')

print("Table created successfully")
conn.close()



ahora = datetime.datetime.utcnow()
with sql.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("INSERT INTO tarea (id,nombre, descripcion, repetible, periodidad_dia, periodicidad_hora) VALUES (?,?,?,?,?,?)",
    (1,'Toma de pastillas', 'Recuerde tomar las pastillas del desayuno tiene que tomar la pastilla de tensión y la del azucar', 'false', '','') )
    cur.execute("INSERT INTO tarea (id,nombre, descripcion, repetible, periodidad_dia, periodicidad_hora) VALUES (?,?,?,?,?,?)",
    (2,'Recogida de niños', 'Recoger a los nietos del colegio para llevarlos a natación', 'false', '','') )
    cur.execute("INSERT INTO historial (id_tarea, time, realizada) VALUES (?,?,?)",(1, ahora + datetime.timedelta(days=1), 'null') )
    cur.execute("INSERT INTO historial (id_tarea, time, realizada) VALUES (?,?,?)",(2, ahora + datetime.timedelta(days=1), 'null') )
    
    
    con.commit()
con.close()



