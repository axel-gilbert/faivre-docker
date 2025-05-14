FROM ubuntu:22.04

# Installation des dépendances
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Création d'un utilisateur non-root
RUN useradd -m appuser

# Création du répertoire de travail
WORKDIR /app

# Copie des fichiers avec bonnes permissions
COPY --chown=appuser:appuser requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser app/app.py .

# Changement des permissions
RUN chmod 755 /app && chmod 644 /app/app.py /app/requirements.txt

# Utilisation de l'utilisateur non-root
USER appuser

# Changement de port
EXPOSE 5001

# Modification pour utiliser python3
CMD ["python3", "app.py"] 