def conversion(convertir) :
    ar = convertir.find("EA")
    if ar != -1:
        somme = convertir[2:]
        somme = int(somme)
        resultat = somme*4000
        print(resultat, "Ariary")


    er = convertir.find("AE")
    if er != -1:
        somme = convertir[2:]
        somme = int(somme)
        resultat = somme/4000
        print(resultat, "Euros")

Euros = 0
AryAry = 0

convertir = str(input("""EA (Euro en Ariary) ou AE (Ariary en Euro)? Précisez le montant à convertir :  """))

conversion(convertir)












