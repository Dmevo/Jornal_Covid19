from flask import render_template, url_for
from application import app
from application.model.entity.noticia import Noticia
from application.model.dao.noticiaDAO import NoticiaDAO
from application.model.entity.estado import Estado
from application.model.dao.estadoDAO import EstadoDAO

@app.route("/")
def home():
    estado_dao = EstadoDAO()
    estado_lista = estado_dao.mostrar_estados()
    return render_template("index.html", lista_estados = estado_lista)

@app.route("/noticia/<id>")
def noticia(id):
    noticia_dao = NoticiaDAO()
    noticia_lista = noticia_dao.mostrar_noticias()
    for noticia in noticia_lista:
        if str(noticia.get_id()) == id:
            return render_template("noticia.html", noticia = noticia)