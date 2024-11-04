

class Rectangulo():
    
    def __init__(self , ancho , largo):
        self._ancho = ancho
        self._largo = largo
    
    def getArea(self):
        area = self._largo * self._ancho
        
        return area

    def perimetro(self):
        perim = (2 * self._largo) + (2 * self._ancho)
        
        return perim
    
    def dibujar(self):
        for i in range(self._largo):
            print("#" * self._ancho)
            


