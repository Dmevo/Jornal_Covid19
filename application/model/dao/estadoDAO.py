from application import estado_lista
from application.model.entity.estado import Estado

class EstadoDAO:

    def __init__(self):
        self.estado_lista = estado_lista

    def mostrar_estados(self):
        return self.estado_lista