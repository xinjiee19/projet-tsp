<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/fr/thumb/1/1d/Logo_T%C3%A9l%C3%A9com_SudParis.svg/153px-Logo_T%C3%A9l%C3%A9com_SudParis.svg.png" alt="TSP logo">
</p>


# CSC 8567 - Architectures distribuées et applications web

Auteur : Xin Jie CHENG

# Fonctionnement de Django 
### Suite de requêtes et d'exécutions permettant l'affichage d'une page HTML index.html à l'URL global / via une application public
Lorsque l'utilisateur accède à l'URL `/`, une requête HTTP GET est envoyé au serveur Django. Django va utiliser le fichier `urls.py` pour faire correspondre l'URL à une vue. 
Par exemple : 
```
# urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]

# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'public/index.html')
```
La vue `index` est appelée et cette vue va retourner une HTML comme réponse. Django va chercher le fichier index.html dans le répertoire `templates`. 
Le contenu HTML du fichier index.html est envoyé en réponse à la requête du client.

### Configuration de la base des données dans un projet Django
On peut configurer la base des données dans la section `DATABASES` du fichier `settings.py`.
Exemple pour une configuration de base des données PostgreSQL: 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todolist',  # Nom de la base de données PostgreSQL
        'USER': 'xinjie',      # Nom de l'utilisateur PostgreSQL
        'PASSWORD': 'xinjie',  # Mot de passe de l'utilisateur
        'HOST': 'db',   # Hôte de la base de données (localhost si local)
        'PORT': '5432',        # Port par défaut de PostgreSQL
    }
}
```

### Configuration du fichier de paramètres dans un projet Django
Pour configurer le fichier des paramètres, on peut l'effectuer dans le fichier `settings.py`.
Ce fichier contient tous les paramètres de configuration pour un projet Django.
Par exemple, définir la base des données utilisée, lister des applications installées dans le projet, configurer des répertoires de templates, etc.

### Effets des commandes makemigrations et migrate
python3 manage.py makemigrations : Cette commande crée des fichiers de migration pour toutes les modifications apportées aux modèles Django (ajout, suppression, etc.).
Elle génère un fichier de migration dans le dossier migrations de chaque application où des changements ont été détectés. 
Ces fichiers contiennent les instructions pour mettre à jour la structure de la base de données afin qu'elle corresponde aux modèles définis dans `models.py`.

python3 manage.py migrate : Cette commande applique les migrations à la base de données, c’est-à-dire qu’elle exécute les changements définis dans les fichiers de migration.
Cette commande lit les fichiers de migration dans le répertoire `migrations`. Elle met à jour la base de données réelle en fonction des instructions dans les migrations.


# Fonctionnement de Docker
### Commandes dans un fichier Dockerfile
- `FROM` : Déclare l'image de base à utiliser pour créer votre conteneur. Cette image de base contient généralement un système d'exploitation minimal ou un environnement spécifique.
- `RUN` : Exécute une commande dans le conteneur au moment de la création de l'image. Généralement utilisé pour installer des packages ou exécuter des scripts.
- `WORKDIR` : Définit le répertoire de travail (current directory) à l'intérieur du conteneur. Les commandes suivantes (comme RUN, COPY, etc.) se basent sur ce répertoire.
- `EXPOSE` : Informe Docker qu'un conteneur écoute sur un certain port à l'intérieur du conteneur.
- `CMD` : Définit la commande par défaut à exécuter lorsque le conteneur démarre.

### Éléments du fichier `docker-compose.yml`
- `ports: - "80:80"` : Mappe le port 80 de la machine hôte au port 80 du conteneur. Cela permet à l'utilisateur d'accéder au service à partir de l'hôte via le port 80. Le service dans le conteneur écoute également sur le port 80.
- `build` : Définit la façon dont l'image Docker sera construite.
  Exemple :
  ```
  build:
    context: .
    dockerfile: Dockerfile.api
  ```
  `context` indique le répertoire à partir duquel le build sera exécuté (dans ce cas, le répertoire courant), et dockerfile spécifie quel Dockerfile utiliser pour construire l'image  (dans ce cas, Dockerfile.api).
- `depends_on` : Assure que les services nécessaires démarrent dans le bon ordre. Cela signifie que Docker Compose s'assurera que les services spécifiés dans `depends_on` démarrent avant le service.
- `environment` : Définit les variables d'environnement dans le conteneur.

### Méthode pour définir des variables d'environnement dans un conteneur
Pour définir les variables d'environnement, on peut utiliser un fichier `.env`. 
Les variables définies dans le fichier .env seront automatiquement chargées dans le conteneur lors il est démarré.
Par exemple : 
```
# .env
POSTGRES_DB=mydatabase
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword

# docker-compose.yml
env_file:
  - .env
```
### Configuration d'un conteneur web et nginx dans le même réseau Docker
L'objectif est de faire en sorte que Nginx (utilisé comme serveur proxy) redirige les requêtes vers l'application Django exécutée sur un autre conteneur (web) dans le même réseau Docker. 
Dans le fichier `nginx.conf`, on configure le proxy inverse pour rediriger le trafic vers le conteneur web. 

```
# nginx.conf
server {
  listen 80;
  location / {
    proxy_read_timeout      1800;
    proxy_connect_timeout   1800;
    proxy_send_timeout      1800;
    send_timeout            1800;
    proxy_set_header        Accept-Encoding   "";
    proxy_set_header        X-Forwarded-By    $server_addr:$server_port;
    proxy_set_header        X-Forwarded-For   $remote_addr;
    proxy_set_header        X-Forwarded-Proto $scheme;
    proxy_set_header        Host $host;
    proxy_set_header        X-Real-IP $remote_addr;
    proxy_pass http://backend;
  }
```
```
  # Application frontend Django
  frontend:
    container_name: frontend
    build:
      context: .
      dockerfile: django-site/todolist/public/Dockerfile.front
    ports:
      - "8001:8000"
    environment:
      - DATABASE_URL=postgres://xinjie:xinjie@db:5432/todolist
    depends_on:
      - db
    networks:
      - webnet
    command: python3 manage.py runserver 0.0.0.0:8000

# Serveur Nginx
  proxy:
    container_name: nginx
    image: nginx
    ports:
      - "80:80"
    depends_on:
      - frontend
      - api
    volumes:
      - ./django-site/nginx/nginx.conf:/etc/nginx/conf.d/default.conf
      - ./django-site/nginx/access.log:/var/log/nginx/access.log
      - ./django-site/todolist/public/staticfiles:/projet-web-tsp/django-site/todolist/public/staticfiles
    networks:
      - webnet
```

Cette configuration fait en sorte que Nginx redirige les requêtes HTTP qu'il reçoit sur le port 80 vers le service Django exécuté sur le conteneur web, sur le port 8000.

