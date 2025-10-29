# Administration des Produits

<|layout|columns=1fr 2fr|
<|card|
## Formulaire Produit

<|{admin_name}|input|label=Nom du Produit|>
<|{admin_category}|selector|lov={categories}|label=Catégorie|>
<|{admin_price}|number|label=Prix (€)|format=$.2f|>
<|{admin_stock}|number|label=Stock|format=int|>
<|{admin_image_url}|input|label=URL de l'Image|>
<|{admin_description}|input|label=Description|multiline=True|>

<|layout|columns=1fr 1fr|
<|button|label=Sauvegarder|on_action=admin_save_product|class_name=btn-primary|>
<|button|label=Annuler/Nouveau|on_action=admin_reset_form|class_name=btn-secondary|>
|>

<|part|render={admin_product_id is not None}|
<|status|image=info|title=Modification|
Vous êtes en mode modification pour le produit : **<|{admin_name}|text|>**
|>
|>
|>

<|card|
## Liste des Produits

<|{products_data}|table|columns={['name', 'category', 'price', 'stock']}|
| Nom | Catégorie | Prix | Stock | Actions |
|:---|:---|:---|:---|:---|
| <|{row['name']}|text|> | <|{row['category']}|text|> | <|{row['price']}|number|format=$.2f|> | <|{row['stock']}|number|format=int|> | <|{row['id']}|button|label=Modifier|on_action=admin_load_product_for_edit|> <|{row['id']}|button|label=Supprimer|on_action=admin_delete_product|class_name=btn-danger|> |
|>
|>
|>
