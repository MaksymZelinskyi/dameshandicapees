LETTRES = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

class PlateauUtil:

    def convertir_coordonnées(x, y):
        x = (13 + int(x))//3 - 1
        y = ((13 + int(y))//3)
        if y < 1:
            y = 1
        if y > 8:
            y = 8    
        if x < 0:
            x = 0
        if x > 7:
            x = 7

        return (y, LETTRES[x])