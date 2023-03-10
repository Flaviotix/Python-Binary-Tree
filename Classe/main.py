import datetime
from commande import Commande
from client import Client


# Test de la classe Commande
date = datetime.date.today()
commande1 = Commande(date, "CMD01", 100)
print(commande1)
print(commande1.calculTVA())

# Test de la classe Client
client1 = Client("Didier Bourdon", "1 rue de la paix")
print(client1)
print(client1.contacter())

print("\n")
# Test de l'opération d'addition entre deux commandes
commande1 = Commande(datetime.date(2023, 1, 12), "CMD01", 100)
commande2 = Commande(datetime.date.today(), "CMD02", 200)
commande3 = commande1 + commande2
print(commande3)

# Test de la méthode acquitter() de la classe Commande
commande1 = Commande(datetime.date(2022, 8, 12), "CMD01", 100)
commande_acquittee = commande1.acquitter()
print("\n")
print(commande1)  # affiche la commande originale
print(commande_acquittee)  # affiche la commande acquittée
