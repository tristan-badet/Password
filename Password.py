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

if mdpLenght == True and mdpLower == True and mdpUpper == True and mdpNumber == True and mdpSpecial == True:
    print("Votre mot de passe respecte les exigences de sécurité")
else:
    print("Erreur, le mot de passe ne respecte pas les exigences de sécurité")
