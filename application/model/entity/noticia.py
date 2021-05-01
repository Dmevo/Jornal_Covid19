class Noticia:

    def __init__(self, url_img = None, titulo = None, texto = None, data_publicacao = None, id = None, visualizacao = None, curtidas = None, url_noticia = None):
        self.url_img = url_img
        self.titulo = titulo
        self.texto = texto
        self.data_publicacao = data_publicacao
        self.id = id
        self.visualizacao = visualizacao
        self.curtidas = curtidas
        self.url_noticia = url_noticia

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

    def get_url_noticia(self):
        return self.url_noticia

    def set_url_noticia(self, url_noticia):
        self.url_noticia = url_noticia
    
    def set_texto(self, texto):
        self.texto = texto

    def set_titulo(self, titulo):
        self.titulo = titulo



'''
noticia1 = Noticia("url_img", "corona virus", "blablablablabla", "12/03/2021", 1)
noticia1.set_texto("bebebebebe")
print(noticia1.get_texto())

'''


