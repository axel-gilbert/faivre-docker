# Stage de build
FROM node:18-alpine AS build

WORKDIR /app

# Copie des fichiers de configuration
COPY package*.json ./

# Installation des dépendances avec cache optimisé
RUN npm install

# Copie du code source
COPY public/ ./public/
COPY src/ ./src/

# Build de l'application
RUN npm run build

# Stage final avec Nginx
FROM nginx:alpine

# Copie de la configuration Nginx personnalisée
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Nettoyage de la configuration par défaut de Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copie des fichiers de build depuis le stage précédent
COPY --from=build /app/build /usr/share/nginx/html

# Exposer le port 5002
EXPOSE 5002

# Commande pour démarrer Nginx en premier plan
CMD ["nginx", "-g", "daemon off;"] 