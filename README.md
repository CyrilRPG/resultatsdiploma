# Plateforme de Visualisation des Résultats Universitaires

Application web statique pour visualiser et analyser les résultats universitaires à partir de fichiers Excel. Fonctionne entièrement dans le navigateur, sans backend.

## Fonctionnalités

- 📊 Import de fichiers Excel (.xlsx, .xls)
- 📈 Calcul automatique des moyennes par étudiant
- 📉 Calcul de la moyenne générale de tous les étudiants
- 🔍 Filtrage par nom, prénom et plage de notes
- 📋 Tri des résultats par ordre croissant (par défaut sur la moyenne)
- 📊 Statistiques en temps réel (total, moyenne générale, note max, note min)

## Installation locale

1. Cloner le dépôt ou télécharger les fichiers
2. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Lancer l'application :
```bash
python app.py
```

5. Ouvrir votre navigateur à l'adresse : `http://localhost:5000`

## Déploiement sur le web

### Option 1 : Déploiement sur Netlify (Recommandé - Site statique)

1. Créer un compte sur [Netlify](https://www.netlify.com)
2. Méthode A - Via l'interface web :
   - Aller sur [app.netlify.com](https://app.netlify.com)
   - Cliquer sur "Add new site" > "Deploy manually"
   - Glisser-déposer le dossier contenant `index.html` et `netlify.toml`
   - Votre site sera déployé immédiatement !

3. Méthode B - Via Git (recommandé pour les mises à jour automatiques) :
   - Créer un dépôt GitHub/GitLab avec vos fichiers
   - Sur Netlify, cliquer sur "Add new site" > "Import an existing project"
   - Connecter votre dépôt Git
   - Netlify détectera automatiquement les paramètres (pas de build nécessaire)
   - Cliquer sur "Deploy site"
   - Votre site sera disponible à l'adresse : `https://votre-site.netlify.app`

**Avantages** :
- ✅ Gratuit et illimité
- ✅ Déploiement instantané
- ✅ HTTPS automatique
- ✅ Mises à jour automatiques via Git
- ✅ Pas de serveur nécessaire (site 100% statique)

### Option 2 : Déploiement sur Render.com (Pour version Flask)

1. Créer un compte sur [Render.com](https://render.com)
2. Créer un nouveau "Web Service"
3. Connecter votre dépôt GitHub/GitLab ou uploader les fichiers
4. Configurer le service :
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `gunicorn app:app`
   - **Environment** : Python 3
5. Cliquer sur "Create Web Service"
6. Votre application sera disponible à l'adresse fournie par Render

### Option 2 : Déploiement sur Heroku

1. Installer [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Se connecter à Heroku :
```bash
heroku login
```

3. Créer une nouvelle application :
```bash
heroku create votre-nom-app
```

4. Déployer :
```bash
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

5. Ouvrir l'application :
```bash
heroku open
```

### Option 3 : Déploiement sur Railway

1. Créer un compte sur [Railway.app](https://railway.app)
2. Créer un nouveau projet
3. Connecter votre dépôt GitHub
4. Railway détectera automatiquement l'application Flask
5. L'application sera déployée automatiquement

### Option 4 : Déploiement sur PythonAnywhere

1. Créer un compte sur [PythonAnywhere](https://www.pythonanywhere.com)
2. Ouvrir un Bash console
3. Cloner votre dépôt ou uploader les fichiers
4. Créer un environnement virtuel et installer les dépendances
5. Configurer une application web Flask dans le dashboard
6. Pointer vers votre fichier `app.py`

## Structure du fichier Excel

Le fichier Excel doit contenir les colonnes suivantes (les noms peuvent varier légèrement) :
- Nom
- Prénom
- Pseudo (optionnel)
- Email (optionnel)
- Quelle note avez vous obtenue en UE 1
- Quelle note avez vous obtenue en UE 2
- Quelle note avez vous obtenue en UE 3.1
- Quelle note avez vous obtenue en UE 4
- Quel est votre rang général (optionnel)

## Notes importantes

- Les notes sont triées par ordre croissant par défaut (sur la moyenne)
- La moyenne générale est calculée automatiquement à partir de toutes les moyennes individuelles
- Les fichiers Excel sont traités directement dans le navigateur (aucune donnée n'est envoyée au serveur)
- Taille maximale des fichiers : limitée par la mémoire du navigateur (généralement plusieurs dizaines de MB)

## Technologies utilisées

- **Frontend** : HTML, CSS (Tailwind CSS), JavaScript vanilla
- **Traitement Excel** : SheetJS (xlsx.js) - traitement côté client
- **Hébergement** : Netlify (site statique)

## Fichiers pour le déploiement Netlify

Pour déployer sur Netlify, vous avez besoin de :
- `index.html` - Le fichier principal de l'application
- `netlify.toml` - Configuration Netlify pour le routage

C'est tout ! Aucun build ou compilation nécessaire.

## Licence

Ce projet est libre d'utilisation.
