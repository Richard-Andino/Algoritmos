#Ejercicio 5 eliminar duplicados, y devolver arreglo sin duplicados

import Funciones

maxSize = 10          
arr = Funciones.Funciones(maxSize) 

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

sinDuplicado = arr.eliminar_duplicado(array)

sinDuplicado.traverse()
