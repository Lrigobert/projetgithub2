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
