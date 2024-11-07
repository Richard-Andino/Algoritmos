class Stack(object):
    def __init__(self, max):
        # La pila se almacena como una lista
        self.__stackList = [None] * max  # Sin elementos inicialmente
        self.__top = -1  # Puntero a la parte superior de la pila

    def push(self, item):
        # Insertar elemento en la parte superior de la pila
        if not self.isFull():  # Comprobar si la pila no está llena
            self.__top += 1  # Avanzar el puntero
            self.__stackList[self.__top] = item  # Almacenar el elemento
        else:
            raise Exception("La pila está llena")  # Lanzar un error si la pila está llena

    def pop(self):
        # Eliminar y devolver el elemento superior de la pila
        if not self.isEmpty():  # Comprobar si la pila no está vacía
            top = self.__stackList[self.__top]  # Elemento superior
            self.__stackList[self.__top] = None  # Eliminar la referencia al elemento
            self.__top -= 1  # Disminuir el puntero
            return top  # Devolver el elemento superior
        else:
            raise Exception("La pila está vacía")  # Lanzar un error si la pila está vacía

    def peek(self):
        # Devolver el elemento superior sin eliminarlo
        if not self.isEmpty():  # Si la pila no está vacía
            return self.__stackList[self.__top]  # Devolver el elemento superior
        else:
            raise Exception("La pila está vacía")  # Lanzar un error si la pila está vacía

    def isEmpty(self):
        # Comprobar si la pila está vacía
        return self.__top < 0

    def isFull(self):
        # Comprobar si la pila está llena
        return self.__top >= len(self.__stackList) - 1

    def __len__(self):
        return self.__top + 1

    def __str__(self):
        ans = "["
        for i in range(self.__top + 1):
            if len(ans) > 1:
                ans += ", "  
            ans += str(self.__stackList[i])  
        ans += "]" 
        return ans

class Deque:
    def __init__(self, maxSize):
        self.__list = [None] * maxSize #almacenamiento del deque
        self.__maxSize = maxSize
        self.__front = 0 #indice del frente
        self.__rear = -1 #indice de la parte trasera
        self.__size = 0 #numero de elementos del deque

    def insertLeft(self, item):
        if not self.isFull():
            self.__front = (self.__front - 1) % self.__maxSize #ajusta la capacidad
            self.__list[self.__front] = item
            self.__size += 1
        else:
            raise Exception("El deque esta lleno")

    def insertRight(self, item):
        if not self.isFull():
            self.__rear = (self.__rear + 1) % self.__maxSize
            self.__list[self.__rear] = item
            self.__size += 1
        else:
            raise Exception("El deque esta lleno")

    def removeLeft(self):
        if not self.isEmpty():
            item = self.__list[self.__front]
            self.__list[self.__front] = None
            self.__front = (self.__front + 1) % self.__maxSize
            self.__size -= 1
            return item
        else:
            raise Exception("El deque esa vacio")

    def removeRight(self):
        if not self.isEmpty():
            item = self.__list[self.__rear]
            self.__list[self.__rear] = None
            self.__rear = (self.__rear - 1 + self.__maxSize) % self.__maxSize
            self.__size -= 1
            return item
        else:
            raise Exception("El deque esta vacio")

    def peekLeft(self):
        if not self.isEmpty():
            return self.__list[self.__front]
        else:
            raise Exception("El deque esta vacio")

    def peekRight(self):
        if not self.isEmpty():
            return self.__list[self.__rear]
        else:
            raise Exception("El deque esta vacio")

    def isEmpty(self):
        return self.__size == 0

    def isFull(self):
        return self.__size == self.__maxSize

    def __len__(self):
        return self.__size

    def __str__(self):
        item = []
        index = self.__front
        for i in range(self.__size):
            item.append(str(self.__list[index]))
            index = (index + 1) % self.__maxSize
        return "[" + ", ".join(item) + "]"

class PriorityQueue:
    def __init__(self):
        self.queue = []  # almacenar elementos

    def insert(self, item, priority): #inserta el elemento
        self.queue.append((priority, item))

    def removeHighestPriority(self):  #encuentra y elimina el elemento con la mayor prioridad
        if self.isEmpty():
            raise Exception("La cola de prioridad esta vacia")
        highest_priority_index = 0  #encuentra el indice del elemento con la mayor prioridad
        for i in range(1, len(self.queue)):
            if self.queue[i][0] > self.queue[highest_priority_index][0]:
                highest_priority_index = i
        return self.queue.pop(highest_priority_index)[1]  #remueve y retorna el elemento de mayor prioridad

    

    def isEmpty(self):  #comprueba si la cola esta vacia
        return len(self.queue) == 0

    def peekHighestPriority(self):   #devuelve el elemento de mayor prioridad sin eliminarlo
        if self.isEmpty():
            raise Exception("La cola de prioridad esta vacia")
        highest_priority_item = self.queue[0]
        for item in self.queue:
            if item[0] > highest_priority_item[0]:
                highest_priority_item = item
        return highest_priority_item[1]
    
    def __str__(self):
        return str([f"({priority}, {item})" for priority,item in self.queue])
