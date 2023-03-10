email = input("Entrez votre adresse e-mail : ")

if "@" in email and email.endswith(".com"):
    print("Ceci est un email valide.")
else:
    print("Ceci n'est pas un email valide.")
