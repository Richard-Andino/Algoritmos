
class ColaEspecial(object):
    def __init__(self, max=10):
        self.__items = 0
        self.__a = [None] * max

    def insert(self, item):
        self.__a[self.__items] = item
        self.__items += 1

    def insertn(self, item, n):
        self.__a[n] = item

        
    def delete(self, item):
        for j in range(self.__items):   
            if self.__a[j] == item:      
                self.__items -= 1
    
    def set(self, n, value):             
        if 0 <= n and n < self.__items:  
            self.__a[n] = value

    def get(self, n):                    
        if 0 <= n and n < self.__items: 
         return self.__a[n] 

    def __len__(self):    
        return self.__items
    

    def traverse(self, function=print): 
        for j in range(self.__items):     
            function(self.__a[j])