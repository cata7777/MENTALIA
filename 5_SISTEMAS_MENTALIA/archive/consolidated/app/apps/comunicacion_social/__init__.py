from flask import Blueprint

bp = Blueprint('comunicacion_social', __name__)

from app.apps.comunicacion_social import routes
