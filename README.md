
# Projet d'Automatisation de la Qualité de Code (DevOps)

Ce projet implémente un pipeline d'intégration continue (CI) pour garantir la qualité et la conformité du code Python, tel que demandé dans les consignes du professeur.

Il se concentre sur trois aspects principaux :
1.  **Typage Strict (Type Hinting)** avec `mypy`.
2.  **Style et Normes de Codage** avec `flake8` et `black`.
3.  **Automatisation et Feedback Personnalisé** avec GitHub Actions et une simulation d'appel à une IA.

## 1. Structure du Projet

```
devops-code-quality/
├── .github/
│   └── workflows/
│       └── main.yml      # Workflow GitHub Actions
├── main.py               # Exemple de code Python non conforme
├── setup.cfg             # Configuration des linters (flake8, black, mypy)
├── ai_feedback.py        # Script Python pour le feedback IA personnalisé
├── .gitignore            # Fichiers à ignorer par Git
└── README.md             # Ce fichier
```

## 2. Outils de Qualité de Code

Les outils suivants sont utilisés et configurés via `setup.cfg` :

| Outil | Rôle | Configuration |
| :--- | :--- | :--- |
| **mypy** | Vérificateur de typage statique (Type Hinting) | `disallow_untyped_defs = True` pour forcer le typage. |
| **flake8** | Linter pour les erreurs de style et de logique | `max-line-length = 88` pour s'aligner avec `black`. |
| **black** | Formatteur de code automatique | `line-length = 88` pour un style uniforme. |

## 3. Mise en Place Locale

Pour tester les outils localement :

1.  **Cloner le dépôt** (après l'avoir créé sur GitHub et y avoir poussé ce code).
2.  **Créer et activer l'environnement virtuel** :
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Installer les dépendances** :
    ```bash
    pip install mypy flake8 black openai
    ```
4.  **Exécuter les vérifications** :
    ```bash
    # Formattage (Black)
    black main.py
    
    # Linter (Flake8)
    flake8 main.py
    
    # Vérification de typage (Mypy)
    mypy main.py
    ```

## 4. Automatisation avec GitHub Actions

Le fichier `.github/workflows/main.yml` configure un workflow qui s'exécute à chaque `push` ou `pull_request` sur la branche `main`.

**Étapes clés du workflow :**

1.  **Installation** des dépendances (`mypy`, `flake8`, `black`).
2.  **Exécution** des vérifications de qualité de code.
3.  **Génération du Rapport** : Les sorties de `flake8` et `mypy` sont capturées dans des fichiers (`flake8_report.txt`, `mypy_report.txt`).
4.  **Feedback IA** : Si les vérifications échouent, le script `ai_feedback.py` est appelé. Il utilise le rapport combiné pour générer un message personnalisé et motivant via l'API OpenAI (nécessite la variable `OPENAI_API_KEY` dans les Secrets GitHub).
5.  **Blocage** : Le workflow est configuré pour **échouer** si les vérifications ne passent pas (`exit 1` dans l'étape de feedback), bloquant ainsi l'intégration du code non conforme.

## 5. Gestion des Secrets (IA et Sécurité)

Conformément aux consignes, la clé API pour l'IA (`OPENAI_API_KEY`) **ne doit pas** être stockée dans le code source.

*   **Dans GitHub Actions** : Elle doit être configurée comme un **Secret de Dépôt** dans les paramètres de votre projet GitHub.
*   **Dans le script `ai_feedback.py`** : Le script utilise la librairie `openai` qui lit automatiquement la clé depuis la variable d'environnement `OPENAI_API_KEY` injectée par GitHub Actions.

Le script `ai_feedback.py` contient une logique de simulation si la clé API n'est pas trouvée, ce qui permet de tester le flux sans clé, mais pour la fonctionnalité complète, la clé est requise.


# Taipy E-commerce : Projet Démonstration

Ce projet est une application e-commerce complète, développée en Python en utilisant le framework **Taipy** (Taipy GUI et Taipy Core) pour l'interface utilisateur et la gestion des données. Il est conçu pour être simple, moderne et prêt à être déployé.

## 🚀 Fonctionnalités

| Catégorie | Fonctionnalité | Description |
| :--- | :--- | :--- |
| **Catalogue** | Liste des Produits | Affichage des produits avec image, prix et description. |
| | Recherche & Filtres | Recherche par nom/description, filtre par catégorie et par prix maximum. |
| | Détails Produit | Page dédiée pour chaque produit. |
| **Achat** | Panier d'Achat | Ajout/suppression d'articles, calcul automatique du total. |
| | Checkout | Formulaire de commande simple (nom, adresse, email, paiement). |
| | Confirmation | Page de confirmation après soumission de la commande. |
| **Administration** | CRUD Produits | Interface d'administration pour **C**réer, **R**echercher, **U**pdate et **D**elete les produits (les données sont stockées dans `data/products.json`). |

## 🛠️ Structure du Projet

```
taipy_ecommerce/
├── app.py                  # Point d'entrée de l'application Taipy
├── data_manager.py         # Module de gestion des données (CRUD, panier)
├── requirements.txt        # Liste des dépendances Python
├── .gitignore              # Fichier d'exclusion pour Git
├── data/
│   └── products.json       # Fichier de données de démonstration (JSON)
├── pages/
│   ├── catalogue.md        # Page d'accueil et de liste des produits
│   ├── details.md          # Page de détails d'un produit
│   ├── panier.md           # Page du panier d'achat
│   ├── checkout.md         # Page de paiement/livraison
│   ├── confirmation.md     # Page de confirmation de commande
│   └── admin.md            # Page d'administration (CRUD)
└── assets/                 # Dossier pour les images locales (actuellement utilise des placeholders)
```

## ⚙️ Installation et Démarrage

Ce projet nécessite Python 3.8+ et utilise le gestionnaire de paquets `pip`.

### 1. Cloner le dépôt

```bash
git clone <URL_DU_DEPOT>
cd taipy_ecommerce
```

### 2. Installer les dépendances

Toutes les dépendances sont listées dans `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 3. Lancer l'application

L'application Taipy démarrera et sera accessible dans votre navigateur.

```bash
python app.py
```

L'application sera accessible à l'adresse par défaut : `http://127.0.0.1:8080` (ou l'adresse affichée dans la console).

## 📝 Données et Stockage

Les données des produits sont stockées dans le fichier `data/products.json`. Ce système de stockage simple (fichiers JSON) permet de respecter l'exigence de ne pas utiliser de base de données complexe.

Toute modification effectuée via l'interface d'administration (CRUD) est sauvegardée en temps réel dans ce fichier `products.json`.

## 🎨 Design et Style

Le design est géré par la librairie Taipy GUI, assurant un rendu moderne et responsive par défaut. Le thème sombre est activé dans `app.py`.

---
*Développé avec Taipy par Manus AI*
=======
# projetgithub2
projet2
 80b7985fdacca9bae12f6f9fb0d3d202ad138490
 a9bdc59952916f8fade2111645237dcfeb1df079
