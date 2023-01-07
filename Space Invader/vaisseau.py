"""
Lucie Fabian - Yamen Ben Guirat 
12/12/22
Classe Vaisseau
ce qu'il manque : mettre les attribus en privé
"""

class Vaisseau:
    #INITIALISATION
    def __init__(self,PosX,PosY):
        self.PosX = PosX
        self.PosY = PosY

    def get_coords(self, canevas):
        """
        récupère et retourne les (4) coordonnées du vaisseau (joueur)
        """
        return canevas.coords(self)

    #tir du projectile et déplacement de celui-ci
    def tirer(self, canevas, fenetre):
        """
        fonction qui créee et tire le projectile
        """
        def deplacement_proj():
            """
            fonction qui permet au projectile (ici bullet) de se déplacer
            """
            canevas.move(bullet,0,-3)
            fenetre.after(20,deplacement_proj)

        #création du projectile dans le canvas
        bullet = canevas.create_rectangle(self.PosX - 1, self.PosY - 10, self.PosX + 1, self.PosY + 10,fill= 'red',outline = 'blue')


        if canevas.coords(bullet)[3]<100:
            canevas.delete(bullet)
            #a, b, c, d = canevas.coords(bullet)
            #return a, b, c, d
        deplacement_proj()


    #fonction pour faire bouger le vaisseau avec le clavier
    def Clavier (self, objet, event, canevas, fenetre):
        """
        permet de déplacer le vaisseau à gauche ou à droite à l'aide des touches du clavier
        """
        touche = event.keysym
        #canevas = Vaisseau.get_canvas(canevas)
        #deplacement vers la droite
        if touche == 'm' :
            self.PosX = self.PosX + 20
            canevas.coords(objet,self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10)

        #deplacement vers la gauche
        elif touche == 'l' : 
            self.PosX = self.PosX - 20
            canevas.coords(objet,self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10) 
        
        elif touche == 'space' :
            self.tirer(canevas, fenetre)
        
