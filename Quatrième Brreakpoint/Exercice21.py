def ecrire_fichier(nom_fichier, n):
    with open(nom_fichier, 'w') as f:
        for i in range(n):
            chaine = input("Entrez une chaîne de caractères : ")
            f.write(chaine + "\n")


ecrire_fichier("data.txt", 3)
