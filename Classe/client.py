class Client:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse

    def set_nom(self, nom):
        self.nom = nom

    def set_adresse(self, adresse):
        self.adresse = adresse

    def get_nom(self):
        return self.nom

    def get_adresse(self):
        return self.adresse

    def contacter(self):
        return f"Nom : {self.nom}\nAdresse : {self.adresse}"

    def __str__(self):
        return f"Client {self.nom} - Adresse : {self.adresse}"
