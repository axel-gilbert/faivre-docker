# Application React avec Nginx (Dockerfile multi-stage)

Cette application React simple est configurée pour être construite dans un conteneur Docker à l'aide d'un build multi-stage, puis servie via Nginx sur le port 5002.

## Caractéristiques

- Build multi-stage pour optimiser la taille de l'image finale
- Premier stage pour compiler l'application React avec Node.js
- Second stage pour servir l'application avec Nginx
- Optimisation de la taille de l'image en utilisant Alpine Linux
- Configuration personnalisée de Nginx pour servir une application React (SPA)

## Construction de l'image

Pour construire l'image Docker, exécutez la commande suivante depuis le répertoire contenant le Dockerfile :

```bash
docker build -t react-nginx-exo2 .
```

## Lancement du conteneur

Pour lancer le conteneur, exécutez la commande suivante :

```bash
docker run -p 5002:5002 react-nginx-exo2
```

L'application sera alors accessible à l'adresse : http://localhost:5002

## Optimisations appliquées

- Utilisation d'images de base légères (Alpine)
- Multi-stage build pour ne conserver que les fichiers nécessaires dans l'image finale
- Nettoyage des fichiers inutiles de Nginx 