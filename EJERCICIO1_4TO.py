class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.apuntador = None


class Lista_enlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza

        while actual.apuntador is not None:
            actual = actual.apuntador

        actual.apuntador = nuevo

    def imprimir(self):
        actual = self.cabeza

        while actual is not None:
            print(actual.dato)
            actual = actual.apuntador

        print("Fin del nodo")


# Se imprimira el programa

# Creamos la lista vacia
mi_lista = Lista_enlazada()

# Insertamos datos
mi_lista.insertar(10)
mi_lista.insertar(20)
mi_lista.insertar(30)

# Mostramos la lista
mi_lista.imprimir()