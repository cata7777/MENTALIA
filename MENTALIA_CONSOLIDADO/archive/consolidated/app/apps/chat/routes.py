from flask import render_template, jsonify
from app.apps.chat import bp

@bp.route('/')
def index():
    return render_template('chat/index.html')

@bp.route('/api/status')
def status():
    return jsonify({'status': 'active', 'app': 'chat'})
