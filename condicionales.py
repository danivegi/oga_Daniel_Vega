if True:
    print("Hola")
    print("otra linea")
    
a = 5
if a == 2:
    print("La variable a vale 2")
if a == 5:
    print("La variable a vale 5")
    
n = 11
if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

comando = "OTRA COSA"
if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDAR":
    print("Hola")
elif comando == "SALIR":
    print("ADIOS")
else:
    print("El comando no se reconoce")
    
#nota = float(input("Introduce una nota: "))
#if nota < 5:
#    print("Suspenso")
#elif nota >= 5 and nota < 6:
#    print("Suficiente")
#elif nota >= 6 and nota < 7:
#    print("Bien")
#elif nota >= 7 and nota < 9:
#    print("Notable")
#elif nota >= 9:
#    print("Sobresaliente")
    
""" print('Mas optimizado')
nota = float(input("Introduce una nota: "))
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente") """
    
c = 0
while c <= 6:
    c += 1
    print("c vale: ", c)
    
for i in range(1,11):
    print(f"Tabla del (i):")
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")

""" num = int(input("Introduce un número: "))
for i in range(1, 11):
    print (f"{num} x {i} = {num * i}") """
    
def saludo():
    print("Hola como estas")
    
saludo()
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print("La suma es: ", resultado)

""" numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es Impar") """
    
def es_par(num):
    return num % 2 == 0
print(es_par(3))