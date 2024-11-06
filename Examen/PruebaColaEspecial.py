from ColaEspecial import *

arr = ColaEspecial()



arr.insert("A")
arr.insert("B")
arr.insert("C")
arr.insert("D")
arr.insert("E")
arr.insert("F")
arr.insert("G")
arr.insert("H")
arr.insert("I")
arr.insert("J")

print("Obteniendo el 10: ", arr.get(9))

for i in range(arr.__len__(), 0, -1):
    
    if i==10:
        print("Imprimiendo i:", i-1)
        arr.delete(arr.get(i))
        arr.insertn("Z", i-1)
    elif i==9:
        print("Imprimiendo i:", i-1)
        print("obteniendo valor")
        print(arr.get(i))



print("Imprimiendo arreglo")
arr.traverse()

print(arr.__len__())