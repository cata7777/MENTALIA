# 🚀 RUNPOD DEPLOYMENT - ECOSISTEMA MENTALIA

## 🎯 CONFIGURACIÓN PARA RUNPOD

### Arquitectura de Despliegue

**MENTALIA está diseñado para despliegue modular en RunPod**, permitiendo escalamiento independiente de cada sistema según demanda y comercialización.

### Módulos de Despliegue

**1. MENTALIA UNIVERSE (Hub Central)**
- **Puerto:** 5000
- **Función:** Portal principal donde usuarios acceden a todas las apps
- **Recursos:** 4 vCPU, 8GB RAM, 50GB storage
- **Escalabilidad:** Auto-scaling 1-10 instancias

**2. CHAT MENTALIA (Como ChatGPT)**
- **Puerto:** 5001
- **Función:** Interfaz de chat con 87 agentes IA
- **Recursos:** 8 vCPU, 16GB RAM, 100GB storage
- **Escalabilidad:** Auto-scaling 2-20 instancias

**3. HIPERFOCO.COM (Presentación Socios)**
- **Puerto:** 5002
- **Función:** Página web para presentar a socios
- **Recursos:** 2 vCPU, 4GB RAM, 20GB storage
- **Escalabilidad:** Fijo, alta disponibilidad

**4. AGENDAS CLÍNICAS (Sistema Médico)**
- **Puerto:** 5003
- **Función:** Sistema médico interoperable
- **Recursos:** 6 vCPU, 12GB RAM, 200GB storage
- **Escalabilidad:** Auto-scaling 1-15 instancias

**5. DESPACHO LEGAL (Automatización Jurídica)**
- **Puerto:** 5004
- **Función:** Sistema legal automatizado
- **Recursos:** 4 vCPU, 8GB RAM, 100GB storage
- **Escalabilidad:** Auto-scaling 1-8 instancias

**6. FORMACIÓN LABORAL (OTEC)**
- **Puerto:** 5005
- **Función:** Plataforma educativa certificada
- **Recursos:** 6 vCPU, 12GB RAM, 150GB storage
- **Escalabilidad:** Auto-scaling 1-12 instancias

**7. MENTAL-IA ND (Herramientas Especializadas)**
- **Puerto:** 5006
- **Función:** Apps específicas para neurodivergentes
- **Recursos:** 4 vCPU, 8GB RAM, 80GB storage
- **Escalabilidad:** Auto-scaling 1-10 instancias

## 🐳 CONFIGURACIÓN DOCKER

### Docker Compose Principal

```yaml
version: '3.8'
services:
  mentalia-universe:
    build: ./universe
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://mentalia:password@db:5432/mentalia_universe
    depends_on:
      - db
      - redis
    
  chat-mentalia:
    build: ./chat
    ports:
      - "5001:5001"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - AGENTS_CONFIG_PATH=/app/config/87_agents.json
    depends_on:
      - db
      - redis
    
  hiperfoco-web:
    build: ./hiperfoco
    ports:
      - "5002:5002"
    environment:
      - FLASK_ENV=production
    
  agendas-clinicas:
    build: ./agendas_clinicas
    ports:
      - "5003:5003"
    environment:
      - MINSAL_API_KEY=${MINSAL_API_KEY}
      - HL7_FHIR_ENDPOINT=${HL7_ENDPOINT}
    depends_on:
      - db
    
  despacho-legal:
    build: ./despacho_legal
    ports:
      - "5004:5004"
    environment:
      - LEGAL_DB_URL=postgresql://mentalia:password@db:5432/mentalia_legal
    depends_on:
      - db
    
  formacion-laboral:
    build: ./formacion_laboral
    ports:
      - "5005:5005"
    environment:
      - SENCE_API_KEY=${SENCE_API_KEY}
      - OTEC_CERTIFICATION=${OTEC_CERT}
    depends_on:
      - db
    
  mental-ia-nd:
    build: ./mental_ia_nd
    ports:
      - "5006:5006"
    environment:
      - ND_PROFILES_DB=postgresql://mentalia:password@db:5432/mentalia_nd
    depends_on:
      - db
    
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=mentalia
      - POSTGRES_USER=mentalia
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    
  redis:
    image: redis:7
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

### Dockerfiles Individuales

**Dockerfile Base (para todos los servicios):**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

## ⚙️ CONFIGURACIÓN DE RUNPOD

### Variables de Entorno Requeridas

```bash
# APIs Externas
OPENAI_API_KEY=sk-...
MINSAL_API_KEY=...
SENCE_API_KEY=...
HL7_ENDPOINT=...

# Base de Datos
DATABASE_URL=postgresql://mentalia:password@db:5432/mentalia
REDIS_URL=redis://redis:6379

# Configuración de Aplicación
FLASK_ENV=production
SECRET_KEY=...
JWT_SECRET_KEY=...

# Certificaciones
OTEC_CERT=...
MINSAL_CERT=...
```

### Recursos Recomendados por Módulo

**Configuración Mínima (Desarrollo):**
- **CPU Total:** 32 vCPU
- **RAM Total:** 64GB
- **Storage Total:** 500GB
- **Costo mensual estimado:** USD $800

**Configuración Producción (Escalado):**
- **CPU Total:** 128 vCPU
- **RAM Total:** 256GB
- **Storage Total:** 2TB
- **Costo mensual estimado:** USD $3,200

**Configuración Enterprise (Máximo):**
- **CPU Total:** 512 vCPU
- **RAM Total:** 1TB
- **Storage Total:** 10TB
- **Costo mensual estimado:** USD $12,800

## 🔧 SCRIPTS DE DESPLIEGUE

### Script de Inicio Automático

```bash
#!/bin/bash
# start_mentalia.sh

echo "🚀 Iniciando Ecosistema MENTALIA en RunPod..."

# Verificar variables de entorno
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ Error: OPENAI_API_KEY no configurada"
    exit 1
fi

# Iniciar servicios base
echo "📊 Iniciando base de datos..."
docker-compose up -d db redis

# Esperar que la base de datos esté lista
echo "⏳ Esperando base de datos..."
sleep 30

# Iniciar aplicaciones principales
echo "🌟 Iniciando MENTALIA UNIVERSE..."
docker-compose up -d mentalia-universe

echo "💬 Iniciando CHAT MENTALIA..."
docker-compose up -d chat-mentalia

echo "🌐 Iniciando HIPERFOCO.COM..."
docker-compose up -d hiperfoco-web

# Iniciar sistemas especializados
echo "🏥 Iniciando Agendas Clínicas..."
docker-compose up -d agendas-clinicas

echo "⚖️ Iniciando Despacho Legal..."
docker-compose up -d despacho-legal

echo "🎓 Iniciando Formación Laboral..."
docker-compose up -d formacion-laboral

echo "🧠 Iniciando Mental-IA ND..."
docker-compose up -d mental-ia-nd

# Verificar estado
echo "✅ Verificando estado de servicios..."
docker-compose ps

echo "🎉 Ecosistema MENTALIA iniciado exitosamente!"
echo "🌐 MENTALIA UNIVERSE: http://localhost:5000"
echo "💬 CHAT MENTALIA: http://localhost:5001"
echo "🌟 HIPERFOCO.COM: http://localhost:5002"
```

### Script de Monitoreo

```bash
#!/bin/bash
# monitor_mentalia.sh

echo "📊 Monitoreo Ecosistema MENTALIA"
echo "================================"

# Estado de servicios
echo "🔍 Estado de servicios:"
docker-compose ps

# Uso de recursos
echo ""
echo "💻 Uso de recursos:"
docker stats --no-stream

# Logs recientes
echo ""
echo "📝 Logs recientes:"
docker-compose logs --tail=10

# Conectividad
echo ""
echo "🌐 Verificando conectividad:"
curl -s http://localhost:5000/api/health || echo "❌ UNIVERSE offline"
curl -s http://localhost:5001/api/health || echo "❌ CHAT offline"
curl -s http://localhost:5002/api/health || echo "❌ HIPERFOCO offline"

echo ""
echo "✅ Monitoreo completado"
```

## 🔄 INTERCONEXIÓN ENTRE MÓDULOS

### API Gateway Central

**Función:** Coordinar comunicación entre todos los módulos
**Puerto:** 5100
**Responsabilidades:**
- Routing inteligente entre servicios
- Autenticación y autorización centralizada
- Rate limiting y throttling
- Logging y monitoreo centralizado

### Base de Datos Compartida

**PostgreSQL Principal:**
- **mentalia_universe:** Datos de usuarios y perfiles
- **mentalia_agents:** Configuraciones de 87 agentes IA
- **mentalia_clinical:** Datos médicos y agendas
- **mentalia_legal:** Información jurídica y casos
- **mentalia_education:** Datos educativos y certificaciones

### Sistema de Comunicación Inter-Módulos

**Redis para Messaging:**
- Comunicación en tiempo real entre módulos
- Cache de sesiones de usuario
- Queue de tareas asíncronas
- Sincronización de estado

---

**Preparado por:** Ecosistema MENTALIA  
**Fecha:** Agosto 2025  
**Estado:** Listo para deploy en RunPod  
**Escalabilidad:** Configuración modular completa

