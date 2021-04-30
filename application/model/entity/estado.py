class Estado:

    def __init__(self, nome = None, sigla = None, url_bandeira = None, id = None, lista_noticia = None):
        self.nome = nome
        self.sigla = sigla
        self.url_bandeira = url_bandeira
        self.id = id
        self.lista_noticia = lista_noticia

    def get_nome(self):
        return self.nome

    def get_sigla(self):
        return self.sigla

    def get_url_bandeira(self):
        return self.url_bandeira

    def get_id(self):
        return self.id

    def get_lista_noticia(self):
        return self.lista_noticia

    



'''
estado1 = Estado("Rio de janeiro", "RJ", "url_bandeira", 1)

print(estado1.get_nome())
print(estado1.get_sigla())
print(estado1.get_url_bandeira())
print(estado1.get_id())

'''