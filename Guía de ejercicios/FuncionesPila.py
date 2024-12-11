class Funciones(object):
    
    def __init__(self, maxSize):
        self.__pila = [None] * maxSize
        self.__nItems = 0
        
    
    def len(self):
        return self.__nItems
    
    def get(self, n):
        if 0 <= n and n < self.__nItems: 
         return self.__pila[n]
    
    def eliminar(self, item):
        for j in range(self.__nItems):
            if self.__pila[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems): 
                    self.__a[k] = self.__pila[k+1]
                return True
        return False 
    
    def push(self, item):
        self.__pila[self.__nItems] = item
        self.__nItems+=1
        
    def pop(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        
        ultimo = self.__pila[self.__nItems - 1]
        self.eliminar(ultimo)
        return ultimo
    
    def peek(self):
        if self.__nItems == 0:
            return "La pila está vacía"
        else:
            return self.__pila[-1]
    
    def is_empty(self):
        return self.__nItems == 0
    
    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__pila[j])
            
            
    def balParentesis(self, cadena):
        pila = Funciones(len(cadena))
        abrir = "{[("
        cerrar = ")]}"

        for a in cadena:
            if a in abrir:
                pila.push(a)
            elif a in cerrar:
                if pila.is_empty():
                    return "Parentesis no balanceados"
                ultimo = pila.pop()
            
                if a == ')' and ultimo != '(':
                    return "Parentesis no balanceados"
                elif a == '}' and ultimo != '{':
                    return "Parentesis no balanceados"
                elif a == ']' and ultimo != '[':
                    return "Parentesis no balanceados"
        if not pila.is_empty():
            return "Parentesis no balanceados"
        return "Parentesis balanceados"


    def invertirCadena(self, cadena):
        pila=Funciones(len(cadena))
        for a in cadena:
            pila.push(a)
        cadeinv=""
        while not pila.is_empty():
            cadeinv+=pila.pop()
        return cadeinv


    def calculadora(self, lista):
        pila=Funciones(len(lista))
        
        for a in lista:
            if isinstance(a, (int, float)):
                pila.push(a)
                
            elif a in ("+", "-", "*", "/"):
                num2=pila.pop()
                num1=pila.pop()
                
                if a=="+":
                    re=num1+num2
                elif a=="-":
                    re=num1-num2
                elif a=="*":
                    re=num1*num2
                elif a=="/":
                    if num2 != 0:
                        re=num1/num2
                    else:
                        return "Division por 0"
                    
                pila.push(re)
        return pila.pop()
    
    
        
