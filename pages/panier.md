# Votre Panier

<|part|render={len(cart_items) == 0}|
<|status|image=info|title=Panier Vide|
Votre panier est actuellement vide. Parcourez notre [catalogue](/catalogue) pour commencer vos achats !
|>
|>

<|part|render={len(cart_items) > 0}|
<|{cart_items}|table|columns={['product', 'quantity']}|
| Nom du Produit | Quantité | Prix Unitaire | Total | Action |
|:---|:---|:---|:---|:---|
| <|{item['product']['name']}|text|> | <|{item['quantity']}|number|format=int|> | <|{item['product']['price']}|number|format=$.2f|> | <|{item['product']['price'] * item['quantity']}|number|format=$.2f|> | <|{item['product']['id']}|button|label=Supprimer|on_action=remove_from_cart_action|> |
|>

<|layout|columns=1fr 1fr|
<|part|
## Total du Panier : <|{cart_total}|number|format=$.2f|> €
|>

<|part|class_name=text-right|
<|button|label=Vider le Panier|on_action=clear_cart_action|class_name=btn-danger|>
<|button|label=Passer à la Caisse|on_action=lambda s: s.gui.navigate("checkout")|class_name=btn-primary|>
|>
|>
|>
