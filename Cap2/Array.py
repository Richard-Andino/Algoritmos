import random

class Array(object): 
    def __init__(self, initialSize):    # Constructor 
        self.__a = [None] * initialSize  # The array stored as a list 
        self.__nItems = 0                # No items in array initially 
  
    def __len__(self):                  # Special def for len() func 
        return self.__nItems             # Return number of items 
  
    def get(self, n):                   # Return the value at index n 
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and 
         return self.__a[n]            # only return item if in bounds 
  
    def set(self, n, value):            # Set the value at index n 
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and 
            self.__a[n] = value           # only set item if in bounds 

    def insert(self, item):             # Insert item at end 
        self.__a[self.__nItems] = item   # Item goes at current end 
        self.__nItems += 1              # Increment number of items 
    
    def push(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1
        
    def pop(self):
        item = self.__a[self.__nItems-1]
        self.__a[self.__nItems-1]= None 
        self.__nItems -= 1
        return item
        
    
    
    def find(self, item):               # Find index for item 
        for j in range(self.__nItems):   # Among current items 
            if self.__a[j] == item:       # If found, 
                return j                   # then return index to item 
        return -1                        # Not found -> return -1 
    
    def search(self, item):                # Search for item 
        return self.get(self.find(item))   # and return item if found 

    def delete(self, item):                # Delete first occurrence
        for j in range(self.__nItems):     # of an item
            if self.__a[j] == item:        # Found item
                self.__nItems -= 1         # One fewer at end
                for k in range(j, self.__nItems):  # Move items from 
                    self.__a[k] = self.__a[k+1]     # right over 1
                return True                # Return success flag
        return False                       # Made it here, so couldn't find the item


    
        


    
            

























 
    def traverse(self, function=print):    # Traverse all items 
        for j in range(self.__nItems):     # and apply a function 
            function(self.__a[j])
    
    
    #Ejercicio 2.1         
    def getMaxNum(self):
        max=0
        for j in range(self.__nItems):
            if isinstance(self.__a[j], (int, float)):
                if max is None or self.__a[j]>max: 
                    max=self.__a[j]
        return max
    
    #Ejercicio 2.2
    def deleteMaxNum(self, n):
        for j in range(self.__nItems):
            if self.__a[j] == n:
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k+1]
                return True
        return False
    
    #Ejercicio 2.4
    def removeDupes(self):
        unique_items = []                # Nueva __a para elementos únicos
        for item in self.__a:
            if item not in unique_items:  # Verificamos si no está en la nueva __a
                unique_items.append(item)  # Agregamos el elemento único

        self.__a = unique_items           # Actualizamos el arreglo original
        self.__nItems = len(unique_items)
        
        
    def promedio(self):
        sum= 0
        cont=0
        for j in range(self.__nItems):
            if isinstance(self.__a[j], (int, float)):
                cont+=1
                sum+=self.__a[j] 
        return sum/cont
    
    def Cuenta(self, tipo):
        par=impar=0
        for j in range(self.__nItems):
            if isinstance(self.__a[j], (int, float)):
                if self.__a[j]%2==0:
                    par+=1
                else:
                    impar+=1
        if tipo==0:
            return par
        elif tipo==1:
            return impar
        
    def ImprimeNoNumeros(self):
        listaStr=[]
        for j in range(self.__nItems):
            print (type(self.__a[j]), self.__a[j])
            if isinstance(self.__a[j], (int, float)):
                pass
            else:
                listaStr.append(self.__a[j])
        return listaStr
        





    
    
    
                
                
                