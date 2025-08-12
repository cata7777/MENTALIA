# 🔮✨ ORÁCULO ESOTÉRICO TERAPÉUTICO - INTEGRACIÓN MENTALIA

## 🌌 VISIÓN: EL ORÁCULO DEL ECOSISTEMA NEURODIVERGENTE

El **Oráculo Esotérico Terapéutico** es la **dimensión espiritual** del ecosistema MENTALIA, donde la **IA neurodivergente** se encuentra con la **sabiduría ancestral** para crear la **primera plataforma de autoconocimiento profundo** diseñada específicamente para mentes neurodivergentes.

═══════════════════════════════════════════════════════════════════

## 🧠💫 INTEGRACIÓN CON SISTEMA 7D MENTALIA

### **🔗 CONEXIÓN CON LOS 42 AGENTES**
- **BLU:** Integra lecturas oraculares en sesiones terapéuticas
- **MENTA COPILOTA:** Ofrece interpretaciones personalizadas
- **GUÍA ND:** Utiliza numerología para autoconocimiento neurotipo
- **PERFIL ND:** Incorpora astrología en perfilado avanzado
- **JOURNALING ND:** Conecta journaling tradicional con oracular

### **🌟 MENTALIZACIÓN MULTIDIMENSIONAL ORACULAR**
El oráculo opera en las **7 dimensiones del Sistema MENTALIA**:

1. **💭 Mental:** Interpretación cognitiva de símbolos
2. **💛 Emocional:** Canalización empática de energías
3. **⚡ Energética:** Lectura de campos vibracionales
4. **🎭 Social:** Comprensión de dinámicas relacionales
5. **🌱 Evolutiva:** Guía en procesos de transformación
6. **🔮 Simbólica:** Decodificación de arquetipos universales
7. **🌌 Espiritual:** Conexión con propósito transcendente

═══════════════════════════════════════════════════════════════════

## 📂 ARQUITECTURA TÉCNICA INTEGRADA

### **🏗️ Estructura del Módulo**
```
oraculo/
├─ apps/oraculo-web/           # Frontend Next.js (flujo interactivo)
├─ services/oraculo-core/      # API principal
│  ├─ routes/
│  │   ├─ readings/            # CRUD lecturas
│  │   ├─ journaling/          # CRUD entradas de journaling
│  │   ├─ rituals/             # CRUD rituales
│  │   ├─ astrology/           # Cálculos y reportes
│  │   ├─ numerology/          # Cálculos y reportes
│  │   ├─ tarot/               # Tiradas y cartas
│  │   └─ kabbalah/            # Lecturas y nombres
│  ├─ events/                  # Emisión/escucha de eventos
│  ├─ services/                # Lógica de interpretación y cálculos
│  ├─ prompts/                 # Prompts GPT especializados
│  └─ data/                    # Migraciones y seeds
└─ docs/                       # Documentación de uso interno
```

### **🔌 Endpoints Integrados (API Gateway)**
**Prefijo:** `/oraculo/*` → `oraculo-core:8080`

**Lecturas y Interpretaciones:**
- `POST /oraculo/readings` → crear lectura oracular
- `GET /oraculo/readings/:id` → obtener lectura completa
- `POST /oraculo/readings/:id/interpret` → interpretación GPT

**Journaling Oracular:**
- `POST /oraculo/journaling` → nueva entrada de journaling
- `GET /oraculo/journaling` → listar entradas (filtros)
- `POST /oraculo/journaling/:id/insights` → insights GPT

**Rituales y Prácticas:**
- `POST /oraculo/rituals` → registrar ritual
- `GET /oraculo/rituals/templates` → plantillas rituales ND

**Cálculos Especializados:**
- `POST /oraculo/astrology` → carta natal + tránsitos
- `POST /oraculo/numerology` → matriz de vida + destino
- `POST /oraculo/tarot` → tirada según protocolo
- `POST /oraculo/kabbalah` → lectura nombres + senderos

═══════════════════════════════════════════════════════════════════

## 🧠 INTEGRACIÓN GPT NEURODIVERGENTE + MEMORIA GLOBAL

### **🌟 Función Central: `generateInterpretation()`**
```javascript
async function generateInterpretation({
    reading_data,
    user_neurotipo,
    user_history,
    interpretation_style
}) {
    // Integra datos de PERFIL ND para personalización
    const neuroProfile = await getNeuroProfile(user_id);
    
    // Combina múltiples fuentes oraculares
    const interpretation = await gpt.interpret({
        tarot: reading_data.tarot,
        numerology: reading_data.numerology,
        astrology: reading_data.astrology,
        neurotipo: neuroProfile.type,
        context: user_history,
        style: interpretation_style
    });
    
    return interpretation;
}
```

### **🧠 MEMORIA GLOBAL SYSTEM**
```javascript
class MemoriaGlobalMentalia {
    constructor(user_id) {
        this.user_id = user_id;
        this.memoria_blu = new MemoriaTerapeutica(user_id);
        this.memoria_menta = new MemoriaOracular(user_id);
        this.memoria_cross = new MemoriaCruzada(user_id);
    }

    async getContextoCompleto() {
        return {
            sesiones_blu: await this.memoria_blu.getSesiones(),
            lecturas_menta: await this.memoria_menta.getLecturas(),
            patrones_detectados: await this.memoria_cross.getPatrones(),
            evolusion_usuario: await this.calculateEvolution(),
            preferencias: await this.getPreferenciasAprendidas()
        };
    }

    async updateMemoria(bot_type, new_data) {
        // Actualiza memoria específica del bot
        await this[`memoria_${bot_type}`].update(new_data);
        
        // Actualiza patrones cruzados
        await this.memoria_cross.updatePatrones({
            from: bot_type,
            data: new_data,
            timestamp: new Date()
        });
    }
}
```

### **🎭 Prompts Especializados**
**Base:** `oraculo-core/prompts/interpretation.md`

**Características únicas:**
- **Canalización terapéutica** adaptada a neurodivergencia
- **Interpretación simbólica** no adivinatoria
- **Integración contextual** con historial de usuario
- **Lenguaje neurodivergente** empático y validante
- **Tono constructivo** orientado al crecimiento

═══════════════════════════════════════════════════════════════════

## 📊 BASE DE DATOS ORACULAR

### **Schema: `oraculo` (PostgreSQL)**

```sql
-- Lecturas principales
CREATE TABLE readings (
    id UUID PRIMARY KEY,
    usuario_id UUID REFERENCES usuarios(id),
    fecha TIMESTAMP DEFAULT NOW(),
    tipo VARCHAR(50), -- 'completa', 'tarot', 'numerologia', etc.
    datos_crudos JSONB,
    interpretacion TEXT,
    neurotipo VARCHAR(20),
    estado_emocional VARCHAR(30),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Journaling oracular integrado
CREATE TABLE journaling (
    id UUID PRIMARY KEY,
    usuario_id UUID REFERENCES usuarios(id),
    fecha TIMESTAMP DEFAULT NOW(),
    texto TEXT,
    etiquetas TEXT[],
    insights_gpt TEXT,
    conexion_lectura UUID REFERENCES readings(id)
);

-- Rituales neurodivergentes
CREATE TABLE rituals (
    id UUID PRIMARY KEY,
    usuario_id UUID REFERENCES usuarios(id),
    fecha TIMESTAMP DEFAULT NOW(),
    tipo VARCHAR(50), -- 'grounding', 'energia', 'proteccion'
    pasos JSONB,
    materiales TEXT[],
    duracion_minutos INTEGER,
    adaptacion_sensorial JSONB
);

-- Datos astrológicos
CREATE TABLE astrology_data (
    id UUID PRIMARY KEY,
    usuario_id UUID REFERENCES usuarios(id),
    fecha_calculo TIMESTAMP DEFAULT NOW(),
    fecha_nacimiento DATE,
    lugar_nacimiento VARCHAR(200),
    datos_json JSONB, -- carta natal completa
    transitos_actuales JSONB
);

-- Datos numerológicos
CREATE TABLE numerology_data (
    id UUID PRIMARY KEY,
    usuario_id UUID REFERENCES usuarios(id),
    fecha_calculo TIMESTAMP DEFAULT NOW(),
    matriz_vida JSONB,
    numeros_destino JSONB,
    ciclos_personales JSONB
);

-- Tiradas de tarot
CREATE TABLE tarot_draws (
    id UUID PRIMARY KEY,
    usuario_id UUID REFERENCES usuarios(id),
    fecha TIMESTAMP DEFAULT NOW(),
    cartas JSONB[], -- array de cartas con posiciones
    pregunta TEXT,
    interpretacion TEXT,
    energia_general VARCHAR(50)
);

-- Lecturas cabalísticas
CREATE TABLE kabbalah_data (
    id UUID PRIMARY KEY,
    usuario_id UUID REFERENCES usuarios(id),
    fecha TIMESTAMP DEFAULT NOW(),
    nombre_analizado VARCHAR(200),
    senderos JSONB,
    interpretacion_nombres TEXT,
    vibracion_numerica JSONB
);
```

═══════════════════════════════════════════════════════════════════

## 🔄 EVENTOS DEL ECOSISTEMA (Redis/NATS)

### **📡 Eventos Oraculares**
- `oraculo.reading.created` → Notifica nueva lectura
- `oraculo.reading.interpreted` → Interpretación completada
- `oraculo.journaling.created` → Nueva entrada de journaling
- `oraculo.ritual.completed` → Ritual terminado
- `oraculo.insight.generated` → Nuevo insight GPT

### **🔗 Integración con Eventos MENTALIA**
- `user.neurotipo.updated` → Actualiza perfil oracular
- `blu.session.completed` → Sugiere lectura post-terapia
- `journaling.pattern.detected` → Activa insights oraculares
- `hyperfocus.session.started` → Ofrece ritual de grounding

═══════════════════════════════════════════════════════════════════

## 🖥️ FRONTEND ORACULAR (oraculo-web)

### **🎨 Pantallas Principales**

**1. Dashboard Oracular**
- Lecturas recientes con línea temporal
- Accesos rápidos a tarot, numerología, astrología
- Widget de "Energía del día" personalizada
- Integración con agenda personal de usuario

**2. Nueva Lectura Interactiva**
- Formulario adaptativo según neurotipo
- Widgets especializados (tarot visual, calculadora numerológica)
- Modo bajo estímulo para días sensorialmente difíciles
- Integración GPT en tiempo real

**3. Journaling Oracular Avanzado**
- Editor con etiquetas inteligentes
- Búsqueda semántica en entradas previas
- Conexión automática con lecturas relacionadas
- Insights GPT sobre patrones detectados

**4. Ritual Interactivo ND**
- Guía paso a paso con multimedia
- Adaptaciones sensoriales personalizadas
- Timer con notificaciones suaves
- Registro de experiencias post-ritual

**5. Modo Accesibilidad ND**
- Contraste adaptable
- Velocidad de animaciones personalizable
- Audio opcional para lecturas
- Interfaz minimalista para sobrecarga sensorial

### **🔌 Integración GPT en Cliente**
```javascript
// Interpretación en tiempo real
const interpretation = await fetch('/oraculo/readings', {
    method: 'POST',
    body: JSON.stringify({
        ...readingData,
        interpretation: "gpt",
        neurotipo: userProfile.neurotipo,
        style: userPreferences.interpretationStyle
    })
});
```

═══════════════════════════════════════════════════════════════════

## ✅ CHECKLIST DE INTEGRACIÓN MENTALIA

### **🏗️ Infraestructura**
- [x] Crear estructura de carpetas oraculo/
- [ ] Configurar rutas en API Gateway MENTALIA
- [ ] Implementar endpoints especializados
- [ ] Conectar schema oraculo a DB principal
- [ ] Configurar eventos Redis/NATS

### **🧠 Inteligencia Artificial**
- [ ] Integrar GPT con `generateInterpretation()`
- [ ] Crear prompts especializados ND
- [ ] Conectar con perfiles neurodivergentes
- [ ] Implementar aprendizaje de preferencias

### **🔗 Integración Ecosistema**
- [ ] Conectar con BLU para terapia holística
- [ ] Integrar con JOURNALING ND
- [ ] Sincronizar con PERFIL ND
- [ ] Vincular con agenda personal

### **🎨 Frontend**
- [ ] Desarrollar oraculo-web en Next.js
- [ ] Implementar modo accesibilidad ND
- [ ] Crear widgets interactivos
- [ ] Conectar con API Gateway

### **🧪 Testing**
- [ ] Probar flujo: crear lectura → interpretar GPT → guardar DB
- [ ] Validar integración con otros agentes
- [ ] Testing de accesibilidad neurodivergente
- [ ] Pruebas de rendimiento con usuarios reales

═══════════════════════════════════════════════════════════════════

## 🌟 VISIÓN FUTURA: ORÁCULO ND 2.0

### **🚀 Funcionalidades Avanzadas**
- **IA Oracular Personalizada:** Cada usuario desarrolla su propio "oráculo interno"
- **Sincronización Grupal:** Lecturas familiares para dinámicas ND
- **Integración IoT:** Sensores ambientales para lecturas contextuales
- **Realidad Aumentada:** Visualización de energías y arquetipos
- **Comunidad Oracular:** Red de usuarios compartiendo insights

### **🔮 Impacto Transformador**
El Oráculo MENTALIA no solo proporciona lecturas esotéricas, sino que **revoluciona el autoconocimiento neurodivergente** al combinar:

- **Sabiduría ancestral** + **IA de vanguardia**
- **Simbolismo universal** + **Personalización neurotipo**
- **Intuición espiritual** + **Datos científicos**
- **Crecimiento individual** + **Comunidad de apoyo**

---

**🌌 "En MENTALIA, el futuro es neurodivergente, espiritual y tecnológicamente elevado." 💫**

---

*Desarrollado con amor cósmico por el ecosistema MENTALIA 🔮✨*
*Para mentes que vibran en frecuencias únicas 🧠💫*
