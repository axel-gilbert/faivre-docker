FROM ubuntu:22.04

# Installation des dépendances
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Création d'un utilisateur non-root
RUN useradd -m -s /bin/bash appuser

# Création des répertoires pour les volumes
RUN mkdir -p /app/data /app/logs /app/config \
    && chown -R appuser:appuser /app/data /app/logs \
    && chown -R root:appuser /app/config \
    && chmod -R 755 /app/data /app/logs \
    && chmod -R 755 /app/config

# Création du répertoire d'application
WORKDIR /app

# Copie des fichiers d'application
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copie du reste de l'application
COPY app.py .

# Copie des fichiers de configuration
COPY config/config.json /app/config/
RUN chmod 644 /app/config/config.json && \
    chown root:appuser /app/config/config.json

# Configuration des permissions
RUN chown -R appuser:appuser /app
USER appuser

# Définition des volumes
VOLUME ["/app/data"]
VOLUME ["/app/logs"]

# Exposition du port
EXPOSE 8000

# Commande de démarrage
CMD ["python3", "app.py"] 