# 🚀 MENTALIA PRODUCTION - Monorepo Organizado

¡Estructura de producción lista para RunPod y desarrollo colaborativo!

## 📁 Estructura del Proyecto

```
MENTALIA_PRODUCTION/
├── 📋 BRIEF_COPILOT_MANUS.md     # Instrucciones completas para dev team
├── 🔧 .env.example               # Variables de entorno template
│
├── core/                         # 🏗️ Servicios transversales
│   ├── api-gateway/              # Nginx gateway + routing
│   ├── auth/                     # Autenticación JWT
│   ├── chat-mentalia/            # Orquestador de agentes
│   ├── common/                   # UI kit + utils compartidos
│   └── observability/            # Logs + métricas + trazas
│
├── mentalizacion-multidimensional/  # 🧠 Sistema de agentes
│   ├── agents/                   # 87 agentes especializados
│   ├── services/routing-agentes/ # Reglas de handoff
│   └── docs/
│
├── oraculo/                      # 🔮 Sistema oracular
│   ├── apps/oraculo-web/         # Frontend Next.js
│   ├── services/oraculo-core/    # API /oraculo/*
│   └── data/                     # Migraciones + seeds
│
├── salud-mental/                 # 🏥 Aplicaciones de salud
│   ├── apps/
│   │   ├── agenda-clinica/       # Gestión de consultas
│   │   └── centro-salud-mental/  # Centro integral
│   ├── services/
│   │   ├── salud-agenda/         # API /salud/*
│   │   └── salud-multibots/      # Agentes especializados
│   └── data/
│
├── legal/                        # ⚖️ Servicios legales
│   ├── apps/despacho-legal/      # Despacho digital
│   ├── services/
│   │   ├── legal-core/           # API /legal/*
│   │   └── firmas-electronicas/  # Firma digital
│   └── data/
│
├── educacion/                    # 📚 Plataformas educativas
│   ├── apps/
│   │   ├── fai/                  # Formación laboral
│   │   └── otec/                 # OTEC digital
│   ├── services/
│   │   ├── fai-core/            # API /educacion/*
│   │   └── otec-core/           # Gestión OTEC
│   └── data/
│
├── kehilá-olamit/               # 🕊️ Ecosistema judío
│   ├── apps/kehilá-web/         # Plataforma comunitaria
│   ├── services/kehilá-core/    # API /kehilá/*
│   └── data/
│
├── adn-nd/                      # 🧬 Neurodiversidad
│   ├── apps/adn-nd/             # APP ADN-ND
│   ├── services/adn-nd-core/    # API /adnnd/*
│   └── data/
│
├── simon/                       # 👶 Juego terapéutico
│   ├── apps/simon/              # APP Simón
│   ├── services/simon-core/     # API /simon/*
│   └── data/
│
├── frontend/                    # 🎨 Dashboard unificado
│   └── (Next.js + TypeScript)
│
├── infra/                       # 🏗️ Infraestructura
│   ├── compose/
│   │   ├── docker-compose.runpod.yml  # Compose para RunPod
│   │   └── init-schemas.sql           # DB schemas + seeds
│   ├── nginx/
│   │   └── nginx.conf                 # Gateway config
│   └── ci-cd/                         # GitHub Actions
│
└── docs/                        # 📚 Documentación técnica
    ├── RUTAS_API.md            # Mapa completo de endpoints
    ├── EVENT_MAP.md            # Sistema de eventos Redis
    └── DATA_MODEL.md           # Esquemas de base de datos
```

## 🚀 Quick Start

### 1. **Setup Inicial**
```bash
cd MENTALIA_PRODUCTION
cp .env.example .env
# Editar .env con tus keys
```

### 2. **Levantar LAB Environment**
```bash
cd infra/compose
docker-compose -f docker-compose.runpod.yml up -d
```

### 3. **Verificar Servicios**
```bash
# Health check
curl localhost:8080/health

# Auth demo
curl -X POST localhost:8080/auth/login \
  -d '{"email":"demo@mentalia.ai","password":"demo"}'
```

## 🎯 Para el Equipo

### **Copilot/Manus** 👨‍💻
- Lee `BRIEF_COPILOT_MANUS.md` para instrucciones completas
- Enfócate en implementar servicios core + dockerización
- Sigue convenciones kebab-case para servicios
- Usa schemas separados en DB única para LAB

### **Cata + GitHub Copilot** 🎨
- Trabajar en branding + logo master MENTALIA
- Diseño de landing page + dashboard
- Sub-marcas por aplicación (Oráculo, Clínica, etc.)

## 🔄 Flujo de Desarrollo

1. **LAB Phase**: Monolito en Docker con DB única
2. **STAGING**: Microservicios + DB por dominio  
3. **PRODUCTION**: RunPod + Kubernetes + observability

## 📞 Coordinación

- **Issues**: GitHub Issues para tracking
- **Branches**: `feature/nombre-feature` → `main`
- **Reviews**: PR reviews obligatorios
- **Deploy**: GitHub Actions → RunPod

---

**🎯 Objetivo**: Tener todo el stack funcionando en RunPod mientras desarrollamos el frontend perfecto.**

**🚀 ¡A codear!**
