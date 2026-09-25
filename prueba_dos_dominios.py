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

class GestorAerolinea(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "vuelos"):
            self.vuelos = []
    def registrar(self, vuelo):
        self.vuelos.append(vuelo)
        self.notificar(vuelo)

class GestorJoyeria(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "joyas"):
            self.joyas = []
    def registrar(self, joya):
        self.joyas.append(joya)
        self.notificar(joya)

# Pruebas de aislamiento entre los 4 dominios
b1 = GestorPrestamos()
b2 = GestorPrestamos()
v1 = GestorVentas()
aero = GestorAerolinea()
joya = GestorJoyeria()

print("¿Mismo gestor de biblioteca?", b1 is b2)
print("¿Biblioteca y Juguetería son distintos?", b1 is not v1)
print("¿Juguetería y Aerolínea son distintos?", v1 is not aero)
print("¿Aerolínea y Joyería son distintos?", aero is not joya)