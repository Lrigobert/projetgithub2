# Page Catalogue

<|layout|columns=1fr 4fr|
<|sidebar|
## Filtres et Recherche

### Recherche
<|{search_text}|input|label=Rechercher un produit|on_change=filter_products|>

### Catégorie
<|{selected_category}|selector|lov={categories}|label=Filtrer par catégorie|on_change=filter_products|>

### Prix (Max: <|{max_price}|text|>)
<|{max_price}|slider|min=10|max=1000|step=10|label=Prix Maximum|on_change=filter_products|>

<|button|label=Réinitialiser les filtres|on_action=reset_filters|>
|>

<|content|
# Catalogue de Produits

<|{filtered_products}|layout|columns=1 1 1|
<|card|class_name=product-card|
### <|{row['name']}|text|>
<|{row['image_url']}|image|width=100%|>
**<|{row['price']}|text|> €**
<|{row['description']}|text|>
<br/>
<|{row['id']}|button|label=Voir Détails|on_action=select_product_action|>
<|{row['id']}|button|label=Ajouter au Panier|on_action=add_to_cart_action|>
|>
|>
|>
|>
