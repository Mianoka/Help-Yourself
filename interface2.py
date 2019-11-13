from tkinter import *
from threading import Thread
import serial



def mihena():

    reste = int(moncontenu.get()) - 1000
    if reste >= 0:
        res = str(reste)
        fichier = open("compte.txt", "w")
        fichier.write(res)
        moncontenu.set(reste)
        fichier.close()


def credit():
    valeur = int(value.get())
    if valeur >= 0:
        nouveau = int(moncontenu.get()) + valeur
        moncontenu.set(nouveau)
        nouv = str(nouveau)
        fichier = open("compte.txt", "w")
        fichier.write(nouv)



def affi():


    photo1 = PhotoImage(file="verre.png")
    labl1 = Label(fenetre, image=photo1)
    labl1.image = photo1
    labl1.pack(side="top")

    crediter.pack_forget()
    entree.pack_forget()
    label.pack_forget()
    photo.blank()

    lab = Label(fenetre, text="Merci d'avoir consommer chez nous! Bonne ambiance!")
    lab.pack(side="bottom")

    quitter = Button(fenetre, text = "Quitter", command = fenetre.destroy)
    quitter.pack()



class arduino(Thread):
    def _init_(self):
        Thread._init_(self)

    def run(self):
        arduino = serial.Serial('COM5', 9600)
        arduino.read()
        fichier = open("compte.txt", "r")
        cont = fichier.read()
        contenu = int(cont)
        fichier.close()
        if TRUE and contenu != 0:
            mihena()
            affi()

thread_1 = arduino()
thread_1.start()

fenetre = Tk()


fichier = open("compte.txt", "r")
contenu = fichier.read()
fichier.close()

label = Label(fenetre, text="De la biere?")
label.pack(side = "left")

cadre = Frame(fenetre, width = 500, height = 300)
cadre.pack(fill = BOTH)

message = Label(cadre, text="Votre crédit  en Ariary")
message.pack(side="top", fill=X)

moncontenu = StringVar()
moncontenu.set(contenu)
affichage = Label(fenetre, textvariable=moncontenu)
affichage.pack()

value = StringVar()
value.set("")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()


crediter = Button(fenetre, text='Créditer', command=credit)
crediter.pack()

photo = PhotoImage(file="1.png")
labl = Label(fenetre, image=photo)
labl.image = photo
labl.pack()


fenetre.geometry("800x600")

fenetre.mainloop()