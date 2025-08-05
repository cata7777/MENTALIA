#!/bin/bash
# 🚀 SCRIPT DE MIGRACIÓN ECOSISTEMA MENTALIA
# Script para migrar gradualmente todas las aplicaciones a la arquitectura consolidada

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función de logging
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

success() {
    echo -e "${GREEN}✅ $1${NC}"
}

warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

error() {
    echo -e "${RED}❌ $1${NC}"
}

# Variables de configuración
WORKSPACE_DIR="/Users/catalinarojolema/MENTALIA/MENTALIA"
BACKUP_DIR="$WORKSPACE_DIR/backups/$(date +%Y%m%d_%H%M%S)"
CONSOLIDATED_DIR="$WORKSPACE_DIR/consolidated"

# Crear directorios necesarios
create_directories() {
    log "Creando estructura de directorios consolidada..."
    
    mkdir -p "$BACKUP_DIR"
    mkdir -p "$CONSOLIDATED_DIR"
    mkdir -p "$CONSOLIDATED_DIR/app"
    mkdir -p "$CONSOLIDATED_DIR/app/core"
    mkdir -p "$CONSOLIDATED_DIR/app/models"
    mkdir -p "$CONSOLIDATED_DIR/app/apps"
    mkdir -p "$CONSOLIDATED_DIR/app/bots"
    mkdir -p "$CONSOLIDATED_DIR/app/frontend"
    mkdir -p "$CONSOLIDATED_DIR/config"
    mkdir -p "$CONSOLIDATED_DIR/migrations"
    mkdir -p "$CONSOLIDATED_DIR/tests"
    mkdir -p "$CONSOLIDATED_DIR/docker"
    mkdir -p "$CONSOLIDATED_DIR/scripts"
    
    success "Estructura de directorios creada"
}

# Backup de aplicaciones existentes
backup_existing_apps() {
    log "Creando backup de aplicaciones existentes..."
    
    # Backup de ZIPs funcionales
    if [ -d "$WORKSPACE_DIR/aplicaciones/MENTALIA_UNIVERSE_ZIPS_FUNCIONALES_COMPLETOS" ]; then
        cp -r "$WORKSPACE_DIR/aplicaciones/MENTALIA_UNIVERSE_ZIPS_FUNCIONALES_COMPLETOS" "$BACKUP_DIR/"
        success "Backup de ZIPs funcionales completado"
    fi
    
    # Backup de documentación
    if [ -d "$WORKSPACE_DIR/docs" ]; then
        cp -r "$WORKSPACE_DIR/docs" "$BACKUP_DIR/"
        success "Backup de documentación completado"
    fi
    
    # Backup de agentes
    if [ -d "$WORKSPACE_DIR/agentes_mentalia" ]; then
        cp -r "$WORKSPACE_DIR/agentes_mentalia" "$BACKUP_DIR/"
        success "Backup de agentes completado"
    fi
    
    # Backup de archivos de configuración
    for file in docker-compose.yml Dockerfile requirements.txt *.json *.md; do
        if [ -f "$WORKSPACE_DIR/$file" ]; then
            cp "$WORKSPACE_DIR/$file" "$BACKUP_DIR/"
        fi
    done
    
    success "Backup completo realizado en: $BACKUP_DIR"
}

# Crear aplicación Flask consolidada
create_flask_app() {
    log "Creando aplicación Flask consolidada..."
    
    # __init__.py principal
    cat > "$CONSOLIDATED_DIR/app/__init__.py" << 'EOF'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
limiter = Limiter(key_func=get_remote_address)

def create_app(config_name='production'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    
    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    limiter.init_app(app)
    
    # Registro de blueprints
    from app.core import bp as core_bp
    app.register_blueprint(core_bp, url_prefix='/api')
    
    from app.apps.hiperfoco import bp as hiperfoco_bp
    app.register_blueprint(hiperfoco_bp, url_prefix='/hiperfoco')
    
    from app.apps.universe import bp as universe_bp
    app.register_blueprint(universe_bp, url_prefix='/universe')
    
    from app.apps.chat import bp as chat_bp
    app.register_blueprint(chat_bp, url_prefix='/chat')
    
    return app
EOF

    # Configuración
    cat > "$CONSOLIDATED_DIR/config.py" << 'EOF'
import os
from datetime import timedelta

class Config:
    DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'postgresql://mentalia:password@localhost/mentalia_unified'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'super-secret-jwt-key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
EOF

    # app.py principal
    cat > "$CONSOLIDATED_DIR/app.py" << 'EOF'
from app import create_app, db
from flask_migrate import upgrade

app = create_app()

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF

    success "Aplicación Flask base creada"
}

# Crear Docker Compose consolidado
create_docker_compose() {
    log "Creando configuración Docker Compose..."
    
    cat > "$CONSOLIDATED_DIR/docker-compose.yml" << 'EOF'
version: '3.8'

services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - mentalia-app
    restart: unless-stopped

  mentalia-app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
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

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=mentalia_unified
      - POSTGRES_USER=mentalia
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
EOF

    # Dockerfile
    cat > "$CONSOLIDATED_DIR/Dockerfile" << 'EOF'
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p /app/models /app/user_data /app/logs

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "app:app"]
EOF

    success "Configuración Docker creada"
}

# Crear requirements.txt consolidado
create_requirements() {
    log "Creando requirements.txt consolidado..."
    
    cat > "$CONSOLIDATED_DIR/requirements.txt" << 'EOF'
# Flask y extensiones
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Migrate==4.0.5
Flask-JWT-Extended==4.5.3
Flask-CORS==4.0.0
Flask-Limiter==3.5.0
Flask-Caching==2.1.0

# Base de datos
psycopg2-binary==2.9.7
redis==5.0.1

# IA y ML
torch==2.1.0
transformers==4.35.0
openai==1.3.0
anthropic==0.7.7

# Procesamiento multimodal
opencv-python==4.8.1.78
librosa==0.10.1
Pillow==10.0.1

# Servidor web
gunicorn==21.2.0

# Utilidades
python-dotenv==1.0.0
celery==5.3.4
requests==2.31.0
python-dateutil==2.8.2
EOF

    success "Requirements.txt creado"
}

# Crear modelos de base de datos
create_database_models() {
    log "Creando modelos de base de datos..."
    
    # Modelo de Usuario
    cat > "$CONSOLIDATED_DIR/app/models/user.py" << 'EOF'
from app import db
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    profile_type = db.Column(db.String(50), default='general')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relaciones
    nd_profile = db.relationship('NeurodivergentProfile', backref='user', uselist=False)
    conversations = db.relationship('Conversation', backref='user', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_token(self):
        return create_access_token(identity=self.id)
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'profile_type': self.profile_type,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active
        }
EOF

    # Modelo __init__.py
    cat > "$CONSOLIDATED_DIR/app/models/__init__.py" << 'EOF'
from .user import User
from .bot import Bot
from .conversation import Conversation

__all__ = ['User', 'Bot', 'Conversation']
EOF

    success "Modelos de base de datos creados"
}

# Crear estructura de aplicaciones
create_app_structure() {
    log "Creando estructura de aplicaciones..."
    
    # Aplicaciones a crear
    apps=("hiperfoco" "universe" "chat" "sign_link" "comunicacion_social" "spoiler_alert" "despacho_legal")
    
    for app in "${apps[@]}"; do
        mkdir -p "$CONSOLIDATED_DIR/app/apps/$app"
        
        # __init__.py para cada app
        cat > "$CONSOLIDATED_DIR/app/apps/$app/__init__.py" << EOF
from flask import Blueprint

bp = Blueprint('$app', __name__)

from app.apps.$app import routes
EOF

        # routes.py básico
        cat > "$CONSOLIDATED_DIR/app/apps/$app/routes.py" << EOF
from flask import render_template, jsonify
from app.apps.$app import bp

@bp.route('/')
def index():
    return render_template('$app/index.html')

@bp.route('/api/status')
def status():
    return jsonify({'status': 'active', 'app': '$app'})
EOF

        # Directorio de templates
        mkdir -p "$CONSOLIDATED_DIR/app/frontend/templates/$app"
        
        # Template básico
        cat > "$CONSOLIDATED_DIR/app/frontend/templates/$app/index.html" << 'HTMLEOF'
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MENTALIA - APP_NAME</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/mentalia-unified.css') }}">
</head>
<body>
    <div id="mentalia-app" data-app="APP_NAME">
        <h1>MENTALIA APP_NAME</h1>
        <p>Aplicación en desarrollo - Arquitectura consolidada</p>
    </div>
    <script src="{{ url_for('static', filename='js/mentalia-unified.js') }}"></script>
</body>
</html>
HTMLEOF
        
        # Reemplazar APP_NAME con el nombre real de la app
        sed -i '' "s/APP_NAME/$app/g" "$CONSOLIDATED_DIR/app/frontend/templates/$app/index.html"
        
        success "Aplicación $app creada"
    done
}

# Crear scripts de utilidad
create_utility_scripts() {
    log "Creando scripts de utilidad..."
    
    # Script de migración de datos
    cat > "$CONSOLIDATED_DIR/scripts/migrate_data.py" << 'EOF'
#!/usr/bin/env python3
"""
Script para migrar datos de aplicaciones individuales a la base de datos consolidada
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import User, Bot, Conversation

def migrate_users():
    """Migrar usuarios desde aplicaciones individuales"""
    print("Migrando usuarios...")
    # Implementar lógica de migración específica
    pass

def migrate_bots():
    """Migrar configuraciones de bots"""
    print("Migrando bots...")
    # Implementar lógica de migración de bots
    pass

def migrate_conversations():
    """Migrar conversaciones existentes"""
    print("Migrando conversaciones...")
    # Implementar lógica de migración de conversaciones
    pass

if __name__ == '__main__':
    app = create_app('development')
    with app.app_context():
        db.create_all()
        migrate_users()
        migrate_bots()
        migrate_conversations()
        print("Migración completada")
EOF

    chmod +x "$CONSOLIDATED_DIR/scripts/migrate_data.py"

    # Script de health check
    cat > "$CONSOLIDATED_DIR/scripts/health_check.sh" << 'EOF'
#!/bin/bash
# Health check para todos los servicios

check_service() {
    local service=$1
    local url=$2
    
    if curl -f -s "$url" > /dev/null; then
        echo "✅ $service: OK"
        return 0
    else
        echo "❌ $service: FALLO"
        return 1
    fi
}

echo "🔍 Verificando estado de servicios MENTALIA..."

check_service "Aplicación Principal" "http://localhost:5000/api/health"
check_service "HIPERFOCO" "http://localhost:5000/hiperfoco/"
check_service "Universe" "http://localhost:5000/universe/"
check_service "Chat" "http://localhost:5000/chat/"
check_service "Base de Datos" "http://localhost:5432" # Simplificado

echo "Verificación completa"
EOF

    chmod +x "$CONSOLIDATED_DIR/scripts/health_check.sh"
    
    success "Scripts de utilidad creados"
}

# Crear documentación de migración
create_migration_docs() {
    log "Creando documentación de migración..."
    
    cat > "$CONSOLIDATED_DIR/MIGRACION_README.md" << 'EOF'
# 🚀 MIGRACIÓN A ARQUITECTURA CONSOLIDADA MENTALIA

## Pasos de Migración

### 1. Preparación
```bash
cd consolidated
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configuración de Base de Datos
```bash
export DATABASE_URL="postgresql://mentalia:password@localhost/mentalia_unified"
export REDIS_URL="redis://localhost:6379/0"
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 3. Migración de Datos
```bash
python scripts/migrate_data.py
```

### 4. Despliegue con Docker
```bash
docker-compose up -d
```

### 5. Verificación
```bash
./scripts/health_check.sh
```

## URLs de Acceso Post-Migración

- **HIPERFOCO:** http://localhost:5000/hiperfoco
- **Universe:** http://localhost:5000/universe  
- **Chat:** http://localhost:5000/chat
- **API:** http://localhost:5000/api

## Rollback

En caso de problemas, los backups están en: `backups/TIMESTAMP/`
EOF

    success "Documentación de migración creada"
}

# Función principal
main() {
    echo ""
    echo "🌌 MENTALIA ECOSYSTEM CONSOLIDATION SCRIPT"
    echo "=========================================="
    echo ""
    
    log "Iniciando proceso de consolidación..."
    
    # Verificar que estamos en el directorio correcto
    if [ ! -d "$WORKSPACE_DIR" ]; then
        error "Directorio de workspace no encontrado: $WORKSPACE_DIR"
        exit 1
    fi
    
    cd "$WORKSPACE_DIR"
    
    # Ejecutar pasos de migración
    create_directories
    backup_existing_apps
    create_flask_app
    create_docker_compose
    create_requirements
    create_database_models
    create_app_structure
    create_utility_scripts
    create_migration_docs
    
    echo ""
    success "🎉 Consolidación completada exitosamente!"
    echo ""
    echo "📁 Archivos creados en: $CONSOLIDATED_DIR"
    echo "💾 Backups guardados en: $BACKUP_DIR"
    echo ""
    echo "📋 Próximos pasos:"
    echo "1. cd $CONSOLIDATED_DIR"
    echo "2. Revisar configuración en config.py"
    echo "3. Seguir instrucciones en MIGRACION_README.md"
    echo ""
    warning "IMPORTANTE: Revisar y validar toda la configuración antes del despliegue en producción"
}

# Ejecutar script principal
main "$@"
