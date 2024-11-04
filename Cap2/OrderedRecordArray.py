def identity(x):                       
    return x  # Función identidad como clave por defecto

class OrderedRecordArray(object): 
    def __init__(self, initialSize, key=identity):   
        # Constructor
        self.__a = [None] * initialSize  # Arreglo como lista
        self.__nItems = 0                # Inicialmente no hay elementos
        self.__key = key                 # Función clave para ordenar

    def __len__(self):                  
        return self.__nItems             # Devolvemos el número de elementos

    def get(self, n):                    
        if n >= 0 and n < self.__nItems:  # Verificamos si el índice está dentro de los límites
            return self.__a[n]            
        raise IndexError("Índice " + str(n) + " fuera de rango") 

    def insert(self, item):
        # Insertamos el elemento en la posición correcta (ordenado)
        if self.__nItems >= len(self.__a):
            raise Exception("El arreglo está lleno")
        
        # Buscamos la posición correcta donde insertar el nuevo elemento
        j = self.__nItems
        while j > 0 and self.__key(self.__a[j - 1]) > self.__key(item):
            self.__a[j] = self.__a[j - 1]  # Desplazamos elementos hacia la derecha
            j -= 1
        self.__a[j] = item
        self.__nItems += 1

    def traverse(self, function=print): 
        # Recorremos todos los elementos y aplicamos una función (por defecto, imprime)
        for j in range(self.__nItems): 
            function(self.__a[j]) 

    def __str__(self):                  
        # Retornamos una representación en string del arreglo
        ans = "["
        for i in range(self.__nItems):   
            if len(ans) > 1:
                ans += ", "  # Añadimos una coma entre los elementos
            ans += str(self.__a[i])  # Convertimos el elemento a string
        ans += "]"
        return ans

    def merge(self, arr):
        # Verificamos si las funciones clave son iguales
        if self.__key != arr.__key:
            raise Exception("Las funciones clave de ambos arreglos no son idénticas")

        # Crear una nueva lista para la fusión
        newSize = self.__nItems + arr.__nItems
        newArray = [None] * newSize

        i, j, k = 0, 0, 0  # Índices para recorrer ambos arreglos y la lista nueva

        # Comparar y fusionar
        while i < self.__nItems and j < arr.__nItems:
            if self.__key(self.__a[i]) <= self.__key(arr.__a[j]):
                newArray[k] = self.__a[i]
                i += 1
            else:
                newArray[k] = arr.__a[j]
                j += 1
            k += 1

        # Copiar los elementos restantes del arreglo original (si quedan)
        while i < self.__nItems:
            newArray[k] = self.__a[i]
            i += 1
            k += 1

        # Copiar los elementos restantes del arreglo fuente (si quedan)
        while j < arr.__nItems:
            newArray[k] = arr.__a[j]
            j += 1
            k += 1

        # Actualizar el arreglo actual con los datos fusionados
        self.__a = newArray
        self.__nItems = newSize

# Pruebas

# Creamos dos OrderedRecordArray
array1 = OrderedRecordArray(10)
array2 = OrderedRecordArray(10)

# Insertamos números en orden aleatorio
array1.insert(1)
array1.insert(3)
array1.insert(5)
array1.insert(7)

array2.insert(2)
array2.insert(4)
array2.insert(6)
array2.insert(8)

print("Array 1 antes de la fusión:")
array1.traverse()

print("Array 2 antes de la fusión:")
array2.traverse()

# Fusionamos array2 en array1
array1.merge(array2)

print("Array 1 después de la fusión:")
array1.traverse()
