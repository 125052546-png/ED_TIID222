#declaracion de un arreglo vacio

arreglo = []

print(arreglo)

n = int(input("Ingrese el tamaño del arreglo: "))

for i in range(n):
    dato = int(input("Ingrese un numero: "))
    arreglo.append(dato)

print("El arreglo es: ", arreglo)