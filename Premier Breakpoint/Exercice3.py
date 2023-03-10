nombre = float(input("Entrez un nombre : "))
if nombre >= 0:
    racine = nombre ** 0.5
    print("La racine carrée de", nombre, "est", racine)
else:
    print("Le nombre doit être positif ou nul.")
