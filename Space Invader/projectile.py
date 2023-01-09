"""
Lucie Fabian - Yamen Ben Guirat
12/12/22
Classe Projectile 
ce qu'il manque : mettre les attribus en privé, récupérer les coordonées du projectile si possible
"""

class Projectile:  

    def __init__(self,canevas,posX,posY):
        self.vitesse = 5
        self.PosX = posX
        self.PosY = posY
        self.canevas = canevas
        self.objet = canevas.create_rectangle(self.PosX - 1, self.PosY - 10, self.PosX + 1, self.PosY + 10,fill= 'red',outline = 'blue')


    def bougertir(self) :
        """
        Fonction qui fait bouger le tirer à une certaine vitesse (ici vitesse = 5)
        """
        self.PosY -= self.vitesse
        self.canevas.move(self.objet,0,-self.vitesse)

    def getcoord(self) :
        return self.PosX, self.PosY
    

    def delete(self) :
        """
        Fonction qui supprime le projectile
        """
        self.canevas.remove(self.objet)