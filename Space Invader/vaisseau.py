"""
Lucie Fabian - Yamen Ben Guirat 
12/12/22
Classe Vaisseau
ce qu'il manque : mettre les attribus en privé
"""

from alien import Alien
from projectile import Projectile

class Vaisseau:
    #INITIALISATION
    def __init__(self,PosX,PosY):
        self.PosX = PosX
        self.PosY = PosY
        self.tir = []
        self.tir_alien = []
        self.vies = 3


    def get_coords(self):
        """
        Récupère et retourne les (4) coordonnées du vaisseau (joueur)
        """
        return self.PosX , self.PosY

    #fonction pour faire bouger le vaisseau avec le clavier
    def Clavier (self, objet, event, canevas):
        """
        Fonction qui permet de déplacer le vaisseau à gauche ou à droite à l'aide des touches du clavier 
        touche 'm' pour aller à gauche et touche 'l' pour aller à droite
        """
        touche = event.keysym
        #deplacement vers la droite
        if touche == 'm' :
            self.PosX = self.PosX + 20
            canevas.coords(objet,self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10)

        #deplacement vers la gauche
        elif touche == 'l' : 
            self.PosX = self.PosX - 20
            canevas.coords(objet,self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10) 
        
        #on tire un projectile qui part du vaisseau
        elif touche == 'space' :
            self.tir.append(Projectile(canevas,self.PosX,self.PosY,1))
               

    def gettir(self) :
        return self.tir
        


    def delete(self,t) :
        """ 
        Fonction qui permet de supprimer un tir.
        """
        if t in self.tir:
            self.tir.remove(t)
            t.delete()