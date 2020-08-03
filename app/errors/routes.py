from . import errors_bp
from flask import render_template, jsonify
from werkzeug.exceptions import HTTPException


@errors_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404


@errors_bp.app_errorhandler(401)
def unathorized(e):
    return render_template('error.html', msg='No tiene permiso para acceder, debera loguearse'), 401


@errors_bp.app_errorhandler(403)
def unathorized(e):
    return render_template('error.html', msg='Su usuario no dispone de permisos para acceder a esta pagina'), 403


@errors_bp.app_errorhandler(HTTPException)
def handle_exception(e):
    return render_template('error.html', msg=str(e)), 500

