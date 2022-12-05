"""" Auteur : BEN GUIRAT; FABIAN
     Début projet : 05/12/22
     Projet : SPACE INVADER        
"""


"""import toutes les fonctions importantes"""

from tkinter import Tk, Label, Button
from tkinter import BOTTOM, Canvas, LEFT

"""Création de fenêtre graphique"""
Fenetre= Tk()
Fenetre.title('Space Invaders')
Fenetre.configure(bg='black')
Title = Label(Fenetre, text = " Space Invaders",relief ='raised', fg = "blue", font = ("Courier", 30))
Title.pack()
BouttonQuitt = Button(Fenetre, text = " QUITER LA PARTIE", fg = "red",relief = 'groove', command =Fenetre.destroy )
BouttonQuitt.pack(side = BOTTOM, padx = 30, pady = 70)
BouttonRejouer = Button(Fenetre, text = " Play again", fg = "red",relief = 'groove' )
BouttonRejouer.pack(side = BOTTOM , padx = 40, pady = 5)

Largeur = 1920
Hauteur = 2500
Canevas = Canvas(Fenetre, width = Largeur, height = Hauteur, bg = 'black')
monCanvas = Canvas(Fenetre, width=70, height=70, bg='ivory', borderwidth=0, highlightthickness=0 )
monCanvas.place(x=600,y=390)

Canevas.pack()
Fenetre.mainloop()