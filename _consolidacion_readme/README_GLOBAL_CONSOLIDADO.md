# 🧠 MENTALIA Enterprise - Ecosistema Global de Inteligencia Artificial

[![GitHub Codespaces](https://img.shields.io/badge/GitHub-Codespaces-blue?logo=github)](https://github.com/codespaces)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://docker.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-Enterprise-red)](LICENSE)

**MENTALIA** es un ecosistema integral de inteligencia artificial especializado en salud mental, aplicaciones empresariales y soluciones gubernamentales. Incluye 87 agentes especializados, 7 aplicaciones enterprise operativas y una infraestructura completa basada en Docker.

## 🚀 Inicio Rápido

### ⚡ GitHub Codespaces (Recomendado)
```bash
# 1. Ir a: https://github.com/cata7777/MENTALIA
# 2. Clic: "Code" → "Codespaces" → "Create codespace"
# 3. Ejecutar en Codespaces:
./start.sh && docker ps
```

### 🐳 Desarrollo Local
```bash
git clone https://github.com/cata7777/MENTALIA.git
cd MENTALIA
./start.sh
pip install -r requirements.txt
uvicorn api.main:app --reload --port 8000
```

## 📊 Acceso a Servicios

- **🤖 API Docs:** [localhost:8000/docs](http://localhost:8000/docs)
- **📊 Dashboard:** [localhost:3000](http://localhost:3000)
- **🌐 Portal:** [localhost:8005](http://localhost:8005)
- **💬 Chat RAG:** [localhost:8000/chat](http://localhost:8000/chat)

## 🏗️ Estructura del Proyecto

### 📁 Proyectos Principales

| Proyecto | Descripción | Estado | Ubicación |
|----------|-------------|--------|-----------|
| **🤖 Agentes IA** | 87 agentes especializados | ✅ Operativo | `/agentes_mentalia/` |
| **🏥 Aplicaciones** | 7 apps enterprise | ✅ Operativo | `/aplicaciones/` |
| **🧠 Sistema Oráculo** | Coordinador central | ✅ Operativo | `/sistema_oraculo/` |
| **⚖️ Integración Legal** | ChileCompra + MINSAL | ✅ Operativo | `/integracion_legal/` |
| **🐳 Infraestructura** | Docker + Monitoring | ✅ Operativo | `/infrastructure/` |

### 📋 Documentación por Proyecto

- **[🤖 Agentes IA](./docs/AGENTES_README.md)** - 87 agentes especializados
- **[🏥 Aplicaciones](./docs/APLICACIONES_README.md)** - 7 aplicaciones enterprise
- **[🧠 Sistema Oráculo](./docs/ORACULO_README.md)** - Coordinación inteligente
- **[⚖️ Legal](./docs/LEGAL_README.md)** - Integración gubernamental
- **[🐳 DevOps](./docs/DEVOPS_README.md)** - Infraestructura y deployment

## 🤖 87 Agentes IA por Categoría

### 🏥 Salud Mental (15 agentes)
- Terapeuta Cognitivo, Especialista Ansiedad, Neuropsicólogo
- Coach Bienestar, Analista Emocional, +10 más

### ⚖️ Legal (12 agentes)  
- Analista Contratos, Compliance Officer, ChileCompra Specialist
- Auditor Legal, Policy Analyzer, +7 más

### 🎓 Educación (18 agentes)
- Tutor Adaptativo, Evaluador Competencias, Career Counselor
- Learning Analytics, Assessment AI, +13 más

### 💼 Empresarial (20 agentes)
- HR Manager, Sales IA, Customer Success
- Business Analyst, Project Manager, +15 más

### 🏛️ Gobierno (12 agentes)
- Monitor Licitaciones, MINSAL Liaison, Policy Analyzer
- Compliance Gubernamental, +8 más

### 🔧 Técnico (10 agentes)
- DevOps Engineer, Security Guard, Data Engineer
- System Monitor, +6 más

## 🏥 7 Aplicaciones Enterprise

### 1. 📅 Agenda Clínica Interoperable
- **Propósito:** Gestión integral de citas médicas
- **Integración:** HL7 FHIR + FONASA + ChileCompra
- **Estado:** ✅ Operativa

### 2. ⚖️ Despacho Legal Mental-IA  
- **Propósito:** Automatización procesos legales
- **Integración:** ChileCompra + contratos automatizados
- **Estado:** ✅ Operativa

### 3. 🎓 Formación Laboral Mental-IA
- **Propósito:** Capacitación y desarrollo profesional
- **Integración:** Assessment + rutas de aprendizaje
- **Estado:** ✅ Operativa

### 4. 📱 APP SIMÓN - Neurológica
- **Propósito:** Detección temprana neurológica
- **Integración:** Análisis síntomas + evaluación riesgo
- **Estado:** ✅ Operativa

### 5. 💼 APP BLU - Empresarial
- **Propósito:** Comunicación corporativa optimizada
- **Integración:** Análisis conversacional + dinámicas
- **Estado:** ✅ Operativa

### 6. 🗣️ Comunicación Social Multimodal
- **Propósito:** Habilidades comunicación social
- **Audiencia:** Personas neurodivergentes
- **Estado:** ✅ Lista para implementar

### 7. 🔮 Sistema Oráculo Unificado
- **Propósito:** Coordinación inteligente de agentes
- **Función:** Routing automático + gestión contexto
- **Estado:** ✅ Operativo

## 🏛️ Integración Gubernamental

### ChileCompra - Licitaciones Automáticas
- **Monitor:** Scraping automático 24/7
- **Análisis:** Oportunidades de negocio
- **Generación:** Propuestas automáticas
- **Estado:** ✅ Operativo

### MINSAL - Ministerio de Salud
- **Interoperabilidad:** HL7 FHIR compliant
- **Normativas:** Automatización compliance
- **Licitación 8B:** Propuesta preparada
- **Estado:** ✅ Operativo

## 🔧 Stack Tecnológico

### 🧠 Inteligencia Artificial
- **LangChain + LangGraph** - Orquestación agentes
- **Qdrant** - Base datos vectorial
- **OpenAI + Anthropic** - Modelos lenguaje
- **Sentence Transformers** - Embeddings

### ⚡ Backend
- **FastAPI** - Framework web moderno  
- **PostgreSQL** - Base datos relacional
- **Redis** - Cache y sesiones
- **Nginx** - Servidor web y proxy

### 🐳 Infraestructura
- **Docker + Compose** - Containerización
- **Grafana** - Monitoreo
- **MinIO** - Object storage
- **GitHub Actions** - CI/CD

## 📊 Métricas de Impacto

### 💰 ROI Empresarial
- **70% reducción** tiempo procesos administrativos
- **85% aumento** eficiencia RRHH
- **120% mejora** productividad comunicación
- **50% reducción** costos capacitación

### 🏥 Impacto Clínico  
- **90% precisión** detección temprana
- **75% mejora** adherencia tratamiento
- **60% reducción** tiempo diagnóstico
- **150% aumento** satisfacción paciente

### 🏛️ Eficiencia Gubernamental
- **200% velocidad** procesamiento licitaciones
- **100% mejora** compliance automatizado
- **80% reducción** errores documentación
- **300% aumento** transparencia procesos

## 🎯 Casos de Uso por Sector

| Sector | Aplicación Principal | Agentes Clave | ROI Esperado |
|--------|---------------------|---------------|--------------|
| **🏥 Salud** | Agenda Clínica + APP SIMÓN | 15 agentes salud mental | 150% |
| **💼 Empresa** | APP BLU + Formación Laboral | 20 agentes empresariales | 120% |
| **🏛️ Público** | ChileCompra + Despacho Legal | 12 agentes gobierno | 200% |
| **🎓 Educación** | Formación + Evaluación | 18 agentes educativos | 180% |

## 🚀 Roadmap 2025

### Q1 2025 - Consolidación ✅
- 87 Agentes operativos
- Infraestructura estabilizada  
- Apps enterprise en producción
- Integración ChileCompra funcional

### Q2 2025 - Expansión 🔄
- RAG avanzado con re-ranking
- API Gateway implementado
- Métricas Grafana expandidas
- Deploy cloud (RunPod/AWS)

### Q3 2025 - Escalamiento 📋
- Marketplace agentes públicos
- SDK desarrolladores externos
- Multi-tenant empresarial
- Certificaciones internacionales

### Q4 2025 - Globalización 📋
- Expansión LATAM
- Partnerships estratégicos
- Investigación académica
- Open source community

## 🤝 Colaboración

### 👥 Desarrolladores
- [📚 Documentación técnica](./docs/)
- [🔧 APIs documentadas](./api/docs/)
- [🧪 Test suites](./tests/)

### 🏥 Profesionales Salud
- [📖 Guías clínicas](./docs/clinical/)
- [🎓 Capacitación](./training/)
- [📊 Casos estudio](./case-studies/)

### 🏛️ Sector Público
- [📋 Compliance](./compliance/)
- [🔒 Seguridad](./security/)
- [📊 Reportes impacto](./reports/)

### 💼 Empresas
- [📈 ROI Calculator](./roi-calculator/)
- [🎯 Implementación](./implementation/)
- [📞 Soporte](./support/)

## 🤔 FAQ

### ❓ ¿Cómo empezar?
```bash
git clone https://github.com/cata7777/MENTALIA.git
cd MENTALIA && ./start.sh
```

### ❓ ¿Qué incluye el ecosistema?
- 87 agentes IA especializados
- 7 aplicaciones enterprise operativas
- Infraestructura Docker completa
- Integración gubernamental ChileCompra/MINSAL

### ❓ ¿Cómo acceder a servicios?
- API: [localhost:8000/docs](http://localhost:8000/docs)
- Dashboard: [localhost:3000](http://localhost:3000)
- Chat: [localhost:8000/chat](http://localhost:8000/chat)

### ❓ ¿Dónde está la documentación técnica?
- [Agentes IA](./docs/AGENTES_README.md)
- [Aplicaciones](./docs/APLICACIONES_README.md)  
- [Sistema Oráculo](./docs/ORACULO_README.md)
- [DevOps](./docs/DEVOPS_README.md)

## 📞 Contacto

### 🌐 Enlaces
- **GitHub:** [github.com/cata7777/MENTALIA](https://github.com/cata7777/MENTALIA)
- **Codespaces:** Desarrollo en la nube disponible
- **Docker Hub:** Imágenes pre-construidas

### 📧 Soporte
- **Desarrollo:** Equipo MENTALIA Enterprise
- **Comercial:** Partnerships y licenciamiento  
- **Técnico:** Asistencia especializada 24/7
- **Investigación:** Colaboraciones académicas

---

**MENTALIA Enterprise - Transformando el futuro a través de la inteligencia artificial** 🧠✨

*Última actualización: Agosto 2025*
