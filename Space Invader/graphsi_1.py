"""
Lucie Fabian
Yamen Ben Guirat
05/12/2022

Programme permetttant de jouer à Space Invader à traver une fenêtre graphique
"""

from tkinter import Tk, Label, Button, Menu, Frame, BOTTOM, StringVar, Canvas, NW 
import random, math

#Création de fenêtre graphique
Fenetre= Tk()
Fenetre.title('Space Invaders')
Fenetre.configure(bg='black')
Title = Label(Fenetre, text = " Space Invaders",relief ='raised', fg = "blue", font = ("Courier", 30))
Title.pack()

#Création Frame 1 (contient boutons, score)
Frame1 = Frame(Fenetre, relief = 'groove', bg = 'black')
Frame1.pack(side = BOTTOM)

#boutton pour rejouer une partie
BouttonPlay = Button(Frame1, text='Rejouer', fg = 'blue')
BouttonPlay.pack(side = 'left', padx = 30, pady = 70)

#zone de texte pour afficher le score
Texte = StringVar()
LabelScore = Label(Frame1, textvariable = Texte, fg = 'red')
LabelScore.pack(side = 'left', padx = 30, pady = 70)

#boutton pour quitter le jeu
BouttonQuitt = Button(Frame1, text = " Quitter", fg = "red",relief = 'groove', command =Fenetre.destroy )
BouttonQuitt.pack(side = 'left', padx = 30, pady = 70)

#création du canvas
Largeur = 1000
Hauteur = 500
Canevas = Canvas(Fenetre, width = Largeur, height = Hauteur, bg = 'black')
item = Canevas.create_image(650,200,anchor=NW)
print("Image de fond(item",")")

#création d'une barre de menu => ne fonctionne pas pour l'instant
menubar = Menu(Fenetre)
menufichier = Menu(menubar, tearoff = 0)
menufichier.add_command(label = 'Quitter', command = Fenetre.destroy)
menufichier.add_command(label = 'Quitter2', command = Fenetre.destroy)
menufichier.add_command(label = 'Quitter3', command = Fenetre.destroy)

menubar.add_cascade(label='Test 1', menu = menufichier)
#menubar.add_cascade(label='Test 2', fg = 'white', menu = menufichier)
Fenetre.config(menu = menubar)

#création d'un oval (alien)

#INITIALISATIONS
RAYON = 15
X = Largeur / 2
Y = Hauteur / 2 - 200

vitesse = random.uniform(5,10)

DX = vitesse 
DY = 0

alien = Canevas.create_oval(X-RAYON, Y-RAYON, X+RAYON, Y+RAYON, width = 1, outline = 'red', fill = 'red')

#creation fonction qui sera dans un autre fichier surement
def deplacement():
    """
    déplacement de l'oval horizontalement avec une vitesse uniforme
    """
    global X, Y, DX, DY, RAYON, Largeur, Hauteur
    if X + RAYON + DX > Largeur or X - RAYON + DX < 0: 
        DX = - DX
    elif Y + RAYON + DY > Hauteur or Y - RAYON + DY < 0 : 
        DY = - DY
    
    X = X + DX
    Y = Y + DY

    Canevas.coords(alien, X-RAYON, Y-RAYON, X+RAYON, Y+RAYON)
    Fenetre.after(20,deplacement)

deplacement()

#creation d'un rectangle (vaisseau)

#INIT
PosX = Largeur / 2
PosY = Hauteur / 2

Vaisseau = Canevas.create_rectangle()

Canevas.pack()
Fenetre.mainloop()