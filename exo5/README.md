# Application Multi-services avec Docker Compose

Ce projet démontre la mise en place d'une application multi-services avec Docker Compose. L'architecture comprend :

- Un service backend (Flask) qui expose une API REST
- Un service frontend (Nginx) qui sert les fichiers statiques et fait proxy vers l'API
- Une configuration des dépendances entre services

## Architecture

- Le service Nginx sert les fichiers statiques et redirige les requêtes API vers le service Flask
- Le service Flask expose une API pour gérer des tâches et stocke les données dans un volume
- Les services communiquent via un réseau Docker dédié

## Fonctionnalités

- Interface utilisateur pour gérer des tâches (ajouter, marquer comme terminée)
- API RESTful pour les opérations CRUD sur les tâches
- Persistance des données via volumes Docker
- Journalisation des activités

## Structure du projet

```
exo5/
├── docker-compose.yml      # Configuration des services
├── flask/                  # Service backend
│   ├── Dockerfile          # Image pour le service Flask
│   ├── app.py              # Application Flask
│   └── requirements.txt    # Dépendances Python
├── nginx/                  # Service frontend
│   ├── Dockerfile          # Image pour le service Nginx
│   ├── conf/               # Configuration Nginx
│   │   └── app.conf        # Configuration du serveur
│   └── static/             # Fichiers statiques
│       ├── index.html      # Page d'accueil
│       ├── css/            # Styles CSS
│       └── js/             # Scripts JavaScript
└── README.md               # Documentation
```

## Démarrage de l'application

Pour démarrer l'application, exécutez :

```bash
cd exo5
docker-compose up -d
```

L'application sera accessible à l'adresse : http://localhost

## Utilisation de l'API

### Récupérer toutes les tâches

```bash
curl http://localhost/api/tasks
```

### Créer une nouvelle tâche

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title":"Nouvelle tâche","description":"Description de la tâche"}' http://localhost/api/tasks
```

### Mettre à jour une tâche (marquer comme terminée)

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"done":true}' http://localhost/api/tasks/1
```

## Volumes et persistance

- Les données des tâches sont stockées dans un volume Docker (`flask_data`)
- Les logs de l'application sont stockés dans un volume dédié (`flask_logs`)
- Les fichiers de configuration Nginx sont montés en lecture seule 