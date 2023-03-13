import hashlib

mdpUtilisateur = str(input("Veuillez entrer votre mot de passe : "))
mdpLenght = False
mdpUpper = False
mdpLower = False
mdpSpecial = False
mdpNumber = False

if len(mdpUtilisateur) > 7:
    mdpLenght = True
else:
    mdpLenght = False

for char in mdpUtilisateur:
    if char.islower():
        mdpLower = True
    elif char.isupper():
        mdpUpper = True
    elif char.isdigit():
        mdpNumber = True
    elif not char.isalnum():
        mdpSpecial = True

while mdpLenght == False or mdpUpper == False or mdpLower == False or mdpNumber == False or mdpSpecial == False:
    print("Votre mot de passe ne répond pas à toutes les exigences de sécurité")
    mdpUtilisateur = str(input("Veuillez réessayer un autre mot de passe : "))
    if len(mdpUtilisateur) > 7:
        mdpLenght = True
    else:
        mdpLenght = False
    for char in mdpUtilisateur:
        if char.islower():
            mdpLower = True
        elif char.isupper():
            mdpUpper = True
        elif char.isdigit():
            mdpNumber = True
        elif not char.isalnum():
            mdpSpecial = True
else:
    print("Votre mot de passe répond aux exigences de sécurité")

crypt = hashlib.sha256(mdpUtilisateur.encode("utf-8")).hexdigest

   