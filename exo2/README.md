# Application Web avec Docker Multi-stage

Ce projet démontre l'utilisation d'un build multi-stage dans Docker pour:
- Compiler une application React dans un premier stage
- Déployer l'application compilée dans un serveur Nginx optimisé

## Caractéristiques

- Build multi-stage pour optimiser la taille de l'image finale
- Configuration Nginx pour servir une application web moderne
- Optimisations de sécurité et de performance

## Comment construire et exécuter

Pour construire l'image Docker:

```bash
docker build -t webapp-multistage .
```

Pour exécuter le conteneur:

```bash
docker run -d -p 8080:80 --name webapp-container webapp-multistage
```

Accédez à l'application à l'adresse: http://localhost:8080 