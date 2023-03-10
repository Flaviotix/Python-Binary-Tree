import datetime


class Commande:
    def __init__(self, date, numero, prix=0):
        self.date = date
        self.numero = numero
        self.prix = prix

    def set_date(self, date):
        self.date = date

    def set_numero(self, numero):
        self.numero = numero

    def set_prix(self, prix):
        self.prix = prix

    def get_date(self):
        return self.date

    def get_numero(self):
        return self.numero

    def get_prix(self):
        return self.prix

    def acquitter(self):
        return CommandeAcquittee(self.date, self.numero, self.prix, datetime.date.today())

    def calculTVA(self):
        return self.prix * 0.196

    def __str__(self):
        return f"Commande {self.numero} du {self.date} - Prix : {self.prix} €"

    def __add__(self, other):
        max_numero = max(int(self.numero[3:]), int(other.numero[3:]))
        new_numero = f"CMD{max_numero + 1:02d}"
        new_prix = self.prix + other.prix
        new_date = max(self.date, other.date)
        return Commande(new_date, new_numero, new_prix)


# J'ai des erreurs d'importation de module concercant des dépendances circulaire (j'ai rien compris) du coup je l'ai mis là meme si c'est pas beau ^^
class CommandeAcquittee(Commande):
    def __init__(self, date, numero, prix, date_paiement=datetime.date.today()):
        super().__init__(date, numero, prix)
        self.date_paiement = date_paiement

    def acquitter(self):
        return self

    def set_date_paiement(self, date_paiement):
        self.date_paiement = date_paiement

    def get_date_paiement(self):
        return self.date_paiement

    def __str__(self):
        if self.date_paiement is not None:
            return f"Commande acquittée {self.numero} du {self.date} le {self.date_paiement} - Prix: {self.prix}"
