import Array
import random




class Cola(object):
    
    def Cola(self):
        maxSize = 20
        arr = Array.Array(maxSize)
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        