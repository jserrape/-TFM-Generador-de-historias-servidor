import os, sys

from declaracionVariables import *
from generar_json import *
#from modelo import *

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/nueva_historia', methods=['GET'])
def get_nueva_historia():
    return render_template('nueva_historia.html')

@app.route('/monitorizacion', methods=['GET'])
def get_monitorizacion():
    return render_template('monitorizacion.html')

@app.route('/rutas', methods=['GET'])
def get_rutas():
    return render_template('rutas.html')

@app.route('/rest/status', methods=['GET'])
def get_status():
    response = Response(json.dumps( server_info, indent=4 ), status=200, mimetype='application/json')
    return response

@app.route('/historia/<id>', methods=['GET'])
def GET_historia(id):
    return historia_json(id)

@app.route('/rest/historia/<post_id>', methods=['POST'])
def POST_historia(post_id):
    #Insertar historia
    file = request.files['imagen_historia']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER_HISTORIA'], filename))
    nombre_historia = request.form["nombre_historia"]
    idioma_historia = request.form["idioma_historia"]
    imagen_historia = app.config['UPLOAD_FOLDER_HISTORIA'] + "/" + filename #<--------
    latitud_historia = request.form["latitud_historia"]
    longitud_historia = request.form["longitud_historia"]
    zoom = request.form["zoom"]
    descripcion_historia = request.form["descripcion_historia"]

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO historia (nombre_historia,idioma_historia,imagen_historia,latitud_historia,longitud_historia,zoom,descripcion_historia) VALUES (?,?,?,?,?,?,?)",(nombre_historia,idioma_historia,imagen_historia,latitud_historia,longitud_historia,zoom,descripcion_historia) )
        con.commit()
        cur.execute('SELECT id FROM historia WHERE nombre_historia="' + nombre_historia + '"')
        for row in cur.fetchall():
            id_historia = row[0]
    con.close()


    #Insertar misiones
    for i in range(int(post_id)):
        num=i+1

        nombre_mision = request.form["nombre_mision_"+str(num)]

        file = request.files['icono_mision_' + str(num)]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER_MISION_ICON'], filename))
        icono_mision = app.config['UPLOAD_FOLDER_MISION_ICON'] + "/" + filename #<--------

        latitud_mision = request.form["latitud_mision_" + str(num) ]
        longitud_mision = request.form["longitud_mision_" + str(num)]
        interaccion = request.form["tipo_mision_" + str(num)]
        codigo_interaccion = request.form["codigo_tipo_mision_" + str(num)]
        precedentes = request.form["precedentes_mision_" + str(num)]

        file = request.files['audio_mision_' + str(num)]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER_MISION_AUDIO'], filename))
        pista_audio = app.config['UPLOAD_FOLDER_MISION_AUDIO'] + "/" + filename

        descripcion = request.form["descripcion_mision_" + str(num)]


        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO mision (id_historia,nombre_mision,icono_mision,latitud_mision,longitud_mision,interaccion,codigo_interaccion,precedentes,pista_audio,descripcion) VALUES (?,?,?,?,?,?,?,?,?,?)",(id_historia,nombre_mision,icono_mision,latitud_mision,longitud_mision,interaccion,codigo_interaccion,precedentes,pista_audio,descripcion) )
            con.commit()
        con.close()

    return "Ok"

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
def GET_mision():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from mision")

   rows = cur.fetchall();
   print(rows)
   return render_template("list_mision.html",rows = rows)

@app.route('/rest/mision', methods=['POST', 'PUT'])
def POST_mision():
    mision_dict = request.form.to_dict()
    print('POST/PUT on mision: ' + str( mision_dict ))
    #nueva_historia = Historia(dict=historia_dict)
    return "Ok"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    #crear_modelo()
    app.run(host='0.0.0.0', port=port, debug=False)
