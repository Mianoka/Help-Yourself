nom = input("Entrez le nom d'un fichier : ")
c = []

try:
    fichier = open(nom + ".txt")
    for i in fichier:
        valeur = i[4:].split("cm\\t")
        val = valeur[1].split("cm\\n")
        print(valeur[0],val[0])
        if valeur[0]>val[0]:
            print("Oui")
        else:
            print("Non")
        print(i)
except:
    print('Fichier non trouvé')