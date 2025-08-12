# 🗄️ MODELO DE DATOS - MENTALIA LAB

## 📊 Esquema General (Postgres + Schemas)

### **Base de Datos Única**: `mentalia_lab`
**Schemas por Módulo**: `auth`, `oraculo`, `salud`, `legal`, `educacion`, `kehilá`, `adnnd`, `simon`, `common`

---

## 🔐 Schema: auth

### **users**
```sql
CREATE TABLE auth.users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    profile JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### **sessions**
```sql
CREATE TABLE auth.sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER REFERENCES auth.users(id),
    token_hash VARCHAR(255) NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🔮 Schema: oraculo

### **readings**
```sql
CREATE TABLE oraculo.readings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER REFERENCES auth.users(id),
    question TEXT NOT NULL,
    cards JSONB DEFAULT '[]',
    interpretation TEXT,
    ritual_suggested TEXT,
    emotional_state VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);
```

### **journal_entries**
```sql
CREATE TABLE oraculo.journal_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    reading_id UUID REFERENCES oraculo.readings(id),
    user_id INTEGER REFERENCES auth.users(id),
    content TEXT NOT NULL,
    tags JSONB DEFAULT '[]',
    mood_before INTEGER CHECK (mood_before BETWEEN 1 AND 10),
    mood_after INTEGER CHECK (mood_after BETWEEN 1 AND 10),
    created_at TIMESTAMP DEFAULT NOW()
);
```

### **card_meanings**
```sql
CREATE TABLE oraculo.card_meanings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    keywords JSONB DEFAULT '[]',
    symbolism TEXT,
    upright_meaning TEXT,
    reversed_meaning TEXT
);
```

---

## 🏥 Schema: salud

### **appointments**
```sql
CREATE TABLE salud.appointments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER REFERENCES auth.users(id),
    doctor_name VARCHAR(255),
    specialty VARCHAR(100),
    appointment_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER DEFAULT 60,
    status VARCHAR(50) DEFAULT 'scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### **patients**
```sql
CREATE TABLE salud.patients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER REFERENCES auth.users(id),
    medical_record_number VARCHAR(50) UNIQUE,
    emergency_contact JSONB DEFAULT '{}',
    medical_history JSONB DEFAULT '{}',
    consent_forms JSONB DEFAULT '[]',
    created_at TIMESTAMP DEFAULT NOW()
);
```

### **consultations**
```sql
CREATE TABLE salud.consultations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    appointment_id UUID REFERENCES salud.appointments(id),
    patient_id UUID REFERENCES salud.patients(id),
    diagnosis TEXT,
    treatment_plan TEXT,
    follow_up_date TIMESTAMP,
    agent_handoffs JSONB DEFAULT '[]',
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## ⚖️ Schema: legal

### **documents**
```sql
CREATE TABLE legal.documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER REFERENCES auth.users(id),
    document_type VARCHAR(100) NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    template_used VARCHAR(100),
    signed BOOLEAN DEFAULT FALSE,
    signature_data JSONB DEFAULT '{}',
    chilecompra_ref VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);
```

### **contracts**
```sql
CREATE TABLE legal.contracts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID REFERENCES legal.documents(id),
    parties JSONB DEFAULT '[]',
    terms JSONB DEFAULT '{}',
    effective_date DATE,
    expiration_date DATE,
    auto_renewal BOOLEAN DEFAULT FALSE,
    status VARCHAR(50) DEFAULT 'draft'
);
```

### **tenders**
```sql
CREATE TABLE legal.tenders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    chilecompra_id VARCHAR(100),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    budget_range JSONB DEFAULT '{}',
    submission_deadline TIMESTAMP,
    status VARCHAR(50) DEFAULT 'open',
    our_proposal JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 📚 Schema: educacion

### **courses**
```sql
CREATE TABLE educacion.courses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    provider VARCHAR(100), -- 'fai' o 'otec'
    duration_hours INTEGER,
    difficulty_level VARCHAR(50),
    content_modules JSONB DEFAULT '[]',
    certification_type VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);
```

### **enrollments**
```sql
CREATE TABLE educacion.enrollments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER REFERENCES auth.users(id),
    course_id UUID REFERENCES educacion.courses(id),
    enrolled_date TIMESTAMP DEFAULT NOW(),
    completion_date TIMESTAMP,
    progress_percentage INTEGER DEFAULT 0,
    current_module INTEGER DEFAULT 1,
    status VARCHAR(50) DEFAULT 'active'
);
```

### **certificates**
```sql
CREATE TABLE educacion.certificates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    enrollment_id UUID REFERENCES educacion.enrollments(id),
    certificate_number VARCHAR(100) UNIQUE,
    issued_date TIMESTAMP DEFAULT NOW(),
    blockchain_hash VARCHAR(255),
    verification_url TEXT
);
```

---

## 🕊️ Schema: kehilá

### **events**
```sql
CREATE TABLE kehilá.events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    event_type VARCHAR(100), -- 'shabbat', 'holiday', 'study', 'social'
    event_date TIMESTAMP NOT NULL,
    location VARCHAR(255),
    max_participants INTEGER,
    current_participants INTEGER DEFAULT 0,
    requirements JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW()
);
```

### **members**
```sql
CREATE TABLE kehilá.members (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER REFERENCES auth.users(id),
    hebrew_name VARCHAR(255),
    community_role VARCHAR(100),
    interests JSONB DEFAULT '[]',
    participation_level VARCHAR(50) DEFAULT 'member',
    joined_date TIMESTAMP DEFAULT NOW()
);
```

---

## 🧬 Schema: adnnd

### **assessments**
```sql
CREATE TABLE adnnd.assessments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER REFERENCES auth.users(id),
    assessment_type VARCHAR(100), -- 'initial', 'follow_up', 'periodic'
    responses JSONB NOT NULL,
    computed_profile JSONB DEFAULT '{}',
    recommendations JSONB DEFAULT '[]',
    completed_at TIMESTAMP DEFAULT NOW()
);
```

### **profiles**
```sql
CREATE TABLE adnnd.profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER REFERENCES auth.users(id),
    neurodivergence_types JSONB DEFAULT '[]', -- ['adhd', 'autism', 'dyslexia']
    strengths JSONB DEFAULT '[]',
    challenges JSONB DEFAULT '[]',
    accommodations JSONB DEFAULT '[]',
    last_updated TIMESTAMP DEFAULT NOW()
);
```

---

## 👶 Schema: simon

### **children**
```sql
CREATE TABLE simon.children (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER REFERENCES auth.users(id), -- parent/guardian
    name VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL,
    developmental_goals JSONB DEFAULT '[]',
    current_level JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW()
);
```

### **games**
```sql
CREATE TABLE simon.games (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    child_id UUID REFERENCES simon.children(id),
    game_type VARCHAR(100), -- 'memory', 'phonetics', 'habits'
    difficulty_level INTEGER DEFAULT 1,
    score INTEGER,
    duration_seconds INTEGER,
    completed BOOLEAN DEFAULT FALSE,
    played_at TIMESTAMP DEFAULT NOW()
);
```

### **habits**
```sql
CREATE TABLE simon.habits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    child_id UUID REFERENCES simon.children(id),
    habit_name VARCHAR(255) NOT NULL,
    frequency_goal VARCHAR(50), -- 'daily', 'weekly'
    current_streak INTEGER DEFAULT 0,
    rewards_earned INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🔄 Schema: common

### **events_log**
```sql
CREATE TABLE common.events_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_type VARCHAR(255) NOT NULL,
    event_data JSONB NOT NULL,
    user_id INTEGER,
    source_service VARCHAR(100),
    correlation_id UUID,
    processed_at TIMESTAMP DEFAULT NOW()
);
```

### **notifications**
```sql
CREATE TABLE common.notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER REFERENCES auth.users(id),
    type VARCHAR(100) NOT NULL,
    title VARCHAR(255) NOT NULL,
    message TEXT,
    read BOOLEAN DEFAULT FALSE,
    action_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🌱 Seeds Mínimos

### **Demo User**
```sql
INSERT INTO auth.users (email, password_hash, role, profile) VALUES 
('demo@mentalia.ai', '$2b$12$demo_hash_change_in_prod', 'admin', 
 '{"name": "Usuario Demo", "preferences": {"theme": "light", "language": "es"}}');
```

### **Oráculo Demo**
```sql
INSERT INTO oraculo.readings (user_id, question, interpretation, ritual_suggested) VALUES 
(1, '¿Cuál es mi propósito?', 'Tu alma busca crear conexiones auténticas...', 
 'Enciende una vela blanca y medita 10 minutos al amanecer');
```

### **Cita Demo**
```sql
INSERT INTO salud.appointments (user_id, doctor_name, specialty, appointment_date) VALUES 
(1, 'Dr. Demo Salud', 'Psicología', NOW() + INTERVAL '1 day');
```

### **Documento Demo**
```sql
INSERT INTO legal.documents (user_id, document_type, title, content) VALUES 
(1, 'Contrato', 'Contrato de Servicios Demo', 'Contenido del contrato...');
```

---

**Este modelo soporta la fase LAB con schemas separados, manteniendo la flexibilidad para migrar a DBs independientes.** 🗄️
