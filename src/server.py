import os, sys

from declaracionVariables import *

@app.route('/')
def hola_mundo():
    return 'Hello, World!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port, debug=True)
