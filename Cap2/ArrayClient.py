import random
import Array
maxSize = 10                    # Max size of the array          
arr = Array.Array(maxSize)      # Create an array object

"""
for i in range(10):
    arr.push(random.randint(1,100))
    
arr.traverse()

sumPar=sumImpar=contPar=contImpar=promPar=promImpar=0

for i in range(10):
    numberPop = arr.pop()
    if numberPop is not None:
        if numberPop % 2 == 0:
            sumPar += numberPop
            contPar += 1
            promPar = sumPar/contPar
        else:
            sumImpar += numberPop
            contImpar += 1
            promImpar = sumImpar / contImpar
        




print(f"La suma Par es {sumPar}, la cantidad de numeros pares: {contPar} y el promedio de los pares es: {promPar} ")

print(f"La suma Impar es {sumImpar}, la cantidad de numeros impares: {contImpar} y el promedio de los impares es: {promImpar} \n")



for i in range(10):
    arr.push(random.randint(1,100))

arr.traverse()

sumPar=sumImpar=contPar=contImpar=promPar=promImpar=0

for i in range (10):
    num1 = arr.get(0)
    if num1 is not None:
        if num1 % 2 == 0:
            sumPar += num1
            contPar += 1
            promPar = sumPar/contPar
            arr.delete(num1)
        else:
            sumImpar += num1
            contImpar += 1
            promImpar = sumImpar / contImpar
            arr.delete(num1)
        

print(f"La suma Par es {sumPar}, la cantidad de numeros pares: {contPar} y el promedio de los pares es: {promPar} ")

print(f"La suma Impar es {sumImpar}, la cantidad de numeros impares: {contImpar} y el promedio de los impares es: {promImpar} \n")
"""



arr.insert(10)
arr.insert("bazz")
arr.insert(50)
arr.insert(12)
arr.insert("foo")
arr.insert(57)
arr.insert(15)
arr.insert("bar")
arr.insert(90)
arr.insert(67)


print("Array after deletions has", len(arr), "items") 
arr.traverse()

print("\n El numero maximo es: ", arr.getMaxNum())

arr.delete(arr.getMaxNum())
print("Array sin el numero maximo:")
arr.traverse()






arr.removeDupes()
print("Lista sin duplicados: ")
arr.traverse()





