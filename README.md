<div align="center">
<h1> Mon vet-conseil </h1>
<img src="https://badgen.net/badge/django/4.2.1/green?icon=pypi" alt="Django">
<img src="https://badgen.net/badge/status/development/red?icon=github" alt="Python">
<br> <br>
Mini-projet universitaire 🎓 de création d'une API REST pour la gestion d'une clinique vétérinaire et services aux animaux domestiques.
</div>

>Lisez attentivement ce document avant de commencer à travailler sur le projet. SVP 😀!


## Prise en main

### Pour les chefs de sous groupes uniquement !

`Forker` le projet dans votre répertoire et créer autant de branche
que vous voulez dans cette `fork` pour que chaque personne puisse
travailler sur une branche différente.

### Pour tout le monde
`Cloner` la branche principale du chef de sous groupe. 
```
git clone https://github.com/<demander a votre chef de sous groupe>.git
```


## Mise en marche
> Soyez sûr d'être dans votre branche de travail avant toute modification
``` git checkout <nom de la branche> ```, pour vérifier la branche sur laquelle vous êtes, utiliser la commande ``` git branch ```

### Prérequis
- Python 3.11

### Création d'un environnement virtuel
On va créer un environnement virtuel pour isoler les dépendances de notre projet par rapport à celles de notre installation globale.
```
python3 -m venv venv
```

### Activation de l'environnement virtuel
```
source venv/bin/activate
```
Pour vérifier que l'environnement virtuel est bien activé, il suffit de taper la commande ``` which python ``` et vous devriez avoir le chemin vers le dossier venv.
> Pour désactiver l'environnement virtuel, il suffit de taper la commande ``` deactivate ```

### Installation des dépendances
Toutes les dépendances python de notre projet sont dans le fichier ``` requirements.txt ```, pour les installer, il suffit de taper la commande suivante :
```
pip install -r requirements.txt
```

### Configuration connexion à la base de données
Créer un fichier `.env` à la racine du projet, ajouter et modifier les lignes suivantes :
```
# Database configuration
VET_DB_NAME=postgres
VET_DB_USER=postgres
VET_DB_PASSWORD=
VET_DB_HOST=localhost
VET_DB_PORT=5432
```
> Ne pas oublier de mettre .env dans le fichier .gitignore pour éviter de donner les informations de connexion à la base de données

### Commencer à travailler
Désormais, vous pouvez commencer à travailler sur le projet
Créer une application pour votre sous groupe, et commencer à travailler dessus.
```
python manage.py startapp <nom de l'application>
```

  
## Règles de gestion de version
  
### Commit et push
  
#### Pour tout le monde
- Vérifier que vous êtes bien sur votre branche de travail
- Vérifier que vous avez bien `pull` la dernière version de la branche principale (afin d'éviter les conflits,
    return JsonResponse({'message': 'Rendez-vous supprimé avec succès.'})
cela permet de mettre à jour votre branche avec la dernière version de la branche principale et voir si votre code est
compatible)
```
git pull origin <nom de la branche principale>
```
- Ajouter les fichiers modifiés
```
git add *
```
- Commiter les fichiers modifiés
```
git commit -m "message du commit"
```
- Pusher les fichiers modifiés
```
git push origin <nom de votre branche>
```
- Créer une `pull request` sur github pour que le chef de sous groupe puisse valider votre code et le merger avec la branche principale,
| Bien donner un titre et une description à votre `pull request` pour que le chef de sous groupe puisse comprendre ce que vous avez fait

#### Pour le chef de sous groupe
Voici les étapes pour merger votre branche avec la branche principale du projet principale
- Vérifier que vous êtes bien sur la branche principale
- Vérifier que vous avez bien `pull` la dernière version de la branche principale du projet principale
```
git pull origin <nom de la branche principale>
```
- Merger votre branche en créant un `pull request` sur github <br>
| Bien donner un titre et une description à votre `pull request` pour que le chef de sous groupe puisse comprendre ce que vous avez fait

### Gitignore
Pour éviter de pusher des fichiers sensibles et inutiles, il faut ajouter les fichiers à ignorer dans le fichier `.gitignore` à commencer par `venv` et `.env`
> Tenez à vérifier cela avant de pusher votre code

### Messages de commit
Pour les messages de commit, il faut commencer par le type de commit, suivi d'une description du commit :
- `feat`: pour les nouvelles fonctionnalités
- `fix`: pour les corrections
- `refactor`: pour les modifications de code qui n'ajoutent pas de fonctionnalités ou ne corrigent pas de bug
- `style`: pour les modifications qui n'apportent aucune altération de sens (indentation, mise en forme, ajout d'espace, renommage de variable, etc.)
- `test`: pour les ajouts de tests
- `perf`: pour les améliorations de performances
> exemple : `feat: add login feature`

### Ajout de dépendances (packages)
Pour ajouter une dépendance, il faut l'ajouter en étant dans l'environnement virtuel en utilisant `pip install ...`, puis l'ajouter au fichier `requirements.txt` en tapant la commande suivante :
```
pip freeze > requirements.txt
```
> Vérifer que la dépendance est bien ajoutée au fichier `requirements.txt`

### Signalement de problèmes
Tout problème rencontré doit être renseigné afin de pouvoir le corriger. <br>
Pour signaler un problème, il faut créer une `issue` sur github en donnant un titre et une description du problème rencontré.
> N'oublier pas de mettre des labels sur votre `issue`

###### Workflow
[![Django CI](https://github.com/mendrika261/S4-API-vet-conseil/actions/workflows/django.yml/badge.svg)](https://github.com/mendrika261/S4-API-vet-conseil/actions/workflows/django.yml)
[![Bandit](https://github.com/mendrika261/S4-API-vet-conseil/actions/workflows/bandit.yml/badge.svg)](https://github.com/mendrika261/S4-API-vet-conseil/actions/workflows/bandit.yml)
