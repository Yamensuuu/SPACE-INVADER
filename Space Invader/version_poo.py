"""
Lucie Fabian
Yamen Ben Guirat
11/12/2022

Programme permetttant de jouer à Space Invader à traver une fenêtre graphique
test POO
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
class Alien :

    #INITIALISATION
    def __init__(self,X,Y,RAYON,vitesse,DX,DY):
        self.X = X
        self.Y = Y
        self.RAYON = RAYON
        self.vitesse = vitesse
        self.DX = DX
        self.DY = DY
    
    def draw(self):
        self = Canevas.create_oval(self.X-self.RAYON, self.Y-self.RAYON, self.X+self.RAYON, self.Y+self.RAYON, width = 1, outline = 'red', fill = 'red')

    #creation fonction qui sera dans un autre fichier surement
    def deplacement(self):
        """
        déplacement de l'oval horizontalement avec une vitesse uniforme
        """
        #global X, Y, DX, DY, RAYON, Largeur, Hauteur
        if self.X + self.RAYON + self.DX > Largeur or self.X - self.RAYON + self.DX < 0: 
            self.DX = - self.DX
        elif self.Y + self.RAYON + self.DY > Hauteur or self.Y - self.RAYON + self.DY < 0 : 
            DY = - DY
    
        self.X = self.X + self.DX
        self.Y = self.Y + self.DY

        Canevas.coords(self, self.X-self.RAYON, self.Y-self.RAYON, self.X+self.RAYON, self.Y+self.RAYON)
        #Fenetre.after(20,deplacement)

vitesse = random.uniform(5,10)
alien = Alien(Largeur / 2, Hauteur / 2 - 200,15,vitesse, vitesse, 0)

"""RAYON = 15
X = Largeur / 2
Y = Hauteur / 2 - 200
DX = vitesse 
DY = 0"""

Alien.deplacement(alien)

#creation d'un rectangle (vaisseau)

#INIT

class Vaisseau:
    #INITIALISATION
    def __init__(self,PosX,PosY):
        self.PosX = PosX
        self.PosY = PosY

    def draw_vaisseau(self):
        """
        dessine le vaisseau (joueur)
        """
        self = Canevas.create_rectangle(self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10, width = 2, outline = 'white', fill = 'grey')

    def get_coords(self):
        """
        récupère et retourne les (4) coordonnées du vaisseau (joueur)
        """
        return Canevas.coords(self)

    #fonction pour faire bouger le vaisseau avec le clavier
    def Clavier (self,event):
        """
        permet de déplacer le vaisseau à gauche ou à droite à l'aide des touches du clavier
        """
        #global PosX, PosY
        touche = event.keysym
        #print (touche)
        #deplacement vers la droite
        if touche == 'm' : 
            self.PosX = self.PosX + 20
            Canevas.coords(self,self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10)

        #deplacement vers la gauche
        elif touche == 'l' : 
            self.PosX = self.PosX - 20
            Canevas.coords(self,self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10)

        elif touche == "space":
            shoot(event)

PosX = Largeur / 2
PosY = Hauteur - 50
vaisseau = Vaisseau(PosX,PosY)

class Projectile:  
    #projectile + tir
    def __init__(self,vitesse_projectile,Dy_proj,Dx_proj):
        self.vitesse_projectile = vitesse_projectile
        self.Dy_proj = Dy_proj
        self.Dx_proj = Dx_proj

    def deplacement_projectile(self):
        """
        lance le projectile vers l'ennemi
        """
        x , y , x1 , y1 = Vaisseau.get_coords() #on récupère les coordonnées du vaisseau (joueur) => lier classes/objets
        y_proj = abs(y + y1) // 2
        x_proj = abs(x + x1) // 2
        x_proj = x_proj + self.Dx_proj
        y_proj = y_proj + self.Dy_proj
        Canevas.coords(self, x, y, x1, y1)
        #Fenetre.after(20,deplacement_projectile)

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
    #Fenetre.after(20,deplacement)


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
Canevas.bind('<Key>', Vaisseau.Clavier)  #il manque 1 argument

Canevas.pack()
Fenetre.mainloop()