from flask import Flask, jsonify, request
import os
import json
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

# Configuration des chemins
DATA_PATH = '/app/data'
LOG_PATH = '/app/logs'

# Création des répertoires s'ils n'existent pas
os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(LOG_PATH, exist_ok=True)

app = Flask(__name__)

# Configuration des logs
handler = RotatingFileHandler(os.path.join(LOG_PATH, 'app.log'), maxBytes=10000, backupCount=3)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Application démarrée')

# Fonctions utilitaires pour manipuler les données
def get_tasks():
    tasks_file = os.path.join(DATA_PATH, 'tasks.json')
    if os.path.exists(tasks_file):
        try:
            with open(tasks_file, 'r') as f:
                return json.load(f)
        except:
            return {'tasks': []}
    return {'tasks': []}

def save_tasks(tasks):
    with open(os.path.join(DATA_PATH, 'tasks.json'), 'w') as f:
        json.dump(tasks, f)

# Routes API
@app.route('/api/health', methods=['GET'])
def health_check():
    app.logger.info('Health check')
    return jsonify({'status': 'OK', 'timestamp': datetime.now().isoformat()})

@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    app.logger.info('Récupération de toutes les tâches')
    return jsonify(get_tasks())

@app.route('/api/tasks', methods=['POST'])
def create_task():
    app.logger.info('Création d\'une nouvelle tâche')
    task = request.json
    if not task or 'title' not in task:
        return jsonify({'error': 'Titre requis'}), 400
    
    tasks = get_tasks()
    task_id = len(tasks['tasks']) + 1
    new_task = {
        'id': task_id,
        'title': task['title'],
        'description': task.get('description', ''),
        'done': False,
        'created_at': datetime.now().isoformat()
    }
    
    tasks['tasks'].append(new_task)
    save_tasks(tasks)
    
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    app.logger.info(f'Récupération de la tâche {task_id}')
    tasks = get_tasks()
    
    task = next((t for t in tasks['tasks'] if t['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({'error': 'Tâche non trouvée'}), 404

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    app.logger.info(f'Mise à jour de la tâche {task_id}')
    tasks = get_tasks()
    
    for i, task in enumerate(tasks['tasks']):
        if task['id'] == task_id:
            update_data = request.json
            tasks['tasks'][i].update({
                'title': update_data.get('title', task['title']),
                'description': update_data.get('description', task['description']),
                'done': update_data.get('done', task['done']),
                'updated_at': datetime.now().isoformat()
            })
            save_tasks(tasks)
            return jsonify(tasks['tasks'][i])
    
    return jsonify({'error': 'Tâche non trouvée'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 