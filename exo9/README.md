# Exercice 9 - Docker Compose avec Sécurité Renforcée

Cette configuration Docker Compose met en place une architecture sécurisée avec Flask et Nginx en appliquant de nombreuses bonnes pratiques de sécurité.

## Architecture sécurisée

```
Client → Nginx (frontend) → Flask (backend isolé)
```

## Mesures de sécurité implémentées

### 1. Utilisateurs non-root
- **Flask**: Exécution avec un utilisateur `flaskuser` dédié et sans privilèges
- **Nginx**: Exécution avec l'utilisateur `nginx` standard sans privilèges root

### 2. Limitation des ressources
- Limites strictes de CPU (50%) et de mémoire (256Mo) pour chaque service
- Réservations de ressources pour garantir les performances minimales

### 3. Isolation des réseaux
- Réseau `frontend` exposé uniquement pour Nginx
- Réseau `backend` interne et isolé pour la communication Flask-Nginx
- Aucun accès direct à l'application Flask depuis l'extérieur

### 4. Durcissement des conteneurs
- Suppression de toutes les capabilities par défaut (`cap_drop: ALL`)
- Attribution uniquement des capabilities nécessaires (`NET_BIND_SERVICE` pour Nginx)
- Option `no-new-privileges` pour éviter l'escalade de privilèges
- Systèmes de fichiers en lecture seule (`read_only: true`)
- Utilisation de volumes `tmpfs` pour les fichiers temporaires avec permissions spécifiques

### 5. Sécurité Nginx
- En-têtes de sécurité (XSS Protection, Content-Security-Policy, etc.)
- Masquage des informations de version (`server_tokens off`)
- Limitation du taux de requêtes et du nombre de connexions par IP
- Timeouts courts pour éviter les attaques de déni de service
- Configuration du fichier PID dans un emplacement accessible à l'utilisateur non-root

## Démarrage de l'application sécurisée

```bash
cd exo9
docker-compose up -d
```

L'application sera accessible à l'adresse : http://localhost:5009

## Vérification des mesures de sécurité

Pour vérifier que les conteneurs s'exécutent bien avec des utilisateurs non-root:

```bash
docker-compose exec flask-app id
docker-compose exec nginx id
```

Pour vérifier que les réseaux sont correctement isolés:

```bash
# Tenter d'accéder à Internet depuis le conteneur Flask (devrait échouer)
docker-compose exec flask-app ping -c 1 google.com
```

## Arrêt de l'application

```bash
docker-compose down
``` 