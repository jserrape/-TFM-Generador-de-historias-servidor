from declaracionVariables import *
from generar_json import *

@app.route('/historia/<id>', methods=['GET'])
def GET_historia(id):
    return historia_json(id)

@app.route('/mision/<id>', methods=['GET'])
def GET_mision(id):
    return mision_json(id)

@app.route('/misiones_asociadas/<id_historia>', methods=['GET'])
def GET_misiones_asociadas(id_historia):
    return misiones_historia_to_json(id_historia,True)

@app.route('/rest/historia/<post_id>', methods=['POST'])
def POST_historia(post_id):
    #Insertar historia
    nombre_historia = request.form["nombre_historia"]
    idioma_historia = request.form["idioma_historia"]
    imagen_historia = str(base64.b64encode((request.files['imagen_historia']).read()))
    latitud_historia = request.form["latitud_historia"]
    longitud_historia = request.form["longitud_historia"]
    zoom = request.form["zoom"]
    descripcion_historia = request.form["descripcion_historia"]

    imagen_historia = str(imagen_historia[2:(len(imagen_historia))-1])

    #decoded_string = base64.b64decode(imagen_historia)
    #with open("test_img.png", "wb") as image_file2:
    #    image_file2.write(decoded_string);


    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO historia (nombre_historia,idioma_historia,imagen_historia,latitud_historia,longitud_historia,zoom,descripcion_historia) VALUES (?,?,?,?,?,?,?)",(nombre_historia,idioma_historia,str(imagen_historia),latitud_historia,longitud_historia,zoom,descripcion_historia) )
        con.commit()
        cur.execute('SELECT id FROM historia WHERE nombre_historia="' + nombre_historia + '"')
        for row in cur.fetchall():
            id_historia = row[0]
    con.close()

    #Insertar misiones
    for i in range(int(post_id)):
        num=i+1

        nombre_mision = request.form["nombre_mision_"+str(num)]
        latitud_mision = request.form["latitud_mision_" + str(num) ]
        longitud_mision = request.form["longitud_mision_" + str(num)]
        interaccion = request.form["tipo_mision_" + str(num)]
        codigo_interaccion = request.form["codigo_tipo_mision_" + str(num)]
        precedentes = request.form["precedentes_mision_" + str(num)]
        descripcion = request.form["descripcion_mision_" + str(num)]

        #pista_audio = str(base64.b64encode((request.files['audio_mision_' + str(num)]).read()))
        pista_audio = ""
        icono_mision = str(base64.b64encode((request.files['icono_mision_' + str(num)]).read()))
        icono_mision = str(icono_mision[2:(len(icono_mision))-1])

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO mision (id_historia,nombre_mision,icono_mision,latitud_mision,longitud_mision,interaccion,codigo_interaccion,precedentes,pista_audio,descripcion) VALUES (?,?,?,?,?,?,?,?,?,?)",(id_historia,nombre_mision,icono_mision,latitud_mision,longitud_mision,interaccion,codigo_interaccion,precedentes,pista_audio,descripcion) )
            con.commit()
        con.close()

    return redirect("/historias", code=302)

@app.route('/rest/list/historia', methods=['GET'])
def GET_historias():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from historia")
   rows = cur.fetchall();
   print(rows)
   return render_template("list_historia.html",rows = rows)

@app.route('/rest/list/mision', methods=['GET'])
def GET_misiones():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from mision")
   rows = cur.fetchall();
   print(rows)
   return render_template("list_mision.html",rows = rows)
