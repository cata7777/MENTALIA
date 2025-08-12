# 🎯 BRIEF PARA COPILOT/MANUS - ORGANIZACIÓN MENTALIA

## 🎯 Objetivo
Crear un monorepo modular con todas las apps y servicios de MENTALIA, listo para:

- **Fase LAB**: 1 sola base de datos Postgres (con schemas por módulo) para pruebas rápidas
- **Rutas unificadas** vía API Gateway (Nginx/Traefik)
- **Microservicios independientes** pero interconectados (HTTP + eventos Redis)
- **Frontend unificado** (Next.js) ya conectable al Gateway

## 📁 Estructura de carpetas (funcional → apps/services/data)

```
mentalia/
├─ core/                         # Transversal
│  ├─ api-gateway/               # Nginx/Traefik + conf
│  ├─ auth/                      # /auth (login, me, logout)
│  ├─ chat-mentalia/             # orquestador de agentes/equipos
│  ├─ common/                    # ui-kit, tipos, sdk, utils
│  └─ observability/             # logging/metrics/tracing
│
├─ mentalizacion-multidimensional/
│  ├─ agents/                    # BLU, MENTA, ORÁCULO, squads
│  ├─ services/routing-agentes/  # reglas de handoff, timeline
│  └─ docs/
│
├─ oraculo/
│  ├─ apps/oraculo-web/          # Next.js app
│  ├─ services/oraculo-core/     # API /oraculo/*
│  └─ data/                      # migraciones (schema oraculo)
│
├─ salud-mental/
│  ├─ apps/agenda-clinica/
│  ├─ apps/centro-salud-mental/
│  ├─ services/salud-agenda/     # API /salud/*
│  ├─ services/salud-multibots/
│  └─ data/
│
├─ legal/
│  ├─ apps/despacho-legal/
│  ├─ services/legal-core/       # API /legal/*
│  ├─ services/firmas-electronicas/
│  └─ data/
│
├─ educacion/
│  ├─ apps/fai/
│  ├─ services/fai-core/         # API /educacion/*
│  ├─ apps/otec/
│  ├─ services/otec-core/
│  └─ data/
│
├─ kehilá-olamit/
│  ├─ apps/kehilá-web/
│  ├─ services/kehilá-core/      # API /kehilá/*
│  └─ data/
│
├─ adn-nd/
│  ├─ apps/adn-nd/
│  ├─ services/adn-nd-core/      # API /adnnd/*
│  └─ data/
│
├─ simon/
│  ├─ apps/simon/
│  ├─ services/simon-core/
│  └─ data/
│
├─ frontend/                     # Dashboard + landing + apps web
│  └─ (Next.js skeleton ya creado)
│
├─ infra/
│  ├─ compose/docker-compose.runpod.yml
│  ├─ nginx/nginx.conf
│  └─ ci-cd/
│
├─ docs/ (README_GLOBAL.md, RUTAS_API.md, EVENT_MAP.md, DATA_MODEL.md)
└─ .env.example
```

## 🔤 Convenciones
- **Servicios**: kebab-case, ex: salud-agenda
- **Rutas**: por prefijo (ej. /oraculo/* → oraculo-core)
- **DB en LAB**: 1 Postgres con schemas: auth, oraculo, salud, legal, educacion, kehilá, adnnd, simon, common
- **Eventos** (Redis/NATS): nombres canónicos dominio.evento (ej. oraculo.reading.completed)

## 🔌 API Gateway (mapa de rutas)
- `/auth/*` → core/auth:8080
- `/chat/*` → core/chat-mentalia:8080
- `/oraculo/*` → oraculo/services/oraculo-core:8080
- `/salud/*` → salud-mental/services/salud-agenda:8080
- `/legal/*` → legal/services/legal-core:8080
- `/educacion/*` → educacion/services/fai-core:8080 (y otec-core)
- `/kehilá/*` → kehilá-olamit/services/kehilá-core:8080
- `/adnnd/*` → adn-nd/services/adn-nd-core:8080
- `/simon/*` → simon/services/simon-core:8080

## 🗄️ Base de datos (LAB)
- Una instancia Postgres, schemas por módulo
- Cada servicio incluye migraciones propias apuntando a su schema
- **Semillas mínimas**: 1 usuario demo, 1 lectura oracular, 1 cita clínica, 1 documento legal

## 🧰 docker-compose (LAB)
**Ruta**: `infra/compose/docker-compose.runpod.yml`
**Servicios mínimos**: api-gateway, auth, chat-mentalia, oraculo-core, salud-agenda, legal-core, bus (Redis), db (Postgres)
**Nota**: chat-mentalia puede pedir GPU; el resto CPU

## 🔐 Variables (plantilla)
`.env.example`
```bash
ENV=lab
LOG_LEVEL=info

# Auth
JWT_SECRET=CAMBIAR
ENCRYPTION_KEY=CAMBIAR

# DB única (LAB)
DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=CAMBIAR
DB_NAME=mentalia_lab

# Redis eventos
REDIS_HOST=bus
REDIS_PASSWORD=CAMBIAR

# APIs externas
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
CHILECOMPRA_API_KEY=
```

## 🖥️ Frontend
- Usar `/frontend` (Next.js)
- `.env.local`: `NEXT_PUBLIC_API_BASE=http://<gateway-host>`
- **Rutas**: /home, /agentes/[id], /apps/oraculo, /apps/clinica, /apps/legal, etc.
- `middleware.ts` ya protege rutas (redirige a /login si no hay token)

## ✅ Tareas para Copilot (paso a paso)

### 1. **Estructura Base**
- [ ] Crear carpetas según estructura
- [ ] Inicializar package.json en frontend/ y en cada services/*

### 2. **Dockerización**
- [ ] Escribir Dockerfiles por servicio (Node 20 / Python 3.11 según stack)
- [ ] Configurar Gateway (infra/nginx/nginx.conf) con el mapa de rutas anterior

### 3. **Compose LAB**
- [ ] Levantar compose LAB (docker-compose.runpod.yml) con:
  - api-gateway, auth, chat-mentalia, oraculo-core, salud-agenda, legal-core, bus, db

### 4. **Base de Datos**
- [ ] DB y schemas: crear schemas por módulo
- [ ] Preparar migraciones por servicio apuntando a su schema
- [ ] Seeds: datos demo mínimos por módulo

### 5. **Sistema de Eventos**
- [ ] Implementar bus (Redis) + productores/consumidores básicos:
  - Emisión oraculo.reading.completed
  - salud.appointment.booked
  - legal.document.signed

### 6. **Documentación**
- [ ] Completar docs/RUTAS_API.md, EVENT_MAP.md, DATA_MODEL.md

### 7. **Smoke Tests**
- [ ] POST /auth/login (dev) → cookie/token
- [ ] GET /auth/me → usuario demo
- [ ] POST /oraculo/reading → 200, crea registro (schema oraculo)
- [ ] POST /salud/appointments → 200, emite salud.appointment.booked
- [ ] POST /legal/document → 200, permite firma simulada

### 8. **Frontend Integration**
- [ ] Frontend: npm i && npm run dev
- [ ] Validar /login, /home, /apps/oraculo llamando al Gateway

## 📏 Criterios de aceptación (LAB)
- ✅ `docker compose up -d` levanta todo sin fallas
- ✅ `GET /auth/me` responde con usuario demo tras login
- ✅ Lectura oracular se crea y devuelve id
- ✅ Cita clínica se crea y se emite evento en Redis (log visible)
- ✅ Documento legal se crea y permite firma simulada
- ✅ Frontend renderiza Dashboard y permite acciones rápidas (aunque el backend sea dummy)

## 🔜 Próximos (luego del LAB)
- Particionar a DB por servicio manteniendo contratos
- HTTPS/SSL + dominios
- CI/CD (build/push/deploy) por servicio
- Métricas y trazas por servicio (Prometheus + Grafana / OpenTelemetry)

---

**Con esto Copilot y Manus pueden avanzar sin fricción mientras Cata y GitHub Copilot trabajan en logo + diseño de página.** 🚀
