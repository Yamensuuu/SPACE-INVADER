""" Auteur : BEN GUIRAT; FABIAN
     Début projet : 05/12/22
     Projet : SPACE INVADER        
"""


"""Import toutes les fonctions importantes"""

from tkinter import Tk, Label, Button
from tkinter import  BOTTOM, Canvas
import math, random
def Clavier(event) :
    global xo,yo, Canevas        
    touche = event.keysym
    print(touche)
    if touche =='Right' :
         xo+= 20  
    if touche =='Left' :
         xo-= 20
    if touche =='Up' :
         tirer(xo) 
    Canevas.coords(vaisseau, xo-10,yo-10,xo+10,yo+10)

"""
Création fonction animation tir / attaque :
"""

def tirer(xo):
     def deplacement_missile():
          Canevas.move(bullet,0,-3)
          Fenetre.after(20,deplacement_missile)

     bullet = Canevas.create_rectangle(xo-1,yo-10,xo+1,yo+10,fill= 'red',outline = 'blue')


     if Canevas.coords(bullet)[3]<100:
          Canevas.delete(bullet)
     deplacement_missile()


"""Création de fenêtre graphique"""
Fenetre= Tk()
Fenetre.title('Space Invaders')
Fenetre.configure(bg='black')
Title = Label(Fenetre, text = "Space Invaders",relief ='raised', fg = "blue", font = ("Courier", 30))
Title.pack()
BouttonQuitt = Button(Fenetre, text = " QUITER LA PARTIE", fg = "red",relief = 'groove', command =Fenetre.destroy )
BouttonQuitt.pack(side = BOTTOM, padx = 30, pady = 70)
BouttonRejouer = Button(Fenetre, text = " Play again", fg = "red",relief = 'groove' )
BouttonRejouer.pack(side = BOTTOM , padx = 40, pady = 5)

Largeur = 1920
Hauteur = 2500
xo = 550
yo = 370

""" 
Création du vaisseau, pour le moment rectangle.
"""
Canevas = Canvas(Fenetre, width = Largeur, height = Hauteur, bg = 'black')
vaisseau = Canevas.create_rectangle(xo, yo, xo+20, yo+20, fill = 'blue')
Canevas.focus_set()

Canevas.bind('<Key>',Clavier)
Canevas.pack(padx=10,pady=3)









Fenetre.mainloop()


