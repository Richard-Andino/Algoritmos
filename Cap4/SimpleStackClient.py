import SimpleStack

print("--- Prueba de la clase Stack ---")
stack = SimpleStack.Stack(5) #creacion del Stack con un tamaño de 5

try: #apilar elementos
    print("-Apilando elementos en la Stack-")
    stack.push("A")
    stack.push("B")
    stack.push("C")
    print("Estado de la Stack:", stack.peek())

    print("\nViendo el elemento superior:", stack.peek()) #elemento superior

    print("\n-Desapilando elementos-") #desapilar y mostrar
    print("Elemento desapilado:", stack.pop())
    print("Estado de la Stack:", stack)

    print("\n-Intentando desapilar todos los elementos-")
    while not stack.isEmpty():
        print("Elemento desapilado:", stack.pop())
    print("Estado de la Stack (vacia):", stack)

    print("\n-Intentando desapilar de una Stack vacia-")
    stack.pop()

except Exception as e:
    print("Error:",e)

#clase deque
print("")
print("\n--- Prueba de la clase Deque ---")
deque = SimpleStack.Deque(4)
try:
    print("-Insertando elementos a la izquierda en el Deque-")
    deque.insertLeft("1")
    deque.insertLeft("2")
    print("Estado del deque:", deque)

    print("\n-Insertando elementos a la derecha del Deque-")
    deque.insertRight("3")
    deque.insertRight("4")
    print("Estado del Deque:", deque)

    print("\n-Eliminando elementos de la izquierda del Deque-")
    print("Elemento eliminado:", deque.removeLeft())
    print("Estado del deque:", deque)

    print("\n-Eliminando elementos de la derecha del Deque-")
    print("Elemento eliminado:", deque.insertRight())
    print("Estado del Deque:", deque)

    print("\n-Intentando insertar en un Deque lleno-")
    deque.insertLeft("5")
except Exception as e:
    print("Error:", e)

#clase PriorityQueue
print("")
print("\n--- Prueba de la clase PriorityQueue ---")
pq = SimpleStack.PriorityQueue()
try:
    print("-Insertando elementos en la PriorituQueue con distintas prioridades-")
    pq.insert("T1", 3)
    pq.insert("T2", 1)
    pq.insert("T3", 5)
    pq.insert("T5", 2)
    print("Estado de la PriorityQueue:", pq)

    print("\nViendo el elemento de mayor prioridad", pq.peekHighestPriority())

    print("\n-Eliminando el elemento de mayor prioridad-")
    print("Elemento de mayor prioridad eliminado:", pq.removeHighestPriority())
    print("Estado de la PriorityQueue:", pq)

    print("\n-Eliminando todos los elementos por prioridad-")
    while not pq.isEmpty():
        print("Elemento de mayor prioridad eliminado:", pq.removeHighestPriority())
        print("Estado actual de la PriorityQueue:", pq)

    print("\n-eliminando de una PriorityQueue vacia-")
    pq.removeHighestPriority()
except Exception as e:
    print("Error:",e)
