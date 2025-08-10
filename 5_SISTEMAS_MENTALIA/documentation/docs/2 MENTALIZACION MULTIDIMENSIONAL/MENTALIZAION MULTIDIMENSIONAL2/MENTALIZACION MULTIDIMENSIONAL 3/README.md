# BLU TERAPIA ND - Aplicación Completa Ejecutable

## 💙 Descripción
IA conversacional especializada en terapia neurodivergente con análisis emocional avanzado, modulación de estados y apoyo terapéutico personalizado. Frontend React y backend JavaScript/Node.js según especificaciones Favi.

## 📁 Estructura del Proyecto
```
blu-terapia-nd-completo-ejecutable/
├── frontend/                 # Aplicación React (Puerto 5173)
├── backend/                  # Backend JavaScript (Puerto 5002)
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
# Backend ejecutándose en http://localhost:5002
```

#### 4. Iniciar Frontend (Terminal 2)
```bash
cd frontend
npm run dev
# Frontend ejecutándose en http://localhost:5173
```

## 🎯 Funcionalidades Incluidas

### Frontend React
- ✅ Chat conversacional con IA BLU
- ✅ Análisis emocional en tiempo real
- ✅ Modulación de estados neurodivergentes
- ✅ Dashboard de progreso terapéutico
- ✅ Herramientas de autoregulación
- ✅ Ejercicios de mindfulness adaptados
- ✅ Seguimiento de estados de ánimo
- ✅ Diseño responsive y estético editable
- ✅ Componentes UI con TailwindCSS y Radix UI

### Backend JavaScript/Node.js
- ✅ API REST completa para terapia ND
- ✅ Base de datos Hyperfoco SQLite
- ✅ IA conversacional avanzada
- ✅ Análisis de emociones y patrones
- ✅ Algoritmos de modulación emocional
- ✅ Sistema de sesiones terapéuticas
- ✅ Reportes de progreso
- ✅ Socket.IO tiempo real para chat

## 🔗 URLs de Acceso
- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:5002
- **Health Check:** http://localhost:5002/api/health

## 📊 Stack Tecnológico
- **Frontend:** React + Vite + TailwindCSS + Radix UI
- **Backend:** Node.js + Express + SQLite
- **Base de Datos:** Hyperfoco SQLite
- **Tiempo Real:** Socket.IO
- **IA:** Algoritmos de procesamiento de lenguaje natural

## 💙 Módulos BLU Incluidos
1. **Chat Terapéutico** - Conversación con IA especializada
2. **Análisis Emocional** - Detección de estados emocionales
3. **Modulación de Estados** - Técnicas de regulación
4. **Autoregulación** - Herramientas de autocontrol
5. **Mindfulness ND** - Meditación adaptada
6. **Seguimiento de Progreso** - Métricas terapéuticas
7. **Ejercicios Personalizados** - Actividades adaptadas
8. **Reportes Clínicos** - Informes para profesionales

## 🌟 Características Principales
- **IA Conversacional Avanzada** especializada en neurodivergencia
- **Análisis Emocional en Tiempo Real** con 64+ emociones
- **Modulación de Estados** para TDAH, Autismo, Ansiedad
- **Herramientas de Autoregulación** personalizadas
- **Ejercicios de Mindfulness** adaptados a neurotipos
- **Seguimiento de Progreso** con métricas detalladas
- **Chat en Tiempo Real** con respuestas inmediatas
- **Reportes Terapéuticos** para profesionales de la salud

## 🎨 Personalización
El diseño es completamente editable:
- Modifica `frontend/src/App.css` para estilos globales
- Edita componentes en `frontend/src/components/`
- Personaliza colores en `frontend/tailwind.config.js`
- Ajusta la paleta de colores ND (morado, lila, verde militar, azul)

## 🔧 Desarrollo
Para desarrollo activo:
1. Mantén ambos servidores ejecutándose
2. Los cambios en frontend se reflejan automáticamente
3. Reinicia backend después de cambios en server.js

## 💙 Especialización Neurodivergente
- **TDAH:** Técnicas de concentración y organización
- **Autismo:** Comunicación y regulación sensorial
- **Ansiedad:** Técnicas de relajación y mindfulness
- **Depresión:** Activación conductual y apoyo emocional
- **Trastornos del Sueño:** Higiene del sueño adaptada
- **Estrés:** Manejo de sobrecarga sensorial

## 📝 Notas
- Aplicación lista para producción
- Incluye datos de ejemplo para testing
- Diseño responsive para móvil y desktop
- Cumple especificaciones Favi 2026
- Integración completa con ecosistema ND
- IA entrenada específicamente para neurodivergencia

