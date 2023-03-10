chaine = "kayak"
inverse = ""
for caractere in chaine:
    inverse = caractere + inverse

if chaine == inverse:
    print("Ceci est un palindrome.")
else:
    print("Ceci n'est pas un palindrome.")
