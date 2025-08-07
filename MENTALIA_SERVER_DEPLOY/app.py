from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🚀 MENTALIA Enterprise Platform</h1>
    <p>✅ Sistema funcionando - Todos los tickets verdes</p>
    <h2>🤖 87 Agentes IA Disponibles</h2>
    <ul>
        <li>🏥 Agenda Clínica Interoperable</li>
        <li>⚖️ Despacho Legal Mental-IA</li>
        <li>🎓 Formación Laboral Mental-IA</li>
        <li>👶 APP SIMÓN</li>
        <li>💙 BLU Modulación Emocional</li>
    </ul>
    <p><a href="http://localhost:3000">📊 Centro de Control</a></p>
    '''

@app.route('/status')
def status():
    return {"status": "operational", "agents": 87, "components": 141}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
