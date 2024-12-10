
class Funciones(object):
    
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0
  
    def len(self):
        return self.__nItems
  
    def get(self, n):
        if 0 <= n and n < self.__nItems: 
         return self.__a[n]
  
    def set(self, n, value):
        if 0 <= n and n < self.__nItems:
            self.__a[n] = value

    def insertar(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1
    
    def eliminar(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems): 
                    self.__a[k] = self.__a[k+1]
                return True
        return False   
    
    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])
            
    def invertir_Array(self, array):
        new_Array = Funciones(len(array))
        for a in range(len(array) - 1, -1, -1):
            new_Array.insertar(array[a])
        return new_Array
    
    def buscar(self, array, item):
        for a in array:
            if item==a:
                print("El numero está presente en el arreglo")
                return
        print("El numero no está presente en el arreglo")
        
    def eliminar_duplicado(self, array):
        new_Array = Funciones(len(array))
        for item in array:
            if item not in new_Array.__a:
                new_Array.insertar(item)
        return new_Array
                

        
