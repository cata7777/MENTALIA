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
