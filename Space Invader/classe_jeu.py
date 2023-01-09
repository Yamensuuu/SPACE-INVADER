"""
Lucie Fabian - Yamen Ben Guirat 
12/12/22
Classe Jeu 
ce qu'il manque : mettre les attribus en privé
"""

from tkinter import Label, Button, Menu, Frame, BOTTOM, StringVar, NW  
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
        self.vaisseau = Vaisseau(self.PosX,self.PosY)

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
        #création d'une barre de menu (test))
        menubar = Menu(self.Fenetre)
        menufichier = Menu(menubar, tearoff = 0)
        menufichier.add_command(label = 'Quitter', command = self.Fenetre.destroy)
        #menufichier.add_command(label = 'Quitter2', command = self.Fenetre.destroy)
        #menufichier.add_command(label = 'Quitter3', command = self.Fenetre.destroy)
        menubar.add_cascade(label='Menu', menu = menufichier)
        self.Fenetre.config(menu = menubar)

    def init_jeu(self):
        """
        initialisation du jeu : création des aliens (ennemis), du vaisseau (joueur), tous 2 mobiles
        """ 
        #création des aliens (ennemis)
        alien = ligne(self.Y, self.RAYON, self.vitesse, self.canevas, self.Fenetre)  
        for i in range(len(alien.getligne())):
            self.al.append(self.canevas.create_oval(self.X-self.RAYON, self.Y-self.RAYON, self.X+self.RAYON, self.Y+self.RAYON, width = 1, outline = 'red', fill = 'red'))

        self.alien = alien
        #création d'un vaisseau (le joueur)
        self.vaiss = self.canevas.create_rectangle(self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10, width = 2, outline = 'white', fill = 'grey')
        self.canevas.bind("<Key>", lambda event : self.vaisseau.Clavier(self.vaiss, event, self.canevas))
        self.refresh()
        

    def refresh(self):
        """ 
        Fonction qui gère le déplacement des aliens, la position de départ du tir, mais aussi le contact entre le tir et les aliens 
        """
        self.alien.setminmax()
        for i in range(len(self.alien.getligne())):
            self.alien.getligne()[i].deplacement(self.al[i],self.canevas)
        for i in self.alien.getligne():
            i.tir_alien()
        for i in self.vaisseau.gettir():
            i.bougertir()

                
        for i in self.alien.getligne() :
            for v in self.vaisseau.gettir():
                if i.getcoord() == v.getcoord() :
                    self.vaisseau.delete(v)
                    self.alien.deletealien(i)

        self.Fenetre.after(20,self.refresh)