from declaracionVariables import *

"""
Función que devuelve una historia a partir de su id con todas
sus misiones en formato JSON
"""
def historia_json(id, email):
    print("llamada la fincion historia_json(id)")
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM historia WHERE id="' + str(id) + '"')
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
            data['misiones'] = []
            data['misiones'] = misiones_historia_to_json(row[0],False,email)
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
            #data['id'] = row[0]
            #data['id_historia'] = row[1]
            #data['nombre_mision'] = row[2]
            #data['icono_mision'] = row[3]
            #data['latitud_mision'] = row[4]
            #data['longitud_mision'] = row[5]
            data['tipo_localizacion'] = row[6]
            data['codigo_localizacion'] = row[7]
            data['tipo_prueba'] = row[8]
            data['codigo_prueba'] = row[9]
            data['descripcion_inicial'] = row[10]
            data['imagen_inicial'] = row[11]
            data['descripcion_final'] = row[12]
            data['imagen_final'] = row[13]
            #data['resumen'] = row[14]
            #data['precedentes'] = row[15]
    con.close()
    return json.dumps(data)

"""
Función que devuelve todas las misiones asociadas al id de una historia
en formato JSON o como cadena de texto
"""
def misiones_historia_to_json(id_historia, jso, email):
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
            #data_min['tipo_localizacion'] = row[6]
            #data_min['codigo_localizacion'] = row[7]
            #data_min['tipo_prueba'] = row[8]
            #data_min['codigo_prueba'] = row[9]
            #data_min['descripcion_inicial'] = row[10]
            #data_min['imagen_inicial'] = row[11]
            #data_min['descripcion_final'] = row[12]
            #data_min['imagen_final'] = row[13]
            data_min['resumen'] = row[14]
            data_min['precedentes'] = row[15]
            data_min['mision_final'] = row[16]
            data_min['completado'] = bool_mision_completada(email, row[1], row[0])
            data_max.append(data_min)
    con.close()
    if jso:
        return json.dumps(data_max)
    else:
        return data_max

def bool_mision_completada(email, id_historia, id_mision):
    val = 'False'
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT fecha FROM mision_usuario WHERE email="' + str(email) + '" AND id_historia="' + str(id_historia) + '" AND id_mision="' + str(id_mision) + '"')
        for row in cur.fetchall():
            val = row[0]
    con.close()
    return val

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

def misiones_pregunta_to_json(codigo_prueba_mision,jso):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM pregunta WHERE codigo_prueba_mision="' + str(codigo_prueba_mision) + '"')
        data = {}
        for row in cur.fetchall():
            data['id'] = row[0]
            data['enunciado'] = row[2]
            data['respues_correcta'] = row[3]
            data['respues_incorrecta_1'] = row[4]
            data['respues_incorrecta_2'] = row[5]
            data['respues_incorrecta_3'] = row[6]
    con.close()
    if jso:
        return json.dumps(data)
    else:
        return data
