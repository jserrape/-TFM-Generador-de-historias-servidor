import os, sys

from declaracionVariables import *
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

@app.route('/rest/status', methods=['GET'])
def get_status():
    response = Response(json.dumps( server_info, indent=4 ), status=200, mimetype='application/json')
    return response

@app.route('/rest/historia/<post_id>', methods=['POST'])
def POST_historia(post_id):
    #Insertar historia
    file = request.files['imagen_historia']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER_HISTORIA'], filename))
    nombre_historia = request.form["nombre_historia"]
    idioma_historia = request.form["idioma_historia"]
    imagen_historia = app.config['UPLOAD_FOLDER_HISTORIA'] + "/" + filename
    latitud_historia = request.form["latitud_historia"]
    longitud_historia = request.form["longitud_historia"]
    zoom = request.form["zoom"]
    descripcion_historia = request.form["descripcion_historia"]

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO historia (nombre_historia,idioma_historia,imagen_historia,latitud_historia,longitud_historia,zoom,descripcion_historia) VALUES (?,?,?,?,?,?,?)",(nombre_historia,idioma_historia,imagen_historia,latitud_historia,longitud_historia,zoom,descripcion_historia) )
        con.commit()
    con.close()

    #Insertar misiones
    for i in range(int(post_id)):
        num=i+1
        print(request.form)
        nombre_mision = request.form["nombre_mision_1"]
        print("Voy a insertar una mision:"+nombre_mision)


        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO mision (nombre_mision) VALUES (?)",(nombre_mision,) )
            con.commit()
        con.close()
    return "Ok"

@app.route('/rest/list/historia', methods=['GET'])
def GET_historia():
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
