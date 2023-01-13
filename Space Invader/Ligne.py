""" 
Lucie Fabian - Yamen Ben Guirat
07/01/23
Création de la classe ligne (pour avoir une ligne d'aliens) 
"""

from alien import Alien

class ligne():

    def __init__(self, Y, Rayon, vitesse, canevas, fenetre) :
        self.liste = []
        self.tir_alien = []
        self.canevas = canevas
        self.fenetre = fenetre
        for i in range(50,500,50) :
            self.liste.append(Alien(i,Y,Rayon,vitesse,50,450, canevas, fenetre))
    
    def getligne(self):
        """ 
        Fonction qui renvoie la liste d'aliens.
        """
        return self.liste
    
    def setminmax(self):
        """
        Fonction qui reinitialise les valeurs de xmin et xmax 
        """
        for i in self.liste :
            i.setxmin(self.liste[0].get())
            i.setxmax(self.liste[-1].get())
        # print(self.liste[-1].get())

    def deletealien(self,alien) :
        alien.delete()
        self.liste.remove(alien)