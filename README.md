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





