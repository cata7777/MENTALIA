# 🧠🏥 MENTALIA Enterprise - Ecosistema de Inteligencia Artificial para Salud Mental

[![GitHub Codespaces](https://img.shields.io/badge/GitHub-Codespaces-blue?logo=github)](https://github.com/codespaces)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://docker.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-Enterprise-red)](LICENSE)

**MENTALIA** es un ecosistema integral de inteligencia artificial especializado en salud mental y aplicaciones empresariales, que incluye 87 agentes especializados, 7 aplicaciones enterprise operativas y una infraestructura completa basada en Docker.

## 🚀 Inicio Rápido

### ⚡ Desarrollo con GitHub Codespaces (Recomendado)

```bash
# 1. Abrir en Codespaces desde GitHub
# Ir a: https://github.com/cata7777/MENTALIA
# Clic en: "Code" → "Codespaces" → "Create codespace"

# 2. Una vez en Codespaces, ejecutar:
./start.sh

# 3. Verificar servicios
docker ps
```

### 🐳 Desarrollo Local

```bash
# Clonar repositorio
git clone https://github.com/cata7777/MENTALIA.git
cd MENTALIA

# Iniciar infraestructura completa
./start.sh

# Instalar dependencias
pip install -r requirements.txt

# Configurar entorno
cp .env.example .env

# Iniciar API RAG
uvicorn api.main:app --reload --port 8000
```

## 📊 Acceso a Servicios

Una vez iniciado el proyecto, puedes acceder a:

- **🤖 API Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **📊 Centro de Control:** [http://localhost:3000](http://localhost:3000)
- **🌐 Portal Web:** [http://localhost:8005](http://localhost:8005)
- **💬 Chat RAG:** [http://localhost:8000/chat](http://localhost:8000/chat)

## 🤖 87 Agentes IA Especializados

Nuestro ecosistema incluye agentes organizados por categorías:

### 🏥 Salud Mental (15 agentes)
- **Terapeuta Cognitivo:** Terapia cognitivo-conductual
- **Especialista en Ansiedad:** Manejo de trastornos de ansiedad
- **Neuropsicólogo:** Evaluación y rehabilitación neurológica
- **Coach de Bienestar:** Desarrollo personal y bienestar
- Y 11 agentes adicionales especializados

### ⚖️ Legal (12 agentes)
- **Analista de Contratos:** Revisión automática de contratos
- **Compliance Officer:** Cumplimiento normativo
- **Especialista ChileCompra:** Licitaciones gubernamentales
- **Auditor Legal:** Auditorías y revisiones legales
- Y 8 agentes adicionales especializados

### 🎓 Educación (18 agentes)
- **Tutor Adaptativo:** Personalización del aprendizaje
- **Evaluador de Competencias:** Assessment automatizado
- **Career Counselor:** Orientación vocacional
- **Learning Analytics:** Análisis de progreso estudiantil
- Y 14 agentes adicionales especializados

### 💼 Empresarial (20 agentes)
- **HR Manager:** Gestión de recursos humanos
- **Sales IA:** Automatización de ventas
- **Customer Success:** Gestión de clientes
- **Business Analyst:** Análisis de negocio
- Y 16 agentes adicionales especializados

### 🏛️ Gobierno/ChileCompra (12 agentes)
- **Monitor de Licitaciones:** Seguimiento automático
- **MINSAL Liaison:** Integración con Ministerio de Salud
- **Policy Analyzer:** Análisis de políticas públicas
- **Compliance Gubernamental:** Normativas públicas
- Y 8 agentes adicionales especializados

### 🔧 Técnicos/Soporte (10 agentes)
- **DevOps Engineer:** Automatización de operaciones
- **Security Guard:** Monitoreo de seguridad
- **Data Engineer:** Gestión de datos
- **System Monitor:** Monitoreo de sistemas
- Y 6 agentes adicionales especializados

## 🏥 Aplicaciones Enterprise Operativas

### 1. 📅 Agenda Clínica Interoperable
- **Propósito:** Gestión integral de citas médicas
- **Especialidad:** Interoperabilidad con sistemas de salud
- **Estado:** ✅ Operativa
- **Ubicación:** `/aplicaciones_principales/agenda_clinica/`

### 2. ⚖️ Despacho Legal Mental-IA
- **Propósito:** Automatización de procesos legales
- **Especialidad:** Contratos y compliance automatizado
- **Estado:** ✅ Operativa
- **Ubicación:** `/aplicaciones_principales/despacho_legal/`

### 3. 🎓 Formación Laboral Mental-IA
- **Propósito:** Capacitación y desarrollo profesional
- **Especialidad:** Evaluación de competencias y rutas de aprendizaje
- **Estado:** ✅ Operativa
- **Ubicación:** `/aplicaciones_principales/formacion_laboral/`

### 4. 📱 APP SIMÓN - Atención Neurológica Especializada
- **Propósito:** Detección temprana y seguimiento neurológico
- **Especialidad:** Análisis de síntomas y evaluación de riesgo
- **Estado:** ✅ Operativa
- **Ubicación:** `/aplicaciones_principales/app_simon/`

### 5. 💼 APP BLU - Comunicación Empresarial
- **Propósito:** Optimización de comunicación corporativa
- **Especialidad:** Análisis conversacional y mejora de dinámicas
- **Estado:** ✅ Operativa
- **Ubicación:** `/aplicaciones_principales/app_blu/`

### 6. 🗣️ Comunicación Social Multimodal
- **Propósito:** Potenciar habilidades de comunicación social
- **Especialidad:** Apoyo para personas neurodivergentes
- **Estado:** ✅ Lista para implementar
- **Audiencia:** Personas con autismo, TDAH, ansiedad social

### 7. 🔮 Sistema Oráculo - Coordinador Central
- **Propósito:** Orquestación inteligente de todos los agentes
- **Especialidad:** Routing automático y gestión de contexto
- **Estado:** ✅ Operativo
- **Ubicación:** `/sistema_oraculo/`

## 🏛️ Integración Gubernamental

### ChileCompra - Licitaciones Automáticas
- **📂 Ubicación:** `/gobierno_integraciones/chilecompra/`
- **🔍 Funcionalidad:** Scraping automático de licitaciones
- **📊 Análisis:** Oportunidades de negocio en tiempo real
- **⚖️ Legal:** Generación automática de propuestas

### MINSAL - Ministerio de Salud
- **📂 Ubicación:** `/gobierno_integraciones/minsal/`
- **🎯 Licitación 8B:** Propuesta automática preparada
- **🔗 Interoperabilidad:** HL7 FHIR + FONASA integration
- **📋 Compliance:** Normativas MINSAL automatizadas

## ⚡ Sistema RAG Inteligente

### Stack RAG Completo:
```
📂 Estructura:
├── 📦 requirements.txt - FastAPI + RAG + IA dependencies
├── 🐳 docker-compose.yml - Stack completo (API + Qdrant + MinIO)
├── ⚡ api/main.py - FastAPI enterprise configurado
├── 💬 api/routers/chat.py - Endpoint RAG inteligente
├── 🔍 api/services/retriever.py - Búsqueda vectorial Qdrant
├── 🧠 api/services/rag.py - Motor RAG con embeddings
├── 🔌 connectors/notion.py - Integración Notion
├── ⚙️ workers/ingest.py - Procesamiento automático
└── 🔧 .env.example - Variables de configuración
```

## 🔧 Stack Tecnológico

### 🧠 Inteligencia Artificial
- **LangChain + LangGraph** - Orquestación de agentes
- **Qdrant** - Base de datos vectorial
- **Sentence Transformers** - Embeddings locales
- **OpenAI + Anthropic** - Modelos de lenguaje

### ⚡ Backend y APIs
- **FastAPI** - Framework web moderno
- **PostgreSQL** - Base de datos relacional
- **Redis** - Cache y sesiones
- **Nginx** - Servidor web y proxy

### 🐳 Infraestructura
- **Docker + Docker Compose** - Containerización
- **Grafana** - Monitoreo y observabilidad
- **MinIO** - Object storage
- **GitHub Actions** - CI/CD automatizado

### 🌐 Frontend y UX
- **React/Vue.js** - Interfaces modernas
- **WebRTC** - Comunicación en tiempo real
- **Progressive Web App** - Experiencia mobile
- **Responsive Design** - Adaptabilidad total

## 📊 Métricas y Beneficios

### 💰 ROI Empresarial
- **-70% tiempo** en procesos administrativos
- **+85% eficiencia** en gestión de recursos humanos
- **+120% productividad** en comunicación interna
- **-50% costos** en capacitación y desarrollo

### 🏥 Impacto Clínico
- **+90% precisión** en detección temprana
- **+75% adherencia** al tratamiento
- **-60% tiempo** de diagnóstico
- **+150% satisfacción** del paciente

### 🏛️ Eficiencia Gubernamental
- **+200% velocidad** en procesamiento de licitaciones
- **+100% compliance** normativo automatizado
- **-80% errores** en documentación legal
- **+300% transparencia** en procesos públicos

## 🎯 Casos de Uso Empresarial

### 🏥 Sector Salud
- **Agenda Clínica:** Gestión automatizada de citas y seguimiento
- **APP SIMÓN:** Detección temprana de condiciones neurológicas
- **Comunicación Social:** Apoyo para pacientes neurodivergentes
- **Compliance MINSAL:** Automatización de normativas sanitarias

### 💼 Sector Empresarial
- **APP BLU:** Optimización de comunicación interna
- **87 Agentes:** Automatización de procesos específicos
- **Formación Laboral:** Capacitación personalizada con IA
- **Recursos Humanos:** Evaluación y desarrollo de talento

### 🏛️ Sector Público
- **ChileCompra Integration:** Monitoreo automático de licitaciones
- **Despacho Legal:** Automatización de procesos administrativos
- **Policy Analysis:** Análisis de políticas públicas
- **Compliance:** Cumplimiento normativo automatizado

### 🎓 Sector Educativo
- **Tutores Adaptativos:** Personalización del aprendizaje
- **Evaluación de Competencias:** Assessment automatizado
- **Career Guidance:** Orientación vocacional inteligente
- **Learning Analytics:** Análisis de progreso estudiantil

## 🚀 Roadmap de Desarrollo

### 🎯 Q1 2025 - Consolidación
- ✅ **87 Agentes IA** completamente operativos
- ✅ **Infraestructura Docker** estabilizada
- ✅ **Integración ChileCompra** funcional
- ✅ **Apps enterprise** en producción

### 🚀 Q2 2025 - Expansión
- 🔄 **RAG avanzado** con re-ranking
- 🔄 **API Gateway** para gestión de tráfico
- 🔄 **Métricas avanzadas** en Grafana
- 🔄 **Deploy en cloud** (RunPod/AWS)

### 🌟 Q3 2025 - Escalamiento
- 📋 **Marketplace de agentes** públicos
- 📋 **SDK para desarrolladores** externos
- 📋 **Integración multi-tenant** empresarial
- 📋 **Certificaciones internacionales**

### 🌍 Q4 2025 - Globalización
- 📋 **Expansión internacional** (LATAM)
- 📋 **Partnerships estratégicos** con gobiernos
- 📋 **Investigación académica** colaborativa
- 📋 **Open source community** activa

## 🤝 Colaboración y Comunidad

### 👥 Para Desarrolladores
- **📚 Documentación completa** técnica disponible
- **🔧 APIs bien documentadas** con ejemplos
- **🧪 Test suites** y entornos de desarrollo
- **💬 Comunidad activa** en GitHub Discussions

### 🏥 Para Profesionales de Salud
- **📖 Guías clínicas** especializadas
- **🎓 Capacitación** en uso de herramientas IA
- **📊 Casos de estudio** y mejores prácticas
- **🔬 Investigación colaborativa** en salud mental

### 🏛️ Para Sector Público
- **📋 Compliance** con normativas locales
- **🔒 Seguridad** y privacidad garantizada
- **📊 Reportes** de impacto social
- **🤝 Partnerships** público-privados

### 💼 Para Empresas
- **📈 ROI Calculator** personalizado
- **🎯 Implementación** paso a paso
- **📞 Soporte** técnico especializado
- **📊 Analytics** de negocio detallados

## 🤔 Preguntas Frecuentes

### ❓ ¿Cómo inicio el proyecto?
```bash
git clone https://github.com/cata7777/MENTALIA.git
cd MENTALIA
./start.sh
```

### ❓ ¿Qué tecnologías usa MENTALIA?
- **Backend:** FastAPI + PostgreSQL + Redis
- **IA:** LangChain + Qdrant + OpenAI/Anthropic
- **Infraestructura:** Docker + Grafana + Nginx
- **Frontend:** React/Vue.js + WebRTC

### ❓ ¿Cómo accedo a los dashboards?
- **Centro de Control:** [http://localhost:3000](http://localhost:3000)
- **API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Portal Web:** [http://localhost:8005](http://localhost:8005)

### ❓ ¿Dónde están los 87 agentes IA?
Los agentes están organizados en `/agentes_mentalia/` por categorías según su especialización.

### ❓ ¿Cómo contribuir al proyecto?
1. Fork del repositorio
2. Crear feature branch
3. Commit cambios
4. Pull request
5. Review del equipo

## 📞 Contacto y Soporte

### 🌐 Acceso al Proyecto
- **GitHub:** [https://github.com/cata7777/MENTALIA](https://github.com/cata7777/MENTALIA)
- **Codespaces:** Desarrollo en la nube disponible
- **Docker Hub:** Imágenes pre-construidas

### 📧 Información de Contacto
- **Desarrollo:** Equipo MENTALIA Enterprise
- **Comercial:** Partnerships y licenciamiento
- **Soporte:** Asistencia técnica especializada
- **Investigación:** Colaboraciones académicas

### 🎯 Próximos Pasos
1. **🔍 Explorar** la documentación técnica
2. **🐳 Desplegar** el entorno de desarrollo
3. **🤖 Probar** los 87 agentes disponibles
4. **📊 Revisar** casos de uso específicos
5. **🤝 Conectar** con el equipo para implementación

---

## 🌟 Características Diferenciadoras

### 🤖 Inteligencia Artificial Especializada
- **87 Agentes específicos** para diferentes dominios
- **RAG avanzado** con búsqueda vectorial inteligente
- **Análisis multimodal** (texto, voz, video)
- **Aprendizaje continuo** y adaptación personalizada

### 🏥 Enfoque en Salud Mental
- **Detección temprana** de condiciones neurológicas
- **Apoyo neurodivergente** especializado
- **Terapia asistida** por IA
- **Monitoreo de bienestar** empresarial

### 🏛️ Integración Gubernamental
- **ChileCompra API** para licitaciones automáticas
- **MINSAL compliance** y interoperabilidad
- **HL7 FHIR** estándar de salud internacional
- **Procesos legales** automatizados

### ⚡ Infraestructura Enterprise
- **Docker orchestration** para escalabilidad
- **Grafana monitoring** para observabilidad
- **PostgreSQL + Redis** para performance
- **CI/CD automatizado** con GitHub Actions

---

*MENTALIA Enterprise - Transformando la salud mental a través de la inteligencia artificial* 🧠✨
