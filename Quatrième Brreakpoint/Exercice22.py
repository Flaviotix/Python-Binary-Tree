def verifier_emails(nom_fichier):
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            email = ligne.strip()
            if "@" in email and email.endswith(".com"):
                print(email, "est un email valide.")
            else:
                print(email, "n'est pas un email valide.")


verifier_emails("data.txt")
