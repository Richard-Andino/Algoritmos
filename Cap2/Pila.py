import Array
import random



class Pila(object):
    def Pila(self):
        maxSize = 20
        arr = Array.Array(maxSize)
        
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

    
    
        
        
    

