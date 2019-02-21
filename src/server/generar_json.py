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
    con.close()
    return json.dumps(data)
