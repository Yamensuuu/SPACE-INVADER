"""
Lucie Fabian - Yamen Ben Guirat 
12/12/22
Classe Alien
ce qu'il manque : mettre les attribus en privé
"""

import random, projectile



#création d'un oval (alien)
class Alien :

    #INITIALISATION
    def __init__(self, X, Y, RAYON, vitesse, xmin, xmax, canevas, fenetre):
        self.X = X #Jeu.Largeur / 2
        self.Y = Y #Jeu.Hauteur / 2 - 200
        self.xmin = xmin
        self.xmax = xmax
        self.RAYON = RAYON
        self.vitesse = vitesse
        self.DX = self.vitesse
        self.sens = 1
        self.canevas = canevas
        self.fenetre = fenetre
        self.objet = self.canevas.create_oval(self.X-self.RAYON, self.Y-self.RAYON, self.X+self.RAYON, self.Y+self.RAYON, width = 1, outline = 'red', fill = 'red')




    def deplacement(self):
        """
        Fonction qui gère le déplacement de l'oval (l'alien) horizontalement avec une vitesse uniforme
        """
        if self.xmin - self.RAYON + self.DX == self.RAYON : 
            self.Y += 10
        elif self.xmax + self.RAYON + self.DX > 1000 or self.xmin - self.RAYON + self.DX < 0: 
            self.DX = - self.DX
        
        self.X = self.X + self.DX
        self.canevas.coords(self.objet, self.X - self.RAYON, self.Y - self.RAYON, self.X + self.RAYON, self.Y + self.RAYON)

    def setxmin(self, xmin):
        """ 
        Fonction qui va modifier la valeur de xmin : valeur minimale du bloc d'alien 
        """
        self.xmin = xmin

    def setxmax(self, xmax):
        """ 
        Fonction qui va modifier la valeur de xmax : valeur max du bloc d'alien 
        sortie : valeur max de x (abscisse de l'alien)
        """
        self.xmax = xmax

        

    def get(self) :
        """ 
        Fonction qui retourne la position de l'alien selon x
        sortie : abscisse de l'alien
        """
        return self.X
    

    def getcoord(self) :
        """
        Fonction qui retourne les coordonnées de l'alien 
        sorties : abscisse (X) et ordonnée (Y) de l'alien 
        """
        return self.X, self.Y
    
    def delete(self) :
        """
        Fonction qui supprime l'alien ( = l'efface du canvas)
        """
        self.canevas.delete(self.objet)
        
    def tir_alien(self, L) :
        """
        Fonction qui fait tirer alétoirement les aliens 
        entree : liste L
        sortie : projectile(s) tire(s)
        """
        if random.randint(0,150) == 0 :
            L.append(projectile.Projectile(self.canevas,self.X,self.Y,-1))


        
