import Rectangulo



rect = Rectangulo.Rectangulo(8 , 2)
rect1 = Rectangulo.Rectangulo(10 , 4)

print("Rectangulo 1: ", rect.getArea())
print("Rectangulo 2: ", rect1.getArea())

print(f"Suma de las areas de ambos rectangulos: {rect.getArea() + rect1.getArea()}" )

print(f"Perimetro del rectangulo 1: {rect.perimetro()}")
print(f"Perimetro del rectangulo 2: {rect1.perimetro()}")

print("Dibujando rectangulos: \n")
rect.dibujar()
print("\n")
rect1.dibujar()
