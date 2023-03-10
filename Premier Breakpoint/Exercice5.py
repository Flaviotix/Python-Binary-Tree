pSeuil = 2.3
vSeuil = 7.41

pression = float(input("Entrez la pression courante : "))
volume = float(input("Entrez le volume courant : "))

if pression > pSeuil and volume > vSeuil:
    print("Arrêt immédiat")
elif pression > pSeuil:
    print("Augmenter le volume de l'enceinte")
elif volume > vSeuil:
    print("Diminuer le volume de l'enceinte")
else:
    print("Tout va bien")
