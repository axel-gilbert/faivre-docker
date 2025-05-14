# Exercice 5 - Docker Compose avec Nginx et Flask

Cette configuration utilise Docker Compose pour orchestrer deux services :
- Un service d'application Flask qui traite les requêtes
- Un service web Nginx qui sert de proxy inverse

## Architecture

```
Client → Nginx (port 5005) → Flask (port 5000 interne)
```

- Nginx écoute sur le port 5005 (exposé à l'extérieur)
- Flask écoute sur le port 5000 (non exposé, accessible uniquement via le réseau interne)
- Les services sont connectés via un réseau Docker nommé "app-network"

## Caractéristiques

- **Dépendances entre services** : Nginx dépend de Flask et ne démarrera qu'après lui
- **Isolation des services** : L'application Flask n'est pas directement accessible depuis l'extérieur
- **Configuration des volumes** : Les fichiers de l'application sont montés en volume pour permettre le développement sans reconstruire l'image
- **Configuration réseau** : Les services communiquent via un réseau dédié

## Démarrage des services

```bash
cd exo5
docker-compose up -d
```

L'application sera accessible à l'adresse : http://localhost:5005

## Arrêt des services

```bash
docker-compose down
```

## Vérification des logs

Pour vérifier les logs de chaque service :

```bash
# Logs du service Flask
docker-compose logs flask-app

# Logs du service Nginx
docker-compose logs nginx
``` 