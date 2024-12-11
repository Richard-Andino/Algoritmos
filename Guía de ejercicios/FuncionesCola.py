class Funciones(object):
    
    def __init__(self, maxSize):
        self.__cola = [None] * maxSize
        self.__nItems = 0
        
    def is_empty(self):
        return self.__nItems == 0
    
    def len(self):
        return self.__nItems
    
    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__cola[j])
    
    def eliminar(self, item):
        for j in range(self.__nItems):
            if self.__cola[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems): 
                    self.__cola[k] = self.__cola[k+1]
                return True
        return False 
    
    def enqueue(self, item):
        self.__cola[self.__nItems] = item
        self.__nItems += 1
        
    def dequeue(self):
        if self.is_empty():
            pass
        
        primero = self.__cola[0]
        self.eliminar(primero)
        return primero
    
    def peek(self):
        return self.__cola[0]