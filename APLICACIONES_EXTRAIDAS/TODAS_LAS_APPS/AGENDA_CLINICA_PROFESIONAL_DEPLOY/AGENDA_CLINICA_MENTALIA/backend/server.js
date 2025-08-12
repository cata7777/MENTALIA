const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 5003;
const JWT_SECRET = 'agenda_clinica_nd_secret_key_2025_super_secure';

// Middleware
app.use(express.json());
app.use(cors({
    origin: ['http://localhost:5173', 'http://localhost:3000', 'http://127.0.0.1:5173'],
    credentials: true
}));

// Configurar directorio de base de datos
const dbDir = path.join(__dirname, 'database');
if (!fs.existsSync(dbDir)) {
    fs.mkdirSync(dbDir, { recursive: true });
}

// Configurar base de datos SQLite (Hyperfoco)
const dbPath = path.join(dbDir, 'hyperfoco_agenda_clinica.db');
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('❌ Error conectando a Hyperfoco:', err.message);
    } else {
        console.log('✅ Agenda Clínica conectada a Hyperfoco - Base de datos central');
    }
});

// Crear tablas si no existen
db.serialize(() => {
    // Tabla de centros médicos
    db.run(`CREATE TABLE IF NOT EXISTS centros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        razon_social TEXT,
        rut TEXT UNIQUE,
        direccion TEXT,
        telefono TEXT,
        email TEXT,
        tipo_centro TEXT DEFAULT 'privado',
        especialidades TEXT,
        certificacion_nd BOOLEAN DEFAULT 0,
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
    )`);

    // Tabla de profesionales
    db.run(`CREATE TABLE IF NOT EXISTS profesionales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT,
        telefono TEXT,
        rut TEXT UNIQUE,
        especialidad TEXT NOT NULL,
        registro_profesional TEXT,
        titulo_profesional TEXT,
        universidad TEXT,
        certificacion_nd BOOLEAN DEFAULT 0,
        especialidades_nd TEXT,
        centro_id INTEGER,
        activo BOOLEAN DEFAULT 1,
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (centro_id) REFERENCES centros (id)
    )`);

    // Tabla de pacientes
    db.run(`CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        email TEXT,
        telefono TEXT,
        rut TEXT UNIQUE,
        fecha_nacimiento DATE,
        neurotipo_principal TEXT,
        neurotipos_secundarios TEXT,
        perfil_nd_id TEXT,
        prevision TEXT,
        numero_prevision TEXT,
        contacto_emergencia TEXT,
        telefono_emergencia TEXT,
        observaciones TEXT,
        activo BOOLEAN DEFAULT 1,
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
    )`);

    // Tabla de citas
    db.run(`CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER NOT NULL,
        profesional_id INTEGER NOT NULL,
        centro_id INTEGER NOT NULL,
        fecha_hora DATETIME NOT NULL,
        duracion_minutos INTEGER DEFAULT 60,
        tipo_cita TEXT NOT NULL,
        modalidad TEXT DEFAULT 'presencial',
        estado TEXT DEFAULT 'programada',
        motivo_consulta TEXT,
        observaciones TEXT,
        valor_sesion DECIMAL(10,2),
        pagada BOOLEAN DEFAULT 0,
        numero_boleta TEXT,
        fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
        fecha_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (paciente_id) REFERENCES pacientes (id),
        FOREIGN KEY (profesional_id) REFERENCES profesionales (id),
        FOREIGN KEY (centro_id) REFERENCES centros (id)
    )`);

    // Tabla de fichas clínicas
    db.run(`CREATE TABLE IF NOT EXISTS fichas_clinicas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER NOT NULL,
        profesional_id INTEGER NOT NULL,
        cita_id INTEGER,
        fecha_sesion DATETIME NOT NULL,
        tipo_sesion TEXT NOT NULL,
        objetivos TEXT,
        actividades_realizadas TEXT,
        observaciones_sesion TEXT,
        estado_emocional TEXT,
        avances TEXT,
        tareas_casa TEXT,
        proximos_pasos TEXT,
        fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (paciente_id) REFERENCES pacientes (id),
        FOREIGN KEY (profesional_id) REFERENCES profesionales (id),
        FOREIGN KEY (cita_id) REFERENCES citas (id)
    )`);

    // Tabla de disponibilidad
    db.run(`CREATE TABLE IF NOT EXISTS disponibilidad (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        profesional_id INTEGER NOT NULL,
        dia_semana INTEGER NOT NULL,
        hora_inicio TIME NOT NULL,
        hora_fin TIME NOT NULL,
        activo BOOLEAN DEFAULT 1,
        fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (profesional_id) REFERENCES profesionales (id)
    )`);

    // Tabla de boletas
    db.run(`CREATE TABLE IF NOT EXISTS boletas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_boleta TEXT UNIQUE NOT NULL,
        paciente_id INTEGER NOT NULL,
        profesional_id INTEGER NOT NULL,
        cita_id INTEGER,
        monto DECIMAL(10,2) NOT NULL,
        fecha_emision DATETIME DEFAULT CURRENT_TIMESTAMP,
        estado_pago TEXT DEFAULT 'pendiente',
        metodo_pago TEXT,
        fecha_pago DATETIME,
        observaciones TEXT,
        FOREIGN KEY (paciente_id) REFERENCES pacientes (id),
        FOREIGN KEY (profesional_id) REFERENCES profesionales (id),
        FOREIGN KEY (cita_id) REFERENCES citas (id)
    )`);

    console.log('✅ Tablas de Agenda Clínica inicializadas en Hyperfoco');

    // Insertar datos de ejemplo
    insertarDatosEjemplo();
});

function insertarDatosEjemplo() {
    // Verificar si ya existen datos
    db.get('SELECT COUNT(*) as count FROM centros', (err, row) => {
        if (err) {
            console.error('Error verificando datos:', err);
            return;
        }

        if (row.count === 0) {
            console.log('🔄 Inicializando datos de ejemplo...');

            // Insertar centro de ejemplo
            db.run(`INSERT INTO centros (nombre, razon_social, rut, direccion, telefono, email, tipo_centro, especialidades, certificacion_nd) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`,
                ['Centro Neurodivergente Santiago', 'Centro ND SpA', '76.123.456-7', 
                 'Av. Providencia 1234, Santiago', '+56 2 2345 6789', 'contacto@centrond.cl',
                 'privado', JSON.stringify(['Psicología Clínica ND', 'Terapia Ocupacional', 'Fonoaudiología']), 1],
                function(err) {
                    if (err) {
                        console.error('Error insertando centro:', err);
                        return;
                    }

                    const centroId = this.lastID;

                    // Insertar profesional de ejemplo
                    bcrypt.hash('password123', 10, (err, hash) => {
                        if (err) {
                            console.error('Error hasheando contraseña:', err);
                            return;
                        }

                        db.run(`INSERT INTO profesionales (nombre, apellido, email, password_hash, telefono, rut, especialidad, registro_profesional, titulo_profesional, universidad, certificacion_nd, especialidades_nd, centro_id) 
                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
                            ['María', 'González', 'maria.gonzalez@centrond.cl', hash, '+56 9 8765 4321',
                             '12.345.678-9', 'Psicología Clínica ND', 'PS12345', 'Psicóloga Clínica',
                             'Universidad de Chile', 1, JSON.stringify(['TEA', 'TDAH', 'Dislexia']), centroId],
                            function(err) {
                                if (err) {
                                    console.error('Error insertando profesional:', err);
                                    return;
                                }

                                const profesionalId = this.lastID;

                                // Insertar pacientes de ejemplo
                                const pacientes = [
                                    ['Alex', 'Rivera', 'alex.rivera@email.com', '+56 9 1234 5678', '19.876.543-2', 'TEA', JSON.stringify(['TDAH']), 'PND001', 'FONASA', 'A12345678'],
                                    ['María José', 'Silva', 'mj.silva@email.com', '+56 9 8765 4321', '18.765.432-1', 'TDAH', null, 'PND002', 'ISAPRE', 'I87654321'],
                                    ['Diego', 'Morales', 'diego.morales@email.com', '+56 9 5555 1234', '20.123.456-8', 'TEA', null, 'PND003', 'FONASA', 'B98765432']
                                ];

                                pacientes.forEach(paciente => {
                                    db.run(`INSERT INTO pacientes (nombre, apellido, email, telefono, rut, neurotipo_principal, neurotipos_secundarios, perfil_nd_id, prevision, numero_prevision) 
                                             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`, paciente);
                                });

                                console.log('✅ Datos de ejemplo creados exitosamente');
                            });
                    });
                });
        }
    });
}

// Middleware de autenticación
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];

    if (!token) {
        return res.status(401).json({ error: 'Token de acceso requerido' });
    }

    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) {
            return res.status(403).json({ error: 'Token inválido' });
        }
        req.user = user;
        next();
    });
};

// Rutas de autenticación
app.post('/api/auth/login', async (req, res) => {
    try {
        const { email, password } = req.body;

        if (!email || !password) {
            return res.status(400).json({ error: 'Email y contraseña son requeridos' });
        }

        db.get(
            'SELECT * FROM profesionales WHERE email = ? AND activo = 1',
            [email],
            async (err, profesional) => {
                if (err) {
                    return res.status(500).json({ error: 'Error en la base de datos' });
                }

                if (!profesional) {
                    return res.status(401).json({ error: 'Credenciales inválidas' });
                }

                const validPassword = await bcrypt.compare(password, profesional.password_hash);
                if (!validPassword) {
                    return res.status(401).json({ error: 'Credenciales inválidas' });
                }

                const token = jwt.sign(
                    { userId: profesional.id, email: profesional.email, tipo: 'profesional' },
                    JWT_SECRET,
                    { expiresIn: '24h' }
                );

                res.json({
                    message: 'Login exitoso en Agenda Clínica ND',
                    token: token,
                    user: {
                        id: profesional.id,
                        email: profesional.email,
                        nombre: profesional.nombre,
                        apellido: profesional.apellido,
                        especialidad: profesional.especialidad,
                        tipo: 'profesional'
                    }
                });
            }
        );
    } catch (error) {
        res.status(500).json({ error: 'Error interno del servidor' });
    }
});

// Rutas de pacientes
app.get('/api/pacientes', authenticateToken, (req, res) => {
    db.all(
        'SELECT * FROM pacientes WHERE activo = 1 ORDER BY apellido, nombre',
        (err, pacientes) => {
            if (err) {
                return res.status(500).json({ error: 'Error obteniendo pacientes' });
            }

            res.json({ 
                pacientes: pacientes.map(p => ({
                    ...p,
                    neurotipos_secundarios: p.neurotipos_secundarios ? JSON.parse(p.neurotipos_secundarios) : []
                }))
            });
        }
    );
});

app.post('/api/pacientes', authenticateToken, (req, res) => {
    const { nombre, apellido, email, telefono, rut, fecha_nacimiento, neurotipo_principal, neurotipos_secundarios, prevision, numero_prevision, contacto_emergencia, telefono_emergencia, observaciones } = req.body;

    if (!nombre || !apellido || !rut) {
        return res.status(400).json({ error: 'Nombre, apellido y RUT son requeridos' });
    }

    db.run(
        `INSERT INTO pacientes (nombre, apellido, email, telefono, rut, fecha_nacimiento, neurotipo_principal, neurotipos_secundarios, prevision, numero_prevision, contacto_emergencia, telefono_emergencia, observaciones) 
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
        [nombre, apellido, email, telefono, rut, fecha_nacimiento, neurotipo_principal, 
         neurotipos_secundarios ? JSON.stringify(neurotipos_secundarios) : null,
         prevision, numero_prevision, contacto_emergencia, telefono_emergencia, observaciones],
        function(err) {
            if (err) {
                if (err.message.includes('UNIQUE constraint failed')) {
                    return res.status(400).json({ error: 'Ya existe un paciente con ese RUT' });
                }
                return res.status(500).json({ error: 'Error creando paciente' });
            }

            res.status(201).json({
                message: 'Paciente creado exitosamente',
                paciente_id: this.lastID
            });
        }
    );
});

// Rutas de citas
app.get('/api/citas', authenticateToken, (req, res) => {
    const { fecha_inicio, fecha_fin, paciente_id, estado } = req.query;

    let query = `
        SELECT c.*, p.nombre as paciente_nombre, p.apellido as paciente_apellido, 
               pr.nombre as profesional_nombre, pr.apellido as profesional_apellido,
               ce.nombre as centro_nombre
        FROM citas c
        JOIN pacientes p ON c.paciente_id = p.id
        JOIN profesionales pr ON c.profesional_id = pr.id
        JOIN centros ce ON c.centro_id = ce.id
        WHERE 1=1
    `;
    
    const params = [];

    if (fecha_inicio) {
        query += ' AND DATE(c.fecha_hora) >= ?';
        params.push(fecha_inicio);
    }

    if (fecha_fin) {
        query += ' AND DATE(c.fecha_hora) <= ?';
        params.push(fecha_fin);
    }

    if (paciente_id) {
        query += ' AND c.paciente_id = ?';
        params.push(paciente_id);
    }

    if (estado) {
        query += ' AND c.estado = ?';
        params.push(estado);
    }

    query += ' ORDER BY c.fecha_hora DESC';

    db.all(query, params, (err, citas) => {
        if (err) {
            return res.status(500).json({ error: 'Error obteniendo citas' });
        }

        res.json({ citas });
    });
});

app.post('/api/citas', authenticateToken, (req, res) => {
    const { paciente_id, profesional_id, centro_id, fecha_hora, duracion_minutos, tipo_cita, modalidad, motivo_consulta, valor_sesion } = req.body;

    if (!paciente_id || !profesional_id || !centro_id || !fecha_hora || !tipo_cita) {
        return res.status(400).json({ error: 'Paciente, profesional, centro, fecha/hora y tipo de cita son requeridos' });
    }

    db.run(
        `INSERT INTO citas (paciente_id, profesional_id, centro_id, fecha_hora, duracion_minutos, tipo_cita, modalidad, motivo_consulta, valor_sesion) 
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`,
        [paciente_id, profesional_id, centro_id, fecha_hora, duracion_minutos || 60, tipo_cita, modalidad || 'presencial', motivo_consulta, valor_sesion],
        function(err) {
            if (err) {
                return res.status(500).json({ error: 'Error creando cita' });
            }

            res.status(201).json({
                message: 'Cita agendada exitosamente',
                cita_id: this.lastID
            });
        }
    );
});

// Rutas de boletas
app.get('/api/boletas', authenticateToken, (req, res) => {
    const { paciente_id, estado_pago } = req.query;

    let query = `
        SELECT b.*, p.nombre as paciente_nombre, p.apellido as paciente_apellido, p.rut as paciente_rut,
               pr.nombre as profesional_nombre, pr.apellido as profesional_apellido
        FROM boletas b
        JOIN pacientes p ON b.paciente_id = p.id
        JOIN profesionales pr ON b.profesional_id = pr.id
        WHERE 1=1
    `;
    
    const params = [];

    if (paciente_id) {
        query += ' AND b.paciente_id = ?';
        params.push(paciente_id);
    }

    if (estado_pago) {
        query += ' AND b.estado_pago = ?';
        params.push(estado_pago);
    }

    query += ' ORDER BY b.fecha_emision DESC';

    db.all(query, params, (err, boletas) => {
        if (err) {
            return res.status(500).json({ error: 'Error obteniendo boletas' });
        }

        res.json({ boletas });
    });
});

app.post('/api/boletas', authenticateToken, (req, res) => {
    const { paciente_id, profesional_id, cita_id, monto, observaciones } = req.body;

    if (!paciente_id || !profesional_id || !monto) {
        return res.status(400).json({ error: 'Paciente, profesional y monto son requeridos' });
    }

    // Generar número de boleta único
    const numero_boleta = `BOL-${Date.now()}-${Math.floor(Math.random() * 1000)}`;

    db.run(
        'INSERT INTO boletas (numero_boleta, paciente_id, profesional_id, cita_id, monto, observaciones) VALUES (?, ?, ?, ?, ?, ?)',
        [numero_boleta, paciente_id, profesional_id, cita_id, monto, observaciones],
        function(err) {
            if (err) {
                return res.status(500).json({ error: 'Error generando boleta' });
            }

            res.status(201).json({
                message: 'Boleta generada exitosamente',
                boleta_id: this.lastID,
                numero_boleta: numero_boleta
            });
        }
    );
});

// Ruta de salud
app.get('/api/health', (req, res) => {
    res.json({
        status: 'OK',
        service: 'Agenda Clínica Interoperable ND - Backend JavaScript',
        version: '2.0.0',
        database: 'Hyperfoco (SQLite)',
        timestamp: new Date().toISOString(),
        endpoints: {
            auth: ['/api/auth/login'],
            pacientes: ['/api/pacientes'],
            citas: ['/api/citas'],
            boletas: ['/api/boletas'],
            profesionales: ['/api/profesionales'],
            centros: ['/api/centros']
        },
        features: [
            'Gestión de Pacientes ND',
            'Agendamiento Inteligente',
            'Boletas Automáticas',
            'Fichas Clínicas',
            'Interoperabilidad',
            'Integración Hyperfoco'
        ]
    });
});

// Servir archivos estáticos del frontend
app.use(express.static(path.join(__dirname, 'static')));

// Manejo de errores
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Error interno del servidor' });
});

// Iniciar servidor
app.listen(PORT, '0.0.0.0', () => {
    console.log('🏥 Agenda Clínica Interoperable ND - Backend JavaScript INICIADO');
    console.log(`📡 API disponible en: http://localhost:${PORT}/api`);
    console.log(`🌐 Frontend disponible en: http://localhost:${PORT}`);
    console.log(`📋 Documentación API: http://localhost:${PORT}/api/health`);
    console.log('✅ MIGRADO DE PYTHON A JAVASCRIPT - CONFORME CON FAVI 2026');
    console.log('🏥 Sistema de gestión clínica neurodivergente con interoperabilidad');
});

// Manejo de cierre graceful
process.on('SIGINT', () => {
    console.log('\n🔄 Cerrando Agenda Clínica...');
    db.close((err) => {
        if (err) {
            console.error('❌ Error cerrando base de datos:', err.message);
        } else {
            console.log('✅ Conexión a Hyperfoco cerrada');
        }
        process.exit(0);
    });
});

