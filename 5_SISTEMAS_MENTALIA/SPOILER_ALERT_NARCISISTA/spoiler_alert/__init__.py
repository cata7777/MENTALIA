from flask import Blueprint

bp = Blueprint('spoiler_alert', __name__)

from app.apps.spoiler_alert import routes
