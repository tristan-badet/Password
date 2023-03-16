import hashlib
import json



mdpUtilisateur = str(input("Veuillez entrer votre mot de passe : "))
mdpLenght = False
mdpUpper = False
mdpLower = False
mdpSpecial = False
mdpNumber = False
passwordstock = []





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
    crypt = hashlib.sha256(mdpUtilisateur.encode('utf-8')).hexdigest()
    passcrypt = {"Password": str(crypt)}
    with open ("passwordstock.json", "r+") as json_file:
        var = json.load(json_file)
        var["mdp"].append(passcrypt)
        json_file.seek(0)
        json.dump(var, json_file, indent=4)
    # différents choix tentative JSON 
    choice = int(input("Sélectionnez 1 si vous voulez rajouter des mots de passe. \nSélectionnez 2 si vous voulez afficher vos mots de passe. \nSélectionnez 3 si vous voulez arrêter le programme.:"))
    if choice == 1:
        mdpAddLengt = False
        mdpAddUpper = False
        mdpAddLower = False
        mdpAddSpecial = False
        mdpAddNumber = False
        mdpAddUtilisateur = str(input("Veuillez ajouter un mot de passe: "))
        if len(mdpAddUtilisateur) > 7:
            mdpAddLenght = True
        else:
            mdpAddLenght = False
        for char in mdpAddUtilisateur:
            if char.islower():
                mdpAddLower = True
            elif char.isupper():
                mdpAddUpper = True
            elif char.isdigit():
                mdpAddNumber = True
            elif not char.isalnum():
                mdpAddSpecial = True
        while mdpAddLenght == False or mdpAddUpper == False or mdpAddLower == False or mdpAddNumber == False or mdpAddSpecial == False:
            print("Votre mot de passe ne répond pas à toutes les exigences de sécurité")
            mdpAddUtilisateur = str(input("Veuillez réessayer un autre mot de passe: "))
            if len(mdpAddUtilisateur) > 7:
                mdpAddLenght = True
            else:
                mdpAddLenght = False
            for char in mdpAddUtilisateur:
                if char.islower():
                    mdpAddLower = True
                elif char.isupper():
                    mdpAddUpper = True
                elif char.isdigit():
                    mdpAddNumber = True
                elif not char.isalnum():
                    mdpAddSpecial = True
        else:
            print("Votre mot de passe répond aux exigences de sécurité")
            cryptAdd = hashlib.sha256(mdpAddUtilisateur.encode('utf-8')).hexdigest()
            passcryptAdd = {"Password": str(cryptAdd)}
            with open ("passwordstock.json", "r+") as json_file:
                varAdd = json.load(json_file)
                varAdd["mdp"].append(passcryptAdd)
                json_file.seek(0)
                json.dump(varAdd, json_file, indent=4)
    elif choice == 2:
        with open("passwordstock.json", "r") as f:
            data = json.load(f)
            print(data)
    elif choice == 3:
        print("Le programme s'arrête")


    
