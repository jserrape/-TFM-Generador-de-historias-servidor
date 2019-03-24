from declaracionVariables import *

"""
Función que devuelve una historia a partir de su id con todas
sus misiones en formato JSON
"""
def historia_json(id):
    print("llamada la fincion historia_json(id)")
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM historia WHERE id="' + id + '"')
        data = {}
        for row in cur.fetchall():
            data['id'] = row[0]
            data['nombre_historia'] = row[1]
            data['idioma_historia'] = row[2]
            data['imagen_historia'] = row[3]
            data['latitud_historia'] = row[4]
            data['longitud_historia'] = row[5]
            data['zoom'] = row[6]
            data['descripcion_historia'] = row[7]
            #data['misiones'] = []
            #data['misiones'] = misiones_historia_to_json(row[0],False)
    con.close()
    print("Han solicitado los datos de la mision con id="+str(id))
    print(json.dumps(data))
    return json.dumps(data)

"""
Función que devuelve en formato JSON todas las historias con sus atributos id y nombre
"""
def historia_json_list():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT id, nombre_historia FROM historia')
        data_max = []
        for row in cur.fetchall():
            data_min = {}
            data_min['id'] = row[0]
            data_min['nombre_historia'] = row[1]
            data_max.append(data_min)
    con.close()
    return  json.dumps(data_max)

"""
Función que devuelve una misión a partir de su id en formato JSON
"""
def mision_json(id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM mision WHERE id="' + str(id) + '"')
        data = {}
        for row in cur.fetchall():
            data['id'] = row[0]
            data['id_historia'] = row[1]
            data['nombre_mision'] = row[2]
            data['icono_mision'] = row[3]
            data['latitud_mision'] = row[4]
            data['longitud_mision'] = row[5]
            data['interaccion'] = row[6]
            data['codigo_interaccion'] = row[7]
            data['precedentes'] = row[8]
            data['pista_audio'] = row[9]
            data['descripcion'] = row[10]
    con.close()
    return json.dumps(data)

"""
Función que devuelve todas las misiones asociadas al id de una historia
en formato JSON o como cadena de texto
"""
def misiones_historia_to_json(id_historia,jso):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM mision WHERE id_historia="' + str(id_historia) + '"')
        data_max = []
        for row in cur.fetchall():
            data_min = {}
            data_min['id'] = row[0]
            data_min['id_historia'] = row[1]
            data_min['nombre_mision'] = row[2]
            data_min['icono_mision'] = row[3]
            data_min['latitud_mision'] = row[4]
            data_min['longitud_mision'] = row[5]
            data_min['interaccion'] = row[6]
            data_min['codigo_interaccion'] = row[7]
            data_min['precedentes'] = row[8]
            data_min['pista_audio'] = row[9]
            data_min['descripcion'] = row[10]
            data_max.append(data_min)
    con.close()
    if jso:
        return json.dumps(data_max)
    else:
        return data_max

def datos_usuario(email):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT email, nombre, imagen FROM usuario WHERE email="' + email + '"')
        data = {}
        for row in cur.fetchall():
            data['email'] = row[0]
            data['nombre'] = row[1]
            data['imagen'] = row[2]
    con.close()
    return json.dumps(data)
