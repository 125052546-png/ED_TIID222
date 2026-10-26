class Nodo:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None

class Listaenlazada:

    def __init__(self):
        self.cabeza = None

    def insertarInicio(self, numero):
        nuevo = Nodo(numero)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertarFinal(self, numero):
        nuevo = Nodo(numero)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def imprimirLista(self):
        actual = self.cabeza

        while actual:
            print(actual.numero, "→", end=" ")
            actual = actual.siguiente
        print("None")

Mi_lista = Listaenlazada()
Mi_lista.insertarInicio(1)
Mi_lista.insertarFinal(56)
Mi_lista.imprimirLista()