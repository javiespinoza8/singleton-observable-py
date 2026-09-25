from singleton_observable import SingletonObservable

class GestorPrestamos(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "prestamos"):
            self.prestamos = []

    def registrar(self, prestamo):
        self.prestamos.append(prestamo)
        self.notificar(prestamo)

class GestorVentas(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "ventas"):
            self.ventas = []

    def registrar(self, venta):
        self.ventas.append(venta)
        self.notificar(venta)

gestor_biblioteca = GestorPrestamos()
gestor_jugueteria = GestorVentas()
otro_gestor_biblioteca = GestorPrestamos()

print("¿Mismo gestor de biblioteca?", gestor_biblioteca is otro_gestor_biblioteca)
print("¿Biblioteca y juguetería son gestores distintos?", gestor_biblioteca is not gestor_jugueteria)