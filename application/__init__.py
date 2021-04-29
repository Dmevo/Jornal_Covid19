from flask import Flask
import os
from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia

app = Flask(__name__, static_folder = os.path.abspath("application/view/static"), template_folder = os.path.abspath("application/view/templates"))

noticia1 = Noticia("url_img", "Covid19 - 1", "texto1", "20/01/2021", 1)
noticia2 = Noticia("url_img", "Covid19 - 2", "texto2", "13/02/2021", 2)
noticia3 = Noticia("url_img", "Covid19 - 3", "texto3", "04/03/2020", 3)
noticia4 = Noticia("url_img", "Covid19 - 4", "texto4", "08/01/2021", 4)

noticia_lista = [noticia1, noticia2, noticia3, noticia4]

estado_lista = []

estado1 = Estado("Rio de Janeiro", "RJ", "url_bandeira", 1, [noticia1, noticia2])
estado2 = Estado("São Paulo", "SP", "url_bandeira", 2, [noticia3, noticia4])

estado_lista = [estado1, estado2]

from application.controller import home_controller