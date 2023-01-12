"""
Lucie Fabian - Yamen Ben Guirat
12/12/22
Classe Projectile 
ce qu'il manque : mettre les attribus en privé, récupérer les coordonées du projectile si possible
                  essayer de mettre dans cette classe la fonction qui permet de tirer un projectile en ppuyant sur la touche espace
"""

class Projectile:  
    """ 
    Classe qui contrôle le projectile.
    """
    def __init__(self,canevas,posX,posY):
        """ 
        Fonction qui matérialise le projectile sous forme de rectangle.
        """
        self.vitesse = 5
        self.PosX = posX
        self.PosY = posY
        self.canevas = canevas
        self.objet = canevas.create_rectangle(self.PosX - 1, self.PosY - 10, self.PosX + 1, self.PosY + 10,fill= 'red',outline = 'blue')


    def bougertir(self) :
        """ 
        Fonction qui fait bouger le projectile, unidirectionnellement et sous une certaine vitesse. 
        """
        self.PosY -= self.vitesse
        self.canevas.move(self.objet,0,-self.vitesse) 

    def getcoord(self) :
        """ 
        Fonction qui récupère les coordonnées du projectile. 
        """
        return self.PosX, self.PosY
    

    def delete(self) :
        """ 
        Fonction qui supprime le projectile.
        """
        self.canevas.delete(self.objet)