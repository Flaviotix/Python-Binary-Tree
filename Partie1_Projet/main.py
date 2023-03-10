from arbre import AB

# Création de l'arbre A1, qui est vide
A1 = AB()

# Test de la méthode estVide() sur A1
print("A1 est vide :", A1.estVide())

# Création de l'arbre A2, qui a une racine avec la valeur 5
A2 = AB(5)

# Test de la méthode estVide() sur A2
print("A2 est vide :", A2.estVide())

# Création de l'arbre A3, qui a une racine avec la valeur 3
A3 = AB(3)

# Modification de la partie gauche de A2 pour y placer A3
A2.setGauche(A3)

# Création de l'arbre Atest
A5 = AB(5, AB(3), AB(8))
A12 = AB(12)
Atest = AB(10, A5, A12)

# Test de la méthode estVide() sur Atest
print("Atest est vide :", Atest.estVide())

# Test de la méthode taille() sur Atest
print("Taille de l'arbre Atest :", Atest.taille())

# Test de la méthode hauteur() sur Atest
print("Hauteur de l'arbre Atest :", Atest.hauteur())

# Test de la méthode estABR() sur Atest
print("Atest est un ABR :", Atest.estABR())

# Test de la méthode estEquilibre() sur Atest
print("Atest est équilibré :", Atest.estEquilibre())

# Test de la méthode prefixe() sur Atest
print("Parcours préfixe de l'arbre Atest :")
Atest.prefixe()

# Test de la méthode infixe() sur Atest
print("Parcours infixe de l'arbre Atest :")
Atest.infixe()

# Test de la méthode postfixe() sur Atest
print("Parcours postfixe de l'arbre Atest :")
Atest.postfixe()
