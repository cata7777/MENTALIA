from flask import Blueprint

bp = Blueprint('sign_link', __name__)

from app.apps.sign_link import routes
