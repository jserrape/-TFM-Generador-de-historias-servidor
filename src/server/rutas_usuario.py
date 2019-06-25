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
        return Response(json.dumps( {'status': '400','resultado': 'Ya existe un usuario con ese email'}, indent=4 ), status=201, mimetype='application/json')
    else:
        print("El usuario no existe")
        #imagen_usu = str(base64.b64encode((request.files['imagen']).read()))
        #imagen_usu = str(imagen_usu[2:(len(imagen_usu))-1])
        #insertar_usuario(usu_dict['email'], usu_dict['nombre'], usu_dict['password'], usu_dict['imagen_usu'])
        insertar_usuario(usu_dict['email'], usu_dict['nombre'], usu_dict['password'], usu_dict['imagen_usu'])
        return Response(json.dumps( {'status': '201','resultado': 'Se ha registrado correctamente'}, indent=4 ), status=201, mimetype='application/json')

"""
Ruta para el login de los usuarios
"""
@app.route('/rest/login', methods=['POST', 'PUT'])
def POST_login():
    print("Ha llegado una peticion post de login")
    usu_dict = request.form.to_dict()
    correcto = passwordCprrecto(usu_dict['email'], usu_dict['password'])
    if correcto:
        print("Login correcto")
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO sesion (email) VALUES (?)",(usu_dict['email']) )
            con.commit()
        con.close()
        return Response(json.dumps( {'status': '200','resultado': datos_usuario(usu_dict['email'])}, indent=4 ), status=201, mimetype='application/json')
    else:
        print("Login incorrecto")
        return Response(json.dumps( {'status': '400','resultado': 'El usuario o la contraseña no son válidos'}, indent=4 ), status=201, mimetype='application/json')

"""
Ruta para completar misión de los usuarios
"""
@app.route('/rest/completar_mision', methods=['POST', 'PUT'])
def POST_completar_mision():
    print("Ha llegado una peticion post de mision completada")
    usu_dict = request.form.to_dict()
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO mision_usuario (email, id_historia, id_mision) VALUES (?,?,?)",(usu_dict['email'], usu_dict['id_historia'], usu_dict['id_mision']) )
        con.commit()
    con.close()
    return Response(json.dumps( {'status': '200','resultado': 'Misión completada con éxito'}, indent=4 ), status=201, mimetype='application/json')

"""
Ruta para solicitar un cambio de contraseña
"""
@app.route('/rest/cambio', methods=['POST', 'PUT'])
def POST_solicitar_cambio_password():
    print("Ha llegado una peticion post de cambio de contrseña")
    usu_dict = request.form.to_dict()
    ruta = hashlib.sha224(usu_dict['email'].encode('utf-8')).hexdigest()
    print("Email: " + usu_dict['email'])
    print("Ruta: " + ruta)
    #Inserto la ruta en la bbdd
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE usuario SET ruta ='" + ruta +"' WHERE email='" + usu_dict['email'] +"'")
        con.commit()
    con.close()

    #Envio email
    m = text("Se ha solicitado un cambio de contraseña de su cuenta de Historias Interactivas. Para cambiar su contraseña entre al siguiente enlace:\n\n\t " + ruta)
    m['From'] = mail_info['email']
    m['To'] = usu_dict['email']
    m['Subject'] = 'Cambio de contraseña: Historias interactivas'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mail_info['email'], mail_info['password'])
    server.sendmail(m['From'], m['To'], m.as_string())
    server.quit()
    return Response(json.dumps( {'status': '200','resultado': 'Solicitud de cambio de contraseña correcto'}, indent=4 ), status=201, mimetype='application/json')

"""
Ruta para cambiar la contraseña
"""
@app.route('/rest/cambio_password', methods=['POST', 'PUT'])
def POST_cambiar_password():
    print("Ha llegado una peticion post de cambio de contrseña")
    usu_dict = request.form.to_dict()
    #Inserto la nueva password en la bbdd
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE usuario SET password ='" + usu_dict['pass'] +"' WHERE email='" + usu_dict['email'] +"'")
        con.commit()
    con.close()
    return Response(json.dumps( {'status': '200','resultado': 'Solicitud de cambio de contraseña correcto'}, indent=4 ), status=201, mimetype='application/json')

"""
Ruta para eliminar usuario
"""
@app.route('/rest/eliminar_usuario', methods=['DELETE'])
def POST_eliminar_usuario():
    print("Ha llegado una peticion DELETE de eliminar usuario")
    usu_dict = request.form.to_dict()
    #Elimino el usuario de la bbdd
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM sesion WHERE email='" + usu_dict['email'] +"'")
        cur.execute("DELETE FROM mision_usuario WHERE email='" + usu_dict['email'] +"'")
        cur.execute("DELETE FROM usuario WHERE email='" + usu_dict['email'] +"'")
        con.commit()
    con.close()
    return Response(json.dumps( {'status': '200','resultado': 'Solicitud de cambio de contraseña correcto'}, indent=4 ), status=201, mimetype='application/json')

"""
Vista para cambiar la contraseña de un usuario
"""
@app.route('/usuario/<cod>', methods=['GET'])
def GET_cambio_password(cod):
    mail = False
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT email FROM usuario WHERE ruta="' + cod + '"')
        for row in cur.fetchall():
            mail = True
    con.close()
    if mail:
        return render_template('cambiar_contraseña.html')
    else:
        return render_template('404.html'), 404


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
Vista auxiliar que muestra la tabla sesiones
"""
@app.route('/rest/list/sesion', methods=['GET'])
def GET_sesiones():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from sesion")
   rows = cur.fetchall();
   return render_template("list_sesion.html",rows = rows)


"""
Vista auxiliar que muestra la tabla de misiones completadas
"""
@app.route('/rest/list/completado', methods=['GET'])
def GET_mision_completada():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from mision_usuario")
   rows = cur.fetchall();
   return render_template("list_mision_completada.html",rows = rows)

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
Ruta para actualizar la contraseña de un usuario
"""
@app.route('/rest/update_password/usuario', methods=['POST'])
def update_password_usuario():
    print("Peticion POST de cambio de contraseña")
    data = request.data.decode("utf-8").split("&")
    data[0] = data[0].replace("ruta=","")
    data[1] = data[1].replace("password=","")
    print(data)
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE usuario SET password ='" + data[1] +"' WHERE ruta='" + data[0] +"'")
        cur.execute("UPDATE usuario SET ruta ='' WHERE ruta='" + data[0] +"'")
        con.commit()
    con.close()
    return Response(json.dumps( {'status': '201'}, indent=4 ), status=201, mimetype='application/json')

"""
Ruta para eliminar el progreso de un usuario en una historia
"""
@app.route('/rest/delete/progreso_historia', methods=['DELETE'])
def DELETE_progreso_historia():
    print("Ha llegado una peticion post")
    usu_dict = request.form.to_dict()
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM mision_usuario WHERE email='" + usu_dict['email'] + "' AND id_historia='" + usu_dict['id_historia'] + "'")
        con.commit()
    con.close()

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
Comprueba si una contraseña está asociada a un correo
"""
def passwordCprrecto(email, password):
    res = False
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT email FROM usuario WHERE email="' + email + '" AND password="' + password + '"')
        for row in cur.fetchall():
            res = True
    con.close()
    return res

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
