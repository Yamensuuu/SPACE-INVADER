""" 
Lucie Fabian - Yamen Ben Guirat
07/01/23
Création de la classe ligne (pour avoir une ligne d'Aliens) 
"""

from alien import Alien

class ligne():
    def __init__(self, Y, Rayon, vitesse) :
        self.liste = []
        for i in range(50,500,50) :
            self.liste.append(Alien(i,Y,Rayon,vitesse,50,450))
    
    def getligne(self):
        return self.liste
    
    def setminmax(self):
<<<<<<< HEAD
        #Renitialiser les valeurs de xmin et xmax
=======
        """
        Renitialiser les valeurs de xmin et xmax 
        """
>>>>>>> aed4f0f1e2b4551af37f03f7768a89739920bda9
        for i in self.liste :
            i.setxmin(self.liste[0].get())
            i.setxmax(self.liste[-1].get())
        print(self.liste[-1].get())

    def deletealien(self,alien,objet,canevas) :
        #Supression alien
        if alien in self.liste:
            self.liste.remove(alien)
            alien.delete(objet,canevas)