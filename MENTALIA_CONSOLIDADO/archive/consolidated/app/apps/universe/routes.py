from flask import render_template, jsonify
from app.apps.universe import bp

@bp.route('/')
def index():
    return render_template('universe/index.html')

@bp.route('/api/status')
def status():
    return jsonify({'status': 'active', 'app': 'universe'})
