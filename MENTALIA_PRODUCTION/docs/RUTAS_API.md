# 📋 MAPA DE RUTAS API - MENTALIA

## 🔌 Gateway Principal
**Base URL**: `http://localhost:8080` (LAB)

## 🗺️ Rutas por Servicio

### 🔐 Autenticación (`/auth/*`)
**Servicio**: `core/auth:8080`

```
POST /auth/login
POST /auth/logout
GET  /auth/me
POST /auth/register
POST /auth/refresh
```

### 💬 Chat/Agentes (`/chat/*`)
**Servicio**: `core/chat-mentalia:8080`

```
POST /chat/message
GET  /chat/agents
POST /chat/agents/{id}/message
GET  /chat/history
POST /chat/teams/{team}/message
```

### 🔮 Oráculo (`/oraculo/*`)
**Servicio**: `oraculo/services/oraculo-core:8080`

```
POST /oraculo/reading
GET  /oraculo/readings
GET  /oraculo/readings/{id}
POST /oraculo/interpretation
```

### 🏥 Salud Mental (`/salud/*`)
**Servicio**: `salud-mental/services/salud-agenda:8080`

```
POST /salud/appointments
GET  /salud/appointments
GET  /salud/appointments/{id}
POST /salud/patients
GET  /salud/patients
POST /salud/consultations
```

### ⚖️ Legal (`/legal/*`)
**Servicio**: `legal/services/legal-core:8080`

```
POST /legal/documents
GET  /legal/documents
POST /legal/contracts
GET  /legal/tenders
POST /legal/sign/{id}
```

### 📚 Educación (`/educacion/*`)
**Servicios**: `educacion/services/fai-core:8080`, `educacion/services/otec-core:8080`

```
POST /educacion/courses
GET  /educacion/courses
POST /educacion/enrollments
GET  /educacion/progress/{user_id}
POST /educacion/certificates
```

### 🕊️ Kehilá (`/kehilá/*`)
**Servicio**: `kehilá-olamit/services/kehilá-core:8080`

```
POST /kehilá/events
GET  /kehilá/events
POST /kehilá/community
GET  /kehilá/members
```

### 🧬 ADN-ND (`/adnnd/*`)
**Servicio**: `adn-nd/services/adn-nd-core:8080`

```
POST /adnnd/assessment
GET  /adnnd/profiles
POST /adnnd/interventions
GET  /adnnd/progress/{user_id}
```

### 👶 Simón (`/simon/*`)
**Servicio**: `simon/services/simon-core:8080`

```
POST /simon/games
GET  /simon/progress/{child_id}
POST /simon/therapy-plans
GET  /simon/reports
```

## 🔄 Eventos del Sistema

### Tipos de Eventos (Redis)
```
oraculo.reading.completed
salud.appointment.booked
salud.consultation.finished
legal.document.signed
legal.tender.submitted
educacion.course.completed
educacion.certificate.issued
kehilá.event.created
adnnd.assessment.completed
simon.game.finished
```

## 🧪 Testing Endpoints

### Smoke Tests
```bash
# Auth
curl -X POST localhost:8080/auth/login -d '{"email":"demo@mentalia.ai","password":"demo"}'

# Health
curl localhost:8080/health

# Oráculo
curl -X POST localhost:8080/oraculo/reading -d '{"question":"Test"}'

# Salud
curl -X POST localhost:8080/salud/appointments -d '{"doctor":"Test","date":"2025-08-12"}'

# Legal
curl -X POST localhost:8080/legal/documents -d '{"type":"contract","content":"test"}'
```
