pila = []

while True:
    print("\n--- MENU PILA ---")
    print("1. Insertar en pila")
    print("2. Borrar en pila")
    print("3. Listar pila")
    print("4. Salir")

    opcion = input("Seleccione una opcion (1-4): ")

    if opcion == "1":
        try:
            numero = int(input("Ingrese el numero que desea agregar a la pila: "))
            pila.append(numero)
            print(f"El numero {numero} ha sido insertado correctamente.")
        except ValueError:
            print("Error: Por favor, ingrese un numero valido.")

    elif opcion == "2":
        if len(pila) > 0:
            elemento_eliminado = pila.pop()
            print(f"Se ha eliminado el elemento del tope de la pila: {elemento_eliminado}")
        else:
            print("La pila esta vacia. No hay elementos para borrar.")

    elif opcion == "3":
        if len(pila) > 0:
            print("Estado actual de la pila:", pila)
        else:
            print("La pila actualmente esta vacia.")

    elif opcion == "4":
        print("Saliendo del programa")
        break

    else:
        print("Opcion no valida Por favor intente de nuevo con un numero del 1 al 4")
