class Noticia:

    def __init__(self, url_img = None, titulo = None, texto = None, data_publicacao = None, id = None, visualizacao = None, curtidas = None):
        self.url_img = url_img
        self.titulo = titulo
        self.texto = texto
        self.data_publicacao = data_publicacao
        self.id = id
        self.visualizacao = visualizacao
        self.curtidas = curtidas

    def get_url_img(self):
        return self.url_img

    def get_titulo(self):
        return self.titulo

    def get_texto(self):
        return self.texto

    def get_data_publicacao(self):
        return self.data_publicacao

    def get_id(self):
        return self.id

    def get_visualizacao(self):
        return self.visualizacao

    def get_curtidas(self):
        return self.curtidas


'''

noticia1 = Noticia("url_img", "corona virus", "blablablablabla", "12/03/2021", 1)

print(noticia1.get_url_img())
print(noticia1.get_titulo())
print(noticia1.get_texto())
print(noticia1.get_data_publicacao())
print(noticia1.get_id())

'''