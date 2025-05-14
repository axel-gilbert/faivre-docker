FROM python:3.9-slim

WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Création des répertoires pour les volumes
RUN mkdir -p /app/data /app/logs
RUN chmod 777 /app/data /app/logs

# Copie de l'application
COPY app.py .

# Exposition du port
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"] 