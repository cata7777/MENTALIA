from flask import render_template, jsonify
from app.apps.sign_link import bp

@bp.route('/')
def index():
    return render_template('sign_link/index.html')

@bp.route('/api/status')
def status():
    return jsonify({'status': 'active', 'app': 'sign_link'})
