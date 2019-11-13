from tkinter import *
fenetre = Tk()

fichier = open("compte.txt", "r")
contenu = fichier.read()
fichier.close()


def mihena():
    reste = int(moncontenu.get()) - 1000
    if reste >= 0:
        res = str(reste)
        fichier = open("compte.txt", "w")
        fichier.write(res)
        fichier.close()
        moncontenu.set(reste)



cadre = Frame(fenetre, width = 500, height = 300)
cadre.pack(fill = BOTH)

message = Label(cadre, text="Votre crédit actuel en Ariary")
message.pack(side="top", fill=X)


moncontenu = StringVar()
moncontenu.set(contenu)
affichage = Label(fenetre, textvariable = moncontenu)
affichage.pack()

acheter = Button(fenetre, text='Commander', command = mihena)
acheter.pack()

value = StringVar()
value.set("")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

def credit():
    valeur = int(value.get())
    if valeur >= 0 :
        nouveau = int(moncontenu.get()) + valeur
        moncontenu.set(nouveau)
        nouv = str(nouveau)
        fichier = open("compte.txt", "w")
        fichier.write(nouv)

   
crediter = Button(fenetre, text='Créditer', command = credit)
crediter.pack()

fenetre.mainloop()

