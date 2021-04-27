class Noticia:

    def __init__(self, url_img = None, titulo = None, texto = None, data_publicacao = None, id = None):
        self.url_img = url_img
        self.titulo = titulo
        self.texto = texto
        self.data_publicacao = data_publicacao
        self.id = id

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


'''

noticia1 = Noticia("url_img", "corona virus", "blablablablabla", "12/03/2021", 1)

print(noticia1.get_url_img())
print(noticia1.get_titulo())
print(noticia1.get_texto())
print(noticia1.get_data_publicacao())
print(noticia1.get_id())

'''