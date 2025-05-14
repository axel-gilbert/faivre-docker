# Exercice 6 - Docker Compose avec Multi-Environnements

Cette configuration utilise Docker Compose pour orchestrer deux services avec une gestion avancée des environnements.

## Architecture

```
Client → Nginx (port configurable) → Flask (port interne)
```

## Caractéristiques

- **Gestion des environnements** : Configuration différente pour développement et production
- **Variables d'environnement** : Utilisation de fichiers .env pour la configuration
- **Override de configuration** : Système de surcharge de configuration par environnement

## Fichiers de configuration

- `.env` : Variables d'environnement communes (valeurs par défaut)
- `.env.development` : Variables spécifiques au développement
- `.env.production` : Variables spécifiques à la production
- `docker-compose.yml` : Configuration de base
- `docker-compose.override.yml` : Surcharges automatiques pour le développement
- `docker-compose.prod.yml` : Surcharges pour la production

## Démarrage en mode développement

Le mode développement est utilisé par défaut (via docker-compose.override.yml) :

```bash
# Utilise .env + .env.development + docker-compose.override.yml
cd exo6
docker-compose --env-file .env.development up -d
```

L'application sera accessible à l'adresse : http://localhost:5006

## Démarrage en mode production

```bash
# Utilise .env + .env.production + docker-compose.prod.yml
cd exo6
docker-compose --env-file .env.production -f docker-compose.yml -f docker-compose.prod.yml up -d
```

L'application sera accessible à l'adresse : http://localhost:80

## Variables d'environnement disponibles

| Variable | Description | Défaut |
|----------|-------------|--------|
| APP_NAME | Nom de l'application | flask-nginx-app |
| FLASK_ENV | Environnement Flask | production |
| FLASK_DEBUG | Mode debug de Flask | 0 |
| FLASK_PORT | Port interne de Flask | 5000 |
| NGINX_PORT | Port interne de Nginx | 80 |
| EXPOSED_PORT | Port exposé à l'externe | 5006 ou 80 |
| RESTART_POLICY | Politique de redémarrage | unless-stopped |
| NETWORK_NAME | Nom du réseau Docker | app-network |

## Arrêt des services

Pour arrêter les services en mode développement:
```bash
docker-compose --env-file .env.development down
```

Pour arrêter les services en mode production:
```bash
docker-compose --env-file .env.production -f docker-compose.yml -f docker-compose.prod.yml down
```

## Vérification des logs

Pour vérifier les logs de chaque service:

```bash
# Logs du service Flask
docker-compose logs flask-app

# Logs du service Nginx
docker-compose logs nginx
``` 