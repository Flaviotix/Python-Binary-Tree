def compterMots(chaine):
    mots = chaine.split()
    freq_mots = {}
    for mot in mots:
        if mot in freq_mots:
            freq_mots[mot] += 1
        else:
            freq_mots[mot] = 1
    return freq_mots


chaine = "Bonjour le monde et le soleil"
print(compterMots(chaine))
