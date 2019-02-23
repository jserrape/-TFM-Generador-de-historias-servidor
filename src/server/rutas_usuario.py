from declaracionVariables import *
from generar_json import *

@app.route('/rest/usuario', methods=['POST', 'PUT'])
def POST_usuario():
    usu_dict = request.form.to_dict()
    print(str( usu_dict ))


    response = Response(json.dumps( {'status': '201'}, indent=4 ), status=201, mimetype='application/json')
    return response


@app.route('/rest/list/usuario', methods=['GET'])
def GET_usuarios():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from usuario")
   rows = cur.fetchall();
   print(rows)
   return render_template("list_usuario.html",rows = rows)
