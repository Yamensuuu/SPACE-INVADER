"""
Lucie Fabian - Yamen Ben Guirat 
12/01/23
Classe Obstacle
"""

class Obstacle() :
    def __init__(self,canevas):
            """ 
            Fonction qui matérialise deux obstacles sous forme de rectangle.
            """
            
            self.canevas1 = canevas
            self.X1 = 500 
            self.Y1 = 50 
            self.R = 15
            self.V = 5
            self.PX = 500
            self.PY = 450
            self.obstacle1 = canevas.create_rectangle(self.PX - 10, self.PY - 10, self.PX + 10, self.PY + 10, width = 2, outline = 'white', fill = 'blue')
            self.obstacle2 = canevas.create_rectangle(self.PX - 10, self.PY - 10, self.PX + 10, self.PY + 10, width = 2, outline = 'white', fill = 'blue')