# Application Flask avec Gestion de Volumes Docker

Cette application Flask démontre l'utilisation des volumes Docker pour :
1. Persistance des données
2. Journalisation (logs)
3. Configuration en lecture seule

## Structure des volumes

- `/app/data` : Volume pour stocker les données persistantes (messages)
- `/app/logs` : Volume pour stocker les logs de l'application
- `/app/config` : Volume en lecture seule pour les fichiers de configuration

## Caractéristiques de l'application

- Stockage persistant des messages
- Journalisation détaillée des actions
- Configuration centralisée
- Utilisation de volumes Docker pour la persistance

## API Endpoints

- `GET /` : Page d'accueil
- `GET /messages` : Récupérer tous les messages
- `POST /messages` : Ajouter un message (JSON avec champ "message")
- `GET /config` : Afficher la configuration actuelle

## Exécution de l'application

Pour lancer l'application avec les volumes Docker correctement configurés, utilisez le script fourni :

```bash
./run.sh
```

Ce script va :
1. Créer les répertoires locaux pour les volumes
2. Construire l'image Docker
3. Lancer un conteneur avec les volumes montés correctement

## Test de l'application

Pour ajouter un message :

```bash
curl -X POST -H "Content-Type: application/json" -d '{"message":"Ceci est un test"}' http://localhost:8000/messages
```

Pour récupérer les messages :

```bash
curl http://localhost:8000/messages
```

## Vérification des volumes

Les données sont stockées dans les répertoires suivants sur l'hôte :
- `./data` : Contient le fichier data.json avec les messages
- `./logs` : Contient les fichiers de logs de l'application
- `./config` : Contient la configuration (montée en lecture seule) 