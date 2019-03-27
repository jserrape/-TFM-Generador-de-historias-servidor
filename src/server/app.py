from rutas_historias import *
from rutas_usuario import *
from flask import send_file

"""
Vista principal de la web que muestra información de la aplicación
"""
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

"""
Vista para crear una nueva historia y sus misiones asociadas
"""
@app.route('/nueva_historia', methods=['GET'])
def get_nueva_historia():
    return render_template('nueva_historia.html')

"""
Vista que permite ver un listado con los principales datos de los usuarios
y permite su borrado e ir a una nueva vista para su edición
"""
@app.route('/usuarios', methods=['GET'])
def get_gestionar_usuarios():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT email, nombre FROM usuario")
    rows = cur.fetchall();
    return render_template('gestionar_usuarios.html',rows = rows)

"""
Vista que permite ver un listado con los principales datos de las historias
y permite su borrado e ir a una nueva vista para su edición
"""
@app.route('/historias', methods=['GET'])
def get_gestionar_historias():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT id, nombre_historia FROM historia")
    rows = cur.fetchall();
    return render_template('gestionar_historias.html',rows = rows)

"""
Vista que permite monitorizar la ubicación de los usuarios activos
"""
@app.route('/monitorizacion', methods=['GET'])
def get_monitorizacion():
    return render_template('monitorizacion.html')

"""
Vista auxiliar con algunas de las rutas implementadas
"""
@app.route('/rutas', methods=['GET'])
def get_rutas():
    return render_template('rutas.html')

"""
Vista que proporciona información de la aplicación como el desarrollador,
estado de la aplicación o versión
"""
@app.route('/rest/status', methods=['GET'])
def get_status():
    response = Response(json.dumps( server_info, indent=4 ), status=200, mimetype='application/json')
    return response

"""
Vista mostrada al acceder a una vista que no existe
"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/prueba', methods=['POST', 'PUT'])
def POST_prueba():
    print("ruta /prueba/texto funcion para ver un texto escaneado")
    hist_dict = request.form.to_dict()
    print(hist_dict['texto'])
    return ""

@app.route('/descargar', methods=['GET', 'POST'])
def descarga():
    return send_from_directory(directory='qr', filename='qr_1.zip', as_attachment=True)

"""
Función de ejecución principal del sistema
"""
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    #crear_modelo()
    app.run(host='0.0.0.0', port=port, debug=True)
