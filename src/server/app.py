from rutas_historias import *
from rutas_usuario import *
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
            data_min['descripcion'] = row[2]
            data_min['repetible'] = row[3]
            data_min['periodidad_dia'] = row[4]
            data_min['periodicidad_hora'] = row[5]
            data_max.append(data_min)
    con.close()

    respons['tareas'] = json.dumps(data_max)

    respons = jsonify(respons)
    respons.status_code = 201

    return respons
    
    
    
    
@app.route('/list/tarea_hoy')
def list_tareas_hoy():
    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/list/tarea'

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT t.*, strftime("%s",h.time), h.realizada FROM tarea t INNER JOIN historial h ON t.id = h.id_tarea WHERE date(h.time) = date("now")')
        data_max = []
        for row in cur.fetchall():
            data_min = {}
            data_min['id'] = row[0]
            data_min['nombre'] = row[1]
            data_min['descripcion'] = row[2]
            data_min['repetible'] = row[3]
            data_min['periodidad_dia'] = row[4]
            data_min['periodicidad_hora'] = row[5]
            data_min['time'] = row[6]
            data_min['realizada'] = row[7]
            data_max.append(data_min)
    con.close()

    respons['tareas'] = json.dumps(data_max)

    respons = jsonify(respons)
    respons.status_code = 201

    return respons
    
    
    
@app.route('/list/tarea_siguiente')
def list_tareas_siguiente():
    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/list/tarea'

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT t.*, strftime("%s",h.time), h.realizada FROM tarea t INNER JOIN historial h ON t.id = h.id_tarea WHERE date(h.time) > date("now") LIMIT 1')
        data_max = []
        for row in cur.fetchall():
            data_min = {}
            data_min['id'] = row[0]
            data_min['nombre'] = row[1]
            data_min['descripcion'] = row[2]
            data_min['repetible'] = row[3]
            data_min['periodidad_dia'] = row[4]
            data_min['periodicidad_hora'] = row[5]
            data_min['time'] = row[6]
            data_min['realizada'] = row[7]
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
            data_min['descripcion'] = row[2]
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
        cur.execute('SELECT h.id, h.id_tarea, strftime("%s",h.time), h.realizada FROM historial h WHERE id_tarea="' + id_tarea + '"')
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
========================================================================================
"""


@app.route('/rest/tarea', methods=['POST', 'PUT'])
def POST_usuario():
    print("Ha llegado una peticion post de tarea")
    tarea_dict = request.form.to_dict()
    ahora = datetime.datetime.utcnow()
    
    print(tarea_dict)
    
    nombre = tarea_dict['nombre']
    descripcion = tarea_dict['descripcion']
    repetible = tarea_dict['repetible']
    periodidad_dia = tarea_dict['periodidad_dia']
    periodicidad_hora = tarea_dict['periodicidad_hora']
    
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO tarea (nombre, descripcion, repetible, periodidad_dia, periodicidad_hora) VALUES (?,?,?,?,?)",(nombre,descripcion,repetible,periodidad_dia,periodicidad_hora) )
        
        if repetible == 'true':
            print("repetible es true")
            cur.execute("INSERT INTO historial (id_tarea, time, realizada) VALUES (?,?,?)",(1, ahora + datetime.timedelta(days=int(periodidad_dia),hours=int(periodicidad_hora)), 'null') )
        else:
            print("repetible es false")
            cur.execute("INSERT INTO historial (id_tarea, time, realizada) VALUES (?,?,?)",(1, ahora + datetime.timedelta(days=int(periodidad_dia),hours=int(periodicidad_hora)), 'null') )

        con.commit()
    con.close()

    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/rest/tarea'
    respons = jsonify(respons)
    respons.status_code = 201
    return respons


"""
========================================================================================
"""


@app.route('/rest/historia/confirmar', methods=['POST', 'PUT'])
def POST_confirmar():
    print("Ha llegado una peticion post de tarea")
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT t.*, strftime("%s",h.time), h.realizada FROM tarea t INNER JOIN historial h ON t.id = h.id_tarea WHERE date(h.time) > date("now") LIMIT 1')
        for row in cur.fetchall():
            id = row[0]
            cur.execute('UPDATE historia SET historial = "true" WHERE id="'+str(id)+'"')
            con.commit()
    con.close()


"""
Función de ejecución principal del sistema
"""
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    #crear_modelo()
    app.run(host='0.0.0.0', port=port, debug=False)
