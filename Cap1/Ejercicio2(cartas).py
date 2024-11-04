import random
lista=[1,2,3,4,5,6,7,8,9,10,11,12,13]
var=0
random.shuffle(lista)
print(lista)
for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j]>lista[j+1]:
            var=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=var
print(lista)