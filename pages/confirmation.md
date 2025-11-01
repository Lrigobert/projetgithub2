# Confirmation de Commande

<|status|image=success|title=Commande Confirmée !|
Votre commande a été passée avec succès. Un e-mail de confirmation a été envoyé à **<|{checkout_email}|text|>** avec les détails de votre commande.

**Montant total :** <|{cart_total}|number|format=$.2f|> €

**Adresse de livraison :** <|{checkout_address}|text|>

Merci de votre confiance !
|>

<br/>
<|button|label=Retour au Catalogue|on_action=lambda s: s.gui.navigate("catalogue")|>
