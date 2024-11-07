from SimpleStack import *

# Crear una pila para almacenar caracteres
stack = Stack(10)

# Definir la frase
phrase = 'A man, a plan, a canal, Panama'

# Normalizar la frase: eliminar puntuación y convertir a minúsculas
normalized_phrase = ''.join(char.lower() for char in phrase if char.isalnum() or char.isspace())

# Dividir la frase en palabras
words = normalized_phrase.split()

# Inicializar una lista para almacenar las palabras invertidas
reversed_words = []

# Invertir cada palabra
for word in words:
    # Vaciar la pila antes de usarla para la nueva palabra
    while not stack.isEmpty():
        stack.pop()

    # Agregar cada carácter de la palabra a la pila
    for char in word:
        if not stack.isFull():
            stack.push(char)

    # Usar una lista para almacenar los caracteres invertidos
    reversed_word_chars = []

    # Sacar caracteres de la pila para crear la palabra invertida
    while not stack.isEmpty():
        reversed_word_chars.append(stack.pop())  # Agregar a la lista

    # Unir los caracteres para formar la palabra invertida
    reversed_word = ''.join(reversed_word_chars)

    # Agregar la palabra invertida a la lista
    reversed_words.append(reversed_word)

# Unir las palabras invertidas en una frase
final_result = ' '.join(reversed_words)

print("Frase con palabras invertidas:", final_result)

if final_result == word:
    print("La cadena es un palindromo")
else:
    print("La cadena no es un palindromo")
    
    