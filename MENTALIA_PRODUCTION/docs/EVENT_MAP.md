# 🔄 MAPA DE EVENTOS - MENTALIA

## 📡 Sistema de Eventos (Redis)

### **Nomenclatura**
Formato: `dominio.entidad.accion`
Ejemplo: `oraculo.reading.completed`

---

## 🎯 Eventos por Dominio

### **Auth (core/auth)**
```
auth.user.registered     # Usuario creado
auth.user.login          # Login exitoso
auth.user.logout         # Logout
auth.session.expired     # Sesión expirada
```

### **Oráculo (oraculo/)**
```
oraculo.reading.started       # Lectura iniciada
oraculo.reading.completed     # Lectura completada
oraculo.reading.shared        # Lectura compartida
oraculo.journal.entry        # Nueva entrada de journaling
```

### **Salud Mental (salud-mental/)**
```
salud.appointment.booked      # Cita agendada
salud.appointment.cancelled   # Cita cancelada
salud.appointment.completed   # Consulta finalizada
salud.patient.registered      # Paciente registrado
salud.consultation.started    # Consulta iniciada
```

### **Legal (legal/)**
```
legal.document.created        # Documento generado
legal.document.signed         # Documento firmado
legal.contract.generated      # Contrato creado
legal.tender.submitted        # Licitación enviada
legal.chilecompra.sync        # Sync con ChileCompra
```

### **Educación (educacion/)**
```
educacion.course.enrolled     # Inscripción a curso
educacion.lesson.completed    # Lección completada
educacion.certificate.issued # Certificado emitido
educacion.progress.updated    # Progreso actualizado
```

### **Kehilá (kehilá-olamit/)**
```
kehilá.event.created          # Evento comunitario creado
kehilá.member.joined          # Nuevo miembro
kehilá.ritual.scheduled       # Ritual programado
kehilá.study.session          # Sesión de estudio
```

### **ADN-ND (adn-nd/)**
```
adnnd.assessment.completed    # Evaluación completada
adnnd.profile.updated         # Perfil actualizado
adnnd.intervention.suggested  # Intervención sugerida
adnnd.progress.tracked        # Progreso registrado
```

### **Simón (simon/)**
```
simon.game.completed          # Juego completado
simon.habit.tracked           # Hábito registrado
simon.reward.earned           # Recompensa ganada
simon.therapy.session         # Sesión terapéutica
```

---

## 🔗 Productores y Consumidores

### **Oráculo**
**Produce**: `oraculo.reading.completed`
**Consume**: `auth.user.login` (para personalización)

### **MENTA (Coordinación)**
**Produce**: `menta.handoff.suggested`, `menta.plan.updated`
**Consume**: TODOS los eventos (para coordinación)

### **BLU (Contención)**
**Produce**: `blu.support.provided`, `blu.crisis.detected`
**Consume**: `salud.appointment.booked`, `adnnd.assessment.completed`

### **Salud Mental**
**Produce**: `salud.appointment.booked`
**Consume**: `auth.user.registered`, `oraculo.reading.completed`

### **Legal**
**Produce**: `legal.document.signed`
**Consume**: `salud.appointment.completed` (para informes)

---

## 📋 Estructura de Evento

```typescript
interface Event {
  id: string;              // UUID único
  type: string;            // ej: "oraculo.reading.completed"
  timestamp: string;       // ISO 8601
  userId?: string;         // Usuario relacionado
  data: Record<string, any>; // Payload específico
  metadata: {
    source: string;        // Servicio que emite
    version: string;       // Versión del evento
    correlationId?: string; // Para tracing
  };
}
```

### **Ejemplo: Lectura Oracular Completada**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "type": "oraculo.reading.completed",
  "timestamp": "2025-08-11T15:30:00Z",
  "userId": "user_123",
  "data": {
    "readingId": "reading_456",
    "cards": ["La Estrella", "El Mago"],
    "interpretation": "Mensaje del alma...",
    "ritual": "Encender vela blanca..."
  },
  "metadata": {
    "source": "oraculo-core",
    "version": "1.0",
    "correlationId": "req_789"
  }
}
```

---

## 🎛️ Handlers de Eventos

### **Chat-Mentalia (Coordinación)**
```typescript
// Escucha TODOS los eventos para coordinación inteligente
eventBus.subscribe('*', async (event) => {
  await mentaCoordinator.processEvent(event);
  await bluSupervisor.checkSupport(event);
});
```

### **Notificaciones**
```typescript
// Eventos que generan notificaciones
const notificationEvents = [
  'oraculo.reading.completed',
  'salud.appointment.booked',
  'legal.document.signed',
  'educacion.certificate.issued'
];

notificationEvents.forEach(eventType => {
  eventBus.subscribe(eventType, sendNotification);
});
```

### **Analytics**
```typescript
// Tracking para métricas
eventBus.subscribe('*.completed', trackCompletion);
eventBus.subscribe('*.created', trackCreation);
eventBus.subscribe('*.error', trackError);
```

---

## 🚀 Implementación Redis

### **Publisher (Ejemplo)**
```typescript
// En oraculo-core
await redis.publish('events', JSON.stringify({
  type: 'oraculo.reading.completed',
  userId: 'user_123',
  data: { readingId, cards, interpretation }
}));
```

### **Subscriber (Ejemplo)**
```typescript
// En chat-mentalia
redis.subscribe('events');
redis.on('message', async (channel, message) => {
  const event = JSON.parse(message);
  await handleEvent(event);
});
```

---

## 📊 Monitoreo de Eventos

### **Métricas Clave**
- Eventos por segundo por tipo
- Latencia promedio de procesamiento
- Eventos fallidos y reintentados
- Volumen por dominio

### **Logs Estructurados**
```json
{
  "level": "info",
  "timestamp": "2025-08-11T15:30:00Z",
  "message": "Event processed",
  "eventType": "oraculo.reading.completed",
  "processingTime": "150ms",
  "success": true
}
```

---

**Este mapa guía la implementación del sistema de eventos distribuidos de MENTALIA.** 🔄
