"""
Lucie Fabian - Yamen 
12/12/22
Classe Alien
ce qu'il manque : mettre les attribus en privé
"""

#création d'un oval (alien)
class Alien :

    #INITIALISATION
    def __init__(self, X, Y, RAYON, vitesse, xmin, xmax):
        self.X = X #Jeu.Largeur / 2
        self.Y = Y #Jeu.Hauteur / 2 - 200
        self.xmin = xmin
        self.xmax = xmax
        self.RAYON = RAYON
        self.vitesse = vitesse
        self.DX = self.vitesse
        self.sens = 1
    def deplacement(self, objet, canvas):
        """
        déplacement de l'oval (l'alien) horizontalement avec une vitesse uniforme
        """
        if self.xmin - self.RAYON + self.DX == self.RAYON : 
            self.Y += 10
        elif self.xmax + self.RAYON + self.DX > 1000 or self.xmin - self.RAYON + self.DX < 0: 
            self.DX = - self.DX
        
    
        self.X = self.X + self.DX
        print(self.xmin-self.RAYON+self.DX)
        canvas.coords(objet, self.X - self.RAYON, self.Y - self.RAYON, self.X + self.RAYON, self.Y + self.RAYON)

        """ Modifier la valeur de xmin : valeur minimale du bloc d'alien """

    def setxmin(self, xmin):
        self.xmin = xmin
        
        """ Modifier la valeur de xmax : valeur max du bloc d'alien """

    def setxmax(self, xmax):
        self.xmax = xmax

        """ Retourne la position de l'alien selon x"""

    def get(self) :
        return self.X
    

    def getcoord(self) :
        return self.X, self.Y
    
    def delete(self,objet,canevas) :
        canevas.remove(objet)
        