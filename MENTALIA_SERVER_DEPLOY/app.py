from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><style>
    body{background:linear-gradient(135deg,#667eea,#764ba2);color:white;font-family:Arial;padding:20px}
    .container{max-width:800px;margin:0 auto;background:rgba(255,255,255,0.1);padding:30px;border-radius:15px}
    a{color:#87CEEB;text-decoration:none;background:rgba(135,206,235,0.3);padding:10px 20px;border-radius:5px;margin:5px;display:inline-block}
    a:hover{background:rgba(135,206,235,0.6);transform:scale(1.05)}
    </style></head>
    <body><div class="container">
    <h1>🚀 MENTALIA Enterprise Platform</h1>
    <p>✅ Sistema funcionando - Puerto 5001</p>
    <h2>🤖 87 Agentes IA Disponibles:</h2>
    <ul>
        <li>🏥 Agenda Clínica Interoperable</li>
        <li>⚖️ Despacho Legal Mental-IA</li>
        <li>🎓 Formación Laboral Mental-IA</li>
        <li>👶 APP SIMÓN</li>
        <li>💙 BLU Modulación Emocional</li>
    </ul>
    <div>
        <a href="/status">🔧 Ver Status API</a>
        <a href="/agentes">🤖 Lista Completa</a>
        <a href="http://localhost:3000" target="_blank">📊 Centro Control</a>
    </div>
    </div></body></html>
    '''

@app.route('/status')
def status():
    return {"status": "OK", "puerto": "5001", "agentes": 87}

@app.route('/agentes')
def agentes():
    return '<h1>🤖 87 Agentes IA</h1><p><a href="/">← Volver</a></p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
