cola = []

while True:
    print("\n--- MENU COLA ---")
    print("1. Insertar cola")
    print("2. Borrar en cola")
    print("3. Listar cola")
    print("4. Salir")
    
    opcion = input("Seleccione una opcion (1-4): ")

    if opcion == "1":
        try:
            numero = int(input("Ingrese el numero que desea agregar a la cola: "))
            cola.append(numero)
            print(f"El numero {numero} ha sido insertado correctamente.")
        except ValueError:
            print("Error: Por favor, ingrese un numero valido.")

    elif opcion == "2":
        if len(cola) > 0:
            elemento_eliminado = cola.pop(0)
            print(f"Se ha eliminado el primer elemento de la cola: {elemento_eliminado}")
        else:
            print("La cola esta vacía. No hay elementos para borrar.")

    elif opcion == "3":
        if len(cola) > 0:
            print("Estado actual de la cola:", cola)
        else:
            print("La cola actualmente esta vacía.")

    elif opcion == "4":
        print("Saliendo del programa")
        break 

    else:
        print("Opcion no valida Por favor intente de nuevo con un numero del 1 al 4")