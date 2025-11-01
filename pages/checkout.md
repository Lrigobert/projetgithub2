# Paiement et Livraison

<|part|render={len(cart_items) > 0}|
<|layout|columns=1fr 1fr|
<|card|
## Informations de Livraison et Paiement

<|{checkout_name}|input|label=Nom Complet|>
<|{checkout_address}|input|label=Adresse de Livraison|>
<|{checkout_email}|input|label=Adresse E-mail|>
<|{checkout_payment}|selector|lov={['Carte Bancaire', 'PayPal', 'Virement Bancaire']}|label=Mode de Paiement|>

<br/>
<|button|label=Confirmer la Commande|on_action=submit_checkout|class_name=btn-primary|>
|>

<|card|
## Récapitulatif de la Commande

<|{cart_items}|table|columns={['product', 'quantity']}|
| Produit | Quantité | Prix |
|:---|:---|:---|
| <|{item['product']['name']}|text|> | <|{item['quantity']}|number|format=int|> | <|{item['product']['price'] * item['quantity']}|number|format=$.2f|> |
|>

<br/>
### Total à Payer : <|{cart_total}|number|format=$.2f|> €
|>
|>
|>

<|part|render={len(cart_items) == 0}|
<|status|image=error|title=Panier Vide|
Votre panier est vide. Impossible de procéder au paiement. Veuillez retourner au [catalogue](/catalogue).
|>
|>
