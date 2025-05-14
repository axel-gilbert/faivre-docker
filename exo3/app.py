from flask import Flask, request, jsonify
import os
import json
import logging
from logging.handlers import RotatingFileHandler
import datetime

# Configuration des chemins
CONFIG_PATH = '/app/config'
DATA_PATH = '/app/data'
LOG_PATH = '/app/logs'

# Création des répertoires s'ils n'existent pas
os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(LOG_PATH, exist_ok=True)

app = Flask(__name__)

# Configuration de l'application à partir du fichier de configuration
try:
    with open(os.path.join(CONFIG_PATH, 'config.json'), 'r') as config_file:
        config = json.load(config_file)
        app.config.update(config)
except Exception as e:
    print(f"Erreur lors du chargement de la configuration: {e}")
    # Configuration par défaut
    app.config.update({
        'APP_NAME': 'Flask Docker Volume Demo',
        'DEBUG': False,
    })

# Configuration des logs
handler = RotatingFileHandler(os.path.join(LOG_PATH, 'app.log'), maxBytes=10000, backupCount=3)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Application démarrée')

# Fonction utilitaire pour manipuler les données persistantes
def get_data():
    data_file = os.path.join(DATA_PATH, 'data.json')
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    return {'messages': []}

def save_data(data):
    with open(os.path.join(DATA_PATH, 'data.json'), 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def hello():
    app.logger.info('Page d\'accueil visitée')
    app_name = app.config.get('APP_NAME', 'Flask App')
    return f"Bienvenue sur {app_name} - Démo Volumes Docker!"

@app.route('/messages', methods=['GET'])
def get_messages():
    app.logger.info('Récupération des messages')
    data = get_data()
    return jsonify(data['messages'])

@app.route('/messages', methods=['POST'])
def add_message():
    app.logger.info('Ajout d\'un message')
    message = request.json.get('message', '')
    if not message:
        return jsonify({'error': 'Le message ne peut pas être vide'}), 400
    
    data = get_data()
    data['messages'].append({
        'id': len(data['messages']) + 1,
        'message': message,
        'created_at': datetime.datetime.now().isoformat()
    })
    save_data(data)
    
    return jsonify({'status': 'success', 'message': 'Message ajouté'}), 201

@app.route('/config')
def show_config():
    app.logger.info('Affichage de la configuration')
    # Filtrer les informations sensibles
    safe_config = {k: v for k, v in app.config.items() if not k.startswith('_') and k != 'SECRET_KEY'}
    return jsonify(safe_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=app.config.get('DEBUG', False)) 