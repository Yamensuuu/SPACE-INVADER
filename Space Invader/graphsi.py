"""" Auteur : BEN GUIRAT; FABIAN
     Début projet : 05/12/22
     Projet : SPACE INVADER        
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
Photo = PhotoImage(file = "jeu2.gif")

Largeur = 2300
Hauteur = 1000
Canevas = Canvas(Fenetre, width = Largeur, height = Hauteur, bg = 'black')
item = Canevas.create_image(650,200,anchor=NW,image=Photo)
print("Image de fond(item",")")
Canevas.pack()
Fenetre.mainloop()