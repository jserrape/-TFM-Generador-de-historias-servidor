import os, sys

from declaracionVariables import *
#from modelo import *

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/nueva_historia', methods=['GET'])
def get_nueva_historia():
    return render_template('nueva_historia.html')

@app.route('/monitorizacion', methods=['GET'])
def get_monitorizacion():
    return render_template('monitorizacion.html')

@app.route('/rest/status', methods=['GET'])
def get_status():
    response = Response(json.dumps( server_info, indent=4 ), status=200, mimetype='application/json')
    return response

@app.route('/rest/historia', methods=['POST', 'PUT'])
def POST_historia():
    historia_dict = request.form.to_dict()
    print('POST/PUT on historia: ' + str( historia_dict ))
    nueva_historia = Historia(dict=historia_dict)
    return "Ok"

@app.route('/rest/historia/<string:nombre_historia>', methods=['GET'])
def GET_historia(nombre_historia):
    print('GET on HISTORIAS: ' + name)
    historia = DAOHistoria.instance().buscar( nombre_historia )

    if historia is not None:
        print("-------------> No none")
        response = Response(json.dumps( historia.toJSON(), indent=4 ), status=201, mimetype='application/json')
    else:
        print("-------------> Si none")
        response = Response( {}, status=201, mimetype='application/json')
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#@app.route('/bbdd', methods=['GET'])
#def get_bbdd():
#    select_employee()
#    return "Hola mundo"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    #crear_modelo()
    app.run(host='0.0.0.0', port=port, debug=True)
