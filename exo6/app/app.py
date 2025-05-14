import os
from flask import Flask

app = Flask(__name__)

# Récupérer les variables d'environnement
env = os.environ.get('FLASK_ENV', 'production')
debug = os.environ.get('FLASK_DEBUG', '0') == '1'

@app.route('/')
def hello_world():
    return f'Hello World from Exo6 ({env} environment)!'

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug) 