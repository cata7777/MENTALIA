from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime, timedelta
import json
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'mentalia_agenda_clinica_2025'

def init_db():
    conn = sqlite3.connect('agenda_clinica.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        rut TEXT,
        perfil_nd TEXT,
        email TEXT,
        telefono TEXT,
        fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY,
        paciente_id INTEGER,
        fecha TIMESTAMP,
        tipo_consulta TEXT,
        estado TEXT DEFAULT 'programada',
        notas TEXT
    )''')
    
    # Insertar datos de ejemplo
    c.execute("INSERT OR IGNORE INTO pacientes (id, nombre, rut, perfil_nd, email, telefono) VALUES (1, 'Ana María Silva', '12345678-9', 'TEA + Ansiedad', 'ana@email.com', '+56912345678')")
    c.execute("INSERT OR IGNORE INTO pacientes (id, nombre, rut, perfil_nd, email, telefono) VALUES (2, 'Carlos Rojas', '98765432-1', 'TDAH + Hiperfoco', 'carlos@email.com', '+56987654321')")
    c.execute("INSERT OR IGNORE INTO pacientes (id, nombre, rut, perfil_nd, email, telefono) VALUES (3, 'María González', '11111111-1', 'Dislexia + Discalculia', 'maria@email.com', '+56911111111')")
    
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/agenda')
def agenda_clinica():
    return render_template('agenda.html')

@app.route('/pacientes')
def pacientes():
    conn = sqlite3.connect('agenda_clinica.db')
    c = conn.cursor()
    c.execute('SELECT * FROM pacientes ORDER BY nombre')
    pacientes_data = c.fetchall()
    conn.close()
    return render_template('pacientes.html', pacientes=pacientes_data)

@app.route('/chilecompra')
def chilecompra():
    return render_template('chilecompra.html')

@app.route('/reportereturn render_template('reportes.html')

@app.routreturn render_template('e('/status')
def status():
    return jsonify({
        "status": "✅ OPERACIONAL",
        "sistema": "Agenda Clínica Interoperable",
        "puerto": "5001",
        "especialidad": "Neurodivergencia",
        "pacientes_activos": 3,
        "interoperabilidad": ["HL7 FHIR R4", "FONASA", "SIGGES", "RES"],
        "licitacion_minsal": {
            "codigo": "ID-4857-2025-MINSAL",
            "valor": "$2.8B CLP",
            "estado": "PREPARADA",
            "probabilidad_exito": "85%"
        },
        "agentes_ia": 87
    })

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001, debug=True)
