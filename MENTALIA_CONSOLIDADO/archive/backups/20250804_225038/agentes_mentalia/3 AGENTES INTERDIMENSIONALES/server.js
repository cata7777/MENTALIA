const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 5002;
const JWT_SECRET = 'blu_terapia_nd_secret_key_2025_super_secure';

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
const dbPath = path.join(dbDir, 'hyperfoco_blu_terapia.db');
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('❌ Error conectando a Hyperfoco:', err.message);
    } else {
        console.log('✅ BLU conectada a Hyperfoco - Base de datos central');
    }
});

// Crear tablas si no existen
db.serialize(() => {
    // Tabla de usuarios
    db.run(`CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
        activo BOOLEAN DEFAULT 1
    )`);

    // Tabla de sesiones terapéuticas
    db.run(`CREATE TABLE IF NOT EXISTS sesiones_terapia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        tipo_sesion TEXT NOT NULL,
        estado_emocional_inicial TEXT,
        estado_emocional_final TEXT,
        duracion_minutos INTEGER,
        notas TEXT,
        fecha_sesion DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )`);

    // Tabla de conversaciones con BLU
    db.run(`CREATE TABLE IF NOT EXISTS conversaciones_blu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        sesion_id INTEGER,
        mensaje_usuario TEXT NOT NULL,
        respuesta_blu TEXT NOT NULL,
        emocion_detectada TEXT,
        estrategia_aplicada TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
        FOREIGN KEY (sesion_id) REFERENCES sesiones_terapia (id)
    )`);

    // Tabla de modulaciones emocionales
    db.run(`CREATE TABLE IF NOT EXISTS modulaciones_emocionales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        emocion_origen TEXT NOT NULL,
        emocion_objetivo TEXT NOT NULL,
        tecnica_utilizada TEXT NOT NULL,
        efectividad INTEGER DEFAULT 1,
        notas TEXT,
        fecha_modulacion DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )`);

    // Tabla de estrategias personalizadas
    db.run(`CREATE TABLE IF NOT EXISTS estrategias_personalizadas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        categoria TEXT NOT NULL,
        titulo TEXT NOT NULL,
        descripcion TEXT NOT NULL,
        efectividad INTEGER DEFAULT 1,
        frecuencia_uso INTEGER DEFAULT 0,
        fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )`);

    // Tabla de estados emocionales
    db.run(`CREATE TABLE IF NOT EXISTS estados_emocionales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        emocion_primaria TEXT NOT NULL,
        intensidad INTEGER NOT NULL,
        contexto TEXT,
        disparador TEXT,
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )`);

    console.log('✅ Tablas de BLU Terapia inicializadas en Hyperfoco');
});

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
app.post('/api/auth/register', async (req, res) => {
    try {
        const { email, password, nombre, apellido } = req.body;

        if (!email || !password || !nombre || !apellido) {
            return res.status(400).json({ error: 'Todos los campos son requeridos' });
        }

        // Verificar si el usuario ya existe
        db.get('SELECT id FROM usuarios WHERE email = ?', [email], async (err, row) => {
            if (err) {
                return res.status(500).json({ error: 'Error en la base de datos' });
            }

            if (row) {
                return res.status(400).json({ error: 'El usuario ya existe' });
            }

            // Hashear contraseña
            const passwordHash = await bcrypt.hash(password, 10);

            // Insertar usuario
            db.run(
                'INSERT INTO usuarios (email, password_hash, nombre, apellido) VALUES (?, ?, ?, ?)',
                [email, passwordHash, nombre, apellido],
                function(err) {
                    if (err) {
                        return res.status(500).json({ error: 'Error creando usuario' });
                    }

                    const token = jwt.sign(
                        { userId: this.lastID, email: email },
                        JWT_SECRET,
                        { expiresIn: '24h' }
                    );

                    res.status(201).json({
                        message: 'Usuario registrado exitosamente en BLU Terapia',
                        token: token,
                        user: {
                            id: this.lastID,
                            email: email,
                            nombre: nombre,
                            apellido: apellido
                        }
                    });
                }
            );
        });
    } catch (error) {
        res.status(500).json({ error: 'Error interno del servidor' });
    }
});

app.post('/api/auth/login', async (req, res) => {
    try {
        const { email, password } = req.body;

        if (!email || !password) {
            return res.status(400).json({ error: 'Email y contraseña son requeridos' });
        }

        db.get(
            'SELECT * FROM usuarios WHERE email = ? AND activo = 1',
            [email],
            async (err, user) => {
                if (err) {
                    return res.status(500).json({ error: 'Error en la base de datos' });
                }

                if (!user) {
                    return res.status(401).json({ error: 'Credenciales inválidas' });
                }

                const validPassword = await bcrypt.compare(password, user.password_hash);
                if (!validPassword) {
                    return res.status(401).json({ error: 'Credenciales inválidas' });
                }

                const token = jwt.sign(
                    { userId: user.id, email: user.email },
                    JWT_SECRET,
                    { expiresIn: '24h' }
                );

                res.json({
                    message: 'Bienvenido a BLU Terapia ND',
                    token: token,
                    user: {
                        id: user.id,
                        email: user.email,
                        nombre: user.nombre,
                        apellido: user.apellido
                    }
                });
            }
        );
    } catch (error) {
        res.status(500).json({ error: 'Error interno del servidor' });
    }
});

// Rutas de sesiones terapéuticas
app.post('/api/sesiones', authenticateToken, (req, res) => {
    const { tipo_sesion, estado_emocional_inicial } = req.body;

    if (!tipo_sesion) {
        return res.status(400).json({ error: 'Tipo de sesión es requerido' });
    }

    db.run(
        'INSERT INTO sesiones_terapia (usuario_id, tipo_sesion, estado_emocional_inicial) VALUES (?, ?, ?)',
        [req.user.userId, tipo_sesion, estado_emocional_inicial || null],
        function(err) {
            if (err) {
                return res.status(500).json({ error: 'Error creando sesión' });
            }

            res.status(201).json({
                message: 'Sesión iniciada exitosamente',
                sesion_id: this.lastID,
                tipo_sesion: tipo_sesion
            });
        }
    );
});

app.get('/api/sesiones', authenticateToken, (req, res) => {
    db.all(
        'SELECT * FROM sesiones_terapia WHERE usuario_id = ? ORDER BY fecha_sesion DESC LIMIT 20',
        [req.user.userId],
        (err, sesiones) => {
            if (err) {
                return res.status(500).json({ error: 'Error obteniendo sesiones' });
            }

            res.json({ sesiones });
        }
    );
});

// Rutas de conversaciones con BLU
app.post('/api/conversacion', authenticateToken, (req, res) => {
    const { mensaje_usuario, sesion_id } = req.body;

    if (!mensaje_usuario) {
        return res.status(400).json({ error: 'Mensaje es requerido' });
    }

    // Simulación de respuesta de BLU (aquí iría la lógica de IA)
    const respuestas_blu = [
        "Entiendo cómo te sientes. Es completamente válido experimentar esas emociones.",
        "¿Podrías contarme más sobre qué específicamente te está generando esa sensación?",
        "Vamos a trabajar juntos en estrategias que te ayuden a regular esa emoción.",
        "Recuerda que cada emoción tiene un propósito. ¿Qué crees que te está comunicando?",
        "Te propongo que probemos una técnica de respiración consciente. ¿Te parece?",
        "Es importante reconocer tus fortalezas neurodivergentes en este momento."
    ];

    const respuesta_blu = respuestas_blu[Math.floor(Math.random() * respuestas_blu.length)];
    const emocion_detectada = detectarEmocion(mensaje_usuario);

    db.run(
        'INSERT INTO conversaciones_blu (usuario_id, sesion_id, mensaje_usuario, respuesta_blu, emocion_detectada) VALUES (?, ?, ?, ?, ?)',
        [req.user.userId, sesion_id || null, mensaje_usuario, respuesta_blu, emocion_detectada],
        function(err) {
            if (err) {
                return res.status(500).json({ error: 'Error guardando conversación' });
            }

            res.json({
                respuesta_blu: respuesta_blu,
                emocion_detectada: emocion_detectada,
                conversacion_id: this.lastID
            });
        }
    );
});

// Función simple de detección de emociones (placeholder para IA más avanzada)
function detectarEmocion(mensaje) {
    const emociones = {
        'ansiedad': ['ansioso', 'nervioso', 'preocupado', 'estresado'],
        'tristeza': ['triste', 'deprimido', 'melancólico', 'desanimado'],
        'ira': ['enojado', 'furioso', 'molesto', 'irritado'],
        'alegría': ['feliz', 'contento', 'alegre', 'emocionado'],
        'miedo': ['miedo', 'temor', 'asustado', 'aterrado'],
        'calma': ['tranquilo', 'relajado', 'sereno', 'en paz']
    };

    const mensajeLower = mensaje.toLowerCase();
    
    for (const [emocion, palabras] of Object.entries(emociones)) {
        if (palabras.some(palabra => mensajeLower.includes(palabra))) {
            return emocion;
        }
    }
    
    return 'neutral';
}

// Rutas de modulaciones emocionales
app.post('/api/modulaciones', authenticateToken, (req, res) => {
    const { emocion_origen, emocion_objetivo, tecnica_utilizada, efectividad, notas } = req.body;

    if (!emocion_origen || !emocion_objetivo || !tecnica_utilizada) {
        return res.status(400).json({ error: 'Emoción origen, objetivo y técnica son requeridos' });
    }

    db.run(
        'INSERT INTO modulaciones_emocionales (usuario_id, emocion_origen, emocion_objetivo, tecnica_utilizada, efectividad, notas) VALUES (?, ?, ?, ?, ?, ?)',
        [req.user.userId, emocion_origen, emocion_objetivo, tecnica_utilizada, efectividad || 1, notas || null],
        function(err) {
            if (err) {
                return res.status(500).json({ error: 'Error guardando modulación' });
            }

            res.status(201).json({
                message: 'Modulación emocional registrada exitosamente',
                modulacion_id: this.lastID
            });
        }
    );
});

app.get('/api/modulaciones', authenticateToken, (req, res) => {
    db.all(
        'SELECT * FROM modulaciones_emocionales WHERE usuario_id = ? ORDER BY fecha_modulacion DESC',
        [req.user.userId],
        (err, modulaciones) => {
            if (err) {
                return res.status(500).json({ error: 'Error obteniendo modulaciones' });
            }

            res.json({ modulaciones });
        }
    );
});

// Rutas de estados emocionales
app.post('/api/estados', authenticateToken, (req, res) => {
    const { emocion_primaria, intensidad, contexto, disparador } = req.body;

    if (!emocion_primaria || !intensidad) {
        return res.status(400).json({ error: 'Emoción primaria e intensidad son requeridos' });
    }

    db.run(
        'INSERT INTO estados_emocionales (usuario_id, emocion_primaria, intensidad, contexto, disparador) VALUES (?, ?, ?, ?, ?)',
        [req.user.userId, emocion_primaria, intensidad, contexto || null, disparador || null],
        function(err) {
            if (err) {
                return res.status(500).json({ error: 'Error registrando estado emocional' });
            }

            res.status(201).json({
                message: 'Estado emocional registrado exitosamente',
                estado_id: this.lastID
            });
        }
    );
});

app.get('/api/estados', authenticateToken, (req, res) => {
    db.all(
        'SELECT * FROM estados_emocionales WHERE usuario_id = ? ORDER BY fecha_registro DESC LIMIT 50',
        [req.user.userId],
        (err, estados) => {
            if (err) {
                return res.status(500).json({ error: 'Error obteniendo estados emocionales' });
            }

            res.json({ estados });
        }
    );
});

// Ruta de salud
app.get('/api/health', (req, res) => {
    res.json({
        status: 'OK',
        service: 'BLU Terapia ND - Backend JavaScript',
        version: '2.0.0',
        database: 'Hyperfoco (SQLite)',
        timestamp: new Date().toISOString(),
        endpoints: {
            auth: ['/api/auth/register', '/api/auth/login'],
            sesiones: ['/api/sesiones'],
            conversacion: ['/api/conversacion'],
            modulaciones: ['/api/modulaciones'],
            estados: ['/api/estados']
        },
        features: [
            'IA Conversacional BLU',
            'Modulación Emocional',
            'Registro de Estados',
            'Sesiones Terapéuticas',
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
    console.log('🤖 BLU Terapia ND - Backend JavaScript INICIADO');
    console.log(`📡 API disponible en: http://localhost:${PORT}/api`);
    console.log(`🌐 Frontend disponible en: http://localhost:${PORT}`);
    console.log(`📋 Documentación API: http://localhost:${PORT}/api/health`);
    console.log('✅ MIGRADO DE PYTHON A JAVASCRIPT - CONFORME CON FAVI 2026');
    console.log('🧠 BLU IA Lista para terapia neurodivergente');
});

// Manejo de cierre graceful
process.on('SIGINT', () => {
    console.log('\n🔄 Cerrando BLU Terapia...');
    db.close((err) => {
        if (err) {
            console.error('❌ Error cerrando base de datos:', err.message);
        } else {
            console.log('✅ Conexión a Hyperfoco cerrada');
        }
        process.exit(0);
    });
});

