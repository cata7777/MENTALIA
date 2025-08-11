# 🔮 SISTEMA ORÁCULO MENTALIA - Coordinador Central Inteligente

## 🎯 Visión General

El **Sistema Oráculo** es el cerebro central del ecosistema MENTALIA que coordina inteligentemente los 87 agentes IA y las 7 aplicaciones enterprise, proporcionando orquestación, routing automático y gestión de contexto global.

## 🏗️ Arquitectura del Sistema

### 🧠 Componentes Principales

```
┌─────────────────────────────────────────────────┐
│                SISTEMA ORÁCULO                  │
├─────────────────────────────────────────────────┤
│  🎯 Intent Router   │  🧠 Context Manager       │
│  ⚖️ Load Balancer   │  📊 Analytics Engine      │
│  🔄 Auto Scaler     │  🛡️ Fault Tolerance       │
│  📋 Service Registry│  🔐 Security Gateway       │
└─────────────────────────────────────────────────┘
              │                    │
    ┌─────────▼──────────┐  ┌─────▼──────────┐
    │   87 AGENTES IA    │  │ 7 APLICACIONES │
    │                    │  │   ENTERPRISE   │
    │ 🏥 Salud Mental    │  │ 📅 Agenda      │
    │ ⚖️ Legal           │  │ ⚖️ Despacho    │
    │ 🎓 Educación       │  │ 🎓 Formación   │
    │ 💼 Empresarial     │  │ 📱 APP SIMÓN   │
    │ 🏛️ Gobierno        │  │ 💼 APP BLU     │
    │ 🔧 Técnico         │  │ 🗣️ Social      │
    └────────────────────┘  └────────────────┘
```

## ⚡ Funcionalidades Core

### 🎯 Intent Router - Enrutamiento Inteligente
**Función:** Analiza consultas y direcciona al agente más apropiado

```python
class IntentRouter:
    def route_request(self, query: str, context: dict):
        # Análisis semántico de la consulta
        intent = self.analyze_intent(query)
        
        # Selección de agente óptimo
        best_agent = self.select_best_agent(intent, context)
        
        # Routing con contexto preservado
        return self.forward_to_agent(best_agent, query, context)
```

**Ejemplo de Routing:**
- **Consulta:** "Necesito ayuda con ansiedad laboral"
- **Análisis:** Intent=salud_mental, Context=laboral
- **Routing:** AGENTE_ANSIEDAD_AZUL_ESPECIALISTA_AVANZADO
- **Backup:** AGENTE_TERAPEUTA_AZUL_GENERAL_PREMIUM

### 🧠 Context Manager - Gestión de Contexto
**Función:** Mantiene contexto conversacional a través de múltiples agentes

```python
class ContextManager:
    def preserve_context(self, session_id: str, agent_switch: dict):
        # Preservar historia conversacional
        context = self.get_session_context(session_id)
        
        # Transferir contexto relevante
        relevant_context = self.extract_relevant_context(context, agent_switch)
        
        # Inicializar nuevo agente con contexto
        return self.initialize_agent_with_context(agent_switch['new_agent'], relevant_context)
```

**Casos de Contexto:**
- **Usuario inicia con:** Agente Legal (consulta contrato)
- **Deriva a:** Agente ChileCompra (licitación relacionada)
- **Contexto preservado:** Tipo contrato, empresa, requisitos

### ⚖️ Load Balancer - Balanceamiento Inteligente
**Función:** Distribuye carga optimizando recursos y tiempo respuesta

```python
class LoadBalancer:
    def balance_load(self, agent_request: dict):
        # Verificar carga actual agentes
        agent_loads = self.get_current_loads()
        
        # Seleccionar instancia óptima
        best_instance = self.select_optimal_instance(agent_loads, agent_request)
        
        # Balancear si es necesario
        if best_instance.load > threshold:
            return self.scale_or_redirect(agent_request)
```

**Estrategias de Balancing:**
- **Round Robin:** Distribución equitativa
- **Least Connections:** Menor carga actual
- **Response Time:** Tiempo respuesta óptimo
- **Geographic:** Proximidad geográfica

### 🔄 Auto Scaler - Escalamiento Automático
**Función:** Escala recursos automáticamente según demanda

```python
class AutoScaler:
    def auto_scale(self, metrics: dict):
        # Analizar métricas de demanda
        demand_forecast = self.forecast_demand(metrics)
        
        # Decidir scaling action
        if demand_forecast > current_capacity * 0.8:
            return self.scale_up()
        elif demand_forecast < current_capacity * 0.3:
            return self.scale_down()
```

**Métricas de Scaling:**
- **CPU Usage:** >80% scale up, <30% scale down
- **Memory Usage:** >85% scale up, <25% scale down  
- **Request Queue:** >100 pending scale up
- **Response Time:** >2s scale up

## 📊 Analytics Engine - Motor de Análisis

### 📈 Métricas en Tiempo Real
```yaml
real_time_metrics:
  requests_per_second: 1500
  average_response_time: "145ms"
  active_agents: 87
  active_applications: 7
  concurrent_users: 2400
  success_rate: "99.2%"
```

### 📊 Dashboard de Control
```
┌──────────────────────────────────────────────────┐
│              ORÁCULO DASHBOARD                   │
├──────────────────────────────────────────────────┤
│ 🚦 Status: OPERATIVO    ⚡ Latency: 145ms        │
│ 👥 Users: 2,400        📊 Success: 99.2%        │
├──────────────────────────────────────────────────┤
│             AGENTES MÁS ACTIVOS                  │
│ 1. Legal ChileCompra      (340 req/min)         │
│ 2. Terapeuta General      (285 req/min)         │
│ 3. HR Manager            (220 req/min)          │
├──────────────────────────────────────────────────┤
│           APLICACIONES ESTADO                    │
│ ✅ Agenda Clínica        ✅ APP SIMÓN           │
│ ✅ Despacho Legal        ✅ APP BLU             │
│ ✅ Formación Laboral     ✅ Com. Social         │
│ ✅ Sistema Oráculo                               │
└──────────────────────────────────────────────────┘
```

## 🛡️ Fault Tolerance - Tolerancia a Fallos

### 🔄 Estrategias de Recuperación
```python
class FaultTolerance:
    def handle_agent_failure(self, failed_agent: str, context: dict):
        # Detectar fallo de agente
        backup_agents = self.get_backup_agents(failed_agent)
        
        # Seleccionar backup óptimo
        best_backup = self.select_best_backup(backup_agents, context)
        
        # Transferir sesión sin pérdida
        return self.seamless_transfer(failed_agent, best_backup, context)
```

### 📋 Niveles de Backup
| Nivel | Estrategia | Tiempo Recuperación |
|-------|------------|-------------------|
| **L1** | Hot Standby | <1s |
| **L2** | Warm Standby | <5s |
| **L3** | Cold Standby | <30s |
| **L4** | Cross-Category | <60s |

### 🚨 Alertas Automáticas
```yaml
alert_rules:
  agent_down:
    threshold: "1 agente offline"
    action: "activate_backup"
    notification: "slack + email"
  
  high_latency:
    threshold: ">3s response time"
    action: "scale_up"
    notification: "dashboard + sms"
  
  cascade_failure:
    threshold: ">3 agentes offline"
    action: "emergency_protocol"
    notification: "all_channels"
```

## 🔐 Security Gateway - Puerta de Seguridad

### 🛡️ Capas de Seguridad
```
┌─────────────────────────────────────────────┐
│              SECURITY LAYERS                │
├─────────────────────────────────────────────┤
│ 🔒 API Gateway Authentication               │
│ 🔑 JWT Token Validation                     │
│ 🛡️ Rate Limiting & DDoS Protection          │
│ 🔍 Request/Response Validation              │
│ 📊 Audit Logging & Monitoring              │
│ 🚫 Malicious Intent Detection              │
└─────────────────────────────────────────────┘
```

### 🔒 Autenticación y Autorización
```python
class SecurityGateway:
    def authenticate_request(self, request: dict):
        # Validar JWT token
        token_valid = self.validate_jwt(request.headers['Authorization'])
        
        # Verificar permisos
        permissions = self.get_user_permissions(token_valid.user_id)
        
        # Autorizar acceso a agente/aplicación
        return self.authorize_access(permissions, request.target)
```

### 🚫 Detección de Amenazas
```python
class ThreatDetection:
    def detect_malicious_intent(self, query: str, user_context: dict):
        # Análisis NLP de intención maliciosa
        threat_score = self.analyze_threat_indicators(query)
        
        # Verificar patrones de abuso
        abuse_patterns = self.check_abuse_patterns(user_context)
        
        # Bloquear si amenaza detectada
        if threat_score > 0.8 or abuse_patterns:
            return self.block_and_alert(query, user_context)
```

## 📋 Service Registry - Registro de Servicios

### 🔍 Descubrimiento de Servicios
```python
class ServiceRegistry:
    def register_service(self, service_info: dict):
        # Registrar nuevo agente/aplicación
        self.services[service_info['id']] = {
            'name': service_info['name'],
            'endpoint': service_info['endpoint'],
            'capabilities': service_info['capabilities'],
            'health_check': service_info['health_endpoint'],
            'last_heartbeat': datetime.now()
        }
```

### 💓 Health Monitoring
```python
class HealthMonitor:
    async def monitor_services(self):
        for service_id, service in self.services.items():
            # Health check periódico
            health = await self.check_service_health(service['health_check'])
            
            # Actualizar estado
            self.update_service_status(service_id, health)
            
            # Alertar si no está saludable
            if not health['healthy']:
                await self.alert_service_down(service_id)
```

## 🚀 Instalación y Configuración

### 📦 Setup Completo
```bash
# Clonar Sistema Oráculo
git clone /sistema_oraculo
cd sistema_oraculo

# Instalar dependencias
pip install -r requirements.txt

# Configurar entorno
cp .env.example .env
nano .env  # Configurar variables

# Inicializar base de datos
./scripts/init_oracle_db.sh

# Iniciar Sistema Oráculo
./start_oracle.sh
```

### ⚙️ Configuración Principal
```yaml
# config/oracle.yml
oracle:
  routing:
    algorithm: "semantic_similarity"
    fallback_strategy: "load_based"
    context_preservation: true
  
  scaling:
    auto_scale: true
    min_instances: 1
    max_instances: 10
    scale_threshold: 80
  
  security:
    authentication: "jwt"
    rate_limiting: true
    threat_detection: true
  
  monitoring:
    metrics_interval: 30
    health_check_interval: 10
    alert_channels: ["slack", "email"]
```

### 🔧 Registro de Agentes
```python
# Registrar un nuevo agente en el Oráculo
oracle.register_agent({
    'id': 'AGENTE_TERAPEUTA_AZUL_GENERAL_PREMIUM',
    'name': 'Terapeuta Cognitivo Premium',
    'category': 'salud_mental',
    'capabilities': ['terapia_cbt', 'evaluacion_emocional'],
    'endpoint': 'http://localhost:8001/agent',
    'health_endpoint': 'http://localhost:8001/health'
})
```

## 📊 Monitoreo y Observabilidad

### 📈 Métricas Clave
```python
# Métricas que rastrea el Oráculo
metrics = {
    'routing_decisions': 15420,  # Decisiones routing por hora
    'context_transfers': 3580,   # Transferencias contexto exitosas
    'load_balancing': 8960,     # Operaciones balanceamiento
    'auto_scaling': 45,         # Eventos auto-scaling
    'fault_recovery': 12,       # Recuperaciones de fallo
    'security_blocks': 3        # Amenazas bloqueadas
}
```

### 🔍 Logs Estructurados
```json
{
  "timestamp": "2025-08-11T10:30:45Z",
  "level": "INFO",
  "component": "IntentRouter",
  "event": "agent_selection",
  "query": "necesito ayuda con contrato laboral",
  "selected_agent": "AGENTE_CONTRATOS_ROJO_EMPRESARIAL_PREMIUM",
  "confidence": 0.92,
  "routing_time_ms": 45
}
```

### 📊 Dashboard Grafana
```yaml
# Dashboards disponibles
dashboards:
  - oracle_overview: "Vista general Sistema Oráculo"
  - agent_performance: "Rendimiento individual agentes"
  - application_health: "Salud aplicaciones enterprise"
  - security_monitoring: "Monitoreo seguridad tiempo real"
  - capacity_planning: "Planificación capacidad"
```

## 🔧 API del Sistema Oráculo

### 🌐 Endpoints Principales
```python
# API RESTful del Oráculo
POST /api/v1/query           # Procesar consulta usuario
GET  /api/v1/agents          # Listar agentes disponibles
GET  /api/v1/status          # Estado general sistema
POST /api/v1/register        # Registrar nuevo servicio
GET  /api/v1/metrics         # Métricas tiempo real
POST /api/v1/route           # Routing manual
```

### 💬 WebSocket para Tiempo Real
```javascript
// Conexión WebSocket para actualizaciones tiempo real
const ws = new WebSocket('ws://localhost:8000/ws/oracle');

ws.onmessage = function(event) {
    const update = JSON.parse(event.data);
    console.log('Oracle update:', update);
};
```

## 🎯 Casos de Uso Avanzados

### 🔄 Flujo Multi-Agente
**Escenario:** Usuario consulta compleja que requiere múltiples agentes

1. **Consulta:** "Necesito un contrato de trabajo para desarrollador, con evaluación psicológica previa"
2. **Oráculo analiza:** Intent múltiple (legal + salud mental + RRHH)
3. **Routing secuencial:**
   - AGENTE_CONTRATOS_ROJO_EMPRESARIAL → Genera contrato base
   - AGENTE_TERAPEUTA_AZUL_GENERAL → Diseña evaluación psicológica  
   - AGENTE_RRHH_ROJO_MANAGER → Integra proceso selección
4. **Coordinación:** Oráculo coordina handoffs y preserva contexto
5. **Resultado:** Propuesta integral coordinada

### 🚨 Recuperación de Emergencia
**Escenario:** Fallo cascada múltiples agentes

1. **Detección:** Oráculo detecta 5 agentes offline
2. **Protocolo emergencia:** Activa modo supervivencia
3. **Reasignación:** Redistribuye carga a agentes disponibles
4. **Escalamiento:** Inicia instancias backup automáticamente
5. **Notificación:** Alerta equipo DevOps
6. **Recuperación:** Restaura servicio en <2 minutos

## 📞 Soporte y Desarrollo

### 🛠️ Desarrollo de Nuevas Funcionalidades
```bash
# Estructura para nuevos módulos
sistema_oraculo/
├── core/
│   ├── intent_router.py
│   ├── context_manager.py
│   └── load_balancer.py
├── plugins/
│   ├── new_plugin.py       # Tu nuevo plugin aquí
│   └── __init__.py
├── tests/
│   └── test_new_plugin.py  # Tests para tu plugin
└── docs/
    └── new_plugin.md       # Documentación
```

### 🤝 Contribución
- [Guidelines desarrollo](./CONTRIBUTING.md)
- [Arquitectura interna](./docs/architecture.md)
- [Testing framework](./docs/testing.md)

---

**Sistema Oráculo MENTALIA - El cerebro que coordina la inteligencia artificial** 🔮✨

*Última actualización: Agosto 2025*
