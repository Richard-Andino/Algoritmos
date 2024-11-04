"""
Escriba una lista de comprensión de Python que devuelva al individuo
caracteres de una cadena que no son espacios en blanco. Aplicarlo a
la cadena "4 and 20 blackbirds.”
"""

cade="4 and 20 blackbirds."
list=[]
for i in range(len(cade)):
    if cade[i]!=' ':
        list.append(cade[i])
        print(cade[i])
print(list)