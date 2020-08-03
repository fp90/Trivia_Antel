from app import login_required
from flask import render_template, session
from . import public_bp
from .models import Categoria, Pregunta, Respuesta
import random
import datetime


@public_bp.route('/trivia')
def index():
    return render_template('trivia.html')


@public_bp.route('/trivia/categorias', methods=['GET'])
@login_required
def mostrarcategorias():
    categorias = Categoria.query.all()
    if 'start' not in session.keys():
        session['start'] = datetime.datetime.now()
        for cat in categorias:
            session[str(cat.id)] = False
    return render_template('categorias.html', categorias=categorias)


@public_bp.route('/trivia/<int:id_categoria>/pregunta/', methods=['GET'])
@login_required
def mostrarpregunta(id_categoria):
    preguntas = Pregunta.query.filter_by(categoria_id=id_categoria).all()
    # elegir pregunta aleatoria pero de la categoria adecuada
    pregunta = random.choice(preguntas)
    categ = Categoria.query.get(id_categoria)
    return render_template('preguntas.html', categoria=categ, pregunta=pregunta)


@public_bp.route('/trivia/<int:id_categoria>/<id_pregunta>/resultado/<int:id_respuesta>', methods=['GET'])
@login_required
def mostrarresultado(id_categoria, id_pregunta, id_respuesta):
    pregunta = Pregunta.query.get(id_pregunta)
    respuesta = Respuesta.query.get(id_respuesta)
    if respuesta.correct:
        session[str(id_categoria)] = True
        the_end = True
        categorias = Categoria.query.all()
        for categoria in categorias:
            if not session[str(categoria.id)]:
                the_end = False
                break
        if the_end:
            session['total_time'] = str(datetime.datetime.now() - session['start'])
            for cat in categorias:
                session[str(cat.id)] = False
            del session['start']
            return render_template('ganador.html')
        return render_template('correcto.html', pregunta=pregunta, respuesta=respuesta)
    else:
        return render_template('incorrecto.html', pregunta=pregunta, respuesta=respuesta)

