# Stage de build
FROM node:18-alpine AS build

WORKDIR /app

# Copie des fichiers de dépendances
COPY package*.json ./
RUN npm install

# Copie du code source
COPY src/ ./src/
COPY public/ ./public/

# Build de l'application
RUN npm run build

# Stage final avec Nginx
FROM nginx:alpine

# Copie de la configuration Nginx personnalisée
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Suppression des fichiers par défaut dans le dossier html
RUN rm -rf /usr/share/nginx/html/*

# Copie des fichiers buildés depuis le stage de build
COPY --from=build /app/build/ /usr/share/nginx/html/

# Optimisation de l'image
RUN apk --no-cache add curl && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

# Exposition du port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"] 