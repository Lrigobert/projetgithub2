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
