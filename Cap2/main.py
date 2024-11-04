import Pila
import Cola

cola=Cola.Cola()
pila=Pila.Pila()

op=1
while op != 3:
    print("\nMenú:")
    print("1-Cola")
    print("2-Pila")
    print("3-Salir")

    op=int(input("Ingrese un número (1-3): "))

    if op == 1:
        print("\nTrabajando con Cola...")
        cola.Cola()
    elif op == 2:
        print("\nTrabajando con Pila...")
        pila.Pila()
    elif op == 3:
        quit()

    
    





