FROM ubuntu:22.04

# Installation des dépendances
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Création d'un utilisateur non-root
RUN useradd -m -s /bin/bash appuser

# Création du répertoire d'application
WORKDIR /app

# Copie des fichiers d'application
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copie du reste de l'application
COPY app.py .

# Configuration des permissions
RUN chown -R appuser:appuser /app
USER appuser

# Exposition du port
EXPOSE 8000

# Commande de démarrage
CMD ["python3", "app.py"] 