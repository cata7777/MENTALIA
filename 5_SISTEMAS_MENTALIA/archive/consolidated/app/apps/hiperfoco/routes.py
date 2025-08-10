from flask import render_template, jsonify
from app.apps.hiperfoco import bp

@bp.route('/')
def index():
    return render_template('hiperfoco/index.html')

@bp.route('/api/status')
def status():
    return jsonify({'status': 'active', 'app': 'hiperfoco'})
