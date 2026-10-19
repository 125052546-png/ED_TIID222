matriz = {
    [71,12,98,34],
    [5,61,27,94],
    [46,18,80,3]
}
matriz.append([26,93,14,33])
print(matriz)
print(matriz[1])


for i in matriz:
    if 61 in i:
            print("61 encontrado en la fila {i}")
            break


for filas in matriz:
      for numeros in filas:
            if numeros == 18:
                  print("18 encontrado en la fila {filas}")
                  break