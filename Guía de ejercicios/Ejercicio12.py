import FuncionesCola

cola = FuncionesCola.Funciones(maxSize=10)

cola.agregarCliente(1)
cola.agregarCliente(2)
cola.agregarCliente(3)
cola.agregarCliente(4)

cola.atenderCliente()
cola.atenderCliente()


print("\nClientes en espera: ")
cola.traverse()