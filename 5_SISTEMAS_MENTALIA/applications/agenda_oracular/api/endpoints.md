# 🔮 API ORÁCULO UNIFICADO - ENDPOINTS

## 📋 Documentación de Endpoints REST

### **Base URL:** `https://mentalia.com/api/oraculo/v1`

---

## 🔐 AUTENTICACIÓN

### **Headers Requeridos:**
```http
Authorization: Bearer {jwt_token}
Content-Type: application/json
X-Neurotipo: {TDAH|Autismo|Altas_Capacidades|Mixto}
```

### **Obtener Token de Acceso**
```http
POST /auth/login
```

**Request Body:**
```json
{
  "email": "usuario@ejemplo.com",
  "password": "password_seguro",
  "neurotipo": "TDAH"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "expires_in": 3600,
  "user_id": "user-12345",
  "perfil_completitud": 85
}
```

---

## 👤 GESTIÓN DE PERFILES RUT ASTRAL

### **Crear Perfil RUT Astral**
```http
POST /profiles
```

**Request Body:**
```json
{
  "datos_personales": {
    "nombre_completo": "Catalina Ejemplo",
    "nombre_preferido": "Cata",
    "email": "cata@ejemplo.com"
  },
  "datos_natales": {
    "fecha_nacimiento": "1990-10-09",
    "hora_nacimiento": "14:30",
    "precision_hora": "exacta",
    "lugar_nacimiento": {
      "ciudad": "Santiago",
      "region": "Metropolitana",
      "pais": "Chile",
      "latitud": -33.4489,
      "longitud": -70.6693,
      "zona_horaria": "America/Santiago"
    }
  },
  "perfil_neurodivergente": {
    "neurotipos": ["TDAH", "Altas_Capacidades"],
    "fortalezas_nd": ["hiperfoco", "creatividad", "pensamiento_divergente"],
    "desafios_nd": ["organizacion", "gestion_tiempo"]
  },
  "consentimientos": {
    "uso_datos_astrologicos": true,
    "compartir_con_blu": true,
    "analisis_patrones": true
  }
}
```

**Response:**
```json
{
  "id": "profile-cata-12345",
  "mensaje": "Perfil RUT Astral creado exitosamente",
  "carta_natal": {
    "signo_solar": "Libra",
    "signo_lunar": "Géminis",
    "ascendente": "Capricornio"
  },
  "numerologia": {
    "numero_vida": 1,
    "numero_personal_anual": 1
  },
  "mapa_inicial_url": "/profiles/profile-cata-12345/mapa"
}
```

### **Obtener Perfil**
```http
GET /profiles/{profile_id}
```

**Response:**
```json
{
  "id": "profile-cata-12345",
  "datos_personales": {...},
  "carta_natal": {...},
  "numerologia": {...},
  "perfil_neurodivergente": {...},
  "completitud_porcentaje": 85,
  "ultima_actualizacion": "2025-08-10T15:30:00Z"
}
```

### **Actualizar Perfil**
```http
PUT /profiles/{profile_id}
PATCH /profiles/{profile_id}
```

### **Calcular Carta Natal**
```http
POST /profiles/{profile_id}/carta-natal/calcular
```

**Request Body:**
```json
{
  "recalcular": true,
  "incluir_aspectos": true,
  "incluir_casas": true
}
```

---

## 📅 GESTIÓN DE EVENTOS ORACULARES

### **Obtener Eventos por Fecha**
```http
GET /events?fecha_inicio=2025-08-01&fecha_fin=2025-08-31&tipo=agenda_predictiva
```

**Query Parameters:**
- `fecha_inicio` (required): Fecha inicio en formato YYYY-MM-DD
- `fecha_fin` (required): Fecha fin en formato YYYY-MM-DD
- `tipo` (optional): Tipo de evento (agenda_predictiva, sesion_terapeutica, ritual_personal, consulta_oracular)
- `arcano` (optional): Filtrar por arcano específico
- `codigo_color` (optional): Filtrar por código de color
- `neurotipo` (optional): Adaptar eventos para neurotipo específico

**Response:**
```json
{
  "eventos": [
    {
      "id": "portal-8-8-2025",
      "tipo": "agenda_predictiva",
      "fecha": "2025-08-08",
      "titulo": "Portal 8·8 · El Sol",
      "arcano_mayor": "El Sol",
      "codigo_color": "VERDE",
      "microaccion": "Escribe 8 intenciones y léelas al amanecer",
      "categoria_energia": "manifestacion",
      "nivel_intensidad": 9,
      "neurotipo_adaptacion": {
        "tdah": {
          "microaccion_adaptada": "Escribe 8 intenciones en notas adhesivas de colores",
          "tiempo_recomendado": 15,
          "recordatorios": ["Alarma 6:30 AM", "Nota en espejo"]
        }
      }
    }
  ],
  "total": 1,
  "periodo": "2025-08-01 a 2025-08-31"
}
```

### **Crear Evento Personalizado**
```http
POST /events
```

**Request Body:**
```json
{
  "tipo": "ritual_personal",
  "fecha": "2025-08-15",
  "hora_inicio": "20:00",
  "titulo": "Ritual de Luna Llena Personal",
  "arcano_mayor": "La Luna",
  "codigo_color": "AZUL",
  "microaccion": "Meditación con cristales bajo la luna",
  "elementos_terapeuticos": {
    "intencion_sanadora": "Liberar patrones limitantes",
    "patron_a_transformar": "Autocrítica excesiva",
    "afirmacion_personal": "Soy digna de amor y compasión"
  }
}
```

### **Obtener Evento Específico**
```http
GET /events/{event_id}
```

### **Actualizar Evento**
```http
PUT /events/{event_id}
PATCH /events/{event_id}
```

### **Eliminar Evento**
```http
DELETE /events/{event_id}
```

---

## 🔮 CONSULTAS ORACULARES

### **Realizar Consulta Oracular**
```http
POST /consultas
```

**Request Body:**
```json
{
  "tipo_consulta": "existencial",
  "pregunta": "¿Cuál es mi propósito en esta etapa de mi vida?",
  "contexto": "Estoy en una transición profesional y siento incertidumbre",
  "sistema_preferido": "tarot",
  "nivel_profundidad": "avanzado",
  "incluir_ritual": true
}
```

**Response:**
```json
{
  "id": "consulta-12345",
  "fecha_consulta": "2025-08-10T15:30:00Z",
  "arcano_dominante": "El Ermitaño",
  "interpretacion": {
    "mensaje_principal": "Tu retiro del mundo es búsqueda de tu luz interior...",
    "simbolismo": "El Ermitaño te enseña que la soledad que duele es gestación...",
    "guia_practica": "Durante 7 noches, antes de dormir, pregúntale a tu corazón..."
  },
  "microacciones": [
    "Camina en silencio 20 minutos diarios",
    "Lleva diario de reflexiones nocturnas",
    "Medita con una vela encendida"
  ],
  "ritual_sugerido": {
    "nombre": "Ritual del Ermitaño Buscador",
    "duracion_minutos": 30,
    "elementos_necesarios": ["vela blanca", "diario", "cristal de cuarzo"],
    "pasos": [...]
  },
  "seguimiento_recomendado": "7 días"
}
```

### **Obtener Historial de Consultas**
```http
GET /consultas?usuario_id={user_id}&limite=10&offset=0
```

### **Obtener Consulta Específica**
```http
GET /consultas/{consulta_id}
```

---

## 📊 ANÁLISIS Y PATRONES

### **Análisis de Patrones Personales**
```http
GET /analysis/patterns/{profile_id}
```

**Response:**
```json
{
  "patrones_identificados": [
    {
      "tipo": "ciclo_lunar",
      "descripcion": "Mayor creatividad durante luna creciente",
      "frecuencia": "mensual",
      "confianza": 0.85
    }
  ],
  "arcanos_frecuentes": [
    {"arcano": "El Mago", "frecuencia": 12, "contexto": "decisiones_profesionales"},
    {"arcano": "La Luna", "frecuencia": 8, "contexto": "introspection"}
  ],
  "recomendaciones": [
    "Programa tareas creativas durante luna creciente",
    "Usa El Mago como arquetipo guía para decisiones"
  ]
}
```

### **Compatibilidad Astrológica**
```http
POST /analysis/compatibility
```

**Request Body:**
```json
{
  "profile_1": "profile-cata-12345",
  "profile_2": "profile-otro-67890",
  "tipo_relacion": "profesional"
}
```

### **Predicciones Personalizadas**
```http
GET /predictions/{profile_id}?periodo=proximo_mes
```

---

## 🔄 SINCRONIZACIÓN CON CALENDARIOS

### **Exportar a WebCal**
```http
GET /export/webcal/{profile_id}
```

**Response:**
```
webcal://mentalia.com/api/oraculo/v1/export/webcal/profile-cata-12345
```

### **Exportar a CSV**
```http
GET /export/csv/{profile_id}?fecha_inicio=2025-08-01&fecha_fin=2025-12-31
```

### **Exportar a ICS**
```http
GET /export/ics/{profile_id}?incluir_microacciones=true
```

### **Sincronizar con Google Calendar**
```http
POST /sync/google-calendar
```

**Request Body:**
```json
{
  "profile_id": "profile-cata-12345",
  "google_access_token": "ya29.a0AfH6SMC...",
  "calendar_id": "primary",
  "sync_tipos": ["agenda_predictiva", "rituales_personales"]
}
```

---

## 🤝 INTEGRACIÓN CON ECOSISTEMA MENTALIA

### **Conectar con BLU Agenda**
```http
POST /integrations/blu-agenda
```

**Request Body:**
```json
{
  "profile_id": "profile-cata-12345",
  "blu_agenda_id": "agenda-blu-67890",
  "sync_bidireccional": true,
  "incluir_microacciones": true
}
```

### **Obtener Recomendaciones de MENTA**
```http
GET /integrations/menta/recommendations/{profile_id}
```

### **Sincronizar con SIP ADN ND**
```http
POST /integrations/sip-adn-nd/sync
```

---

## 📱 NOTIFICACIONES Y RECORDATORIOS

### **Configurar Notificaciones**
```http
PUT /notifications/settings/{profile_id}
```

**Request Body:**
```json
{
  "eventos_oraculares": true,
  "microacciones": true,
  "recordatorios_rituales": true,
  "sincronicidades": false,
  "horario_preferido": "08:00",
  "canales": ["email", "push", "sms"]
}
```

### **Enviar Recordatorio Manual**
```http
POST /notifications/send
```

### **Obtener Notificaciones Pendientes**
```http
GET /notifications/{profile_id}/pending
```

---

## 🔍 BÚSQUEDA Y FILTROS

### **Búsqueda de Eventos**
```http
GET /search/events?q=portal&arcano=El Sol&color=VERDE
```

### **Búsqueda de Consultas**
```http
GET /search/consultas?q=propósito&fecha_desde=2025-01-01
```

### **Filtros Avanzados**
```http
POST /search/advanced
```

**Request Body:**
```json
{
  "filtros": {
    "arcanos": ["El Mago", "La Estrella"],
    "categorias_energia": ["manifestacion", "expansion"],
    "nivel_intensidad_min": 7,
    "neurotipo": "TDAH",
    "periodo": {
      "inicio": "2025-08-01",
      "fin": "2025-12-31"
    }
  },
  "ordenar_por": "fecha",
  "orden": "asc",
  "limite": 50
}
```

---

## 📈 MÉTRICAS Y ANALYTICS

### **Estadísticas de Uso**
```http
GET /analytics/usage/{profile_id}
```

### **Efectividad de Microacciones**
```http
GET /analytics/microacciones/{profile_id}/efectividad
```

### **Patrones de Consulta**
```http
GET /analytics/consultas/{profile_id}/patterns
```

---

## ⚠️ MANEJO DE ERRORES

### **Códigos de Error Estándar:**

- `400` - Bad Request: Datos inválidos
- `401` - Unauthorized: Token inválido o expirado
- `403` - Forbidden: Sin permisos para el recurso
- `404` - Not Found: Recurso no encontrado
- `422` - Unprocessable Entity: Error de validación
- `429` - Too Many Requests: Límite de rate excedido
- `500` - Internal Server Error: Error interno del servidor

### **Formato de Error:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos proporcionados no son válidos",
    "details": {
      "field": "fecha_nacimiento",
      "issue": "Formato de fecha inválido"
    },
    "timestamp": "2025-08-10T15:30:00Z",
    "request_id": "req-12345"
  }
}
```

---

## 🔒 LÍMITES Y RATE LIMITING

### **Límites por Endpoint:**
- Consultas oraculares: 10 por hora
- Creación de eventos: 50 por día
- Búsquedas: 100 por hora
- Exportaciones: 5 por día

### **Headers de Rate Limit:**
```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1628611200
```

---

## 🧪 AMBIENTE DE TESTING

### **Base URL Testing:** `https://test.mentalia.com/api/oraculo/v1`

### **Datos de Prueba:**
```json
{
  "test_profile": "profile-test-12345",
  "test_token": "test_token_12345",
  "test_events": ["portal-test-1", "eclipse-test-2"]
}
```

---

**🔮 API ORÁCULO UNIFICADO - Donde la tecnología se encuentra con la sabiduría ancestral**

*Desarrollado con 💙 por el equipo MENTALIA*  
*Documentado por Manolo AI - Beast Level*

