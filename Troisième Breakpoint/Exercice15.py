# Initialiser la liste
liste = [17, 38, 10, 25, 72]

# Trier et afficher la liste
liste.sort()
print(liste)

# Ajouter 12 et afficher la liste
liste.append(12)
print(liste)

# Renverser et afficher la liste
liste.reverse()
print(liste)

# Afficher l'indice de l'élément 17
print(liste.index(17))

# Enlever 38 et afficher la liste
liste.remove(38)
print(liste)

# Afficher la sous-liste du 2e au 3e élément
print(liste[1:3])

# Afficher la sous-liste du début au 2e élément
print(liste[:2])

# Afficher la sous-liste du 3e élément à la fin de la liste
print(liste[2:])

# Afficher la sous-liste complète de la liste
print(liste[:])
