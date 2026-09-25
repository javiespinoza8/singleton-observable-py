import ttkbootstrap as ttk
from ttkbootstrap.constants import *
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

app = ttk.Window(title="Demo — Librería SingletonObservable", themename="flatly")
app.geometry("640x420")

notebook = ttk.Notebook(app)
notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)

# ---------- Pestaña 1: Biblioteca ----------
tab_biblioteca = ttk.Frame(notebook)
notebook.add(tab_biblioteca, text="Biblioteca")

tabla_prestamos = ttk.Treeview(tab_biblioteca, columns=("libro", "multa"), show="headings")
tabla_prestamos.heading("libro", text="Libro")
tabla_prestamos.heading("multa", text="Multa")
tabla_prestamos.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_biblioteca = GestorPrestamos()

def refrescar_prestamos(_=None):
    tabla_prestamos.delete(*tabla_prestamos.get_children())
    for p in gestor_biblioteca.prestamos:
        tabla_prestamos.insert("", "end", values=(p["libro"], p["multa"]))

gestor_biblioteca.suscribir(refrescar_prestamos)

ttk.Button(
    tab_biblioteca, 
    text="Agregar préstamo de prueba", 
    bootstyle="success",
    command=lambda: gestor_biblioteca.registrar({"libro": "1984", "multa": 5.0})
).pack(pady=8)

# ---------- Pestaña 2: Juguetería ----------
tab_jugueteria = ttk.Frame(notebook)
notebook.add(tab_jugueteria, text="Juguetería")

tabla_ventas = ttk.Treeview(tab_jugueteria, columns=("juguete", "total"), show="headings")
tabla_ventas.heading("juguete", text="Juguete")
tabla_ventas.heading("total", text="Total")
tabla_ventas.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_jugueteria = GestorVentas()

def refrescar_ventas(_=None):
    tabla_ventas.delete(*tabla_ventas.get_children())
    for v in gestor_jugueteria.ventas:
        tabla_ventas.insert("", "end", values=(v["juguete"], v["total"]))

gestor_jugueteria.suscribir(refrescar_ventas)

ttk.Button(
    tab_jugueteria, 
    text="Agregar venta de prueba", 
    bootstyle="success",
    command=lambda: gestor_jugueteria.registrar({"juguete": "Robot", "total": 150.0})
).pack(pady=8)

if __name__ == "__main__":
    app.mainloop()