import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from singleton_observable import SingletonObservable

# --- Clases de Negocio (Todas heredan de SingletonObservable) ---
class GestorPrestamos(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "prestamos"):
            self.prestamos = []
    def registrar(self, p):
        self.prestamos.append(p)
        self.notificar(p)

class GestorVentas(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "ventas"):
            self.ventas = []
    def registrar(self, v):
        self.ventas.append(v)
        self.notificar(v)

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

# --- Configuración de la Ventana Principal ---
app = ttk.Window(title="Demo JMEC — Múltiples Dominios SingletonObservable", themename="flatly")
app.geometry("850x520")

notebook = ttk.Notebook(app)
notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)

# ---------- Pestaña 1: Biblioteca (JMEC) ----------
tab_biblio = ttk.Frame(notebook)
notebook.add(tab_biblio, text="Biblioteca (JMEC)")

tabla_p = ttk.Treeview(tab_biblio, columns=("libro", "multa"), show="headings")
tabla_p.heading("libro", text="Libro [JMEC]")
tabla_p.heading("multa", text="Multa")
tabla_p.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_biblio = GestorPrestamos()
def ref_biblio(_=None):
    tabla_p.delete(*tabla_p.get_children())
    for p in gestor_biblio.prestamos:
        tabla_p.insert("", "end", values=(p["libro"], p["multa"]))

gestor_biblio.suscribir(ref_biblio)
ttk.Button(
    tab_biblio, 
    text="Registrar Préstamo (JMEC)", 
    bootstyle="success",
    command=lambda: gestor_biblio.registrar({"libro": "Cien Años de Soledad", "multa": 2.5})
).pack(pady=8)

# ---------- Pestaña 2: Juguetería (JMEC) ----------
tab_juguete = ttk.Frame(notebook)
notebook.add(tab_juguete, text="Juguetería (JMEC)")

tabla_v = ttk.Treeview(tab_juguete, columns=("juguete", "total"), show="headings")
tabla_v.heading("juguete", text="Juguete [JMEC]")
tabla_v.heading("total", text="Total")
tabla_v.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_juguete = GestorVentas()
def ref_juguete(_=None):
    tabla_v.delete(*tabla_v.get_children())
    for v in gestor_juguete.ventas:
        tabla_v.insert("", "end", values=(v["juguete"], v["total"]))

gestor_juguete.suscribir(ref_juguete)
ttk.Button(
    tab_juguete, 
    text="Registrar Venta Juguete (JMEC)", 
    bootstyle="success",
    command=lambda: gestor_juguete.registrar({"juguete": "Lego Star Wars", "total": 85.0})
).pack(pady=8)

# ---------- Pestaña 3: Aerolínea (JMEC) ----------
tab_aero = ttk.Frame(notebook)
notebook.add(tab_aero, text="Aerolínea (JMEC)")

tabla_a = ttk.Treeview(tab_aero, columns=("vuelo", "destino"), show="headings")
tabla_a.heading("vuelo", text="Vuelo [JMEC]")
tabla_a.heading("destino", text="Destino")
tabla_a.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_aero = GestorAerolinea()
def ref_aero(_=None):
    tabla_a.delete(*tabla_a.get_children())
    for vuelo in gestor_aero.vuelos:
        tabla_a.insert("", "end", values=(vuelo["vuelo"], vuelo["destino"]))

gestor_aero.suscribir(ref_aero)
ttk.Button(
    tab_aero, 
    text="Registrar Vuelo (JMEC)", 
    bootstyle="info",
    command=lambda: gestor_aero.registrar({"vuelo": "LA-402", "destino": "Buenos Aires"})
).pack(pady=8)

# ---------- Pestaña 4: Joyería (JMEC) ----------
tab_joya = ttk.Frame(notebook)
notebook.add(tab_joya, text="Joyería (JMEC)")

tabla_j = ttk.Treeview(tab_joya, columns=("joya", "precio"), show="headings")
tabla_j.heading("joya", text="Joya [JMEC]")
tabla_j.heading("precio", text="Precio ($)")
tabla_j.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_joya = GestorJoyeria()
def ref_joya(_=None):
    tabla_j.delete(*tabla_j.get_children())
    for joya in gestor_joya.joyas:
        tabla_j.insert("", "end", values=(joya["joya"], joya["precio"]))

gestor_joya.suscribir(ref_joya)
ttk.Button(
    tab_joya, 
    text="Registrar Joya (JMEC)", 
    bootstyle="warning",
    command=lambda: gestor_joya.registrar({"joya": "Anillo de Oro", "precio": 1200.0})
).pack(pady=8)

if __name__ == "__main__":
    app.mainloop()