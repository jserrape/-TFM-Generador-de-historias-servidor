from declaracionVariables import *
from generar_json import *

"""
Ruta para el registro de usuarios
"""
@app.route('/rest/usuario', methods=['POST', 'PUT'])
def POST_usuario():
    print("Ha llegado una peticion post")
    usu_dict = request.form.to_dict()
    print("dic mail: "+usu_dict['email'])
    existe = existe_usuario(usu_dict['email'])
    if existe:
        print("Ya existe el usuario")
        return Response(json.dumps( {'status': '400','resultado': 'Ya existe un usuario con ese email'}, indent=4 ), status=400, mimetype='application/json')
    else:
        print("El usuario no existe")
        #imagen_usu = str(base64.b64encode((request.files['imagen']).read()))
        #imagen_usu = str(imagen_usu[2:(len(imagen_usu))-1])
        #insertar_usuario(usu_dict['email'], usu_dict['nombre'], usu_dict['password'], usu_dict['imagen_usu'])
        insertar_usuario(usu_dict['email'], usu_dict['nombre'], usu_dict['password'], imagen_usu)
        return Response(json.dumps( {'status': '201','resultado': 'Se ha registrado correctamente'}, indent=4 ), status=201, mimetype='application/json')

"""
Vista auxiliar que muestra la tabla usuario
"""
@app.route('/rest/list/usuario', methods=['GET'])
def GET_usuarios():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from usuario")
   rows = cur.fetchall();
   return render_template("list_usuario.html",rows = rows)

"""
Vista para la edición de un usuario a partir de su email
"""
@app.route('/editar_usuario/<string:mail>', methods=['GET'])
def GET_editar_usuarios(mail):
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT * FROM usuario WHERE email='" + mail + "'")
   rows = cur.fetchall();
   return render_template("editar_usuario.html",rows = rows)

"""
Ruta para eliminar un usuario a partir de su email
"""
@app.route('/rest/delete/usuario/<string:mail>', methods=['DELETE'])
def DELETE_usuario(mail):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM usuario WHERE email='" + mail + "'")
        con.commit()
    con.close()
    return Response(json.dumps( {'status': '201'}, indent=4 ), status=201, mimetype='application/json')

"""
Ruta para actualizar el email de un usuario
"""
@app.route('/rest/update_mail/usuario', methods=['POST'])
def UPDATE_mail_usuario():
    emailNuevo = request.form['emailNuevo']
    correo = request.form['correo']
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE usuario SET email ='" + emailNuevo +"' WHERE email='" + correo +"'")
        con.commit()
    con.close()
    return Response(json.dumps( {'status': '201'}, indent=4 ), status=201, mimetype='application/json')

"""
Ruta para actualizar el nombre de un usuario
"""
@app.route('/rest/update_nombre/usuario', methods=['POST'])
def UPDATE_nombre_usuario():
    nombrelNuevo = request.form['nombreNuevo']
    correo = request.form['correo']
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE usuario SET nombre ='" + nombrelNuevo +"' WHERE email='" + correo +"'")
        con.commit()
    con.close()
    return Response(json.dumps( {'status': '201'}, indent=4 ), status=201, mimetype='application/json')

"""
Función para comprobar si existe un usuario
"""
def existe_usuario(email):
    print("Compruebo si existe el usuario")
    mail = False
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT email FROM usuario WHERE email="' + email + '"')
        for row in cur.fetchall():
            mail = True
    con.close()
    return mail

"""
Función para insertar un usuario
"""
def insertar_usuario(email, nombre, password, imagen):
    print("Inserto el nuevo usuario en la bbdd")
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO usuario (email, nombre, password, imagen) VALUES (?,?,?,?)",(email, nombre, password, imagen) )
        con.commit()
    con.close()
