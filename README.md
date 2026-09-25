# singleton-observable-py

Una clase base reutilizable que agrega los patrones Singleton y Observer a cualquier clase de Python, sin tener que reescribir el mecanismo cada vez.

## Instalación
Copia `singleton_observable.py` a tu proyecto (por ahora no está publicada en PyPI).

## Uso básico
```python
from singleton_observable import SingletonObservable

class MiGestor(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "datos"):
            self.datos = []

    def registrar(self, dato):
        self.datos.append(dato)
        self.notificar(dato)