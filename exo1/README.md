# Application Flask sous Docker

Cette application Flask simple est configurée pour s'exécuter dans un conteneur Docker basé sur Ubuntu avec un utilisateur non-root pour plus de sécurité.

## Prérequis

- Docker installé sur votre machine

## Construction de l'image

Pour construire l'image Docker, exécutez la commande suivante depuis le répertoire contenant le Dockerfile :

```bash
docker build -t flask-exo1 .
```

## Lancement du conteneur

Pour lancer le conteneur, exécutez la commande suivante :

```bash
docker run -p 5001:5001 flask-exo1
```

L'application sera alors accessible à l'adresse : http://localhost:5001

## Caractéristiques de sécurité

- Utilise Ubuntu comme image de base
- Exécute l'application avec un utilisateur non-root (appuser)
- Définit des permissions appropriées sur les fichiers
- Nettoie le cache APT pour réduire la taille de l'image 