# app.py - Point d'entrée de l'application E-commerce Taipy

from taipy.gui import Gui
import data_manager
from taipy.gui.state import State
import pandas as pd

# Configuration de base de l'application
pages = {
    "/": "pages/catalogue.md",  # Page d'accueil par défaut
    "catalogue": "pages/catalogue.md",
    "details": "pages/details.md",
    "panier": "pages/panier.md",
    "checkout": "pages/checkout.md",
    "confirmation": "pages/confirmation.md",
    "admin": "pages/admin.md",
}

# Initialisation des variables d'état globales
# Ces variables seront gérées et mises à jour par les fonctions Python
products_data = []  # Liste des produits chargée depuis data/products.json
filtered_products = pd.DataFrame()  # DataFrame pour les produits filtrés/recherchés
categories = []  # Liste des catégories
cart_items = (
    []
)  # Liste des articles dans le panier (dictionnaires avec 'product', 'quantity')
cart_total = 0.0  # Total du panier
selected_product = None  # Produit actuellement affiché sur la page de détails
search_text = ""  # Texte de recherche
selected_category = "Toutes"  # Filtre de catégorie
min_price = 0.0  # Filtre de prix minimum
max_price = 1000.0  # Filtre de prix maximum

# --- Fonctions de gestion des données et du panier (à implémenter dans data_manager.py) ---


def load_products():
    """Charge les données des produits au démarrage."""
    global products_data, categories, filtered_products
    print("Chargement des données de produits...")
    products_data = data_manager.load_products_from_json()
    categories = data_manager.get_categories(products_data)
    # Initialiser filtered_products comme un DataFrame pour l'affichage Taipy
    filtered_products = pd.DataFrame(products_data)


def calculate_cart_total(state):
    """Calcule le total du panier."""
    # Cette fonction utilise data_manager.py
    global cart_total
    state.cart_total = data_manager.calculate_total(state.cart_items)


def add_to_cart_action(state: State, product_id: str):
    """Ajoute un produit au panier."""
    product = data_manager.read_product(products_data, product_id)
    if product:
        state.cart_items = data_manager.add_to_cart(state.cart_items, product, 1)
        calculate_cart_total(state)


def remove_from_cart_action(state: State, product_id: str):
    """Retire un produit du panier."""
    state.cart_items = data_manager.remove_from_cart(state.cart_items, product_id)
    calculate_cart_total(state)


def clear_cart_action(state: State):
    """Vide le panier."""
    state.cart_items = data_manager.clear_cart()
    calculate_cart_total(state)


def filter_products(state: State):
    """Filtre les produits en fonction de la recherche, catégorie et prix."""
    global filtered_products, products_data

    df = pd.DataFrame(products_data)

    # 1. Filtrer par catégorie
    if state.selected_category != "Toutes":
        df = df[df["category"] == state.selected_category]

    # 2. Filtrer par prix
    df = df[(df["price"] >= state.min_price) & (df["price"] <= state.max_price)]

    # 3. Filtrer par texte de recherche (nom ou description)
    if state.search_text:
        search_lower = state.search_text.lower()
        df = df[
            df["name"].str.lower().str.contains(search_lower)
            | df["description"].str.lower().str.contains(search_lower)
        ]

    state.filtered_products = df.reset_index(drop=True)


def select_product_action(state: State, product_id: str):
    """Sélectionne un produit pour la page de détails et navigue."""
    state.selected_product = data_manager.read_product(products_data, product_id)
    state.gui.navigate("details")


# Variables d'état pour le Checkout
checkout_name = "John Doe"
checkout_address = "123 Rue de Taipy"
checkout_email = "john.doe@taipy.com"
checkout_payment = "Carte Bancaire"

# Variables d'état pour l'Administration (CRUD)
admin_product_id = None
admin_name = ""
admin_category = "Électronique"
admin_price = 0.0
admin_description = ""
admin_image_url = ""
admin_stock = 0


def admin_reset_form(state: State):
    """Réinitialise le formulaire d'administration."""
    state.admin_product_id = None
    state.admin_name = ""
    state.admin_category = "Électronique"
    state.admin_price = 0.0
    state.admin_description = ""
    state.admin_image_url = ""
    state.admin_stock = 0


def admin_load_product_for_edit(state: State, product_id: str):
    """Charge les données d'un produit sélectionné dans le formulaire d'administration."""
    product = data_manager.read_product(products_data, product_id)
    if product:
        state.admin_product_id = product["id"]
        state.admin_name = product["name"]
        state.admin_category = product["category"]
        state.admin_price = product["price"]
        state.admin_description = product["description"]
        state.admin_image_url = product["image_url"]
        state.admin_stock = product["stock"]


def admin_save_product(state: State):
    """Sauvegarde ou met à jour un produit."""
    global products_data

    new_data = {
        "id": state.admin_product_id,
        "name": state.admin_name,
        "category": state.admin_category,
        "price": state.admin_price,
        "description": state.admin_description,
        "image_url": state.admin_image_url,
        "stock": state.admin_stock,
    }

    if state.admin_product_id:
        # Update
        products_data = data_manager.update_product(products_data, new_data)
    else:
        # Create
        products_data = data_manager.create_product(products_data, new_data)

    # Après sauvegarde, réinitialiser le formulaire et mettre à jour le catalogue
    admin_reset_form(state)
    filter_products(state)  # Pour mettre à jour l'affichage du catalogue


def admin_delete_product(state: State, product_id: str):
    """Supprime un produit."""
    global products_data
    products_data = data_manager.delete_product(products_data, product_id)
    filter_products(state)  # Pour mettre à jour l'affichage du catalogue


def reset_filters(state: State):
    """Réinitialise les variables de filtre à leurs valeurs par défaut."""
    state.search_text = ""
    state.selected_category = "Toutes"
    state.min_price = 0.0
    state.max_price = 1000.0
    filter_products(state)


def submit_checkout(state: State):
    """Simule la soumission de la commande."""
    if state.cart_items:
        print(f"Commande soumise par {state.checkout_name} ({state.checkout_email})")
        print(f"Adresse de livraison: {state.checkout_address}")
        print(f"Total: {state.cart_total} €")

        # Logique de commande (ici, simple impression)

        # Vider le panier et naviguer vers la confirmation
        clear_cart_action(state)
        state.gui.navigate("confirmation")
    else:
        print("Erreur: Le panier est vide.")


# --- Configuration de l'interface utilisateur (GUI) ---

# Définition du template de base (layout, menu de navigation)
root_md = """
<|navbar|lov={['catalogue', 'panier', 'admin']}|>

<|content|>
"""

# Création de l'application Taipy
gui = Gui(pages=pages)

if __name__ == "__main__":
    load_products()  # Chargement initial des données
    gui.run(title="Taipy E-commerce", host="0.0.0.0", port=8080, dark_mode=True)
