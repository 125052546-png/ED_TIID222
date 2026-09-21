arreglo = []
n = 15
dato = 0
for i in range(n):
   
    dato = int(input("Ingrese un numero: "))
    while dato > 500 or dato < 0:
        dato = int(input("Ingrese un numero entre 0 y 500: "))
    
    arreglo.append(dato)

for i in range(n):
    num = arreglo[i]
    while arreglo[i] % 5 != 0:
        arreglo[i] += 1

        

print(arreglo)