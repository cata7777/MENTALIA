from flask import render_template, jsonify
from app.apps.despacho_legal import bp

@bp.route('/')
def index():
    return render_template('despacho_legal/index.html')

@bp.route('/api/status')
def status():
    return jsonify({'status': 'active', 'app': 'despacho_legal'})
