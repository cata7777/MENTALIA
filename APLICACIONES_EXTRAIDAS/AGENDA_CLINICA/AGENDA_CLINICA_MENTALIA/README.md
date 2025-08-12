# AGENDA CLÍNICA INTEROPERABLE ND - Aplicación Completa Ejecutable

## 🏥 Descripción
Sistema de gestión clínica especializado en pacientes neurodivergentes con agenda inteligente, telemedicina integrada y reportes automáticos. Frontend React y backend JavaScript/Node.js según especificaciones Favi.

## 📁 Estructura del Proyecto
```
agenda-clinica-completo-ejecutable/
├── frontend/                 # Aplicación React (Puerto 5173)
├── backend/                  # Backend JavaScript (Puerto 5003)
├── README.md                # Este archivo
└── start-all.sh            # Script para iniciar todo
```

## 🚀 Instalación y Ejecución

### Opción 1: Ejecución Automática
```bash
chmod +x start-all.sh
./start-all.sh
```

### Opción 2: Ejecución Manual

#### 1. Instalar dependencias del Frontend
```bash
cd frontend
npm install
```

#### 2. Instalar dependencias del Backend
```bash
cd ../backend
npm install
```

#### 3. Iniciar Backend (Terminal 1)
```bash
cd backend
npm start
# Backend ejecutándose en http://localhost:5003
```

#### 4. Iniciar Frontend (Terminal 2)
```bash
cd frontend
npm run dev
# Frontend ejecutándose en http://localhost:5173
```

## 🎯 Funcionalidades Incluidas

### Frontend React
- ✅ Dashboard clínico con métricas en tiempo real
- ✅ Gestión de citas y agenda inteligente
- ✅ Perfiles de pacientes neurodivergentes
- ✅ Sistema de telemedicina integrado
- ✅ Generación de reportes clínicos
- ✅ Seguimiento de tratamientos
- ✅ Configuración personalizable
- ✅ Diseño responsive y estético editable
- ✅ Componentes UI con TailwindCSS y Radix UI

### Backend JavaScript/Node.js
- ✅ API REST completa para gestión clínica
- ✅ Base de datos Hyperfoco SQLite
- ✅ Sistema de autenticación médica
- ✅ Gestión de pacientes neurodivergentes
- ✅ Programación inteligente de citas
- ✅ Historiales clínicos digitales
- ✅ Integración con telemedicina
- ✅ Generación automática de reportes
- ✅ Socket.IO tiempo real

## 🔗 URLs de Acceso
- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:5003
- **Health Check:** http://localhost:5003/api/health

## 📊 Stack Tecnológico
- **Frontend:** React + Vite + TailwindCSS + Radix UI
- **Backend:** Node.js + Express + SQLite
- **Base de Datos:** Hyperfoco SQLite
- **Tiempo Real:** Socket.IO
- **Telemedicina:** WebRTC integrado

## 🏥 Módulos Clínicos Incluidos
1. **Gestión de Pacientes** - Historiales neurodivergentes
2. **Agenda Inteligente** - Programación optimizada
3. **Telemedicina** - Consultas virtuales
4. **Reportes Clínicos** - Documentación automática
5. **Seguimiento de Tratamientos** - Evolución de pacientes
6. **Análisis de Datos** - Métricas clínicas
7. **Configuración** - Personalización del sistema
8. **Interoperabilidad** - Integración con otros sistemas

## 🌟 Características Principales
- **Especialización Neurodivergente** (TDAH, TEA, Dislexia, etc.)
- **Agenda Inteligente** con optimización automática
- **Telemedicina Integrada** con videollamadas y chat
- **Historiales Clínicos Digitales** con búsqueda avanzada
- **Reportes Automáticos** con análisis de progreso
- **Dashboard en Tiempo Real** con métricas clave
- **Sistema Interoperable** con estándares HL7
- **Configuración Flexible** para diferentes especialidades

## 🎨 Personalización
El diseño es completamente editable:
- Modifica `frontend/src/App.css` para estilos globales
- Edita componentes en `frontend/src/components/`
- Personaliza colores en `frontend/tailwind.config.js`
- Ajusta la paleta de colores ND (azul, verde, morado, lila)

## 🔧 Desarrollo
Para desarrollo activo:
1. Mantén ambos servidores ejecutándose
2. Los cambios en frontend se reflejan automáticamente
3. Reinicia backend después de cambios en server.js

## 🏥 Especialización Clínica
- **TDAH:** Seguimiento de medicación y terapias
- **TEA:** Planes de intervención personalizados
- **Dislexia:** Evaluaciones y seguimiento académico
- **Ansiedad:** Monitoreo de síntomas y tratamientos
- **Depresión:** Seguimiento de estado de ánimo
- **Neurotipos Combinados:** Abordaje integral

## 📝 Notas
- Aplicación lista para producción
- Incluye datos de ejemplo para testing
- Diseño responsive para móvil y desktop
- Cumple especificaciones Favi 2026
- Integración completa con ecosistema ND
- Cumple estándares de seguridad médica

