from flask import Blueprint

bp = Blueprint('hiperfoco', __name__)

from app.apps.hiperfoco import routes
