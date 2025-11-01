import json
import os
import uuid
from typing import List, Dict, Any

# Chemin vers le fichier de données
DATA_FILE = "data/products.json"


def load_products_from_json() -> List[Dict[str, Any]]:
    """Charge la liste des produits depuis le fichier JSON."""
    if not os.path.exists(DATA_FILE):
        print(
            f"Attention: Le fichier {DATA_FILE} n'existe pas. Retourne une liste vide."
        )
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(
            f"Erreur: Impossible de décoder le fichier JSON {DATA_FILE}. Retourne une liste vide."
        )
        return []


def save_products_to_json(products: List[Dict[str, Any]]):
    """Sauvegarde la liste des produits dans le fichier JSON."""
    # Assurer que le dossier 'data' existe
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)


def get_categories(products: List[Dict[str, Any]]) -> List[str]:
    """Extrait la liste unique des catégories, y compris 'Toutes'."""
    categories = sorted(list(set(p["category"] for p in products)))
    return ["Toutes"] + categories


# --- Opérations CRUD pour l'administration ---


def create_product(
    products: List[Dict[str, Any]], new_product: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """Ajoute un nouveau produit à la liste."""
    new_product["id"] = str(uuid.uuid4())
    # Assurer que les champs numériques sont au bon format
    try:
        new_product["price"] = float(new_product["price"])
        new_product["stock"] = int(new_product["stock"])
    except (ValueError, TypeError):
        # Gérer l'erreur de conversion si nécessaire, ici on laisse l'application Taipy gérer la validation
        pass

    products.append(new_product)
    save_products_to_json(products)
    return products


def read_product(
    products: List[Dict[str, Any]], product_id: str
) -> Dict[str, Any] | None:
    """Récupère un produit par son ID."""
    return next((p for p in products if p["id"] == product_id), None)


def update_product(
    products: List[Dict[str, Any]], updated_product: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """Met à jour un produit existant."""
    for i, product in enumerate(products):
        if product["id"] == updated_product["id"]:
            # Assurer que les champs numériques sont au bon format
            try:
                updated_product["price"] = float(updated_product["price"])
                updated_product["stock"] = int(updated_product["stock"])
            except (ValueError, TypeError):
                # Gérer l'erreur de conversion si nécessaire
                pass

            products[i] = updated_product
            save_products_to_json(products)
            return products
    return products  # Si non trouvé, retourne la liste inchangée


def delete_product(
    products: List[Dict[str, Any]], product_id: str
) -> List[Dict[str, Any]]:
    """Supprime un produit par son ID."""
    products[:] = [p for p in products if p["id"] != product_id]
    save_products_to_json(products)
    return products


# --- Fonctions de gestion du panier ---


def add_to_cart(
    cart_items: List[Dict[str, Any]], product: Dict[str, Any], quantity: int
) -> List[Dict[str, Any]]:
    """Ajoute un produit au panier ou augmente sa quantité."""
    # Vérifier si l'article est déjà dans le panier
    for item in cart_items:
        if item["product"]["id"] == product["id"]:
            item["quantity"] += quantity
            return cart_items

    # Ajouter le nouvel article
    cart_items.append({"product": product, "quantity": quantity})
    return cart_items


def remove_from_cart(
    cart_items: List[Dict[str, Any]], product_id: str
) -> List[Dict[str, Any]]:
    """Retire un produit du panier."""
    cart_items[:] = [item for item in cart_items if item["product"]["id"] != product_id]
    return cart_items


def calculate_total(cart_items: List[Dict[str, Any]]) -> float:
    """Calcule le total du panier."""
    return sum(item["product"]["price"] * item["quantity"] for item in cart_items)


def clear_cart() -> List[Dict[str, Any]]:
    """Vide le panier après une commande."""
    return []
