from flask import render_template, jsonify
from app.apps.spoiler_alert import bp

@bp.route('/')
def index():
    return render_template('spoiler_alert/index.html')

@bp.route('/api/status')
def status():
    return jsonify({'status': 'active', 'app': 'spoiler_alert'})
