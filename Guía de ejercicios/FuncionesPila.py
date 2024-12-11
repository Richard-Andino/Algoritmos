class Funciones(object):
    
    def __init__(self, maxSize):
        self.__pila = [None] * maxSize
        self.__nItems = 0
        
    
    def len(self):
        return self.__nItems
    
    def push(self, item):
        self.__pila[self.__nItems] = item
        self.__nItems+=1
        
    def pop(self):
        item=self.__pila[-1]
        self.__nItems-=1
        return item
    
    def peek(self):
        if self.__nItems == 0:
            return "La pila está vacía"
        else:
            return self.__pila[-1]
        
    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__pila[j])
        