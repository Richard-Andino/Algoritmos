import FuncionesCola

cola = FuncionesCola.Funciones(maxSize=10)
print("Añadiendo elementos")
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(5)
cola.enqueue(9)
cola.enqueue(0)

cola.traverse()

print("Eliminando elementos")
cola.dequeue()

cola.traverse()