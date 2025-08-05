from flask import Blueprint

bp = Blueprint('despacho_legal', __name__)

from app.apps.despacho_legal import routes
