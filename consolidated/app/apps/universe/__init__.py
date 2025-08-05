from flask import Blueprint

bp = Blueprint('universe', __name__)

from app.apps.universe import routes
