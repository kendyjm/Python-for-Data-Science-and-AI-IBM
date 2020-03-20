class Rectangle(object):

    def __init__(self, lo, la):
        self.longueur = lo
        self.largeur = la

    def printdef(self):
        print('longueur:', self.longueur, ", largeur:", self.largeur)


myRect = Rectangle(4, 2)
myRect.printdef()
