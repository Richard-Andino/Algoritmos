class Array(object):
    def __init__(self, initialSize): # Constructor
        self.__a = [None] * initialSize # The array stored as a list
        self.__nItems = 0 # No items in array initially
    
    def __len__(self): # Special def for len() func
        return self.__nItems # Return number of items
 
    def get(self, n): # Return the value at index n
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
            return self.__a[n] # only return item if in bounds
 
    def set(self, n, value): # Set the value at index n
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
            self.__a[n] = value # only set item if in bounds
 
    def swap(self, j, k): # Swap the values at 2 indices
        if (0 <= j and j < self.__nItems and # Check if indices are in
            0 <= k and k < self.__nItems): # bounds, before processing
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]
 
    def insert(self, item): # Insert item at end
        if self.__nItems >= len(self.__a): # If array is full,
            raise Exception("Array overflow") # raise exception
        self.__a[self.__nItems] = item # Item goes at current end
        self.__nItems += 1 # Increment number of items
 
    def find(self, item): # Find index for item
        for j in range(self.__nItems): # Among current items
            if self.__a[j] == item: # If found,
                return j # then return index to element
        return -1 # Not found -> return -1
 
    def search(self, item): # Search for item
        return self.get(self.find(item)) # and return item if found
 
    def delete(self, item): # Delete first occurrence
        for j in range(self.__nItems): # of an item
            if self.__a[j] == item: # Found item
                self.__nItems -= 1 # One fewer at end
                for k in range(j, self.__nItems): # Move items from
                    self.__a[k] = self.__a[k+1] # right over 1
                return True # Return success flag
        return False # Made it here, so couldn't find the item
 
    def traverse(self, function=print): # Traverse all items
        for j in range(self.__nItems): # and apply a function
            function(self.__a[j])
 
    def __str__(self): # Special def for str() func
        ans = "[" # Surround with square brackets
        for i in range(self.__nItems): # Loop through items
            if len(ans) > 1: # Except next to left bracket,
                ans += ", " # separate items with comma
            ans += str(self.__a[i]) # Add string form of item
        ans += "]" # Close with right bracket
        return ans
 
    def bubbleSort(self):  # Sort with alternating passes
        left = 0  # Inicio del arreglo
        right = self.__nItems - 1  # Final del arreglo
        
        while left < right:
            # Paso 1: Lleva el número mayor al final
            for inner in range(left, right):
                if self.__a[inner] > self.__a[inner + 1]:
                    self.swap(inner, inner + 1)
            right -= 1  # Reducimos el límite derecho
            
            # Paso 2: Lleva el número menor al inicio
            for inner in range(right, left, -1):
                if self.__a[inner] < self.__a[inner - 1]:
                    self.swap(inner, inner - 1)
            left += 1  # Aumentamos el límite izquierdo

        
    def selectionSort(self): # Sort by selecting min and
        for outer in range(self.__nItems-1): # swapping min to leftmost
            min = outer # Assume min is leftmost
            for inner in range(outer+1, self.__nItems): # Hunt to right
                if self.__a[inner] < self.__a[min]: # If we find new min,
                    min = inner # update the min index
 # __a[min] is smallest among __a[outer]...__a[__nItems-1]
            self.swap(outer, min) # Swap leftmost and min
 
    def insertionSort(self):  # Ordenar por inserciones repetidas con contadores
        copy_count = 0           # Contador de copias
        comparison_count = 0      # Contador de comparaciones

        for outer in range(1, self.__nItems):  # Marca un elemento
            temp = self.__a[outer]             # Almacena el elemento marcado en temp
            copy_count += 1                    # Contamos la copia inicial a temp
            inner = outer                      # El bucle interno comienza en el marcado

            # Comparación y desplazamiento en el ciclo while
            while inner > 0 and temp < self.__a[inner - 1]:
                comparison_count += 1          # Contamos la comparación en el while
                self.__a[inner] = self.__a[inner - 1]  # Desplazamiento del elemento a la derecha
                copy_count += 1                # Contamos el desplazamiento como copia
                inner -= 1

            # Se realiza una última comparación al salir del while, si no está en el primer índice
            if inner > 0:
                comparison_count += 1

            # Coloca el elemento marcado en la posición correcta
            self.__a[inner] = temp
            copy_count += 1                    # Contamos la copia final de temp a su posición

        # Muestra los resultados
        print(f"Total de copias: {copy_count}")
        print(f"Total de comparaciones: {comparison_count}")

            
            
    def mediana(self):
        medio = self.__nItems // 2
        
        if self.__nItems % 2 == 1:
            return self.__a[medio]
        else:
            return (self.__a[medio - 1] + self.__a[medio]) // 2
        
        
    def delete_duplicates(self):  # Eliminar duplicados sin múltiples movimientos
        unique_count = 0  # Contador de elementos únicos encontrados
        
        for j in range(self.__nItems):
            # Verificar si el elemento actual es un duplicado
            is_duplicate = False
            for k in range(unique_count):
                if self.__a[j] == self.__a[k]:  # Comprobar duplicado en la lista única
                    is_duplicate = True
                    break

            # Si no es un duplicado, moverlo a la posición `unique_count`
            if not is_duplicate:
                self.__a[unique_count] = self.__a[j]
                unique_count += 1  
        
        # Actualizar el número de elementos
        self.__nItems = unique_count
        
        
        
    def oddEvenSort(self):
        is_sorted = False  # Bandera para controlar si el arreglo está ordenado
        pass_count = 0     # Contador de pasadas (pares e impares)
        
        while not is_sorted:
            is_sorted = True  # Suponemos que está ordenado hasta que encontremos un intercambio
            
            # Primera pasada: Comparar e intercambiar elementos en posiciones impares
            for j in range(1, self.__nItems - 1, 2):  # j es impar (1, 3, 5, ...)
                if self.__a[j] > self.__a[j + 1]:
                    self.swap(j, j + 1)
                    is_sorted = False  # Si hubo un intercambio, no está ordenado

            # Segunda pasada: Comparar e intercambiar elementos en posiciones pares
            for j in range(0, self.__nItems - 1, 2):  # j es par (0, 2, 4, ...)
                if self.__a[j] > self.__a[j + 1]:
                    self.swap(j, j + 1)
                    is_sorted = False  # Si hubo un intercambio, no está ordenado

            pass_count += 1  # Incrementar el contador de pasadas
        
        print(f"Total de pasadas necesarias: {pass_count}")



    def insertionSortAndDedupe(self):
        n = self.__nItems  

        LOW_KEY = float('-inf')  

        for i in range(1, n):
            key = self.__a[i]  

            j = i - 1
            while j >= 0 and self.__a[j] > key:
            
                if self.__a[j] == key:
                    self.__a[j] = LOW_KEY

                self.swap(j, j + 1)
                j -= 1

            if key != LOW_KEY:
                self.__a[j + 1] = key

        num_duplicates = 0
        for i in range(n):
            if self.__a[i] == LOW_KEY:
                num_duplicates += 1
                
        j = num_duplicates
        for i in range(num_duplicates, n):
            if self.__a[i] != LOW_KEY:
                self.swap(j, i)
                j += 1
        self.__nItems = n - num_duplicates  
        
    
    
