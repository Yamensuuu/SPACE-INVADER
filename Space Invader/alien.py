"""
Lucie Fabian - Yamen 
12/12/22
Classe Alien
ce qu'il manque : mettre les attribus en privé
"""

#création d'un oval (alien)
class Alien :

    #INITIALISATION
    def __init__(self, X, Y, RAYON, vitesse, DY):
        self.X = X #Jeu.Largeur / 2
        self.Y = Y #Jeu.Hauteur / 2 - 200
        self.RAYON = RAYON
        self.vitesse = vitesse
        self.DX = self.vitesse
        self.DY = DY
    
    def deplacement(self, objet, canvas, fenetre):
        """
        déplacement de l'oval (l'alien) horizontalement avec une vitesse uniforme
        """
        if self.X + self.RAYON + self.DX > 1000 or self.X - self.RAYON + self.DX < 0: 
            self.DX = - self.DX
        elif self.Y + self.RAYON + self.DY > 500 or self.Y - self.RAYON + self.DY < 0 : 
            DY = - DY
    
        self.X = self.X + self.DX
        self.Y = self.Y + self.DY

        canvas.coords(objet, self.X - self.RAYON, self.Y - self.RAYON, self.X + self.RAYON, self.Y + self.RAYON)
        fenetre.after(20,lambda : self.deplacement(objet, canvas, fenetre))