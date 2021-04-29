from application import noticia_lista
from application.model.entity.noticia import Noticia

class VideoDAO():

    def __init__(self):
        self.noticia_lista = noticia_lista

    def mostrar_noticias(self):
        return self.noticia_lista