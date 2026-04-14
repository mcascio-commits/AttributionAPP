# Attributions — Version Railway (cloud)

## Déploiement sur Railway

### Étape 1 — Créer un compte Railway
1. Aller sur https://railway.app
2. Créer un compte (gratuit, carte de crédit requise pour le volume persistant)

### Étape 2 — Créer le projet
1. Cliquer **New Project** → **Deploy from GitHub repo**
2. Connecter votre compte GitHub si nécessaire
3. Créer un nouveau repository GitHub et y pousser ce dossier (voir ci-dessous)

### Étape 3 — Pousser le code sur GitHub
```bash
cd railway_app
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/VOTRE_USERNAME/attributions-isnd.git
git push -u origin main
```

### Étape 4 — Ajouter PostgreSQL sur Railway
1. Dans votre projet Railway, cliquer **+ New** → **Database** → **PostgreSQL**
2. Railway crée automatiquement la variable `DATABASE_URL`
3. Votre app la détecte automatiquement et utilise PostgreSQL

### Étape 5 — Variables d'environnement
Dans Railway → votre service → **Variables**, ajouter :
```
SECRET_KEY = une_chaine_aleatoire_longue_et_secrete_ex_abc123xyz789
```

Pour générer une clé secrète :
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

### Étape 6 — Volume persistant (optionnel — SQLite seulement)
Si vous préférez SQLite plutôt que PostgreSQL :
1. Railway → votre service → **Volumes**
2. Créer un volume monté sur `/app/data`
3. Coût : ~5$/mois

### Étape 7 — Importer les données depuis votre base locale
Une fois déployé, pour transférer vos données SQLite vers PostgreSQL :
```bash
python3 migrate_sqlite_to_pg.py
```
(script inclus dans ce dossier)

---

## Comptes par défaut

Après le premier déploiement, deux comptes sont créés automatiquement :

| Rôle | Identifiant | Mot de passe |
|------|-------------|--------------|
| Administrateur | `admin` | `admin123` |
| Consultation | `consultation` | `consult123` |

**⚠️ IMPORTANT : Changez ces mots de passe immédiatement après connexion !**
Page Utilisateurs → icône clé → Changer mot de passe

---

## Rôles

**Administrateur** — accès complet :
- Modifier toutes les attributions
- Ajouter/supprimer cours, classes, filières
- Gérer le personnel
- Envoyer des mails
- Gérer les comptes utilisateurs

**Consultation** — lecture seule :
- Voir toutes les attributions
- Voir la synthèse et le récapitulatif
- Exporter Excel
- Aucune modification possible

---

## Structure des fichiers

```
railway_app/
├── app.py              # Application Flask principale
├── database.py         # Adaptateur SQLite/PostgreSQL
├── requirements.txt    # Dépendances Python
├── Procfile            # Commande de démarrage Railway
├── railway.json        # Configuration Railway
├── migrate_sqlite_to_pg.py  # Script de migration des données
├── templates/          # Pages HTML
│   ├── base.html       # Template de base avec navigation
│   ├── login.html      # Page de connexion
│   ├── utilisateurs.html    # Gestion des comptes
│   ├── filiere.html    # Vue filière
│   ├── ntpp.html       # NTPP
│   ├── synthese.html   # Synthèse
│   ├── recap.html      # Cours non attribués
│   ├── personnel.html  # Personnel
│   ├── mails.html      # Envoi mails
│   └── gestion.html    # Gestion filières
├── static/
│   ├── css/style.css
│   └── js/app.js, drag.js
└── data/               # Base SQLite locale (ignorée sur Railway)
```
