# Détails du Produit

<|{selected_product}|
<|part|render={selected_product is not None}|
<|layout|columns=1fr 2fr|
<|{selected_product['image_url']}|image|width=100%|>

<|part|
# <|{selected_product['name']}|text|>

**Catégorie :** <|{selected_product['category']}|text|>

## Prix : <|{selected_product['price']}|text|> €

### Description
<|{selected_product['description']}|text|>

**Stock disponible :** <|{selected_product['stock']}|text|>

<br/>
<|{selected_product['id']}|button|label=Ajouter au Panier|on_action=add_to_cart_action|class_name=btn-primary|>
<|button|label=Retour au Catalogue|on_action=lambda s: s.gui.navigate("catalogue")|>
|>
|>
|>

<|part|render={selected_product is None}|
<|status|image=info|title=Produit non sélectionné|
Veuillez sélectionner un produit dans le [catalogue](/catalogue).
|>
|>
