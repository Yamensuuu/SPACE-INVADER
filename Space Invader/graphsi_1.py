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
PosY = Hauteur - 50

Vaisseau = Canevas.create_rectangle(PosX - 10, PosY - 10, PosX + 10, PosY + 10, width = 2, outline = 'white', fill = 'grey')

#fonction pour faire bouger le vaisseau avec le clavier

def Clavier (event):
    """
    permet de déplacer le vaisseau à gauche ou à droite à l'aide des touches du clavier
    """
    global PosX, PosY
    touche = event.keysym
    #print (touche)
    #deplacement vers la droite
    if touche == 'm' : 
        PosX = PosX + 20
        Canevas.coords(Vaisseau,PosX - 10, PosY - 10, PosX + 10, PosY + 10)

    #deplacement vers la gauche
    elif touche == 'l' : 
        PosX = PosX - 20
        Canevas.coords(Vaisseau,PosX - 10, PosY - 10, PosX + 10, PosY + 10)

    elif touche == "space":
        shoot(event)
#tir du projectile

#x_depart_proj = 0
#y_depart_proj = 0
vitesse_projectile = random.uniform(1,2)

Dy_proj = vitesse_projectile
Dx_proj = 0

def deplacement_projectile(item):
    """
    lance le projectile vers l'ennemi
    """
    x , y , x1 , y1 = Canevas.coords(item)
    y_proj = abs(y + y1) // 2
    x_proj = abs(x + x1) // 2
    x_proj = x_proj + Dx_proj
    y_proj = y_proj + Dy_proj
    Canevas.coords(item, x, y, x1, y1)
    Fenetre.after(20,deplacement_projectile)


def shoot(event):
    """
    tire un projectile vers le haut à partir de son point de depart
    """
    touche = event.keysym
    #print (touche)
    global Hauteur, Dy_proj, Dx_proj
    x_dep_proj , y_dep_proj , x1_dep_proj , y1_dep_proj = Canevas.coords(Vaisseau) 
    #x_depart_proj = abs(x_dep_proj + x1_dep_proj) // 2
    #y_depart_proj = abs(y_dep_proj + y1_dep_proj) // 2
    #if touche == 'space' : 
    projectile = Canevas.create_rectangle(x_dep_proj, y_dep_proj, x1_dep_proj, y1_dep_proj, outline = 'white', fill = 'blue')
    Canevas.coords(projectile, x_dep_proj, y_dep_proj, x1_dep_proj, y1_dep_proj)
    deplacement_projectile(projectile)
    

Canevas.focus_set()
Canevas.bind('<Key>', Clavier)

Canevas.pack()
Fenetre.mainloop()