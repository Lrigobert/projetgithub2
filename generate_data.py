import json
import random
import uuid


def generate_products():
    """Génère une liste de produits de démonstration pour l'e-commerce."""

    categories = ["Électronique", "Vêtements", "Livres", "Maison", "Sport"]

    products = [
        {
            "id": str(uuid.uuid4()),
            "name": "Smartphone Ultra",
            "category": "Électronique",
            "price": 799.99,
            "description": "Le smartphone le plus rapide avec un écran OLED 120Hz et un appareil photo 200MP.",
            "image_url": "https://via.placeholder.com/400x300?text=Smartphone",
            "stock": 50,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "T-shirt Coton Bio",
            "category": "Vêtements",
            "price": 29.50,
            "description": "T-shirt 100% coton biologique, doux et confortable. Disponible en plusieurs tailles.",
            "image_url": "https://via.placeholder.com/400x300?text=T-shirt",
            "stock": 200,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "L'Art de Taipy",
            "category": "Livres",
            "price": 45.00,
            "description": "Un guide complet pour maîtriser le framework Taipy, du débutant à l'expert.",
            "image_url": "https://via.placeholder.com/400x300?text=Livre+Taipy",
            "stock": 80,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Enceinte Bluetooth Portable",
            "category": "Électronique",
            "price": 129.99,
            "description": "Son puissant et clair, autonomie de 10 heures. Résistante à l'eau (IPX7).",
            "image_url": "https://via.placeholder.com/400x300?text=Enceinte",
            "stock": 120,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Lampe de Bureau LED",
            "category": "Maison",
            "price": 59.90,
            "description": "Lampe de bureau avec variateur d'intensité et température de couleur réglable.",
            "image_url": "https://via.placeholder.com/400x300?text=Lampe+Bureau",
            "stock": 90,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Chaussures de Course Pro",
            "category": "Sport",
            "price": 110.00,
            "description": "Chaussures légères et amortissantes, idéales pour le marathon.",
            "image_url": "https://via.placeholder.com/400x300?text=Chaussures+Course",
            "stock": 60,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Montre Connectée",
            "category": "Électronique",
            "price": 249.99,
            "description": "Suivi d'activité, GPS intégré et notifications intelligentes.",
            "image_url": "https://via.placeholder.com/400x300?text=Montre+Connectee",
            "stock": 75,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Pull en Laine Mérinos",
            "category": "Vêtements",
            "price": 89.00,
            "description": "Pull chaud et élégant en laine mérinos de haute qualité.",
            "image_url": "https://via.placeholder.com/400x300?text=Pull+Laine",
            "stock": 150,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Roman Fantastique",
            "category": "Livres",
            "price": 19.99,
            "description": "Le premier tome d'une saga épique acclamée par la critique.",
            "image_url": "https://via.placeholder.com/400x300?text=Roman+Fantastique",
            "stock": 110,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Set de Couteaux de Cuisine",
            "category": "Maison",
            "price": 149.99,
            "description": "Set de 5 couteaux professionnels en acier inoxydable.",
            "image_url": "https://via.placeholder.com/400x300?text=Couteaux",
            "stock": 40,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Tapis de Yoga Antidérapant",
            "category": "Sport",
            "price": 35.00,
            "description": "Tapis de yoga épais et écologique, parfait pour tous les niveaux.",
            "image_url": "https://via.placeholder.com/400x300?text=Tapis+Yoga",
            "stock": 130,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Casque Audio sans Fil",
            "category": "Électronique",
            "price": 199.00,
            "description": "Casque à réduction de bruit active, son haute fidélité.",
            "image_url": "https://via.placeholder.com/400x300?text=Casque+Audio",
            "stock": 65,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Veste Imperméable",
            "category": "Vêtements",
            "price": 135.00,
            "description": "Veste légère et totalement imperméable, idéale pour la randonnée.",
            "image_url": "https://via.placeholder.com/400x300?text=Veste+Impermeable",
            "stock": 95,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Cafetière Programmable",
            "category": "Maison",
            "price": 75.00,
            "description": "Cafetière avec minuterie, capacité de 12 tasses.",
            "image_url": "https://via.placeholder.com/400x300?text=Cafetiere",
            "stock": 105,
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Haltères Ajustables (Paire)",
            "category": "Sport",
            "price": 199.99,
            "description": "Haltères ajustables de 2 à 24 kg, gain de place maximal.",
            "image_url": "https://via.placeholder.com/400x300?text=Halteres",
            "stock": 30,
        },
    ]

    # Assurer que tous les produits ont un ID unique
    for product in products:
        if not product.get("id"):
            product["id"] = str(uuid.uuid4())

    return products


if __name__ == "__main__":
    products = generate_products()
    file_path = "data/products.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

    print(
        f"{len(products)} produits de démonstration générés et sauvegardés dans {file_path}"
    )
