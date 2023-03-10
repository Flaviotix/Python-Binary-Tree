email = input("Entrez votre adresse e-mail : ")
if "@" in email and "." in email and email.split(".")[-1].isalpha() and len(email.split(".")[-1]) <= 3:
    print("Ceci est une adresse e-mail valide.")
else:
    print("Ceci n'est pas une adresse e-mail valide.")
