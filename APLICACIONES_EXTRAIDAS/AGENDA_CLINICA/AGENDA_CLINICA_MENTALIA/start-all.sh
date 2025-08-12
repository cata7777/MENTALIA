#!/bin/bash

echo "🏥 Iniciando AGENDA CLÍNICA INTEROPERABLE ND"
echo "==========================================="

# Verificar si Node.js está instalado
if ! command -v node &> /dev/null; then
    echo "❌ Node.js no está instalado. Por favor instala Node.js primero."
    exit 1
fi

# Verificar si npm está instalado
if ! command -v npm &> /dev/null; then
    echo "❌ npm no está instalado. Por favor instala npm primero."
    exit 1
fi

echo "✅ Node.js y npm detectados"

# Instalar dependencias del frontend
echo "📦 Instalando dependencias del frontend..."
cd frontend
if [ ! -d "node_modules" ]; then
    npm install
    if [ $? -ne 0 ]; then
        echo "❌ Error instalando dependencias del frontend"
        exit 1
    fi
fi

# Instalar dependencias del backend
echo "📦 Instalando dependencias del backend..."
cd ../backend
if [ ! -d "node_modules" ]; then
    npm install
    if [ $? -ne 0 ]; then
        echo "❌ Error instalando dependencias del backend"
        exit 1
    fi
fi

echo "✅ Dependencias instaladas correctamente"

# Iniciar backend en segundo plano
echo "🚀 Iniciando backend Agenda Clínica en puerto 5003..."
node server.js &
BACKEND_PID=$!

# Esperar un momento para que el backend se inicie
sleep 3

# Verificar si el backend está funcionando
if curl -s http://localhost:5003/api/health > /dev/null; then
    echo "✅ Backend Agenda Clínica iniciado correctamente"
else
    echo "❌ Error iniciando backend Agenda Clínica"
    kill $BACKEND_PID 2>/dev/null
    exit 1
fi

# Iniciar frontend
echo "🎨 Iniciando frontend Agenda Clínica en puerto 5173..."
cd ../frontend
npm run dev -- --host &
FRONTEND_PID=$!

echo ""
echo "🎉 AGENDA CLÍNICA INTEROPERABLE ND iniciada exitosamente!"
echo "======================================================="
echo "🌐 Frontend: http://localhost:5173"
echo "🔧 Backend:  http://localhost:5003"
echo "📊 Health:   http://localhost:5003/api/health"
echo ""
echo "🏥 Módulos clínicos disponibles:"
echo "   • Gestión de Pacientes - Historiales neurodivergentes"
echo "   • Agenda Inteligente - Programación optimizada"
echo "   • Telemedicina - Consultas virtuales"
echo "   • Reportes Clínicos - Documentación automática"
echo "   • Seguimiento de Tratamientos - Evolución de pacientes"
echo "   • Análisis de Datos - Métricas clínicas"
echo "   • Configuración - Personalización del sistema"
echo "   • Interoperabilidad - Integración con otros sistemas"
echo ""
echo "🧠 Especialización neurodivergente:"
echo "   • TDAH - Seguimiento de medicación y terapias"
echo "   • TEA - Planes de intervención personalizados"
echo "   • Dislexia - Evaluaciones y seguimiento académico"
echo "   • Ansiedad - Monitoreo de síntomas"
echo "   • Depresión - Seguimiento de estado de ánimo"
echo "   • Neurotipos Combinados - Abordaje integral"
echo ""
echo "Presiona Ctrl+C para detener ambos servicios"

# Función para limpiar procesos al salir
cleanup() {
    echo ""
    echo "🛑 Deteniendo servicios Agenda Clínica..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "✅ Servicios Agenda Clínica detenidos"
    exit 0
}

# Capturar señal de interrupción
trap cleanup SIGINT SIGTERM

# Mantener el script ejecutándose
wait

