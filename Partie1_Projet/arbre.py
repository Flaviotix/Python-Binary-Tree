class AB:
    def __init__(self, racine=None, gauche=None, droite=None):
        self.racine = [racine]
        self.gauche = gauche
        self.droite = droite

    def setRacine(self, racine):
        self.racine = [racine]

    def setGauche(self, gauche):
        self.gauche = gauche

    def setDroite(self, droite):
        self.droite = droite

    def getRacine(self):
        return self.racine[0]

    def getGauche(self):
        return self.gauche

    def getDroite(self):
        return self.droite

    def estVide(self):
        return self.racine[0] is None

    def taille(self):
        if self.estVide():
            return 0
        taille_gauche = 0 if self.gauche is None else self.gauche.taille()
        taille_droite = 0 if self.droite is None else self.droite.taille()
        return 1 + taille_gauche + taille_droite

    def hauteur(self):
        if self.estVide():
            return -1
        else:
            hauteur_gauche = -1 if self.gauche is None else self.gauche.hauteur()
            hauteur_droite = -1 if self.droite is None else self.droite.hauteur()
            return 1 + max(hauteur_gauche, hauteur_droite)

    def estABR(self):
        if self.estVide():
            return True
        elif self.gauche is None and self.droite is None:
            return True
        elif self.gauche is None:
            return self.droite.estABR() and self.racine[0] <= self.droite.min()
        elif self.droite is None:
            return self.gauche.estABR() and self.racine[0] >= self.gauche.max()
        else:
            estABR_gauche = self.gauche.estABR(
            ) and self.gauche.max() <= self.racine[0]
            estABR_droite = self.droite.estABR(
            ) and self.racine[0] <= self.droite.min()
            return estABR_gauche and estABR_droite

    def min(self):
        if self.gauche is None:
            return self.racine[0]
        else:
            return self.gauche.min()

    def max(self):
        if self.droite is None:
            return self.racine[0]
        else:
            return self.droite.max()

    def prefixe(self):
        if not self.estVide():
            print(self.racine[0])
            if self.gauche is not None:
                self.gauche.prefixe()
            if self.droite is not None:
                self.droite.prefixe()

    def infixe(self):
        if not self.estVide():
            if self.gauche is not None:
                self.gauche.infixe()
            print(self.racine[0])
            if self.droite is not None:
                self.droite.infixe()

    def postfixe(self):
        if not self.estVide():
            if self.gauche is not None:
                self.gauche.postfixe()
            if self.droite is not None:
                self.droite.postfixe()
            print(self.racine[0])

    def estEquilibre(self):
        if self.estVide():
            return True
        else:
            hauteur_gauche = -1 if self.gauche is None else self.gauche.hauteur()
            hauteur_droite = -1 if self.droite is None else self.droite.hauteur()
            return abs(hauteur_gauche - hauteur_droite) <= 1 and (self.gauche is None or self.gauche.estEquilibre()) and (self.droite is None or self.droite.estEquilibre())
