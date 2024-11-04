
class MiClase:
    def __init__(self):
        self.__a = [5, 3, 8, 6, 2]
        self.__nItems = len(self.__a)
    
    def bubbleSort(self):
        # Ordenar comparando valores adyacentes
        for last in range(self.__nItems - 1, 0, -1):  # Se recorre desde el último hacia el primero
            print(last)
            for inner in range(last):  # El bucle interno va desde 0 hasta "last"
                if self.__a[inner] > self.__a[inner + 1]:  # Si el valor actual es mayor que el siguiente
                    self.swap(inner, inner + 1)  # Intercambiamos los elementos

clas = MiClase()

clas.bubbleSort()