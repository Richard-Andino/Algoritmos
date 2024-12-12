import heapq
from collections import Counter

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(texto):
    frecuencia = Counter(texto)
    heap = [NodoHuffman(caracter, freq) for caracter, freq in frecuencia.items()]
    heapq.heapify(heap) 

    while len(heap) > 1:
        izquierda = heapq.heappop(heap)
        derecha = heapq.heappop(heap)
        combinado = NodoHuffman(None, izquierda.frecuencia + derecha.frecuencia)
        combinado.izquierda = izquierda
        combinado.derecha = derecha
        heapq.heappush(heap, combinado)
    
    return heap[0] 

def construir_tabla_codigos(nodo, prefijo="", tabla_codigos=None):
    if tabla_codigos is None:
        tabla_codigos = {}
    if nodo is not None:
        if nodo.caracter is not None: 
            tabla_codigos[nodo.caracter] = prefijo
        construir_tabla_codigos(nodo.izquierda, prefijo + "0", tabla_codigos)
        construir_tabla_codigos(nodo.derecha, prefijo + "1", tabla_codigos)
    return tabla_codigos

def codificar_texto(texto, tabla_codigos):
    return ''.join(tabla_codigos[caracter] for caracter in texto)

def decodificar_texto(cadena_binaria, raiz):
    texto_decodificado = []
    nodo_actual = raiz
    
    for bit in cadena_binaria:
        nodo_actual = nodo_actual.izquierda if bit == '0' else nodo_actual.derecha
        if nodo_actual.caracter is not None:
            texto_decodificado.append(nodo_actual.caracter)
            nodo_actual = raiz
    
    return ''.join(texto_decodificado)

if __name__ == "__main__":
    mensaje = input("Ingrese el mensaje de texto: ")

    raiz_huffman = construir_arbol_huffman(mensaje)
    tabla_codigos_huffman = construir_tabla_codigos(raiz_huffman)
    
    mensaje_codificado = codificar_texto(mensaje, tabla_codigos_huffman)
    mensaje_decodificado = decodificar_texto(mensaje_codificado, raiz_huffman)
    
    print("\nTabla de códigos de Huffman:")
    for caracter, codigo in tabla_codigos_huffman.items():
        print(f"'{caracter}': {codigo}")
    
    print(f"\nTexto codificado: {mensaje_codificado}")
    print(f"Texto decodificado: {mensaje_decodificado}")
    print(f"\nNúmero de bits en el mensaje codificado: {len(mensaje_codificado)}")
    print(f"Número de caracteres en el mensaje original: {len(mensaje)}")

