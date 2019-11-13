from tkinter import *
from threading import Thread
import serial

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
        moncontenu.set(reste)
        fichier.close()


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


def credit():
    valeur = int(value.get())
    if valeur >= 0:
        nouveau = int(moncontenu.get()) + valeur
        moncontenu.set(nouveau)
        nouv = str(nouveau)
        fichier = open("compte.txt", "w")
        fichier.write(nouv)


crediter = Button(fenetre, text='Créditer', command=credit)
crediter.pack()


class arduino(Thread):
    def _init_(self):
        Thread._init_(self)

    def run(self):
        arduino = serial.Serial('COM5', 9600)
        arduino.read()
        if TRUE:
            mihena()


thread_1 = arduino()
thread_1.start()

fenetre.mainloop()
