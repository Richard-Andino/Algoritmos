Array=[1,2,3,4,5,6,7,8,9]

#Ejercicio 2 Máximo y mínimo

max=Array[0]
min=Array[0]
for i in Array:
    if i>max:
        max=i
    if i<min:
        min=i
        
print("Ejercicio 2")
print("Numero max: ", max)
print("Numero min: ", min)