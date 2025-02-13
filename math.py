import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio


circulo = Circulo(5)

# Mostrar los valores
print(f"Radio: {circulo.radio}")
print(f"Área: {circulo.area()}")
print(f"Perímetro: {circulo.perimetro()}")