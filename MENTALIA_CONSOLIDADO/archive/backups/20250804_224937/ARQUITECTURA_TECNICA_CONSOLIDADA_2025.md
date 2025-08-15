# 🏗️ ARQUITECTURA TÉCNICA CONSOLIDADA MENTALIA
## Especificaciones de Implementación RunPod Unificada

---

## 📋 CONFIGURACIÓN RUNPOD OPTIMIZADA

### **Especificaciones de Hardware Recomendadas:**
```
INSTANCIA RUNPOD UNIFICADA
├── GPU: NVIDIA RTX 4090 24GB (o superior)
├── CPU: 16+ cores (AMD EPYC/Intel Xeon)
├── RAM: 64GB DDR4/DDR5
├── Storage: 1TB NVMe SSD
├── Network: 1Gbps simétrico
└── OS: Ubuntu 22.04 LTS
```

### **Justificación Técnica:**
- **GPU 24GB:** Ejecutar múltiples modelos IA simultáneamente sin swapping
- **16+ CPU Cores:** Manejar 500+ usuarios concurrentes
- **64GB RAM:** Cache de aplicaciones, sesiones, y modelos "calientes"
- **1TB NVMe:** Aplicación completa, DBs, logs, y espacio de crecimiento

---

## 🐳 DOCKER COMPOSE UNIFICADO

```yaml
version: '3.8'

services:
  # Proxy Reverso y Load Balancer
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - mentalia-app
    restart: unless-stopped

  # Aplicación Principal MENTALIA
  mentalia-app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://mentalia:${DB_PASSWORD}@postgres:5432/mentalia_unified
      - REDIS_URL=redis://redis:6379/0
      - JWT_SECRET_KEY=${JWT_SECRET}
      - OPENAI_API_KEY=${OPENAI_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_KEY}
    volumes:
      - ./models:/app/models
      - ./user_data:/app/user_data
      - ./logs:/app/logs
    depends_on:
      - postgres
      - redis
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    restart: unless-stopped

  # Base de Datos Principal
  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=mentalia_unified
      - POSTGRES_USER=mentalia
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./sql/init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"
    restart: unless-stopped

  # Cache y Sesiones
  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    restart: unless-stopped

  # Procesamiento Asíncrono
  celery:
    build:
      context: .
      dockerfile: Dockerfile
    command: celery -A app.celery worker --loglevel=info
    environment:
      - DATABASE_URL=postgresql://mentalia:${DB_PASSWORD}@postgres:5432/mentalia_unified
      - REDIS_URL=redis://redis:6379/0
    volumes:
      - ./models:/app/models
      - ./user_data:/app/user_data
    depends_on:
      - postgres
      - redis
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    restart: unless-stopped

  # Monitoreo y Métricas
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    restart: unless-stopped

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD}
    volumes:
      - grafana_data:/var/lib/grafana
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
  prometheus_data:
  grafana_data:
```

---

## 🗃️ ESQUEMA DE BASE DE DATOS UNIFICADA

```sql
-- ESQUEMA PRINCIPAL MENTALIA UNIFIED
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- USUARIOS Y AUTENTICACIÓN
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    profile_type VARCHAR(50) DEFAULT 'general', -- 'neurodivergent', 'professional', 'enterprise'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT true
);

-- PERFILES NEURODIVERGENTES
CREATE TABLE neurodivergent_profiles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    condition_type VARCHAR(100), -- 'autism', 'adhd', 'high_abilities', etc.
    communication_preferences JSONB,
    sensory_preferences JSONB,
    learning_style JSONB,
    accessibility_settings JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- APLICACIONES DEL ECOSISTEMA
CREATE TABLE applications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    category VARCHAR(100) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT true,
    config JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ACCESO DE USUARIOS A APLICACIONES
CREATE TABLE user_app_access (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    app_id UUID REFERENCES applications(id) ON DELETE CASCADE,
    access_level VARCHAR(50) DEFAULT 'basic', -- 'basic', 'premium', 'professional'
    granted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    UNIQUE(user_id, app_id)
);

-- BOTS ESPECIALIZADOS
CREATE TABLE bots (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    category VARCHAR(100) NOT NULL,
    specialty TEXT,
    personality_config JSONB,
    capabilities JSONB,
    model_config JSONB,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- CONVERSACIONES Y SESIONES
CREATE TABLE conversations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    bot_id UUID REFERENCES bots(id),
    app_context VARCHAR(100), -- Aplicación donde ocurre la conversación
    title VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- MENSAJES DE CONVERSACIONES
CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    conversation_id UUID REFERENCES conversations(id) ON DELETE CASCADE,
    sender_type VARCHAR(20) NOT NULL, -- 'user', 'bot'
    content TEXT NOT NULL,
    metadata JSONB, -- Información adicional (emociones, análisis, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ANÁLISIS MULTIMODAL
CREATE TABLE multimodal_analyses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    conversation_id UUID REFERENCES conversations(id),
    analysis_type VARCHAR(100), -- 'emotion', 'coherence', 'social_cues'
    input_data JSONB, -- Datos de entrada (texto, audio, video)
    results JSONB, -- Resultados del análisis
    confidence_score FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SESIONES DE ENTRENAMIENTO (Comunicación Social)
CREATE TABLE training_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    app_id UUID REFERENCES applications(id),
    session_type VARCHAR(100),
    objectives JSONB,
    results JSONB,
    progress_metrics JSONB,
    duration_minutes INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SERVICIOS PROFESIONALES (Despacho Legal)
CREATE TABLE legal_cases (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    case_type VARCHAR(100), -- 'civil', 'penal', 'laboral', etc.
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'active',
    assigned_ia VARCHAR(100), -- IA especializada asignada
    documents JSONB, -- Referencias a documentos del caso
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- MÉTRICAS Y ANALYTICS
CREATE TABLE user_metrics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    app_id UUID REFERENCES applications(id),
    metric_type VARCHAR(100),
    metric_value JSONB,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- CONFIGURACIONES GLOBALES
CREATE TABLE system_config (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    config_key VARCHAR(255) UNIQUE NOT NULL,
    config_value JSONB NOT NULL,
    description TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ÍNDICES PARA OPTIMIZACIÓN
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_conversations_user_id ON conversations(user_id);
CREATE INDEX idx_messages_conversation_id ON messages(conversation_id);
CREATE INDEX idx_user_app_access_user_id ON user_app_access(user_id);
CREATE INDEX idx_multimodal_analyses_user_id ON multimodal_analyses(user_id);
CREATE INDEX idx_training_sessions_user_id ON training_sessions(user_id);
CREATE INDEX idx_legal_cases_user_id ON legal_cases(user_id);
CREATE INDEX idx_user_metrics_user_app ON user_metrics(user_id, app_id);
```

---

## 🚀 ESTRUCTURA DE APLICACIÓN FLASK UNIFICADA

```python
# app/__init__.py - Aplicación Principal
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis

# Inicialización de extensiones
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
limiter = Limiter(key_func=get_remote_address)

def create_app(config_name='production'):
    app = Flask(__name__)
    
    # Configuración
    app.config.from_object(f'config.{config_name}')
    
    # Inicialización de extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    limiter.init_app(app)
    
    # Registro de Blueprints
    from app.core import bp as core_bp
    app.register_blueprint(core_bp, url_prefix='/api')
    
    from app.apps.hiperfoco import bp as hiperfoco_bp
    app.register_blueprint(hiperfoco_bp, url_prefix='/hiperfoco')
    
    from app.apps.universe import bp as universe_bp
    app.register_blueprint(universe_bp, url_prefix='/universe')
    
    from app.apps.chat import bp as chat_bp
    app.register_blueprint(chat_bp, url_prefix='/chat')
    
    from app.apps.sign_link import bp as sign_link_bp
    app.register_blueprint(sign_link_bp, url_prefix='/sign-link')
    
    from app.apps.comunicacion_social import bp as com_social_bp
    app.register_blueprint(com_social_bp, url_prefix='/comunicacion-social')
    
    from app.apps.spoiler_alert import bp as spoiler_bp
    app.register_blueprint(spoiler_bp, url_prefix='/spoiler-alert')
    
    from app.apps.despacho_legal import bp as legal_bp
    app.register_blueprint(legal_bp, url_prefix='/despacho-legal')
    
    return app

# Estructura de directorios
"""
app/
├── __init__.py                 # Aplicación principal
├── models/                     # Modelos de base de datos
│   ├── __init__.py
│   ├── user.py
│   ├── bot.py
│   ├── conversation.py
│   └── ...
├── core/                       # Funcionalidades centrales
│   ├── __init__.py
│   ├── auth.py                # Autenticación SSO
│   ├── multimodal.py          # Análisis multimodal
│   ├── ai_models.py           # Gestión de modelos IA
│   └── utils.py               # Utilidades compartidas
├── apps/                       # Aplicaciones específicas
│   ├── hiperfoco/             # Vitrina profesional
│   ├── universe/              # Hub de aplicaciones
│   ├── chat/                  # Sistema conversacional
│   ├── sign_link/             # Lengua de señas
│   ├── comunicacion_social/   # Entrenamiento social
│   ├── spoiler_alert/         # Detector vínculos
│   ├── despacho_legal/        # Servicios jurídicos
│   └── ...
├── bots/                       # Sistemas de bots
│   ├── __init__.py
│   ├── botmaker.py            # Fábrica de bots
│   ├── blu_psicologa.py       # Terapia especializada
│   ├── gerencia_ia.py         # Gestión empresarial
│   └── ...
├── frontend/                   # Interfaces generadas con Suna.so
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── templates/
│       ├── base.html
│       ├── hiperfoco/
│       ├── universe/
│       └── ...
└── tests/                      # Tests automatizados
    ├── unit/
    ├── integration/
    └── e2e/
"""
```

---

## 🔄 SISTEMA DE NAVEGACIÓN UNIFICADA

```javascript
// frontend/static/js/unified-navigation.js
class MentaliaNavigator {
    constructor() {
        this.currentApp = this.detectCurrentApp();
        this.user = null;
        this.initializeNavigation();
    }

    detectCurrentApp() {
        const path = window.location.pathname;
        if (path.startsWith('/hiperfoco')) return 'hiperfoco';
        if (path.startsWith('/universe')) return 'universe';
        if (path.startsWith('/chat')) return 'chat';
        if (path.startsWith('/sign-link')) return 'sign-link';
        if (path.startsWith('/comunicacion-social')) return 'comunicacion-social';
        if (path.startsWith('/spoiler-alert')) return 'spoiler-alert';
        if (path.startsWith('/despacho-legal')) return 'despacho-legal';
        return 'home';
    }

    initializeNavigation() {
        this.createUnifiedHeader();
        this.createAppSidebar();
        this.loadUserProfile();
        this.setupCrossAppCommunication();
    }

    createUnifiedHeader() {
        const header = document.createElement('header');
        header.className = 'mentalia-unified-header';
        header.innerHTML = `
            <nav class="navbar">
                <div class="nav-brand">
                    <img src="/static/img/mentalia-logo.svg" alt="MENTALIA">
                    <span class="current-app">${this.currentApp.toUpperCase()}</span>
                </div>
                <div class="nav-center">
                    <div class="app-quick-switcher">
                        <button class="app-btn" data-app="universe">🌌 Universe</button>
                        <button class="app-btn" data-app="chat">💬 Chat</button>
                        <button class="app-btn" data-app="hiperfoco">🏢 Hiperfoco</button>
                    </div>
                </div>
                <div class="nav-right">
                    <div class="user-menu">
                        <button class="user-avatar" id="user-menu-toggle">
                            <img src="/api/user/avatar" alt="Usuario">
                        </button>
                    </div>
                </div>
            </nav>
        `;
        document.body.insertBefore(header, document.body.firstChild);
    }

    createAppSidebar() {
        const sidebar = document.createElement('aside');
        sidebar.className = 'mentalia-app-sidebar';
        sidebar.innerHTML = `
            <div class="sidebar-content">
                <div class="app-categories">
                    <div class="category" data-category="salud-mental">
                        <h3>🧠 Salud Mental</h3>
                        <ul>
                            <li><a href="/comunicacion-social">Comunicación Social</a></li>
                            <li><a href="/spoiler-alert">Spoiler Alert</a></li>
                            <li><a href="/chat/blu-psicologa">BLU Psicóloga</a></li>
                        </ul>
                    </div>
                    <div class="category" data-category="inclusion">
                        <h3>🌐 Inclusión</h3>
                        <ul>
                            <li><a href="/sign-link">Sign-Link</a></li>
                            <li><a href="/universe/perfil-nd">Perfil ND</a></li>
                        </ul>
                    </div>
                    <div class="category" data-category="profesional">
                        <h3>⚖️ Servicios Profesionales</h3>
                        <ul>
                            <li><a href="/despacho-legal">Despacho Legal</a></li>
                            <li><a href="/chat/gerencia-ia">Gerencia IA</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        `;
        document.body.appendChild(sidebar);
    }

    async loadUserProfile() {
        try {
            const response = await fetch('/api/user/profile');
            this.user = await response.json();
            this.updateUIForUser();
        } catch (error) {
            console.error('Error loading user profile:', error);
        }
    }

    updateUIForUser() {
        if (this.user.profile_type === 'neurodivergent') {
            this.applyNeurodivergentAdaptations();
        }
        if (this.user.profile_type === 'professional') {
            this.showProfessionalTools();
        }
    }

    setupCrossAppCommunication() {
        // Sistema de comunicación entre aplicaciones
        window.addEventListener('mentalia-cross-app', (event) => {
            this.handleCrossAppMessage(event.detail);
        });
    }

    navigateToApp(appName, route = '') {
        window.location.href = `/${appName}${route}`;
    }
}

// Inicializar navegación unificada
document.addEventListener('DOMContentLoaded', () => {
    window.mentaliaNav = new MentaliaNavigator();
});
```

---

## 📊 SISTEMA DE MONITOREO UNIFICADO

```python
# app/core/monitoring.py
import time
import psutil
import GPUtil
from flask import request, g
from functools import wraps
from app import db
from app.models import UserMetrics

class MentaliaMonitor:
    def __init__(self):
        self.start_time = time.time()
        
    def track_request(self, app_name, endpoint, user_id=None):
        """Decorator para trackear requests"""
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                start_time = time.time()
                
                try:
                    result = f(*args, **kwargs)
                    status = 'success'
                except Exception as e:
                    status = 'error'
                    raise
                finally:
                    duration = time.time() - start_time
                    self.record_metric(
                        app_name=app_name,
                        metric_type='request',
                        metric_value={
                            'endpoint': endpoint,
                            'duration': duration,
                            'status': status,
                            'user_id': user_id
                        }
                    )
                
                return result
            return decorated_function
        return decorator
    
    def get_system_metrics(self):
        """Métricas del sistema"""
        gpu_info = GPUtil.getGPUs()[0] if GPUtil.getGPUs() else None
        
        return {
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_percent': psutil.disk_usage('/').percent,
            'gpu_utilization': gpu_info.load * 100 if gpu_info else 0,
            'gpu_memory_used': gpu_info.memoryUsed if gpu_info else 0,
            'gpu_memory_total': gpu_info.memoryTotal if gpu_info else 0,
            'active_users': self.get_active_users_count(),
            'total_conversations': self.get_conversations_count(),
            'uptime': time.time() - self.start_time
        }
    
    def record_metric(self, app_name, metric_type, metric_value, user_id=None):
        """Registrar métrica en base de datos"""
        metric = UserMetrics(
            user_id=user_id,
            app_id=self.get_app_id(app_name),
            metric_type=metric_type,
            metric_value=metric_value
        )
        db.session.add(metric)
        db.session.commit()
    
    def get_app_performance_report(self, app_name, hours=24):
        """Reporte de rendimiento por aplicación"""
        # Implementar consultas para métricas específicas
        pass

# Instancia global del monitor
monitor = MentaliaMonitor()
```

---

## 🔐 CONFIGURACIÓN DE SEGURIDAD

```python
# config.py
import os
from datetime import timedelta

class Config:
    # Base de datos
    DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'postgresql://mentalia:password@localhost/mentalia_unified'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Redis
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    
    # JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'super-secret-jwt-key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    
    # APIs externas
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
    
    # Seguridad
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    BCRYPT_LOG_ROUNDS = 12
    
    # Rate limiting
    RATELIMIT_STORAGE_URL = REDIS_URL
    RATELIMIT_DEFAULT = "1000 per hour"
    
    # CORS
    CORS_ORIGINS = ['https://hiperfoco.com', 'https://mentalia.com']
    
    # Uploads
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB max file size
    UPLOAD_FOLDER = '/app/user_data/uploads'
    
    # SSL
    SSL_REQUIRE = True
    SSL_REDIRECT = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    SSL_REQUIRE = False
    SSL_REDIRECT = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
```

---

## 🚀 SCRIPT DE DESPLIEGUE AUTOMATIZADO

```bash
#!/bin/bash
# deploy.sh - Script de despliegue unificado

set -e

echo "🚀 Iniciando despliegue MENTALIA UNIVERSE consolidado..."

# Variables de entorno
export COMPOSE_FILE=docker-compose.yml
export ENVIRONMENT=${ENVIRONMENT:-production}

# Funciones de utilidad
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

# Pre-deployment checks
log "Verificando prerrequisitos..."
command -v docker >/dev/null 2>&1 || { echo "Docker no está instalado"; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo "Docker Compose no está instalado"; exit 1; }

# Backup de base de datos
log "Creando backup de base de datos..."
docker-compose exec -T postgres pg_dump -U mentalia mentalia_unified > backup_$(date +%Y%m%d_%H%M%S).sql

# Build de nuevas imágenes
log "Construyendo imágenes Docker..."
docker-compose build --no-cache

# Aplicar migraciones de base de datos
log "Aplicando migraciones de base de datos..."
docker-compose run --rm mentalia-app flask db upgrade

# Reiniciar servicios
log "Reiniciando servicios..."
docker-compose down
docker-compose up -d

# Health checks
log "Verificando estado de servicios..."
sleep 30

# Verificar aplicación principal
if curl -f http://localhost:5000/api/health; then
    log "✅ Aplicación principal: OK"
else
    log "❌ Aplicación principal: FALLO"
    exit 1
fi

# Verificar base de datos
if docker-compose exec -T postgres pg_isready -U mentalia; then
    log "✅ Base de datos: OK"
else
    log "❌ Base de datos: FALLO"
    exit 1
fi

# Verificar Redis
if docker-compose exec -T redis redis-cli ping | grep -q PONG; then
    log "✅ Redis: OK"
else
    log "❌ Redis: FALLO"
    exit 1
fi

# Limpiar imágenes antiguas
log "Limpiando imágenes Docker antiguas..."
docker image prune -f

log "🎉 Despliegue completado exitosamente!"

# Mostrar estado final
echo ""
echo "📊 Estado de servicios:"
docker-compose ps

echo ""
echo "🌐 URLs de acceso:"
echo "- HIPERFOCO.COM: https://hiperfoco.com"
echo "- MENTALIA Universe: https://mentalia.com/universe"
echo "- Chat MENTALIA: https://mentalia.com/chat"
echo "- Monitoreo: https://mentalia.com:3000"
```

---

## 📈 MÉTRICAS Y KPIs DE CONSOLIDACIÓN

### **Métricas Técnicas de Rendimiento:**
```python
# app/core/kpis.py
class ConsolidationKPIs:
    @staticmethod
    def infrastructure_efficiency():
        return {
            'cost_reduction': '70%',  # vs. servicios separados
            'resource_utilization': '85%',  # GPU/CPU compartidos
            'response_time_avg': '< 2 segundos',
            'uptime_target': '99.9%'
        }
    
    @staticmethod
    def user_experience_metrics():
        return {
            'cross_app_adoption': '80%',  # usuarios usando 3+ apps
            'session_duration': '+150%',  # tiempo en plataforma
            'user_satisfaction': 'NPS > 50',
            'churn_reduction': '-40%'
        }
    
    @staticmethod
    def business_impact():
        return {
            'development_velocity': '+50%',  # nuevas features
            'maintenance_cost': '-80%',  # complejidad reducida
            'revenue_per_user': '+200%',  # cross-selling
            'market_differentiation': 'Única plataforma integral ND'
        }
```

---

**ARQUITECTURA TÉCNICA CONSOLIDADA MENTALIA 2025**

*"Una infraestructura, infinitas posibilidades"*
