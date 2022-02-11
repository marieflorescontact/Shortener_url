# Utilitaires python

## Pré-requis

- Python >= 3.9

## Environnement de développement (local)

Cloner le projet avec git et créer un [virtual env](https://docs.python.org/3/tutorial/venv.html) dans le dossier `.venv` :

    python3 -m venv .venv

**TIP:** Vous pouvez ensuite activer le virtual env, en utilisant la commande: `source .venv/bin/activate`.



### Installation des dépendances

Pour installer les dépendances :

    pip install -r requirements.txt


**TIP:** Vous pouvez récupérer la liste *complète* des paquets installés avec la commande: `pip freeze`.

### Linter

Pour lancer le linter, vous pouvez utiliser la commande ci-dessous :

    python -m flake8 

### Pour run le projet

    python manage.py runserver

### Pour lancer le serveur taillwind
    
    python3 manage.py tailwind start