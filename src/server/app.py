from rutas_historias import *
from rutas_usuario import *
from open import *
from flask import send_file









@app.route('/list/tarea')
def list_users():
    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/list/tarea'

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM tarea')
        data_max = []
        for row in cur.fetchall():
            data_min = {}
            data_min['id'] = row[0]
            data_min['nombre'] = row[1]
            data_min['descripcon'] = row[2]
            data_min['repetible'] = row[3]
            data_min['periodidad_dia'] = row[4]
            data_min['periodicidad_hora'] = row[5]
            data_max.append(data_min)
    con.close()

    respons['tareas'] = json.dumps(data_max)

    respons = jsonify(respons)
    respons.status_code = 201

    return respons

@app.route('/list/historial')
def list_historial():
    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/list/historial'

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM historial')
        data_max = []
        for row in cur.fetchall():
            data_min = {}
            data_min['id'] = row[0]
            data_min['id_tarea'] = row[1]
            data_min['time'] = row[2]
            data_min['realizada'] = row[3]
            data_max.append(data_min)
    con.close()

    respons['tareas'] = json.dumps(data_max)

    respons = jsonify(respons)
    respons.status_code = 201

    return respons


@app.route('/list/tarea/<id_tarea>', methods=['GET'])
def get_tarea(id_tarea):
    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/list/tarea'

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM tarea WHERE id="' + id_tarea + '"')
        data_max = []
        for row in cur.fetchall():
            data_min = {}
            data_min['id'] = row[0]
            data_min['nombre'] = row[1]
            data_min['descripcon'] = row[2]
            data_min['repetible'] = row[3]
            data_min['periodidad_dia'] = row[4]
            data_min['periodicidad_hora'] = row[5]
            data_max.append(data_min)
    con.close()

    respons['tareas'] = json.dumps(data_max)

    respons = jsonify(respons)
    respons.status_code = 201

    return respons

@app.route('/list/historial/<id_historial>', methods=['GET'])
def get_historial_id(id_historial):
    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/list/historial/id'

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM historial WHERE id="' + id_historial + '"')
        data_max = []
        for row in cur.fetchall():
            data_min = {}
            data_min['id'] = row[0]
            data_min['id_tarea'] = row[1]
            data_min['time'] = row[2]
            data_min['realizada'] = row[3]
            data_max.append(data_min)
    con.close()

    respons['tareas'] = json.dumps(data_max)

    respons = jsonify(respons)
    respons.status_code = 201

    return respons



@app.route('/list/historial_tarea/<id_tarea>', methods=['GET'])
def get_historial_id_tarea(id_tarea):
    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/list/historial/id_tarea'

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM historial WHERE id_tarea="' + id_tarea + '"')
        data_max = []
        for row in cur.fetchall():
            data_min = {}
            data_min['id'] = row[0]
            data_min['id_tarea'] = row[1]
            data_min['time'] = row[2]
            data_min['realizada'] = row[3]
            data_max.append(data_min)
    con.close()

    respons['tareas'] = json.dumps(data_max)

    respons = jsonify(respons)
    respons.status_code = 201

    return respons


"""
Función de ejecución principal del sistema
"""
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    #crear_modelo()
    app.run(host='0.0.0.0', port=port, debug=False)
