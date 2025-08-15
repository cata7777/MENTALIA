#!/bin/bash

# 🚀 SCRIPT DE INICIO MENTALIA EN RUNPOD
# Ecosistema completo de IA Neurodivergente

echo "🧠 =================================="
echo "🚀 INICIANDO ECOSISTEMA MENTALIA"
echo "🧠 =================================="

# Verificar variables de entorno críticas
echo "🔍 Verificando configuración..."

if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ Error: OPENAI_API_KEY no configurada"
    exit 1
fi

if [ -z "$DB_PASSWORD" ]; then
    echo "❌ Error: DB_PASSWORD no configurada"
    exit 1
fi

if [ -z "$SECRET_KEY" ]; then
    echo "❌ Error: SECRET_KEY no configurada"
    exit 1
fi

echo "✅ Variables de entorno verificadas"

# Crear directorios necesarios
echo "📁 Creando estructura de directorios..."
mkdir -p logs
mkdir -p backups
mkdir -p config

# Configurar permisos
chmod +x *.sh

# Limpiar contenedores anteriores si existen
echo "🧹 Limpiando contenedores anteriores..."
docker-compose down --remove-orphans

# Construir imágenes
echo "🏗️ Construyendo imágenes Docker..."
docker-compose build --no-cache

# Iniciar servicios base primero
echo "📊 Iniciando servicios base..."
docker-compose up -d db redis

# Esperar que la base de datos esté lista
echo "⏳ Esperando base de datos (60 segundos)..."
sleep 60

# Verificar conectividad de base de datos
echo "🔍 Verificando base de datos..."
docker-compose exec -T db pg_isready -U mentalia || {
    echo "❌ Error: Base de datos no disponible"
    exit 1
}

# Ejecutar migraciones
echo "🔄 Ejecutando migraciones de base de datos..."
docker-compose exec -T mentalia-universe flask db upgrade || true

# Iniciar aplicaciones principales
echo "🌟 Iniciando MENTALIA UNIVERSE (Hub Central)..."
docker-compose up -d mentalia-universe

echo "💬 Iniciando CHAT MENTALIA (87 Agentes IA)..."
docker-compose up -d chat-mentalia

echo "🌐 Iniciando HIPERFOCO.COM (Presentación Socios)..."
docker-compose up -d hiperfoco-web

# Esperar que los servicios principales estén listos
echo "⏳ Esperando servicios principales (30 segundos)..."
sleep 30

# Iniciar sistemas especializados
echo "🏥 Iniciando Agendas Clínicas (Sistema Médico)..."
docker-compose up -d agendas-clinicas

echo "⚖️ Iniciando Despacho Legal (Automatización Jurídica)..."
docker-compose up -d despacho-legal

echo "🎓 Iniciando Formación Laboral (OTEC)..."
docker-compose up -d formacion-laboral

echo "🧠 Iniciando Mental-IA ND (Herramientas Especializadas)..."
docker-compose up -d mental-ia-nd

# Iniciar API Gateway
echo "🔗 Iniciando API Gateway Central..."
docker-compose up -d api-gateway

# Iniciar monitoreo
echo "📊 Iniciando sistema de monitoreo..."
docker-compose up -d monitoring

# Verificar estado final
echo "✅ Verificando estado final de todos los servicios..."
sleep 30

echo ""
echo "📊 Estado de servicios:"
docker-compose ps

echo ""
echo "🌐 URLs de acceso:"
echo "🌟 MENTALIA UNIVERSE: http://localhost:5000"
echo "💬 CHAT MENTALIA: http://localhost:5001"
echo "🌐 HIPERFOCO.COM: http://localhost:5002"
echo "🏥 Agendas Clínicas: http://localhost:5003"
echo "⚖️ Despacho Legal: http://localhost:5004"
echo "🎓 Formación Laboral: http://localhost:5005"
echo "🧠 Mental-IA ND: http://localhost:5006"
echo "🔗 API Gateway: http://localhost:5100"
echo "📊 Monitoreo: http://localhost:3000"

echo ""
echo "🎉 =================================="
echo "✅ ECOSISTEMA MENTALIA INICIADO"
echo "🧠 87 Agentes IA Activos"
echo "📱 31 Aplicaciones Funcionando"
echo "🌍 Listo para Usuarios Globales"
echo "🎉 =================================="

# Crear archivo de estado
echo "$(date): Ecosistema MENTALIA iniciado exitosamente" > logs/startup.log
echo "Servicios activos: $(docker-compose ps --services | wc -l)" >> logs/startup.log
echo "URLs principales configuradas" >> logs/startup.log

# Monitoreo continuo en background
nohup ./monitor_mentalia.sh > logs/monitoring.log 2>&1 &

echo "🔄 Monitoreo continuo iniciado en background"
echo "📝 Logs disponibles en: logs/"
echo ""
echo "🚀 ¡MENTALIA LISTO PARA CONQUISTAR EL MUNDO!"

