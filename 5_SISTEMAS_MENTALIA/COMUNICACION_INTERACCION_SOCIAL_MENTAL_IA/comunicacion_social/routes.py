from flask import render_template, jsonify
from app.apps.comunicacion_social import bp

@bp.route('/')
def index():
    return render_template('comunicacion_social/index.html')

@bp.route('/api/status')
def status():
    return jsonify({'status': 'active', 'app': 'comunicacion_social'})
