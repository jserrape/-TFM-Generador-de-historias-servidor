from declaracionVariables import *
from generar_json import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        return Response(json.dumps( {'status': '200','resultado': 'Inicio de sesión correcto'}, indent=4 ), status=201, mimetype='application/json')
    else:
        print("Login incorrecto")
        return Response(json.dumps( {'status': '400','resultado': 'El usuario o la contraseña no son válidos'}, indent=4 ), status=201, mimetype='application/json')

"""
Ruta para solicitar un cambio de contraseña
"""
@app.route('/rest/cambio', methods=['POST', 'PUT'])
def POST_cambio_password():
    print("Ha llegado una peticion post de cambio de contrseña")
    usu_dict = request.form.to_dict()
    ruta = hashlib.sha224(usu_dict['email'].encode('utf-8')).hexdigest()
    #Inserto la ruta en la bbdd
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE usuario SET ruta ='" + ruta +"' WHERE email='" + usu_dict['email'] +"'")
        con.commit()
    con.close()
    #Envio email
    # create message object instance
    msg = MIMEMultipart()

    message = "Ha solicitado un cambio de contraseña de Historias interactivas. Para cambiar su contraseña acceda al siguiente enlace:\n https://tfm-historias.herokuapp.com/usuario/" + ruta

    # setup the parameters of the message
    password = "jcsp0003"
    msg['From'] = "gestor.predictivo@gmail.com"
    msg['To'] = usu_dict['email']
    msg['Subject'] = "Cambio de contraseña: Historias interactivas"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    return "Correo enviado"

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
