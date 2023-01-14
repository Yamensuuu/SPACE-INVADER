"""
Lucie Fabian - Yamen Ben Guirat 
12/12/22
Classe Jeu 
ce qu'il manque : mettre les attribus en privé
                  régler la fonction rejouer() (problème: la vitesse des aliens augmente à chaque fois)
"""

from tkinter import Label, Button, Menu, Frame, BOTTOM, StringVar, NW  
from alien import Alien
from vaisseau import Vaisseau
from projectile import Projectile
from Ligne import ligne

class Jeu:
    """ 
    Création de la classe jeu, comprenant les points indispensables.
    """

    def __init__(self, Fenetre,canevas):
        self.Fenetre = Fenetre
        self.Title = Label(self.Fenetre, text = " Space Invaders",relief ='raised', fg = "blue", font = ("Courier", 30))
        self.Frame1 = Frame(self.Fenetre, relief = 'groove', bg = 'black')
        self.BoutonPlay = Button(self.Frame1, text='Rejouer', fg = 'blue', command = self.rejouer)
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
        self.canevas = canevas
        self.vaisseau = Vaisseau(self.PosX,self.PosY)
        self.tir = [[],[]]



    def draw_fenetre(self):
        """
        Création de la fenêtre graphique.
        """
        self.Fenetre.title('Space Invaders')
        self.Fenetre.configure(bg='black')
        self.Title.pack()
        self.Frame1.pack(side = BOTTOM)
        self.BoutonPlay.pack(side = 'left', padx = 30, pady = 70)
        self.LabelScore.pack(side = 'left', padx = 30, pady = 70)
        self.BoutonQuitt.pack(side = 'left', padx = 30, pady = 70)
        self.canevas.focus_set()
        """
        Création d'une barre de menu (test)).
        """
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
        print (self.vitesse)

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
        for i in self.tir[0] :
            i.bougertir()
        for i in range(len(self.alien.getligne())):
            self.alien.getligne()[i].deplacement()
        for i in self.alien.getligne():
            i.tir_alien(self.tir[0])
        for i in self.vaisseau.gettir():
            i.bougertir()
        for i in self.tir[0] :
                if abs(i.getcoord()[0]-self.vaisseau.get_coords()[0])<=10 and abs(i.getcoord()[1]-self.vaisseau.get_coords()[1]) <=10 :
                    i.delete()
                    self.tir[0].remove(i)
                    print('vaisseau touché')
                    self.vaisseau.vies -= 1 
                    if self.vaisseau.vies == 0 :
                        self.canevas.delete(self.vaiss)
                        self.Fenetre.after(20,self.findepartie)
                        return True 
        """ Gestion de la collision, destruction de l'alien et du tir."""
        for i in self.alien.getligne() :
            for v in self.vaisseau.gettir():
                if abs(i.getcoord()[0]-v.getcoord()[0])<=10 and abs(i.getcoord()[1]-v.getcoord()[1]) <=10 :
                    self.vaisseau.delete(v)
                    self.alien.deletealien(i)

        if self.alien.getligne() != [] :
            self.Fenetre.after(20,self.refresh)
        else :
            self.Fenetre.after(20,self.findepartie)


    def findepartie(self) :
        self.canevas.delete("all")
        self.canevas.create_rectangle(100,200,600,700 , fill = "#EED"  )
        self.canevas.create_text(350,450, text = " FIN DE PARTIE")
    
    def rejouer(self):
        """
        Fonction qui permet de rejouer une partie 
        """
        self.canevas.delete("all")
        Jeu(self.Fenetre, self.canevas)
        self.init_jeu()
        #print ("rejouer")