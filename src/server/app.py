from rutas_historias import *
from rutas_usuario import *

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/nueva_historia', methods=['GET'])
def get_nueva_historia():
    return render_template('nueva_historia.html')

@app.route('/usuarios', methods=['GET'])
def get_gestionar_usuarios():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT email, nombre, apellidos FROM usuario")
    rows = cur.fetchall();
    return render_template('gestionar_usuarios.html',rows = rows)

@app.route('/historias', methods=['GET'])
def get_gestionar_historias():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT id, nombre_historia FROM historia")
    rows = cur.fetchall();
    return render_template('gestionar_historias.html',rows = rows)

@app.route('/monitorizacion', methods=['GET'])
def get_monitorizacion():
    return render_template('monitorizacion.html')

@app.route('/rutas', methods=['GET'])
def get_rutas():
    return render_template('rutas.html')

@app.route('/rest/status', methods=['GET'])
def get_status():
    response = Response(json.dumps( server_info, indent=4 ), status=200, mimetype='application/json')
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/registro', methods=['GET'])
def prueba():
    return render_template('registro_usuario.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    #crear_modelo()
    app.run(host='0.0.0.0', port=port, debug=False)
