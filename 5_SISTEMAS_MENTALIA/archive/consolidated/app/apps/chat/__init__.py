from flask import Blueprint

bp = Blueprint('chat', __name__)

from app.apps.chat import routes
