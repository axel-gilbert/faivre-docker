#!/bin/bash

# Création des répertoires pour les volumes si nécessaire
mkdir -p ./data ./logs ./config

# Construction de l'image
docker build -t flask-volumes-app .

# Arrêt et suppression du conteneur s'il existe déjà
docker stop flask-volumes-container 2>/dev/null || true
docker rm flask-volumes-container 2>/dev/null || true

# Lancement du conteneur avec les volumes configurés
docker run -d \
  --name flask-volumes-container \
  -p 8001:8000 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  -v $(pwd)/config:/app/config:ro \
  flask-volumes-app

echo "Application lancée sur http://localhost:8001"
echo "- Volume de données: $(pwd)/data"
echo "- Volume de logs: $(pwd)/logs"
echo "- Configuration (lecture seule): $(pwd)/config" 