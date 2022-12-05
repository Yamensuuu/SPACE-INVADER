"""
Lucie Fabian
Yamen Ben Guirat
05/12/2022

Programme permetttant de jouer à Space Invader à traver une fenêtre graphique
"""

from tkinter import Tk, Label, Button
from tkinter import *

"""Création de fenêtre graphique"""
Fenetre= Tk()
Fenetre.title('Space Invaders')
Fenetre.configure(bg='black')
Title = Label(Fenetre, text = " Space Invaders",relief ='raised', fg = "blue", font = ("Courier", 30))
Title.pack()
BouttonQuitt = Button(Fenetre, text = " QUITER LA PARTIE", fg = "red",relief = 'groove', command =Fenetre.destroy )
BouttonQuitt.pack(side = BOTTOM, padx = 30, pady = 70)

Largeur = 2300
Hauteur = 1000
Canevas = Canvas(Fenetre, width = Largeur, height = Hauteur, bg = 'black')
item = Canevas.create_image(650,200,anchor=NW)
print("Image de fond(item",")")
Canevas.pack()
Fenetre.mainloop()