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
PosY = Hauteur - 50

Vaisseau = Canevas.create_rectangle(PosX - 10, PosY - 10, PosX + 10, PosY + 10, width = 5, outline = 'white', fill = 'grey')

#fonction pour faire bouger le vaisseau avec le clavier
def Clavier (event):
    """
    permet de déplacer le vaisseau à gauche ou à droite à l'aide des touches du clavier
    """
    global PosX, PosY
    touche = event.keysym
    print (touche)
    #deplacement vers la droite
    if touche == 'm' : 
        PosX = PosX + 20
    #deplacement vers la gauche
    elif touche == 'l' : 
        PosX = PosX - 20
    Canevas.coords(Vaisseau,PosX - 10, PosY - 10, PosX + 10, PosY + 10)

Canevas.focus_set()
Canevas.bind('<Key>', Clavier)

Canevas.pack()
Fenetre.mainloop()