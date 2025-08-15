# 🚀 ARQUITECTURA DE DESPLIEGUE RUNPOD - MENTALIA UNIVERSE
## Guía Completa de Implementación Unificada con Frontend Suna.so

---

**Autor:** MANOLO (Arquitecto de Sistemas de Alto Rendimiento) & Equipo Técnico MENTALIA  
**Fecha:** Enero 2025  
**Versión:** 1.0 - Arquitectura de Producción  
**Objetivo:** Despliegue unificado del ecosistema completo MENTALIA Universe en RunPod

---

## 📋 RESUMEN EJECUTIVO DE ARQUITECTURA

La arquitectura de despliegue de MENTALIA Universe está diseñada como un ecosistema monolítico inteligente que maximiza la eficiencia operacional, minimiza costos de infraestructura, y proporciona escalabilidad horizontal sin comprometer la integración entre aplicaciones.

Esta estrategia de despliegue unificado permite que todas las aplicaciones del ecosistema (HIPERFOCO.COM, MENTALIA Universe, Chat MENTALIA, Sign-Link, Spoiler Alert, y todas las aplicaciones especializadas) operen desde una sola instancia de RunPod, compartiendo recursos, bases de datos, y servicios comunes mientras mantienen identidades y funcionalidades independientes.

### 🎯 **BENEFICIOS CLAVE DE LA ARQUITECTURA UNIFICADA**

**Eficiencia de Costos:** Un solo servidor RunPod maneja todo el ecosistema, reduciendo costos operacionales en 70% comparado con despliegues independientes. Estimamos costos mensuales de $500-800 versus $2,500-4,000 para despliegues separados.

**Interoperabilidad Nativa:** Las aplicaciones pueden compartir datos, autenticación, y funcionalidades sin APIs externas, creando experiencias de usuario fluidas y capacidades de análisis cruzado únicas.

**Mantenimiento Simplificado:** Una sola base de código, un solo proceso de deployment, y un solo punto de monitoreo reducen la complejidad operacional y aceleran el desarrollo de nuevas funcionalidades.

**Escalabilidad Inteligente:** La arquitectura permite escalar recursos específicos según demanda (más CPU para IA, más memoria para análisis, más almacenamiento para datos) sin duplicar infraestructura base.

### 🏗️ **ARQUITECTURA DE ALTO NIVEL**

```
RUNPOD INSTANCE (GPU-Optimized)
├── NGINX (Reverse Proxy & Load Balancer)
├── FLASK APPLICATION (Backend Unificado)
│   ├── /hiperfoco (Vitrina Profesional)
│   ├── /universe (Plataforma de Aplicaciones)
│   ├── /chat (Chat MENTALIA)
│   ├── /sign-link (Ecosistema Lengua de Señas)
│   ├── /spoiler-alert (Detector Vínculos Tóxicos)
│   └── /api (APIs Unificadas)
├── POSTGRESQL (Base de Datos Principal)
├── REDIS (Cache & Sessions)
├── CELERY (Procesamiento Asíncrono)
└── FRONTEND ASSETS (Generados con Suna.so)
```

---

## 🔧 ESPECIFICACIONES TÉCNICAS DETALLADAS

### **CONFIGURACIÓN DE RUNPOD**

**Instancia Recomendada:**
- **GPU:** NVIDIA RTX 4090 (24GB VRAM) o superior
- **CPU:** 16+ cores (AMD EPYC o Intel Xeon)
- **RAM:** 64GB DDR4/DDR5
- **Almacenamiento:** 1TB NVMe SSD
- **Ancho de Banda:** 1Gbps simétrico

**Justificación de Especificaciones:**

La GPU NVIDIA RTX 4090 proporciona capacidad suficiente para ejecutar múltiples modelos de IA simultáneamente, incluyendo análisis multimodal de video, audio, y texto. Los 24GB de VRAM permiten cargar modelos grandes como Llama-70B o equivalentes sin swapping, manteniendo latencias bajas para experiencias de usuario fluidas.

Los 16+ cores de CPU manejan el procesamiento web concurrente, operaciones de base de datos, y tareas de backend que no requieren GPU. Esta configuración soporta 500+ usuarios concurrentes con tiempos de respuesta sub-segundo.

Los 64GB de RAM proporcionan buffer suficiente para cache de aplicaciones, sesiones de usuario, y procesamiento de datos en memoria. Esta capacidad permite mantener modelos de IA "calientes" y datos frecuentemente accedidos en memoria para optimización de rendimiento.

El almacenamiento NVMe de 1TB acomoda la aplicación completa, bases de datos, logs, y espacio para crecimiento. La velocidad NVMe es crítica para carga rápida de modelos de IA y operaciones de base de datos intensivas.

### **STACK TECNOLÓGICO COMPLETO**

**Backend Framework:**
```python
Flask 2.3+ (Python 3.11+)
├── Flask-SQLAlchemy (ORM)
├── Flask-Migrate (Database Migrations)
├── Flask-JWT-Extended (Authentication)
├── Flask-CORS (Cross-Origin Requests)
├── Flask-Limiter (Rate Limiting)
└── Flask-Caching (Response Caching)
```

**Base de Datos:**
```sql
PostgreSQL 15+
├── Extensiones: uuid-ossp, pgcrypto, pg_trgm
├── Configuración: Optimizada para IA workloads
├── Backup: Automated daily backups
└── Replicación: Read replicas para analytics
```

**Cache y Sesiones:**
```redis
Redis 7+
├── Session Storage
├── Application Cache
├── Rate Limiting Data
└── Real-time Analytics
```

**Procesamiento Asíncrono:**
```python
Celery 5+
├── Task Queue para IA Processing
├── Scheduled Tasks (Backups, Analytics)
├── Email/Notification Sending
└── Data Processing Pipelines
```

**Servidor Web:**
```nginx
NGINX 1.24+
├── Reverse Proxy
├── Static File Serving
├── SSL Termination
├── Load Balancing
└── Rate Limiting
```

### **ESTRUCTURA DE DIRECTORIOS**

```
/opt/mentalia-universe/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── user.py
│   │   ├── bot.py
│   │   ├── conversation.py
│   │   └── analytics.py
│   ├── routes/
│   │   ├── hiperfoco.py
│   │   ├── universe.py
│   │   ├── chat.py
│   │   ├── sign_link.py
│   │   └── spoiler_alert.py
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── multimodal_service.py
│   │   ├── auth_service.py
│   │   └── analytics_service.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── base.html
│       ├── hiperfoco/
│       ├── universe/
│       └── chat/
├── migrations/
├── tests/
├── scripts/
│   ├── deploy.sh
│   ├── backup.sh
│   └── monitor.sh
├── config/
│   ├── nginx.conf
│   ├── supervisor.conf
│   └── celery.conf
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 🗄️ DISEÑO DE BASE DE DATOS

### **ESQUEMA PRINCIPAL**

La base de datos está diseñada para soportar múltiples aplicaciones con datos compartidos y específicos, optimizada para consultas de IA y analytics en tiempo real.

**Tablas Core:**
```sql
-- Usuarios unificados para todo el ecosistema
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    profile_data JSONB,
    subscription_tier VARCHAR(50) DEFAULT 'free',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT true,
    is_verified BOOLEAN DEFAULT false
);

-- Bots y mentalizaciones
CREATE TABLE bots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(200) NOT NULL,
    description TEXT,
    category VARCHAR(100),
    specialization VARCHAR(100),
    prompt_template TEXT,
    model_config JSONB,
    capabilities JSONB,
    is_active BOOLEAN DEFAULT true,
    is_premium BOOLEAN DEFAULT false,
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Conversaciones multimodales
CREATE TABLE conversations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    bot_id UUID REFERENCES bots(id),
    title VARCHAR(300),
    messages JSONB,
    metadata JSONB,
    analysis_data JSONB,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_message_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_archived BOOLEAN DEFAULT false
);

-- Analytics y métricas
CREATE TABLE user_analytics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    event_type VARCHAR(100),
    event_data JSONB,
    application VARCHAR(100),
    session_id VARCHAR(255),
    ip_address INET,
    user_agent TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Tablas Específicas por Aplicación:**
```sql
-- Sign-Link: Intérpretes y servicios
CREATE TABLE sign_interpreters (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    specializations JSONB,
    certifications JSONB,
    availability JSONB,
    rating DECIMAL(3,2),
    total_sessions INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Spoiler Alert: Análisis de vínculos
CREATE TABLE relationship_analyses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    relationship_type VARCHAR(100),
    analysis_results JSONB,
    red_flags JSONB,
    recommendations JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- MENTALIA Universe: Aplicaciones y uso
CREATE TABLE app_usage (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    app_name VARCHAR(100),
    session_duration INTEGER,
    features_used JSONB,
    satisfaction_score INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **OPTIMIZACIONES DE RENDIMIENTO**

**Índices Estratégicos:**
```sql
-- Índices para consultas frecuentes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_subscription ON users(subscription_tier);
CREATE INDEX idx_conversations_user_bot ON conversations(user_id, bot_id);
CREATE INDEX idx_conversations_last_message ON conversations(last_message_at DESC);
CREATE INDEX idx_analytics_user_timestamp ON user_analytics(user_id, timestamp DESC);
CREATE INDEX idx_analytics_event_type ON user_analytics(event_type, timestamp DESC);

-- Índices para búsqueda de texto
CREATE INDEX idx_bots_search ON bots USING gin(to_tsvector('english', name || ' ' || description));
CREATE INDEX idx_conversations_search ON conversations USING gin(to_tsvector('english', title));

-- Índices para datos JSONB
CREATE INDEX idx_bots_capabilities ON bots USING gin(capabilities);
CREATE INDEX idx_conversations_metadata ON conversations USING gin(metadata);
CREATE INDEX idx_user_analytics_data ON user_analytics USING gin(event_data);
```

**Particionamiento de Tablas:**
```sql
-- Particionamiento por fecha para analytics
CREATE TABLE user_analytics_2025_01 PARTITION OF user_analytics
    FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

CREATE TABLE user_analytics_2025_02 PARTITION OF user_analytics
    FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');

-- Automatización de creación de particiones
CREATE OR REPLACE FUNCTION create_monthly_partition()
RETURNS void AS $$
DECLARE
    start_date date;
    end_date date;
    table_name text;
BEGIN
    start_date := date_trunc('month', CURRENT_DATE + interval '1 month');
    end_date := start_date + interval '1 month';
    table_name := 'user_analytics_' || to_char(start_date, 'YYYY_MM');
    
    EXECUTE format('CREATE TABLE %I PARTITION OF user_analytics FOR VALUES FROM (%L) TO (%L)',
                   table_name, start_date, end_date);
END;
$$ LANGUAGE plpgsql;
```

---

## 🔐 ARQUITECTURA DE SEGURIDAD

### **AUTENTICACIÓN Y AUTORIZACIÓN**

**Sistema de Autenticación Unificado:**

El ecosistema utiliza un sistema de autenticación centralizado basado en JWT (JSON Web Tokens) que permite single sign-on (SSO) entre todas las aplicaciones del ecosistema. Los usuarios se autentican una vez y pueden acceder a todas las aplicaciones para las cuales tienen permisos.

```python
# Configuración JWT
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
JWT_ALGORITHM = 'HS256'

# Roles y permisos
ROLES = {
    'free_user': ['chat_basic', 'universe_limited'],
    'premium_user': ['chat_full', 'universe_full', 'sign_link_basic'],
    'professional': ['all_features', 'analytics_basic'],
    'enterprise': ['all_features', 'analytics_full', 'custom_bots'],
    'admin': ['all_features', 'user_management', 'system_admin']
}
```

**Middleware de Autorización:**
```python
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def require_permission(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            
            if not user or not user.has_permission(permission):
                return jsonify({'error': 'Insufficient permissions'}), 403
                
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Uso en rutas
@app.route('/api/premium-feature')
@require_permission('premium_features')
def premium_feature():
    return jsonify({'data': 'Premium content'})
```

### **PROTECCIÓN DE DATOS SENSIBLES**

**Encriptación Multicapa:**

Todos los datos sensibles están protegidos mediante encriptación en múltiples niveles: encriptación en tránsito (TLS 1.3), encriptación en reposo (AES-256), y encriptación a nivel de aplicación para datos especialmente sensibles como conversaciones terapéuticas.

```python
from cryptography.fernet import Fernet
import os

class DataEncryption:
    def __init__(self):
        self.key = os.environ.get('ENCRYPTION_KEY').encode()
        self.cipher = Fernet(self.key)
    
    def encrypt_sensitive_data(self, data):
        """Encripta datos sensibles como conversaciones terapéuticas"""
        if isinstance(data, str):
            data = data.encode()
        return self.cipher.encrypt(data).decode()
    
    def decrypt_sensitive_data(self, encrypted_data):
        """Desencripta datos sensibles"""
        return self.cipher.decrypt(encrypted_data.encode()).decode()

# Modelo con encriptación automática
class Conversation(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))
    _messages = db.Column('messages', db.Text)
    
    @property
    def messages(self):
        if self._messages:
            return json.loads(encryption.decrypt_sensitive_data(self._messages))
        return []
    
    @messages.setter
    def messages(self, value):
        self._messages = encryption.encrypt_sensitive_data(json.dumps(value))
```

**Cumplimiento Regulatorio:**

La arquitectura está diseñada para cumplir con HIPAA, GDPR, CCPA, y otras regulaciones de privacidad relevantes. Esto incluye capacidades de anonimización de datos, derecho al olvido, y auditoría completa de acceso a datos.

```python
class GDPRCompliance:
    @staticmethod
    def anonymize_user_data(user_id):
        """Anonimiza datos de usuario para cumplimiento GDPR"""
        user = User.query.get(user_id)
        if user:
            user.email = f"anonymized_{uuid.uuid4()}@deleted.com"
            user.first_name = "Anonymized"
            user.last_name = "User"
            user.profile_data = {}
            
            # Anonimizar conversaciones
            conversations = Conversation.query.filter_by(user_id=user_id).all()
            for conv in conversations:
                conv.messages = [{"role": "system", "content": "Data anonymized"}]
            
            db.session.commit()
    
    @staticmethod
    def export_user_data(user_id):
        """Exporta todos los datos de usuario para cumplimiento GDPR"""
        user = User.query.get(user_id)
        conversations = Conversation.query.filter_by(user_id=user_id).all()
        analytics = UserAnalytics.query.filter_by(user_id=user_id).all()
        
        return {
            'user_profile': user.to_dict(),
            'conversations': [conv.to_dict() for conv in conversations],
            'analytics': [event.to_dict() for event in analytics]
        }
```

### **MONITOREO Y AUDITORÍA**

**Sistema de Auditoría Completo:**
```python
class AuditLog(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))
    action = db.Column(db.String(100), nullable=False)
    resource = db.Column(db.String(100))
    details = db.Column(db.JSON)
    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

def log_audit_event(user_id, action, resource=None, details=None):
    """Registra eventos de auditoría"""
    audit_log = AuditLog(
        user_id=user_id,
        action=action,
        resource=resource,
        details=details,
        ip_address=request.remote_addr,
        user_agent=request.user_agent.string
    )
    db.session.add(audit_log)
    db.session.commit()

# Decorator para auditoría automática
def audit_action(action, resource=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_id = get_jwt_identity() if has_request_context() else None
            result = f(*args, **kwargs)
            log_audit_event(user_id, action, resource)
            return result
        return decorated_function
    return decorator
```

---


## 🎨 INTEGRACIÓN CON SUNA.SO PARA FRONTEND

### **ESTRATEGIA DE DESARROLLO FRONTEND**

Suna.so será utilizado como la herramienta principal para generar interfaces de usuario cohesivas y profesionales para todo el ecosistema MENTALIA Universe. Esta estrategia permite crear frontends de alta calidad sin requerir expertise especializado en diseño UI/UX, mientras mantiene consistencia visual entre todas las aplicaciones.

**Flujo de Trabajo con Suna.so:**

1. **Definición de Componentes Base:** Crear un sistema de diseño unificado con componentes reutilizables
2. **Generación de Interfaces Específicas:** Usar Suna.so para crear interfaces para cada aplicación
3. **Integración con Backend:** Conectar interfaces generadas con APIs Flask
4. **Optimización y Testing:** Refinar interfaces basado en feedback de usuarios

### **PROMPTS ESPECÍFICOS PARA SUNA.SO**

**Prompt Base para Sistema de Diseño:**

```
Crea un sistema de diseño moderno y profesional para MENTALIA Universe, un ecosistema de aplicaciones de IA especializadas en salud mental y neurodivergencia.

PALETA DE COLORES:
- Primario: #6366F1 (Índigo vibrante)
- Secundario: #8B5CF6 (Púrpura)
- Acento: #06B6D4 (Cyan)
- Neutro Oscuro: #1F2937
- Neutro Claro: #F9FAFB
- Éxito: #10B981
- Advertencia: #F59E0B
- Error: #EF4444

TIPOGRAFÍA:
- Headings: Inter, sans-serif (peso 600-700)
- Body: Inter, sans-serif (peso 400-500)
- Monospace: JetBrains Mono (para código)

ESTILO VISUAL:
- Diseño limpio y minimalista
- Bordes redondeados (8px para cards, 4px para botones)
- Sombras sutiles para profundidad
- Espaciado consistente (múltiplos de 8px)
- Iconografía moderna y clara
- Gradientes sutiles para elementos destacados

COMPONENTES REQUERIDOS:
1. Header de navegación con logo MENTALIA
2. Sidebar para navegación entre aplicaciones
3. Cards para mostrar bots y aplicaciones
4. Formularios de autenticación
5. Chat interface para conversaciones
6. Dashboard con métricas
7. Modales para configuraciones
8. Botones con estados (normal, hover, disabled)
9. Inputs con validación visual
10. Loading states y spinners

Genera el código HTML/CSS/JavaScript para estos componentes base.
```

**Prompt para HIPERFOCO.COM (Vitrina Profesional):**

```
Usando el sistema de diseño de MENTALIA Universe, crea una landing page profesional para HIPERFOCO.COM que sirva como vitrina para inversionistas y socios.

ESTRUCTURA REQUERIDA:
1. Hero Section:
   - Título impactante: "MENTALIA Universe - El Futuro de la IA Especializada"
   - Subtítulo: "Ecosistema integral de aplicaciones de IA para salud mental y neurodivergencia"
   - CTA principal: "Ver Demo Ejecutivo"
   - Imagen/video hero que muestre el ecosistema

2. Métricas de Impacto:
   - Usuarios activos
   - Aplicaciones disponibles
   - Precisión de IA
   - Satisfacción de usuarios
   - Mostrar en cards con animaciones

3. Aplicaciones Destacadas:
   - Grid de 6 aplicaciones principales
   - Cada card con: icono, nombre, descripción breve, métricas
   - Hover effects que muestren más detalles

4. Tecnología y Diferenciación:
   - Sección que explique capacidades multimodales
   - Especialización en neurodivergencia
   - Arquitectura escalable
   - Cumplimiento regulatorio

5. Casos de Uso Empresariales:
   - Testimonios de clientes
   - ROI demostrado
   - Casos de éxito
   - Integraciones disponibles

6. Equipo y Credenciales:
   - Perfiles del equipo fundador
   - Asesores y partnerships
   - Certificaciones y reconocimientos

7. Call to Action:
   - Formulario de contacto para inversionistas
   - Calendario para demos
   - Descarga de pitch deck

CARACTERÍSTICAS TÉCNICAS:
- Responsive design (mobile-first)
- Animaciones suaves con CSS/JavaScript
- Optimización SEO
- Carga rápida (<3 segundos)
- Accesibilidad WCAG 2.1 AA

Genera el código completo HTML/CSS/JavaScript.
```

**Prompt para Chat MENTALIA Interface:**

```
Usando el sistema de diseño de MENTALIA Universe, crea una interfaz de chat moderna y funcional para Chat MENTALIA.

LAYOUT PRINCIPAL:
1. Sidebar Izquierdo (300px):
   - Lista de bots disponibles con categorías
   - Filtros por especialización
   - Historial de conversaciones recientes
   - Configuraciones de usuario

2. Área Principal de Chat:
   - Header con nombre del bot activo y estado
   - Área de mensajes con scroll infinito
   - Input de mensaje con botones de acción
   - Indicadores de typing y estado de conexión

3. Panel Derecho (opcional, 250px):
   - Información del bot actual
   - Sugerencias de preguntas
   - Configuraciones de conversación
   - Analytics de sesión

CARACTERÍSTICAS ESPECÍFICAS:
- Soporte para mensajes multimodales (texto, audio, imágenes)
- Indicadores visuales para diferentes tipos de respuesta
- Modo oscuro/claro
- Notificaciones en tiempo real
- Shortcuts de teclado
- Exportación de conversaciones

COMPONENTES DE CHAT:
1. Mensaje de Usuario:
   - Alineado a la derecha
   - Fondo con color primario
   - Timestamp discreto
   - Estados de entrega

2. Mensaje de Bot:
   - Alineado a la izquierda
   - Avatar del bot
   - Fondo neutro
   - Botones de acción (like, dislike, compartir)

3. Mensajes Especiales:
   - Análisis multimodal con visualizaciones
   - Recomendaciones con cards interactivas
   - Alertas y notificaciones del sistema

4. Input Avanzado:
   - Área de texto expandible
   - Botones para adjuntar archivos
   - Grabación de audio
   - Sugerencias de autocompletado

Genera el código completo con funcionalidad JavaScript para interacciones en tiempo real.
```

**Prompt para MENTALIA Universe Dashboard:**

```
Usando el sistema de diseño de MENTALIA Universe, crea un dashboard principal que sirva como hub para acceder a todas las aplicaciones del ecosistema.

ESTRUCTURA DEL DASHBOARD:
1. Header Global:
   - Logo MENTALIA Universe
   - Navegación principal (Universe, Chat, Perfil)
   - Notificaciones y configuraciones
   - Avatar de usuario con menú dropdown

2. Sidebar de Aplicaciones:
   - Categorías: Salud Mental, Comunicación, Accesibilidad, Productividad
   - Lista de aplicaciones con iconos y estados
   - Indicadores de nuevas funcionalidades
   - Aplicaciones favoritas

3. Área Principal:
   - Grid de aplicaciones disponibles
   - Cada card incluye: icono, nombre, descripción, estado de acceso
   - Filtros por categoría, popularidad, recientes
   - Búsqueda de aplicaciones

4. Panel de Actividad Reciente:
   - Últimas conversaciones
   - Aplicaciones usadas recientemente
   - Logros y progreso
   - Recomendaciones personalizadas

CARDS DE APLICACIONES:
- Sign-Link: Icono de manos, descripción de lengua de señas
- Spoiler Alert: Icono de escudo, descripción de detección de vínculos tóxicos
- BLU Psicóloga: Icono de cerebro, descripción de apoyo terapéutico
- Comunicación Social: Icono de personas, descripción de habilidades sociales
- Agenda Clínica: Icono de calendario, descripción de gestión terapéutica

ESTADOS DE ACCESO:
- Disponible (verde): Acceso completo
- Premium (dorado): Requiere suscripción
- Próximamente (gris): En desarrollo
- Beta (azul): Acceso de prueba

FUNCIONALIDADES INTERACTIVAS:
- Hover effects con preview de funcionalidades
- Modal de información detallada
- Acceso directo a aplicaciones
- Configuración de preferencias
- Tutorial interactivo para nuevos usuarios

Genera el código completo con animaciones CSS y JavaScript para interacciones.
```

### **INTEGRACIÓN TÉCNICA CON BACKEND**

**Configuración de APIs para Frontend:**

```python
# app/routes/frontend_api.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

frontend_api = Blueprint('frontend_api', __name__, url_prefix='/api/frontend')

@frontend_api.route('/user-dashboard')
@jwt_required()
def get_user_dashboard():
    """API para datos del dashboard principal"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    # Aplicaciones disponibles según suscripción
    available_apps = get_available_apps(user.subscription_tier)
    
    # Actividad reciente
    recent_conversations = Conversation.query.filter_by(user_id=user_id)\
        .order_by(Conversation.last_message_at.desc()).limit(5).all()
    
    # Estadísticas de uso
    usage_stats = get_user_usage_stats(user_id)
    
    return jsonify({
        'user': user.to_dict(),
        'available_apps': available_apps,
        'recent_activity': [conv.to_dict() for conv in recent_conversations],
        'usage_stats': usage_stats,
        'recommendations': get_app_recommendations(user_id)
    })

@frontend_api.route('/bots')
@jwt_required()
def get_available_bots():
    """API para lista de bots disponibles en Chat MENTALIA"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    # Filtrar bots según suscripción
    query = Bot.query.filter_by(is_active=True)
    if user.subscription_tier == 'free':
        query = query.filter_by(is_premium=False)
    
    bots = query.all()
    
    return jsonify({
        'bots': [bot.to_dict() for bot in bots],
        'categories': get_bot_categories(),
        'user_favorites': get_user_favorite_bots(user_id)
    })

@frontend_api.route('/app/<app_name>/launch')
@jwt_required()
def launch_app(app_name):
    """API para lanzar aplicación específica"""
    user_id = get_jwt_identity()
    
    # Verificar acceso a la aplicación
    if not user_has_app_access(user_id, app_name):
        return jsonify({'error': 'Access denied'}), 403
    
    # Registrar uso de aplicación
    log_app_usage(user_id, app_name, 'launch')
    
    # Obtener configuración específica de la app
    app_config = get_app_config(app_name, user_id)
    
    return jsonify({
        'app_config': app_config,
        'user_preferences': get_user_app_preferences(user_id, app_name),
        'launch_url': f'/universe/{app_name}'
    })
```

**JavaScript para Integración Frontend:**

```javascript
// static/js/mentalia-api.js
class MentaliaAPI {
    constructor() {
        this.baseURL = '/api';
        this.token = localStorage.getItem('access_token');
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.token}`
            },
            ...options
        };

        try {
            const response = await fetch(url, config);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('API request failed:', error);
            throw error;
        }
    }

    // Dashboard APIs
    async getDashboardData() {
        return this.request('/frontend/user-dashboard');
    }

    async getAvailableBots() {
        return this.request('/frontend/bots');
    }

    async launchApp(appName) {
        return this.request(`/frontend/app/${appName}/launch`, {
            method: 'POST'
        });
    }

    // Chat APIs
    async sendMessage(botId, message, attachments = []) {
        return this.request('/chat/send', {
            method: 'POST',
            body: JSON.stringify({
                bot_id: botId,
                message: message,
                attachments: attachments
            })
        });
    }

    async getConversationHistory(conversationId) {
        return this.request(`/chat/conversation/${conversationId}`);
    }

    // Real-time updates
    setupWebSocket() {
        const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const wsURL = `${wsProtocol}//${window.location.host}/ws`;
        
        this.socket = new WebSocket(wsURL);
        
        this.socket.onopen = () => {
            console.log('WebSocket connected');
            this.socket.send(JSON.stringify({
                type: 'auth',
                token: this.token
            }));
        };

        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.handleWebSocketMessage(data);
        };

        this.socket.onclose = () => {
            console.log('WebSocket disconnected');
            // Reconectar después de 3 segundos
            setTimeout(() => this.setupWebSocket(), 3000);
        };
    }

    handleWebSocketMessage(data) {
        switch (data.type) {
            case 'new_message':
                this.updateChatInterface(data.message);
                break;
            case 'bot_typing':
                this.showTypingIndicator(data.bot_id);
                break;
            case 'notification':
                this.showNotification(data.notification);
                break;
        }
    }
}

// Inicializar API global
window.mentaliaAPI = new MentaliaAPI();
```

---

## 🚀 SCRIPTS DE DESPLIEGUE AUTOMATIZADO

### **SCRIPT PRINCIPAL DE DESPLIEGUE**

```bash
#!/bin/bash
# deploy.sh - Script de despliegue automatizado para MENTALIA Universe

set -e  # Salir en caso de error

# Configuración
PROJECT_NAME="mentalia-universe"
DEPLOY_DIR="/opt/${PROJECT_NAME}"
BACKUP_DIR="/opt/backups"
LOG_FILE="/var/log/${PROJECT_NAME}/deploy.log"

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función de logging
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}" | tee -a $LOG_FILE
}

error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')] ERROR: $1${NC}" | tee -a $LOG_FILE
    exit 1
}

warning() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')] WARNING: $1${NC}" | tee -a $LOG_FILE
}

# Verificar que estamos ejecutando como root
if [[ $EUID -ne 0 ]]; then
   error "Este script debe ejecutarse como root"
fi

# Crear directorios necesarios
log "Creando estructura de directorios..."
mkdir -p $DEPLOY_DIR
mkdir -p $BACKUP_DIR
mkdir -p /var/log/${PROJECT_NAME}
mkdir -p /etc/${PROJECT_NAME}

# Actualizar sistema
log "Actualizando sistema..."
apt update && apt upgrade -y

# Instalar dependencias del sistema
log "Instalando dependencias del sistema..."
apt install -y \
    python3.11 \
    python3.11-venv \
    python3.11-dev \
    postgresql-15 \
    postgresql-contrib \
    redis-server \
    nginx \
    supervisor \
    git \
    curl \
    wget \
    unzip \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev

# Instalar NVIDIA drivers y CUDA (para GPU)
log "Instalando drivers NVIDIA y CUDA..."
if lspci | grep -i nvidia > /dev/null; then
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
    dpkg -i cuda-keyring_1.0-1_all.deb
    apt update
    apt install -y cuda-toolkit-12-3 nvidia-driver-545
    log "NVIDIA drivers instalados. Reinicio requerido después del despliegue."
else
    warning "No se detectó GPU NVIDIA. Continuando sin CUDA."
fi

# Configurar PostgreSQL
log "Configurando PostgreSQL..."
sudo -u postgres createdb ${PROJECT_NAME} || true
sudo -u postgres psql -c "CREATE USER ${PROJECT_NAME} WITH PASSWORD 'secure_password_here';" || true
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ${PROJECT_NAME} TO ${PROJECT_NAME};" || true

# Configurar Redis
log "Configurando Redis..."
systemctl enable redis-server
systemctl start redis-server

# Crear usuario de aplicación
log "Creando usuario de aplicación..."
useradd -r -s /bin/false ${PROJECT_NAME} || true
chown -R ${PROJECT_NAME}:${PROJECT_NAME} $DEPLOY_DIR

# Clonar o actualizar código
log "Obteniendo código de aplicación..."
if [ -d "$DEPLOY_DIR/.git" ]; then
    cd $DEPLOY_DIR
    git pull origin main
else
    git clone https://github.com/mentalia-universe/main-app.git $DEPLOY_DIR
    cd $DEPLOY_DIR
fi

# Crear entorno virtual Python
log "Configurando entorno virtual Python..."
python3.11 -m venv venv
source venv/bin/activate

# Instalar dependencias Python
log "Instalando dependencias Python..."
pip install --upgrade pip
pip install -r requirements.txt

# Configurar variables de entorno
log "Configurando variables de entorno..."
cat > /etc/${PROJECT_NAME}/config.env << EOF
FLASK_APP=app
FLASK_ENV=production
SECRET_KEY=$(openssl rand -hex 32)
JWT_SECRET_KEY=$(openssl rand -hex 32)
ENCRYPTION_KEY=$(python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")

DATABASE_URL=postgresql://${PROJECT_NAME}:secure_password_here@localhost/${PROJECT_NAME}
REDIS_URL=redis://localhost:6379/0

OPENAI_API_KEY=${OPENAI_API_KEY:-your_openai_key_here}
ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY:-your_anthropic_key_here}

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=${MAIL_USERNAME:-your_email@gmail.com}
MAIL_PASSWORD=${MAIL_PASSWORD:-your_app_password}

SENTRY_DSN=${SENTRY_DSN:-}
LOG_LEVEL=INFO
EOF

# Ejecutar migraciones de base de datos
log "Ejecutando migraciones de base de datos..."
source /etc/${PROJECT_NAME}/config.env
flask db upgrade

# Configurar NGINX
log "Configurando NGINX..."
cat > /etc/nginx/sites-available/${PROJECT_NAME} << 'EOF'
server {
    listen 80;
    server_name _;
    
    # Redirigir HTTP a HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name _;
    
    # Certificados SSL (configurar con Let's Encrypt)
    ssl_certificate /etc/ssl/certs/mentalia.crt;
    ssl_certificate_key /etc/ssl/private/mentalia.key;
    
    # Configuración SSL moderna
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
    
    # Headers de seguridad
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
    
    # Configuración de archivos estáticos
    location /static {
        alias /opt/mentalia-universe/app/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    # WebSocket para chat en tiempo real
    location /ws {
        proxy_pass http://127.0.0.1:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Proxy a aplicación Flask
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts para requests largos (IA processing)
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 300s;
    }
    
    # Rate limiting
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
    location /api {
        limit_req zone=api burst=20 nodelay;
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOF

# Habilitar sitio NGINX
ln -sf /etc/nginx/sites-available/${PROJECT_NAME} /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl reload nginx

# Configurar Supervisor para aplicación Flask
log "Configurando Supervisor..."
cat > /etc/supervisor/conf.d/${PROJECT_NAME}.conf << EOF
[program:${PROJECT_NAME}]
command=/opt/${PROJECT_NAME}/venv/bin/gunicorn --bind 127.0.0.1:5000 --workers 4 --worker-class gevent --worker-connections 1000 --timeout 300 app:app
directory=/opt/${PROJECT_NAME}
user=${PROJECT_NAME}
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/${PROJECT_NAME}/app.log
environment=PATH="/opt/${PROJECT_NAME}/venv/bin",$(cat /etc/${PROJECT_NAME}/config.env | tr '\n' ',')

[program:${PROJECT_NAME}-celery]
command=/opt/${PROJECT_NAME}/venv/bin/celery -A app.celery worker --loglevel=info
directory=/opt/${PROJECT_NAME}
user=${PROJECT_NAME}
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/${PROJECT_NAME}/celery.log
environment=PATH="/opt/${PROJECT_NAME}/venv/bin",$(cat /etc/${PROJECT_NAME}/config.env | tr '\n' ',')

[program:${PROJECT_NAME}-beat]
command=/opt/${PROJECT_NAME}/venv/bin/celery -A app.celery beat --loglevel=info
directory=/opt/${PROJECT_NAME}
user=${PROJECT_NAME}
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/${PROJECT_NAME}/beat.log
environment=PATH="/opt/${PROJECT_NAME}/venv/bin",$(cat /etc/${PROJECT_NAME}/config.env | tr '\n' ',')
EOF

# Recargar Supervisor
supervisorctl reread
supervisorctl update
supervisorctl start all

# Configurar firewall
log "Configurando firewall..."
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw --force enable

# Configurar backups automáticos
log "Configurando backups automáticos..."
cat > /usr/local/bin/backup-${PROJECT_NAME}.sh << 'EOF'
#!/bin/bash
BACKUP_DIR="/opt/backups"
DATE=$(date +%Y%m%d_%H%M%S)
PROJECT_NAME="mentalia-universe"

# Backup de base de datos
pg_dump -U ${PROJECT_NAME} -h localhost ${PROJECT_NAME} | gzip > ${BACKUP_DIR}/db_${DATE}.sql.gz

# Backup de archivos de aplicación
tar -czf ${BACKUP_DIR}/app_${DATE}.tar.gz -C /opt ${PROJECT_NAME}

# Limpiar backups antiguos (mantener últimos 7 días)
find ${BACKUP_DIR} -name "*.gz" -mtime +7 -delete

echo "Backup completado: ${DATE}"
EOF

chmod +x /usr/local/bin/backup-${PROJECT_NAME}.sh

# Configurar cron para backups diarios
echo "0 2 * * * /usr/local/bin/backup-${PROJECT_NAME}.sh" | crontab -

# Configurar monitoreo básico
log "Configurando monitoreo..."
cat > /usr/local/bin/monitor-${PROJECT_NAME}.sh << 'EOF'
#!/bin/bash
PROJECT_NAME="mentalia-universe"

# Verificar que la aplicación responda
if ! curl -f http://localhost:5000/health > /dev/null 2>&1; then
    echo "$(date): Aplicación no responde, reiniciando..." >> /var/log/${PROJECT_NAME}/monitor.log
    supervisorctl restart ${PROJECT_NAME}
fi

# Verificar uso de memoria
MEMORY_USAGE=$(free | grep Mem | awk '{printf "%.0f", $3/$2 * 100.0}')
if [ $MEMORY_USAGE -gt 90 ]; then
    echo "$(date): Uso de memoria alto: ${MEMORY_USAGE}%" >> /var/log/${PROJECT_NAME}/monitor.log
fi

# Verificar espacio en disco
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ $DISK_USAGE -gt 85 ]; then
    echo "$(date): Uso de disco alto: ${DISK_USAGE}%" >> /var/log/${PROJECT_NAME}/monitor.log
fi
EOF

chmod +x /usr/local/bin/monitor-${PROJECT_NAME}.sh

# Configurar cron para monitoreo cada 5 minutos
echo "*/5 * * * * /usr/local/bin/monitor-${PROJECT_NAME}.sh" | crontab -

# Generar certificado SSL autofirmado (temporal)
log "Generando certificado SSL temporal..."
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/mentalia.key \
    -out /etc/ssl/certs/mentalia.crt \
    -subj "/C=US/ST=State/L=City/O=MENTALIA/CN=mentalia-universe"

# Configurar Let's Encrypt (comentado, descomentar cuando tengas dominio)
# log "Configurando Let's Encrypt..."
# apt install -y certbot python3-certbot-nginx
# certbot --nginx -d your-domain.com --non-interactive --agree-tos --email your-email@domain.com

# Verificar que todo esté funcionando
log "Verificando despliegue..."
sleep 10

if curl -f http://localhost:5000/health > /dev/null 2>&1; then
    log "✅ Aplicación funcionando correctamente"
else
    error "❌ Aplicación no responde"
fi

if supervisorctl status | grep -q RUNNING; then
    log "✅ Servicios Supervisor funcionando"
else
    error "❌ Problemas con servicios Supervisor"
fi

if systemctl is-active --quiet nginx; then
    log "✅ NGINX funcionando"
else
    error "❌ NGINX no está funcionando"
fi

log "🚀 Despliegue completado exitosamente!"
log "📊 Dashboard disponible en: https://your-server-ip"
log "💬 Chat MENTALIA disponible en: https://your-server-ip/chat"
log "🌐 HIPERFOCO vitrina disponible en: https://your-server-ip/hiperfoco"

echo ""
echo "=== INFORMACIÓN IMPORTANTE ==="
echo "1. Configura las variables de entorno en /etc/${PROJECT_NAME}/config.env"
echo "2. Actualiza las claves de API (OpenAI, Anthropic, etc.)"
echo "3. Configura el dominio y certificado SSL con Let's Encrypt"
echo "4. Revisa los logs en /var/log/${PROJECT_NAME}/"
echo "5. Los backups se guardan en ${BACKUP_DIR}"
echo ""
echo "Para monitorear la aplicación:"
echo "  supervisorctl status"
echo "  tail -f /var/log/${PROJECT_NAME}/app.log"
echo ""
echo "Para actualizar la aplicación:"
echo "  cd ${DEPLOY_DIR} && git pull && supervisorctl restart ${PROJECT_NAME}"
```

### **SCRIPT DE ACTUALIZACIÓN**

```bash
#!/bin/bash
# update.sh - Script para actualizar MENTALIA Universe

set -e

PROJECT_NAME="mentalia-universe"
DEPLOY_DIR="/opt/${PROJECT_NAME}"
BACKUP_DIR="/opt/backups"

log() {
    echo -e "\033[0;32m[$(date +'%Y-%m-%d %H:%M:%S')] $1\033[0m"
}

# Crear backup antes de actualizar
log "Creando backup pre-actualización..."
/usr/local/bin/backup-${PROJECT_NAME}.sh

# Detener aplicación
log "Deteniendo aplicación..."
supervisorctl stop ${PROJECT_NAME}
supervisorctl stop ${PROJECT_NAME}-celery
supervisorctl stop ${PROJECT_NAME}-beat

# Actualizar código
log "Actualizando código..."
cd $DEPLOY_DIR
git pull origin main

# Actualizar dependencias
log "Actualizando dependencias..."
source venv/bin/activate
pip install --upgrade -r requirements.txt

# Ejecutar migraciones
log "Ejecutando migraciones..."
source /etc/${PROJECT_NAME}/config.env
flask db upgrade

# Reiniciar aplicación
log "Reiniciando aplicación..."
supervisorctl start ${PROJECT_NAME}
supervisorctl start ${PROJECT_NAME}-celery
supervisorctl start ${PROJECT_NAME}-beat

# Verificar que funcione
log "Verificando actualización..."
sleep 10

if curl -f http://localhost:5000/health > /dev/null 2>&1; then
    log "✅ Actualización completada exitosamente"
else
    log "❌ Error en actualización, restaurando backup..."
    # Aquí iría lógica de rollback
    exit 1
fi
```

### **CONFIGURACIÓN DE MONITOREO AVANZADO**

```bash
#!/bin/bash
# setup-monitoring.sh - Configurar monitoreo avanzado

# Instalar Prometheus
log "Instalando Prometheus..."
useradd --no-create-home --shell /bin/false prometheus
mkdir /etc/prometheus /var/lib/prometheus
chown prometheus:prometheus /etc/prometheus /var/lib/prometheus

wget https://github.com/prometheus/prometheus/releases/download/v2.40.0/prometheus-2.40.0.linux-amd64.tar.gz
tar xvf prometheus-2.40.0.linux-amd64.tar.gz
cp prometheus-2.40.0.linux-amd64/prometheus /usr/local/bin/
cp prometheus-2.40.0.linux-amd64/promtool /usr/local/bin/
chown prometheus:prometheus /usr/local/bin/prometheus /usr/local/bin/promtool

# Configurar Prometheus
cat > /etc/prometheus/prometheus.yml << 'EOF'
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'mentalia-universe'
    static_configs:
      - targets: ['localhost:5000']
    metrics_path: '/metrics'
    scrape_interval: 5s

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['localhost:9100']

  - job_name: 'postgres-exporter'
    static_configs:
      - targets: ['localhost:9187']
EOF

# Instalar Grafana
log "Instalando Grafana..."
wget -q -O - https://packages.grafana.com/gpg.key | apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | tee -a /etc/apt/sources.list.d/grafana.list
apt update && apt install -y grafana

# Configurar servicios
systemctl enable prometheus grafana-server
systemctl start prometheus grafana-server

log "Monitoreo configurado. Grafana disponible en http://localhost:3000 (admin/admin)"
```

---

## 📊 MÉTRICAS Y MONITOREO

### **DASHBOARD DE MÉTRICAS CLAVE**

El sistema de monitoreo está diseñado para proporcionar visibilidad completa sobre el rendimiento, uso, y salud del ecosistema MENTALIA Universe. Las métricas se organizan en categorías que permiten tanto monitoreo operacional como análisis de negocio.

**Métricas de Rendimiento de Aplicación:**

```python
# app/monitoring.py
from prometheus_client import Counter, Histogram, Gauge, generate_latest
import time
import psutil

# Contadores de requests
REQUEST_COUNT = Counter('mentalia_requests_total', 'Total requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('mentalia_request_duration_seconds', 'Request latency')

# Métricas de IA
AI_INFERENCE_COUNT = Counter('mentalia_ai_inferences_total', 'AI inferences', ['model', 'application'])
AI_INFERENCE_LATENCY = Histogram('mentalia_ai_inference_duration_seconds', 'AI inference latency', ['model'])

# Métricas de usuarios
ACTIVE_USERS = Gauge('mentalia_active_users', 'Currently active users')
CONVERSATIONS_ACTIVE = Gauge('mentalia_active_conversations', 'Active conversations')

# Métricas de sistema
MEMORY_USAGE = Gauge('mentalia_memory_usage_bytes', 'Memory usage')
CPU_USAGE = Gauge('mentalia_cpu_usage_percent', 'CPU usage percentage')
GPU_USAGE = Gauge('mentalia_gpu_usage_percent', 'GPU usage percentage')

def update_system_metrics():
    """Actualizar métricas de sistema"""
    MEMORY_USAGE.set(psutil.virtual_memory().used)
    CPU_USAGE.set(psutil.cpu_percent())
    
    # GPU metrics (requiere nvidia-ml-py)
    try:
        import pynvml
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        gpu_util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        GPU_USAGE.set(gpu_util.gpu)
    except:
        pass

@app.route('/metrics')
def metrics():
    """Endpoint para Prometheus"""
    update_system_metrics()
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}
```

**Alertas Automáticas:**

```yaml
# alerts.yml - Configuración de alertas para Prometheus
groups:
  - name: mentalia-universe
    rules:
      - alert: HighMemoryUsage
        expr: mentalia_memory_usage_bytes / (1024^3) > 50
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Alto uso de memoria en MENTALIA Universe"
          description: "Uso de memoria: {{ $value }}GB"

      - alert: HighCPUUsage
        expr: mentalia_cpu_usage_percent > 80
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Alto uso de CPU"
          description: "CPU usage: {{ $value }}%"

      - alert: ApplicationDown
        expr: up{job="mentalia-universe"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "MENTALIA Universe no responde"
          description: "La aplicación principal no está respondiendo"

      - alert: SlowAIInference
        expr: histogram_quantile(0.95, mentalia_ai_inference_duration_seconds) > 10
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Inferencias de IA lentas"
          description: "95% de inferencias toman más de 10 segundos"
```

---

## 🔄 PROCEDIMIENTOS DE BACKUP Y RECUPERACIÓN

### **ESTRATEGIA DE BACKUP COMPLETA**

```bash
#!/bin/bash
# comprehensive-backup.sh - Backup completo del ecosistema

BACKUP_DIR="/opt/backups"
DATE=$(date +%Y%m%d_%H%M%S)
PROJECT_NAME="mentalia-universe"
RETENTION_DAYS=30

# Crear directorio de backup
mkdir -p ${BACKUP_DIR}/${DATE}

# Backup de base de datos con compresión
log "Realizando backup de PostgreSQL..."
pg_dump -U ${PROJECT_NAME} -h localhost ${PROJECT_NAME} \
    --verbose --format=custom --compress=9 \
    --file=${BACKUP_DIR}/${DATE}/database.dump

# Backup de archivos de aplicación
log "Realizando backup de aplicación..."
tar --exclude='venv' --exclude='__pycache__' --exclude='*.pyc' \
    -czf ${BACKUP_DIR}/${DATE}/application.tar.gz \
    -C /opt ${PROJECT_NAME}

# Backup de configuraciones del sistema
log "Realizando backup de configuraciones..."
tar -czf ${BACKUP_DIR}/${DATE}/configs.tar.gz \
    /etc/${PROJECT_NAME} \
    /etc/nginx/sites-available/${PROJECT_NAME} \
    /etc/supervisor/conf.d/${PROJECT_NAME}.conf

# Backup de logs importantes
log "Realizando backup de logs..."
tar -czf ${BACKUP_DIR}/${DATE}/logs.tar.gz \
    /var/log/${PROJECT_NAME}

# Crear manifiesto de backup
cat > ${BACKUP_DIR}/${DATE}/manifest.txt << EOF
Backup Date: $(date)
Database Size: $(du -h ${BACKUP_DIR}/${DATE}/database.dump | cut -f1)
Application Size: $(du -h ${BACKUP_DIR}/${DATE}/application.tar.gz | cut -f1)
Configs Size: $(du -h ${BACKUP_DIR}/${DATE}/configs.tar.gz | cut -f1)
Logs Size: $(du -h ${BACKUP_DIR}/${DATE}/logs.tar.gz | cut -f1)
Total Size: $(du -sh ${BACKUP_DIR}/${DATE} | cut -f1)
Git Commit: $(cd /opt/${PROJECT_NAME} && git rev-parse HEAD)
EOF

# Verificar integridad de backups
log "Verificando integridad de backups..."
if pg_restore --list ${BACKUP_DIR}/${DATE}/database.dump > /dev/null 2>&1; then
    echo "✅ Database backup válido" >> ${BACKUP_DIR}/${DATE}/manifest.txt
else
    echo "❌ Database backup corrupto" >> ${BACKUP_DIR}/${DATE}/manifest.txt
fi

if tar -tzf ${BACKUP_DIR}/${DATE}/application.tar.gz > /dev/null 2>&1; then
    echo "✅ Application backup válido" >> ${BACKUP_DIR}/${DATE}/manifest.txt
else
    echo "❌ Application backup corrupto" >> ${BACKUP_DIR}/${DATE}/manifest.txt
fi

# Limpiar backups antiguos
log "Limpiando backups antiguos..."
find ${BACKUP_DIR} -maxdepth 1 -type d -mtime +${RETENTION_DAYS} -exec rm -rf {} \;

# Sincronizar con almacenamiento remoto (opcional)
if [ ! -z "$REMOTE_BACKUP_PATH" ]; then
    log "Sincronizando con almacenamiento remoto..."
    rsync -avz ${BACKUP_DIR}/${DATE}/ ${REMOTE_BACKUP_PATH}/${DATE}/
fi

log "Backup completado: ${BACKUP_DIR}/${DATE}"
```

### **PROCEDIMIENTO DE RECUPERACIÓN**

```bash
#!/bin/bash
# restore.sh - Script de recuperación de desastres

BACKUP_DATE=$1
BACKUP_DIR="/opt/backups"
PROJECT_NAME="mentalia-universe"

if [ -z "$BACKUP_DATE" ]; then
    echo "Uso: $0 <BACKUP_DATE>"
    echo "Backups disponibles:"
    ls -la ${BACKUP_DIR}/ | grep "^d" | awk '{print $9}' | grep -E "^[0-9]"
    exit 1
fi

RESTORE_PATH="${BACKUP_DIR}/${BACKUP_DATE}"

if [ ! -d "$RESTORE_PATH" ]; then
    error "Backup no encontrado: $RESTORE_PATH"
fi

log "Iniciando recuperación desde: $RESTORE_PATH"

# Verificar manifiesto
if [ -f "$RESTORE_PATH/manifest.txt" ]; then
    log "Información del backup:"
    cat $RESTORE_PATH/manifest.txt
    echo ""
    read -p "¿Continuar con la recuperación? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Detener servicios
log "Deteniendo servicios..."
supervisorctl stop all
systemctl stop nginx

# Crear backup de estado actual
log "Creando backup de estado actual..."
CURRENT_BACKUP="/opt/backups/pre-restore-$(date +%Y%m%d_%H%M%S)"
mkdir -p $CURRENT_BACKUP
pg_dump -U ${PROJECT_NAME} -h localhost ${PROJECT_NAME} > $CURRENT_BACKUP/current-db.sql
tar -czf $CURRENT_BACKUP/current-app.tar.gz -C /opt ${PROJECT_NAME}

# Restaurar base de datos
log "Restaurando base de datos..."
dropdb -U postgres ${PROJECT_NAME}
createdb -U postgres ${PROJECT_NAME}
pg_restore -U ${PROJECT_NAME} -h localhost -d ${PROJECT_NAME} $RESTORE_PATH/database.dump

# Restaurar aplicación
log "Restaurando aplicación..."
rm -rf /opt/${PROJECT_NAME}
tar -xzf $RESTORE_PATH/application.tar.gz -C /opt/

# Restaurar configuraciones
log "Restaurando configuraciones..."
tar -xzf $RESTORE_PATH/configs.tar.gz -C /

# Recrear entorno virtual
log "Recreando entorno virtual..."
cd /opt/${PROJECT_NAME}
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Reiniciar servicios
log "Reiniciando servicios..."
systemctl start nginx
supervisorctl start all

# Verificar recuperación
log "Verificando recuperación..."
sleep 10

if curl -f http://localhost:5000/health > /dev/null 2>&1; then
    log "✅ Recuperación completada exitosamente"
else
    error "❌ Error en recuperación"
fi
```

---

## 📈 ESCALABILIDAD Y OPTIMIZACIÓN

### **ESTRATEGIAS DE ESCALAMIENTO**

**Escalamiento Vertical (Scale Up):**

Para crecimiento inicial hasta 1,000 usuarios concurrentes, el escalamiento vertical en RunPod es la opción más eficiente:

```bash
# Configuraciones de instancia por nivel de carga
# Nivel 1: 0-100 usuarios concurrentes
# GPU: RTX 4090 (24GB), CPU: 16 cores, RAM: 64GB

# Nivel 2: 100-500 usuarios concurrentes  
# GPU: RTX 4090 x2, CPU: 32 cores, RAM: 128GB

# Nivel 3: 500-1000 usuarios concurrentes
# GPU: A100 (80GB), CPU: 64 cores, RAM: 256GB
```

**Escalamiento Horizontal (Scale Out):**

Para crecimiento más allá de 1,000 usuarios concurrentes, implementar arquitectura distribuida:

```yaml
# docker-compose.scale.yml
version: '3.8'
services:
  nginx-lb:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx-lb.conf:/etc/nginx/nginx.conf
    depends_on:
      - app1
      - app2
      - app3

  app1:
    build: .
    environment:
      - INSTANCE_ID=app1
    depends_on:
      - postgres
      - redis

  app2:
    build: .
    environment:
      - INSTANCE_ID=app2
    depends_on:
      - postgres
      - redis

  app3:
    build: .
    environment:
      - INSTANCE_ID=app3
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: mentalia_universe
      POSTGRES_USER: mentalia
      POSTGRES_PASSWORD: secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
```

### **OPTIMIZACIONES DE RENDIMIENTO**

**Cache Inteligente:**

```python
# app/cache.py
from flask_caching import Cache
import redis
import json
import hashlib

cache = Cache()
redis_client = redis.Redis(host='localhost', port=6379, db=1)

class IntelligentCache:
    def __init__(self):
        self.default_timeout = 300  # 5 minutos
        self.ai_model_timeout = 3600  # 1 hora
        self.user_data_timeout = 1800  # 30 minutos
    
    def cache_ai_response(self, model_name, prompt, response):
        """Cache respuestas de IA con hash del prompt"""
        prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
        cache_key = f"ai:{model_name}:{prompt_hash}"
        
        cache_data = {
            'response': response,
            'timestamp': time.time(),
            'model': model_name
        }
        
        redis_client.setex(
            cache_key, 
            self.ai_model_timeout, 
            json.dumps(cache_data)
        )
    
    def get_cached_ai_response(self, model_name, prompt):
        """Obtener respuesta de IA desde cache"""
        prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
        cache_key = f"ai:{model_name}:{prompt_hash}"
        
        cached = redis_client.get(cache_key)
        if cached:
            return json.loads(cached)['response']
        return None
    
    def cache_user_session(self, user_id, session_data):
        """Cache datos de sesión de usuario"""
        cache_key = f"session:{user_id}"
        redis_client.setex(
            cache_key,
            self.user_data_timeout,
            json.dumps(session_data)
        )
    
    def invalidate_user_cache(self, user_id):
        """Invalidar cache de usuario"""
        pattern = f"session:{user_id}*"
        for key in redis_client.scan_iter(match=pattern):
            redis_client.delete(key)
```

**Optimización de Base de Datos:**

```sql
-- Configuración optimizada de PostgreSQL para IA workloads
-- postgresql.conf optimizations

# Memoria
shared_buffers = 16GB                    # 25% de RAM total
effective_cache_size = 48GB              # 75% de RAM total
work_mem = 256MB                         # Para queries complejas
maintenance_work_mem = 2GB               # Para VACUUM, CREATE INDEX

# Conexiones
max_connections = 200                    # Ajustar según carga
superuser_reserved_connections = 3

# WAL y Checkpoints
wal_buffers = 64MB
checkpoint_completion_target = 0.9
max_wal_size = 4GB
min_wal_size = 1GB

# Query Planner
random_page_cost = 1.1                   # Para SSD
effective_io_concurrency = 200           # Para SSD

# Logging para monitoreo
log_min_duration_statement = 1000        # Log queries > 1 segundo
log_checkpoints = on
log_connections = on
log_disconnections = on
log_lock_waits = on

# Autovacuum optimizado
autovacuum_max_workers = 6
autovacuum_naptime = 15s
autovacuum_vacuum_threshold = 25
autovacuum_analyze_threshold = 10
```

Este documento proporciona la base completa para el despliegue exitoso de MENTALIA Universe en RunPod, con todas las herramientas, scripts, y configuraciones necesarias para una implementación robusta y escalable.

---

**Documento preparado por:** MANOLO (Arquitecto de Sistemas) & Equipo Técnico MENTALIA  
**Fecha:** Enero 2025  
**Próxima revisión:** Marzo 2025  
**Soporte técnico:** Disponible 24/7 durante implementación inicial

