from alien import Alien

""" Creer class ligne Aliens """

class ligne():
    def __init__(self, Y, Rayon, vitesse) :
        self.liste = []
        for i in range(50,500,50) :
            self.liste.append(Alien(i,Y,Rayon,vitesse,50,450))
    
    def getligne(self):
        return self.liste
    
    def setminmax(self):
        """ Renitialiser les valeurs de xmin et xmax """
        for i in self.liste :
            i.setxmin(self.liste[0].get())
            i.setxmax(self.liste[-1].get())
        print(self.liste[-1].get())