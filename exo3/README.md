# Application React avec Nginx et Volumes (Exercice 3)

Cette application React est basée sur l'exercice 2, avec l'ajout de volumes Docker pour la persistance des données et la gestion des logs.

## Caractéristiques

- Build multi-stage pour optimiser la taille de l'image finale
- Utilisation de volumes Docker pour:
  - Persistance des données (`/data`)
  - Stockage des logs Nginx (`/var/log/nginx`)
- Configuration en lecture seule pour les fichiers de configuration
- Application accessible sur le port 5003

## Lancement avec Docker Compose

La méthode recommandée pour lancer cette application est d'utiliser Docker Compose, qui gère automatiquement les volumes:

```bash
docker-compose up -d
```

L'application sera accessible à l'adresse: http://localhost:5003

## Arrêt de l'application

Pour arrêter l'application tout en conservant les volumes:

```bash
docker-compose down
```

Pour arrêter l'application et supprimer les volumes:

```bash
docker-compose down -v
```

## Lancement manuel (sans Docker Compose)

Si vous préférez ne pas utiliser Docker Compose, vous pouvez construire et lancer manuellement:

```bash
# Construction de l'image
docker build -t react-nginx-exo3 .

# Création des volumes
docker volume create data-volume
docker volume create log-volume

# Lancement du conteneur avec les volumes
docker run -d \
  -p 5003:5003 \
  -v data-volume:/data \
  -v log-volume:/var/log/nginx \
  -v $(pwd)/nginx.conf:/etc/nginx/conf.d/default.conf:ro \
  react-nginx-exo3
```

## Accès aux logs

Pour accéder aux logs stockés dans le volume, vous pouvez:

```bash
# Identifier le conteneur
docker ps

# Voir les logs du conteneur
docker logs <container_id>

# Ou exécuter un shell dans le conteneur pour accéder au volume des logs
docker exec -it <container_id> sh -c "ls -la /var/log/nginx"
``` 