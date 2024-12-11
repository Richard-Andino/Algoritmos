import FuncionesPila

pila=FuncionesPila.Funciones(maxSize=10)

lista=[1, 2, "+",2, "*", 7, "+"]

re=pila.calculadora(lista)

print("el resultado es: ", re)