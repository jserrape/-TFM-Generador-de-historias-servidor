from declaracionVariables import *

def historia_json(id):
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
            data['misiones'] = []
            data['misiones'] = misiones_historia_to_json(row[0],False)
    con.close()
    return json.dumps(data)

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
