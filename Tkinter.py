from tkinter import *

def nettoyage():
    valeur = value.get().upper()
    val1 = valeur.split("\B\T")
    val2 = val1[1].split("\T")
    val3 = val2[1].split("\\N")
    val4 = val2[0]
    val5= val3[0]
    destination1.set(val4)
    destination2.set(val5)



fenetre = Tk()

source = Label(fenetre, text='Source : ')
source.pack()


value = StringVar()
value.set("")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

bouton_clean = Button(fenetre, text='CLEAN', command=nettoyage)
bouton_clean.pack()


champ_label = Label(fenetre, text='Déstination ')
champ_label.pack()

destination1 = StringVar()
destination1.set("")
entree1 = Entry(fenetre, textvariable=destination1, width=20)
entree1.pack()

destination2 = StringVar()
destination2.set("")
entree2 = Entry(fenetre, textvariable=destination2, width=20)
entree2.pack()

fenetre.mainloop()




