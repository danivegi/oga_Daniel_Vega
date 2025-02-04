print('Hola')
print(3+2)
n = 4
print('n =', n)

nota_1 = 2
nota_2 = 5
nota_media = (nota_1 + nota_2) / 2
print('Nota media =', nota_media)

'Hola mundo'
"Hola mundo"
"Esta \"palabra\" va entre comillas"

print("una linea \n otra linea")

cadena1 = "Hola"
print(cadena1)

cadena2 = "          "
print(cadena1 + "" + cadena2 + "" + cadena1)

diez_espacios = " " * 10
print("Esto son diez espacios:" + diez_espacios + "fin.")

palabra = "Python"
print(palabra[1])
print(palabra[-1])
print(palabra[0:2])

numeros=[1,2,3,4,5]
print(numeros)
datos = [4, "una cadena", 3.14, -15, "otra cadena", "1", 1]
print(datos)
print(len(datos))
print(datos[1])
print(datos[len(datos)-1])
print(datos[0:2])
print(datos[-7:-1])

print(numeros + [6,7,8,9])
pares = [2,4,6,8,10]
print(pares)
print(pares[2])
print(pares.append(12))

letras = ['a', 'b', 'c', 'd', 'e']
print(letras[0:3])
print(letras[:3])

letras[0:3] = ['A','B','C']
print(letras)

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]

print(r)
print(r[1])
print(r[1][1])
print(r[-1])
print(r[-1][-1])

print(1+1 == 3)
print(1+1 == 2)
print(3 > 2)
print(3 != 2)

a = 10
b = 5
print('Div =', a/b == 2)

print("Hola" == "Hola")
l1 = [0,1,2]
l2 = [2,3,4]
print(l1 == l2)
print(len(l1) == len(l2))

print("=======Falsos and Trues========")
print(False * 3)
print(not True)
print(True and True)
print(False and True)
print(False or True)

print('=====Cosas con Cadenas====')
c = "Hola mundo"
print(len(c) >= 20 and c[0] == 'H')
print(len(c) >= 20 or c[0] == 'H')
c = "Lectura"
print(c[0] == 'H' or c[0]=='h')

print("====Acumuladores====")
a = 5
a = a + 2
print(a)
a += 2
print(a)