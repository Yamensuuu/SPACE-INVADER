"""
Lucie Fabian - Yamen Ben Guirat 
12/12/22
Classe Jeu 
ce qu'il manque : mettre les attribus en privé
"""

from tkinter import Label, Button, Menu, Frame, BOTTOM, StringVar, Canvas, NW  
from alien import Alien
from vaisseau import Vaisseau
from projectile import Projectile
from Ligne import ligne

class Jeu:

    def __init__(self, Fenetre,canevas):
        self.Fenetre = Fenetre
        self.Title = Label(self.Fenetre, text = " Space Invaders",relief ='raised', fg = "blue", font = ("Courier", 30))
        self.Frame1 = Frame(self.Fenetre, relief = 'groove', bg = 'black')
        self.BoutonPlay = Button(self.Frame1, text='Rejouer', fg = 'blue')
        self.Texte = StringVar()
        self.LabelScore = Label(self.Frame1, textvariable = self.Texte, fg = 'red')
        self.BoutonQuitt = Button(self.Frame1, text = " Quitter", fg = "red",relief = 'groove', command = self.Fenetre.destroy)
        self.X = 500 #Jeu.Largeur / 2
        self.Y = 50 #Jeu.Hauteur / 2 - 200
        self.RAYON = 15
        self.vitesse = 5
        self.DX = self.vitesse
        self.PosX = 500
        self.PosY = 450
        self.al = []
        self.canevas = canevas
        print("initialisation")


    #def get(self,x):
        #return self.__x
    
    def draw_fenetre(self):
        self.Fenetre.title('Space Invaders')
        self.Fenetre.configure(bg='black')
        self.Title.pack()
        self.Frame1.pack(side = BOTTOM)
        self.BoutonPlay.pack(side = 'left', padx = 30, pady = 70)
        self.LabelScore.pack(side = 'left', padx = 30, pady = 70)
        self.BoutonQuitt.pack(side = 'left', padx = 30, pady = 70)
        self.canevas.focus_set()

    def init_jeu(self):
        """
        initialisation du jeu : création de l'alien (ennemi), du vaisseau (joueur), tous 2 mobiles
        """
        #création de l'alien (ennemi)
        alien = ligne(self.Y, self.RAYON, self.vitesse)
        for i in range(len(alien.getligne())):
            self.al.append(self.canevas.create_oval(self.X-self.RAYON, self.Y-self.RAYON, self.X+self.RAYON, self.Y+self.RAYON, width = 1, outline = 'red', fill = 'red'))
            
        self.alien = alien
        #création d'un vaisseau (le joueur)
        vaisseau = Vaisseau(self.PosX, self.PosY)
        self.vaiss = self.canevas.create_rectangle(self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10, width = 2, outline = 'white', fill = 'grey')
        self.canevas.bind("<Key>", lambda event : vaisseau.Clavier(self.vaiss, event, self.canevas, self.Fenetre))
        self.vaisseau = vaisseau
        self.refresh()
        #création des projectiles
        projectile = Projectile()
        #canevas.bind("<space>", lambda event : projectile.tirer(canevas, self.Fenetre, self.PosX, self.PosY, event))

    def refresh(self):
        """ 
        Fonction qui gère le deplacement des aliens
        """
        self.alien.setminmax()
        for i in range(len(self.alien.getligne())):
            self.alien.getligne()[i].deplacement(self.al[i],self.canevas)
        self.Fenetre.after(20,self.refresh)
