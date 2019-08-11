from declaracionVariables import *
from generar_json import *

from random import choice

"""
Vista que devuelve un JSON completo de una historia a partir de su id
"""
@app.route('/historia', methods=['POST', 'PUT'])
def GET_historia():
    print("ruta /historia/id funcion GET_historia")
    hist_dict = request.form.to_dict()
    return historia_json(hist_dict['id'], hist_dict['email'])

"""
Vista que devuelve un JSON completo de una mision a partir de su id
"""
@app.route('/mision_json', methods=['POST', 'PUT'])
def GET_mision_json():
    print("ruta /mision_json/id funcion GET_mision_json")
    mis_dict = request.form.to_dict()
    return mision_json(mis_dict['id'])

"""
Vista que devuelve un JSON completo de una pregunta a partir de su codigo_prueba_mision
"""
@app.route('/pregunta_json', methods=['POST', 'PUT'])
def GET_pregunta():
    print("ruta /pregunta_json/codigo_prueba_mision funcion GET_pregunta")
    pre_dict = request.form.to_dict()
    return misiones_pregunta_to_json(pre_dict['codigo_prueba_mision'],True)

"""
Vista que devuelve un JSON con el id y nombre de todas las historias
"""
@app.route('/historia/list', methods=['GET'])
def GET_historias_list():
    return historia_json_list()

"""
Vista que devuelve un JSON completo de una misión a partir de su id
"""
@app.route('/mision/<id>', methods=['GET'])
def GET_mision(id):
    return mision_json(id)

"""
Vista que devuelve el JSON completo de las misiones asociadas a un historia en formato JSON
"""
@app.route('/misiones_asociadas/<id_historia>', methods=['GET'])
def GET_misiones_asociadas(id_historia):
    return misiones_historia_to_json(id_historia,True)

"""
Ruta para el registro de una historia y sus misiones asociadas
"""
@app.route('/rest/historia/nueva', methods=['POST'])
def POST_historia():
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
        #cur.execute('SELECT id FROM historia WHERE nombre_historia="' + nombre_historia + '"')
        #for row in cur.fetchall():
        #    id_historia = row[0]
    con.close()

    #zip = zipfile.ZipFile('qr/qr_' + nombre_historia.replace(" ","_") + '.zip', 'w')

    """
    #Insertar misiones
    for i in range(int(post_id)):
        num=i+1
        #Nombre de la mision
        nombre_mision = request.form["nombre_mision_"+str(num)]

        #Icono de la mision
        icono_mision = str(base64.b64encode((request.files['icono_mision_' + str(num)]).read()))
        icono_mision = str(icono_mision[2:(len(icono_mision))-1])

        #Latitud de la mision
        latitud_mision = request.form["latitud_mision_" + str(num) ]

        #Longitud de la mision
        longitud_mision = request.form["longitud_mision_" + str(num)]

        #Localizacion
        tipo_localizacion = request.form["tipo_localizacion_" + str(num)]

        #Codigo de localización
        codigo_localizacion = request.form["codigo_localizacion_" + str(num)]

        #Tipo de prueba
        tipo_prueba = request.form["tipo_prueba_" + str(num)]

        #Código de la prueba
        if tipo_prueba == "qr":
            print("Encontrado qr")
            codigo_prueba = request.form["codigo_prueba_" + str(num)]
        else:
            codigo_prueba = str(id_historia) + "_" + nombre_mision

        #Descripcion inicial
        descripcion_inicial = request.form["descripcion_inicial_" + str(num)]

        #Imagen inicial
        imagen_inicial = str(base64.b64encode((request.files['imagen_inicial_' + str(num)]).read()))
        imagen_inicial = str(imagen_inicial[2:(len(imagen_inicial))-1])

        #Descipción final
        descripcion_final = request.form["descripcion_final_" + str(num)]

        #Imagen final
        imagen_final = str(base64.b64encode((request.files['imagen_final_' + str(num)]).read()))
        imagen_final = str(imagen_final[2:(len(imagen_final))-1])

        #Resumen
        resumen = request.form["resumen_" + str(num)]

        #Localizacion
        final = request.form["prueba" + str(num)]

        #Precedentes
        precedentes = request.form["precedentes_" + str(num)]

        #Misiones a cancelar
        misiones_a_cancelar = request.form["misiones_a_cancelar_" + str(num)]

        """"""
        interaccion = ""
        if interaccion == 'qr':
            img = qrcode.make(codigo_interaccion)
            f = open("qr/" + nombre_historia + "___" + nombre_mision + ".png", "wb")
            img.save(f)
            f.close()
            zip.write("qr/" + nombre_historia + "___" + nombre_mision + ".png", compress_type=zipfile.ZIP_DEFLATED)
            os.remove("qr/" + nombre_historia + "___" + nombre_mision + ".png")
        """"""

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO mision (id_historia, nombre_mision, icono_mision, latitud_mision, longitud_mision, tipo_localizacion, codigo_localizacion, tipo_prueba, codigo_prueba, descripcion_inicial, imagen_inicial, descripcion_final, imagen_final, resumen, precedentes, final, misiones_a_cancelar) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(id_historia, nombre_mision, icono_mision, latitud_mision, longitud_mision, tipo_localizacion, codigo_localizacion, tipo_prueba, codigo_prueba, descripcion_inicial, imagen_inicial, descripcion_final, imagen_final, resumen, precedentes, final, misiones_a_cancelar) )
            con.commit()
        con.close()

        if tipo_prueba == "pregunta":
            print("Voy a insertar la pregunta en la bbdd")
            #Enunciado
            enunciado = request.form["enunciado_" + str(num)]

            #Respuesta correcta
            respues_correcta = request.form["respues_correcta_" + str(num)]

            #Respuesta incorrecta 1
            respues_incorrecta_1 = request.form["respues_incorrecta_1_" + str(num)]

            #Respuesta incorrecta 2
            respues_incorrecta_2 = request.form["respues_incorrecta_2_" + str(num)]

            #Respuesta incorrecta 3
            respues_incorrecta_3 = request.form["respues_incorrecta_3_" + str(num)]

            #Inserto la pregunta en la bbdd
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO pregunta (codigo_prueba_mision, enunciado, respues_correcta, respues_incorrecta_1, respues_incorrecta_2, respues_incorrecta_3) VALUES (?,?,?,?,?,?)",(codigo_prueba, enunciado, respues_correcta, respues_incorrecta_1, respues_incorrecta_2, respues_incorrecta_3) )
                con.commit()
            con.close()
            """
    #zip.close()
    return redirect("privado/historias", code=302)

"""
Ruta para el registro de una historia y sus misiones asociadas
"""
@app.route('/rest/nueva_mision/<id_historia>', methods=['POST'])
def POST_mision(id_historia):
    print(request.form);
    #Nombre de la mision
    nombre_mision = request.form["nombre_mision"]

    #Icono de la mision
    icono_mision = str(base64.b64encode((request.files['icono_mision']).read()))
    icono_mision = str(icono_mision[2:(len(icono_mision))-1])

    #Latitud de la mision
    latitud_mision = request.form["latitud_mision"]

    #Longitud de la mision
    longitud_mision = request.form["longitud_mision"]

    #Localizacion
    tipo_localizacion = request.form["tipo_localizacion"]

    #Codigo de localización
    codigo_localizacion = request.form["codigo_localizacion"]

    #Miro si hay prueba
    bool_loc = request.form["prueba_loc_op"]

    if bool_loc == '1':
        print("if 1")
        #Tipo de prueba
        tipo_prueba = request.form["tipo_prueba"]

        #Código de la prueba
        if tipo_prueba == "qr":
            codigo_prueba = request.form["codigo_prueba"]
        else:
            codigo_prueba = str(id_historia) + "_" + nombre_mision
            print("Voy a insertar la pregunta en la bbdd")
            #Enunciado
            enunciado = request.form["enunciado"]

            #Respuesta correcta
            respues_correcta = request.form["respues_correcta"]

            #Respuesta incorrecta 1
            respues_incorrecta_1 = request.form["respues_incorrecta_1"]

            #Respuesta incorrecta 2
            respues_incorrecta_2 = request.form["respues_incorrecta_2"]

            #Respuesta incorrecta 3
            respues_incorrecta_3 = request.form["respues_incorrecta_3"]

            #Inserto la pregunta en la bbdd
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO pregunta (codigo_prueba_mision, enunciado, respues_correcta, respues_incorrecta_1, respues_incorrecta_2, respues_incorrecta_3) VALUES (?,?,?,?,?,?)",(codigo_prueba, enunciado, respues_correcta, respues_incorrecta_1, respues_incorrecta_2, respues_incorrecta_3) )
                con.commit()
            con.close()
    else:
        tipo_prueba = ""
        codigo_prueba = ""
        print("if 0")

    #Descripcion inicial
    descripcion_inicial = request.form["descripcion_inicial"]

    #Imagen inicial
    imagen_inicial = str(base64.b64encode((request.files['imagen_inicial']).read()))
    imagen_inicial = str(imagen_inicial[2:(len(imagen_inicial))-1])

    #Descipción final
    descripcion_final = request.form["descripcion_final"]

    #Imagen final
    imagen_final = str(base64.b64encode((request.files['imagen_final']).read()))
    imagen_final = str(imagen_final[2:(len(imagen_final))-1])

    #Resumen
    resumen = request.form["resumen"]

    #Precedentes
    precedentes = request.form["precedentes"]

    #Misiones a cancelar
    misiones_a_cancelar = request.form["misiones_a_cancelar"]

    #Final
    final = request.form["final"]

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO mision (id_historia, nombre_mision, icono_mision, latitud_mision, longitud_mision, tipo_localizacion, codigo_localizacion, tipo_prueba, codigo_prueba, descripcion_inicial, imagen_inicial, descripcion_final, imagen_final, resumen, precedentes, final, misiones_a_cancelar,bool_loc) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(id_historia, nombre_mision, icono_mision, latitud_mision, longitud_mision, tipo_localizacion, codigo_localizacion, tipo_prueba, codigo_prueba, descripcion_inicial, imagen_inicial, descripcion_final, imagen_final, resumen, precedentes, final, misiones_a_cancelar,bool_loc) )
        con.commit()
    con.close()

    return redirect("/privado/editar_historia/"+id_historia, code=302)

"""
Vista auxiliar que muestra la tabla historia
"""
@app.route('/rest/list/historia', methods=['GET'])
def GET_historias():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from historia")
   rows = cur.fetchall();
   print(rows)
   return render_template("list_historia.html",rows = rows)

"""
Vista auxiliar que muestra la tabla mision
"""
@app.route('/rest/list/mision', methods=['GET'])
def GET_misiones():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from mision")
   rows = cur.fetchall();
   print(rows)
   return render_template("list_mision.html",rows = rows)

"""
Vista auxiliar que muestra la tabla pregunta
"""
@app.route('/rest/list/pregunta', methods=['GET'])
def GET_preguntas():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from pregunta")
   rows = cur.fetchall();
   print(rows)
   return render_template("list_preguntas.html",rows = rows)

"""
Ruta para eliminar una historia y sus misiones asociadas
"""
@app.route('/rest/delete/historia/<string:id>', methods=['DELETE'])
def DELETE_historia(id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM mision WHERE id_historia='" + id + "'")
        cur.execute("DELETE FROM historia WHERE id='" + id + "'")
        con.commit()
    con.close()
    return Response(json.dumps( {'status': '201'}, indent=4 ), status=201, mimetype='application/json')

"""
Ruta para eliminar una misión
"""
@app.route('/rest/delete/mision/<string:id>', methods=['DELETE'])
def DELETE_mision(id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM mision WHERE id='" + id + "'")
        con.commit()
    con.close()
    return Response(json.dumps( {'status': '201'}, indent=4 ), status=201, mimetype='application/json')

"""
Ruta para eliminar una mision completada
"""
@app.route('/rest/delete/mision_completada/<string:email>_<string:id_historia>_<string:id_mision>', methods=['GET'])
def DELETE_mision_completada(email,id_historia,id_mision):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM mision_usuario WHERE email='" + email + "' AND id_historia='" + id_historia + "' AND id_mision='" + id_mision + "'")
        con.commit()
    con.close()
    return redirect("/rest/list/completado", code=302)

"""
Vista para la edición de una historia a partir de su id
"""
@app.route('/privado/editar_historia/<string:id>', methods=['GET'])
def GET_editar_historias(id):
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT * FROM historia WHERE id='" + id + "'")
   rows = cur.fetchall();

   cur.execute("SELECT id, nombre_mision FROM mision WHERE id_historia='" + id + "'")
   rowsM = cur.fetchall();

   return render_template("editar_historia.html",rows = rows, rowsM = rowsM)
