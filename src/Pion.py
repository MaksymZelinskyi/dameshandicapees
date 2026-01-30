COULEURS = ('Blanc', 'Noir')

class Pion:

    def __init__(self, couleur):
        if couleur not in COULEURS:
            raise Exception('La couleur du pion doit être ''Blanc'' et ''Noir''!')
        self.__couleur__ = couleur
        self.__dame__ = False

    def obtenir_couleur(self):
        return self.__couleur__

    def est_dame(self):
        return self.__dame__

    def promouvoir(self):
        self.__dame__ = True    