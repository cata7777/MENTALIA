-- Crear schemas para cada módulo en la DB única (LAB)

CREATE SCHEMA IF NOT EXISTS auth;
CREATE SCHEMA IF NOT EXISTS oraculo;
CREATE SCHEMA IF NOT EXISTS salud;
CREATE SCHEMA IF NOT EXISTS legal;
CREATE SCHEMA IF NOT EXISTS educacion;
CREATE SCHEMA IF NOT EXISTS kehilá;
CREATE SCHEMA IF NOT EXISTS adnnd;
CREATE SCHEMA IF NOT EXISTS simon;
CREATE SCHEMA IF NOT EXISTS common;

-- Tablas básicas de auth
CREATE TABLE IF NOT EXISTS auth.users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Tabla básica de oraculo
CREATE TABLE IF NOT EXISTS oraculo.readings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES auth.users(id),
    question TEXT NOT NULL,
    response TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tabla básica de salud
CREATE TABLE IF NOT EXISTS salud.appointments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES auth.users(id),
    doctor_name VARCHAR(255),
    appointment_date TIMESTAMP,
    status VARCHAR(50) DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tabla básica de legal
CREATE TABLE IF NOT EXISTS legal.documents (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES auth.users(id),
    document_type VARCHAR(100),
    content TEXT,
    signed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Usuario demo
INSERT INTO auth.users (email, password_hash, role) 
VALUES ('demo@mentalia.ai', '$2b$12$demo_hash_here', 'admin')
ON CONFLICT (email) DO NOTHING;

-- Datos demo
INSERT INTO oraculo.readings (user_id, question, response) 
VALUES (1, '¿Cuál es mi propósito?', 'Tu propósito es crear soluciones innovadoras')
ON CONFLICT DO NOTHING;

INSERT INTO salud.appointments (user_id, doctor_name, appointment_date) 
VALUES (1, 'Dr. Demo', NOW() + INTERVAL '1 day')
ON CONFLICT DO NOTHING;

INSERT INTO legal.documents (user_id, document_type, content) 
VALUES (1, 'Contrato Demo', 'Contenido del contrato de demostración')
ON CONFLICT DO NOTHING;
