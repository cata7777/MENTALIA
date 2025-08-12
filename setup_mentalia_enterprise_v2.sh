nano setup_mentalia_enterprise_v2.s#!/bin/bash
# ===========================================
# 🚀 SETUP COMPLETO MENTALIA ENTERPRISE v2.0
# ===========================================

set -e  # Salir si cualquier comando falla
set -u  # Error si variable no definida

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 INICIANDO SETUP MENTALIA ENTERPRISE v2.0${NC}"

# Verificar requisitos del sistema
check_requirements() {
    echo -e "${YELLOW}📋 Verificando requisitos del sistema...${NC}"
    
    # Verificar Docker
    if ! command -v docker &> /dev/null; then
        echo -e "${RED}❌ Docker no está instalado${NC}"
        exit 1
    fi
    
    # Verificar Docker Compose
    if ! command -v docker-compose &> /dev/null; then
        echo -e "${RED}❌ Docker Compose no está instalado${NC}"
        exit 1
    fi
    
    # Verificar espacio en disco (mínimo 10GB)
    available_space=$(df . | tail -1 | awk '{print $4}')
    min_space=10485760  # 10GB en KB
    if [ "$available_space" -lt "$min_space" ]; then
        echo -e "${RED}❌ Espacio insuficiente en disco (mínimo 10GB requerido)${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Todos los requisitos cumplidos${NC}"
}

# Crear backup de archivos existentes
create_backup() {
    if [ -d "MENTALIA-ENTERPRISE" ]; then
        echo -e "${YELLOW}📦 Creando backup de instalación anterior...${NC}"
        mv MENTALIA-ENTERPRISE "MENTALIA-ENTERPRISE-backup-$(date +%Y%m%d_%H%M%S)"
    fi
}

# Función principal de setup
main_setup() {
    echo -e "${BLUE}📁 Creando estructura enterprise...${NC}"
    
    # 1. Crear estructura completa
    mkdir -p MENTALIA-ENTERPRISE/{deployment,containers,documentation,testing,data,logs,config,secrets}
    
    # Crear subdirectorios de datos
    mkdir -p MENTALIA-ENTERPRISE/data/{clinico,ai-models,cache,uploads,exports}
    
    # Crear subdirectorios de logs
    mkdir -p MENTALIA-ENTERPRISE/logs/{application,access,error,debug}
    
    # 2. Mover archivos CON VERIFICACIÓN DE EXISTENCIA
    echo -e "${BLUE}📂 Organizando archivos del ecosistema...${NC}"
    
    # Verificar y mover archivos backups
    if [ -d "./backups/20250804_224937" ]; then
        cp -r ./backups/20250804_224937/* ./MENTALIA-ENTERPRISE/containers/ 2>/dev/null || echo -e "${YELLOW}⚠️ Algunos archivos de backup no se pudieron copiar${NC}"
    else
        echo -e "${YELLOW}⚠️ Directorio backups no encontrado, creando estructura base${NC}"
    fi
    
    # Verificar y mover agentes
    if [ -d "./agentes_mentalia" ]; then
        cp -r ./agentes_mentalia ./MENTALIA-ENTERPRISE/containers/ai-agents
    else
        mkdir -p ./MENTALIA-ENTERPRISE/containers/ai-agents
        echo -e "${YELLOW}⚠️ Directorio agentes_mentalia no encontrado, creando estructura vacía${NC}"
    fi
    
    # Verificar y mover agenda clínica
    if [ -f "./AGENDA_CLINICA_INTEROPERABLE_CHILECOMPRA.md" ]; then
        mkdir -p ./MENTALIA-ENTERPRISE/containers/agenda-clinica
        cp ./AGENDA_CLINICA_INTEROPERABLE_CHILECOMPRA.md ./MENTALIA-ENTERPRISE/containers/agenda-clinica/
    else
        echo -e "${YELLOW}⚠️ Archivo agenda clínica no encontrado${NC}"
    fi
}

# Crear Dockerfiles optimizados
create_dockerfiles() {
    echo -e "${BLUE}🐳 Creando Dockerfiles optimizados...${NC}"
    
    modules=("agenda-clinica" "chilecompra-scraper" "ai-agents" "motor-comunicacional" "web-platform" "apps-especificas")
    
    for module in "${modules[@]}"; do
        mkdir -p "./MENTALIA-ENTERPRISE/containers/$module"
        
        cat <<DOCKER > "./MENTALIA-ENTERPRISE/containers/$module/Dockerfile"
# Dockerfile optimizado para $module
FROM python:3.11-slim

# Metadatos
LABEL maintainer="MENTALIA Enterprise <enterprise@mentalia.ai>"
LABEL version="2.0"
LABEL description="$module container for MENTALIA Enterprise"

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV MODULE_NAME=$module

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \\
    build-essential \\
    curl \\
    git \\
    && rm -rf /var/lib/apt/lists/*

# Crear usuario no-root para seguridad
RUN groupadd -r mentalia && useradd -r -g mentalia mentalia

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements primero (cache de Docker)
COPY requirements*.txt ./
RUN pip install --no-cache-dir --upgrade pip && \\
    pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt found"

# Copiar código fuente
COPY . .

# Cambiar ownership a usuario mentalia
RUN chown -R mentalia:mentalia /app

# Cambiar a usuario no-root
USER mentalia

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1

# Puerto por defecto
EXPOSE 8000

# Comando por defecto
CMD ["python", "main.py"]
DOCKER
    done
}

# Crear archivo .env completo
create_env_file() {
    echo -e "${BLUE}⚙️ Creando configuración de entorno...${NC}"
    
    cat <<ENV > MENTALIA-ENTERPRISE/.env.example
# ===========================================
# 🔧 CONFIGURACIÓN MENTALIA ENTERPRISE
# ===========================================

# Configuración general
NODE_ENV=production
LOG_LEVEL=info
DEBUG=false

# APIs y Claves
CHILECOMPRA_API_KEY=tu_api_key_chilecompra_aqui
OPENAI_API_KEY=tu_openai_key_aqui
ANTHROPIC_API_KEY=tu_anthropic_key_aqui

# Base de datos
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mentalia_enterprise
DB_USER=mentalia
DB_PASSWORD=secure_password_here

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=redis_password_here

# Configuración MINSAL
MINSAL_INTEGRATION=ENABLED
MINSAL_API_URL=https://api.minsal.cl
MINSAL_TIMEOUT=30000

# ChileCompra
SCRAPING_INTERVAL=3600
MAX_CONCURRENT_REQUESTS=10
REQUEST_DELAY=1000

# IA y GPU
GPU_MEMORY=24GB
AGENTS_COUNT=87
SISTEMA_7D=ENABLED
MODEL_CACHE_SIZE=10GB

# Motor Comunicacional
MULTIMODAL_ANALYSIS=FULL
MICROEXPRESSIONS=ENABLED
FACIAL_RECOGNITION=ENABLED
VOICE_ANALYSIS=ENABLED

# Aplicaciones específicas
BLU_TERAPIA=ENABLED
COMUNICACION_MULTIMODAL=ENABLED
APP_ESPEJO=ENABLED
FIRMA_ELECTRONICA=ENABLED

# Seguridad
JWT_SECRET=your_jwt_secret_256_bit_key_here
ENCRYPTION_KEY=your_encryption_key_here
CORS_ORIGIN=*
RATE_LIMIT=100

# Monitoreo
PROMETHEUS_ENABLED=true
GRAFANA_ENABLED=true
HEALTH_CHECK_INTERVAL=30

# Volúmenes y paths
DATA_PATH=/app/data
LOGS_PATH=/app/logs
CACHE_PATH=/app/cache
UPLOADS_PATH=/app/uploads

# Networking
PROXY_ENABLED=false
SSL_ENABLED=false
DOMAIN=localhost
ENV
}

# Crear docker-compose.yml robusto
create_docker_compose() {
    echo -e "${BLUE}🐙 Creando Docker Compose enterprise...${NC}"
    
    mkdir -p MENTALIA-ENTERPRISE/deployment
    
    cat <<'COMPOSE' > MENTALIA-ENTERPRISE/deployment/docker-compose.yml
version: '3.8'

networks:
  mentalia-network:
    driver: bridge

volumes:
  postgres-data:
  redis-data:
  app-data:
  logs-data:

services:
  # Base de datos PostgreSQL
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: ${DB_NAME:-mentalia_enterprise}
      POSTGRES_USER: ${DB_USER:-mentalia}
      POSTGRES_PASSWORD: ${DB_PASSWORD:-secure_password}
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ../data:/backup
    ports:
      - "5432:5432"
    networks:
      - mentalia-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER:-mentalia}"]
      interval: 30s
      timeout: 10s
      retries: 5

  # Redis para caché
  redis:
    image: redis:7-alpine
    command: redis-server --requirepass ${REDIS_PASSWORD:-redis_password}
    volumes:
      - redis-data:/data
    ports:
      - "6379:6379"
    networks:
      - mentalia-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "--raw", "incr", "ping"]
      interval: 30s
      timeout: 10s
      retries: 5

  # Nginx como proxy reverso
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ../config/nginx.conf:/etc/nginx/nginx.conf:ro
      - ../logs/nginx:/var/log/nginx
    depends_on:
      - mentalia-web
      - mentalia-core-clinico
    networks:
      - mentalia-network
    restart: unless-stopped

  # Core clínico
  mentalia-core-clinico:
    build: ../containers/agenda-clinica
    environment:
      - MODE=PRODUCTION
      - MINSAL_INTEGRATION=${MINSAL_INTEGRATION:-ENABLED}
      - DB_HOST=postgres
      - REDIS_HOST=redis
    volumes:
      - app-data:/app/data
      - logs-data:/app/logs
    ports:
      - "8001:8000"
    depends_on:
      - postgres
      - redis
    networks:
      - mentalia-network
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 2G
        reservations:
          memory: 1G

  # ChileCompra Engine
  chilecompra-engine:
    build: ../containers/chilecompra-scraper
    environment:
      - CHILECOMPRA_API_KEY=${CHILECOMPRA_API_KEY}
      - SCRAPING_INTERVAL=${SCRAPING_INTERVAL:-3600}
      - DB_HOST=postgres
      - REDIS_HOST=redis
    volumes:
      - app-data:/app/data
      - logs-data:/app/logs
    ports:
      - "8002:8000"
    depends_on:
      - postgres
      - redis
    networks:
      - mentalia-network
    restart: unless-stopped

  # IA Agents Hub
  mentalia-ai-hub:
    build: ../containers/ai-agents
    environment:
      - GPU_MEMORY=${GPU_MEMORY:-24GB}
      - AGENTS_COUNT=${AGENTS_COUNT:-87}
      - SISTEMA_7D=${SISTEMA_7D:-ENABLED}
      - DB_HOST=postgres
      - REDIS_HOST=redis
    volumes:
      - app-data:/app/data
      - logs-data:/app/logs
      - ../data/ai-models:/app/models
    ports:
      - "8003:8000"
    depends_on:
      - postgres
      - redis
    networks:
      - mentalia-network
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  # Motor Comunicacional
  motor-comunicacional:
    build: ../containers/motor-comunicacional
    environment:
      - MULTIMODAL_ANALYSIS=${MULTIMODAL_ANALYSIS:-FULL}
      - MICROEXPRESSIONS=${MICROEXPRESSIONS:-ENABLED}
      - DB_HOST=postgres
      - REDIS_HOST=redis
    volumes:
      - app-data:/app/data
      - logs-data:/app/logs
    ports:
      - "8004:8000"
    depends_on:
      - postgres
      - redis
    networks:
      - mentalia-network
    restart: unless-stopped

  # Web Platform
  mentalia-web:
    build: ../containers/web-platform
    environment:
      - NODE_ENV=production
      - DB_HOST=postgres
      - REDIS_HOST=redis
    volumes:
      - app-data:/app/data
      - logs-data:/app/logs
    ports:
      - "8005:3000"
    depends_on:
      - mentalia-core-clinico
      - mentalia-ai-hub
      - postgres
      - redis
    networks:
      - mentalia-network
    restart: unless-stopped

  # Apps Ecosystem
  apps-ecosystem:
    build: ../containers/apps-especificas
    environment:
      - BLU_TERAPIA=${BLU_TERAPIA:-ENABLED}
      - COMUNICACION_MULTIMODAL=${COMUNICACION_MULTIMODAL:-ENABLED}
      - APP_ESPEJO=${APP_ESPEJO:-ENABLED}
      - DB_HOST=postgres
      - REDIS_HOST=redis
    volumes:
      - app-data:/app/data
      - logs-data:/app/logs
    ports:
      - "8006:8000"
    depends_on:
      - postgres
      - redis
    networks:
      - mentalia-network
    restart: unless-stopped

  # Prometheus para monitoreo
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ../config/prometheus.yml:/etc/prometheus/prometheus.yml
    networks:
      - mentalia-network
    restart: unless-stopped

  # Grafana para dashboards
  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin123
    volumes:
      - ../config/grafana:/etc/grafana/provisioning
    depends_on:
      - prometheus
    networks:
      - mentalia-network
    restart: unless-stopped
COMPOSE
}

# Crear scripts de gestión
create_management_scripts() {
    echo -e "${BLUE}📝 Creando scripts de gestión...${NC}"
    
    # Script de inicio mejorado
    cat <<'SH' > MENTALIA-ENTERPRISE/run_enterprise.sh
#!/bin/bash
set -e

echo "🚀 Iniciando MENTALIA ENTERPRISE..."

# Verificar archivo .env
if [ ! -f ".env" ]; then
    echo "❌ Archivo .env no encontrado. Copiando .env.example..."
    cp .env.example .env
    echo "⚠️ Por favor, edita el archivo .env con tus configuraciones"
    exit 1
fi

# Verificar Docker
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker no está corriendo"
    exit 1
fi

cd deployment
echo "🐳 Iniciando contenedores..."
docker-compose up --build -d

echo "📊 Verificando estado de servicios..."
sleep 10
docker-compose ps

echo "✅ MENTALIA Enterprise iniciado correctamente"
echo "🌐 Accesos:"
echo "  - Web Platform: http://localhost:8005"
echo "  - Core Clínico: http://localhost:8001"
echo "  - IA Hub: http://localhost:8003"
echo "  - Grafana: http://localhost:3000 (admin/admin123)"
SH

    # Script de parada
    cat <<'SH' > MENTALIA-ENTERPRISE/stop_enterprise.sh
#!/bin/bash
echo "🛑 Deteniendo MENTALIA Enterprise..."
cd deployment
docker-compose down
echo "✅ Servicios detenidos"
SH

    # Script de logs
    cat <<'SH' > MENTALIA-ENTERPRISE/logs_enterprise.sh
#!/bin/bash
cd deployment
echo "📋 Logs en tiempo real (Ctrl+C para salir):"
docker-compose logs -f
SH

    # Script de backup
    cat <<'SH' > MENTALIA-ENTERPRISE/backup_enterprise.sh
#!/bin/bash
BACKUP_DIR="backups/$(date +%Y%m%d_%H%M%S)"
echo "📦 Creando backup en $BACKUP_DIR..."
mkdir -p "$BACKUP_DIR"
cd deployment
docker-compose exec postgres pg_dump -U mentalia mentalia_enterprise > "../$BACKUP_DIR/database.sql"
cp -r ../data "$BACKUP_DIR/"
echo "✅ Backup completado en $BACKUP_DIR"
SH

    # Hacer scripts ejecutables
    chmod +x MENTALIA-ENTERPRISE/*.sh
}

# Crear configuraciones adicionales
create_additional_configs() {
    echo -e "${BLUE}⚙️ Creando configuraciones adicionales...${NC}"
    
    mkdir -p MENTALIA-ENTERPRISE/config
    
    # Nginx config
    cat <<'NGINX' > MENTALIA-ENTERPRISE/config/nginx.conf
events {
    worker_connections 1024;
}

http {
    upstream mentalia_web {
        server mentalia-web:3000;
    }
    
    upstream mentalia_api {
        server mentalia-core-clinico:8000;
    }
    
    server {
        listen 80;
        server_name localhost;
        
        location / {
            proxy_pass http://mentalia_web;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
        
        location /api/ {
            proxy_pass http://mentalia_api;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
NGINX

    # Prometheus config
    cat <<'PROMETHEUS' > MENTALIA-ENTERPRISE/config/prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'mentalia-services'
    static_configs:
      - targets: ['mentalia-core-clinico:8000', 'mentalia-ai-hub:8000']
PROMETHEUS
}

# Función principal
main() {
    echo -e "${GREEN}🎯 INICIANDO SETUP MENTALIA ENTERPRISE v2.0${NC}"
    
    check_requirements
    create_backup
    main_setup
    create_dockerfiles
    create_env_file
    create_docker_compose
    create_management_scripts
    create_additional_configs
    
    echo -e "${GREEN}✅ SETUP COMPLETADO EXITOSAMENTE${NC}"
    echo -e "${BLUE}📋 PRÓXIMOS PASOS:${NC}"
    echo -e "   1. ${YELLOW}cd MENTALIA-ENTERPRISE${NC}"
    echo -e "   2. ${YELLOW}cp .env.example .env${NC}"
    echo -e "   3. ${YELLOW}nano .env${NC} (editar configuración)"
    echo -e "   4. ${YELLOW}./run_enterprise.sh${NC}"
    echo ""
    echo -e "${GREEN}🚀 MENTALIA Enterprise estará disponible en http://localhost${NC}"
}

# Ejecutar función principal
main "$@"