"""
Lucie Fabian
12/12/22
Programme principal du jeu Space Invader
"""

from tkinter import Tk, Canvas, NW  
#on importe le ou les classes qui sont chacunes dans un fichier
from classe_jeu import Jeu
from vaisseau import Vaisseau

mw = Tk()
Largeur = 1000
Hauteur = 500
Canevas = Canvas(mw, width = Largeur, height = Hauteur, bg = 'black')
item = Canevas.create_image(650,200,anchor=NW)

#création de la fenetre de jeu 
fenetre = Jeu(mw)
fenetre.draw_fenetre(Canevas)

fenetre.init_jeu(Canevas)

Canevas.pack()
mw.mainloop()