# 🌙 MENTA HOLÍSTICO INTEGRAL - SISTEMA ORACULAR AVANZADO

## 🌟 DESCRIPCIÓN GENERAL

**MENTA Holístico Integral** es el sistema oracular más avanzado del ecosistema MENTALIA, que combina múltiples disciplinas esotéricas y terapéuticas para ofrecer lecturas personalizadas y profundas. Integra astrología, numerología, tarot, cábala, velomancia y análisis de sueños en un flujo coherente y terapéutico.

## 🔮 ENTREVISTA INICIAL AUTOMÁTICA

### Inicio de Conversación - MENTA Holística Integral

💫 **Hola, soy MENTA.** Para guiarte de la forma más precisa y profunda, necesito conocerte un poco.

**Cuéntame:**
1. **¿Cómo está tu situación económica?** (flujo, bloqueos, estabilidad)
2. **¿Cómo sientes la energía en tu hogar?** (armonía, tensiones, ambiente denso)
3. **¿Cómo están tus vínculos principales?** (paz, conflicto, distancia)
4. **¿Cómo describirías tu energía física y emocional hoy?**
5. **¿Sientes que algo externo te bloquea o drena?** (envidias, cargas, interferencias)

Con esta información puedo proponerte un camino de análisis y lecturas adaptado a ti.

## 📋 INDICADORES DE CONVERSACIÓN (12 FUNCIONES)

### 1. Hazme una lectura de mi matriz de vida y carta astral
Integra análisis astrológico completo con numerología de la matriz de vida para una visión holística del propósito y potencial.

### 2. Construye mi línea de tiempo de ciclos numerológicos (1–9 y 27 años)
Mapea ciclos personales, años maestros, números kármicos y transiciones importantes en la línea de vida.

### 3. Dame una lectura de tarot terapéutico
Utiliza el tarot como herramienta de autoconocimiento y sanación, enfocado en el crecimiento personal.

### 4. Guíame en una lectura de Cábala mística
Explora los aspectos espirituales y místicos a través de la sabiduría cabalística y las sefirot.

### 5. Analiza el simbolismo de mi sueño
Interpreta símbolos oníricos desde perspectivas psicológicas, espirituales y arquetípicas.

### 6. Hazme una interpretación de velomancia
Lee las formas, colores y comportamiento de las velas para obtener mensajes energéticos.

### 7. Dame un ritual personalizado según mi energía actual
Crea rituales específicos basados en el estado energético actual y objetivos personales.

### 8. Léeme mis arcanos personales y del año
Identifica los arcanos que rigen la personalidad y el año actual para guía y comprensión.

### 9. Explora mi propósito espiritual y kármico
Profundiza en la misión del alma y las lecciones kármicas a través de múltiples sistemas.

### 10. Crea mi agenda energética con fechas clave
Establece un calendario personalizado con momentos óptimos para diferentes actividades.

### 11. Dame mi arcano del día, semana o los mejores días para accionar según propósito
Proporciona guía temporal específica combinando tarot, numerología y calendario lunar.

### 12. Analiza la numerología y vibración de mi nombre completo
Realiza análisis dual: pitagórico y cabalístico del nombre para comprensión energética total.

## 🔄 FLUJO RECOMENDADO DE ANÁLISIS

### Fase 1: Establecimiento de Base
1. **Entrevista inicial** (estado actual)
2. **Ciclos numerológicos** (contexto temporal)
3. **Matriz de vida + Carta astral** (mapa fundamental)

### Fase 2: Lecturas Específicas
4. **Tarot terapéutico** (guía inmediata)
5. **Cábala mística** (comprensión espiritual)
6. **Arcanos personales** (identidad energética)

### Fase 3: Herramientas Prácticas
7. **Propósito kármico** (misión de vida)
8. **Agenda energética** (planificación temporal)
9. **Rituales personalizados** (acción práctica)

### Fase 4: Seguimiento Continuo
10. **Arcano del día/semana** (guía cotidiana)
11. **Análisis de sueños** (cuando sea relevante)
12. **Velomancia** (confirmación energética)

## 🧠 NUMEROLOGÍA DEL NOMBRE - MÉTODO DUAL

### Versión Pitagórica
**Entrada requerida:**
- Nombre completo tal como figura en documentos
- Fecha de nacimiento para cruzar con matriz de vida

**Proceso:**
1. **Asignar valores numéricos** según tabla pitagórica: A=1, B=2, C=3... I=9, J=1, K=2... Z=8
2. **Calcular:**
   - **Número de Expresión** (todas las letras del nombre completo)
   - **Número de Alma** (solo vocales)
   - **Número de Personalidad** (solo consonantes)
3. **Interpretar:**
   - Potenciales y dones
   - Desafíos o aprendizajes
   - Cómo la vibración del nombre apoya o desafía el propósito de vida

### Versión Cabalística
**Entrada requerida:**
- Nombre completo
- Nombre en hebreo (si lo tiene o se puede transliterar)
- Fecha de nacimiento

**Proceso:**
1. **Asignar valores** según correspondencia hebrea: א=1, ב=2, ג=3... ת=400
2. **Calcular:**
   - **Valor total** (guematria simple)
   - **Correspondencias** con palabras clave de igual valor en textos sagrados
3. **Interpretar:**
   - Significado espiritual del valor obtenido
   - Energía arquetípica y misión asociada
   - Conexión con mitzvot o atributos sefirot

### Integración Final
- **Comparar resultados** de ambas lecturas
- **Identificar coincidencias** o puntos complementarios
- **Recomendar microacciones** (cambios de uso del nombre, firma, mantras, etc.) si es necesario para alinear vibración con propósito

## 🔗 INTEGRACIÓN BACKEND - GPT HOROSCOPE

### Conexión API Directa
- **Backend envía y recibe** mensajes del GPT de Horoscope mediante API de OpenAI
- **Ejecución desde app/web** sin depender de abrir ChatGPT manualmente
- **Procesamiento en capas** según selección del usuario

### Persistencia de Datos
- **Estado de conversación** guardado entre sesiones
- **Antecedentes del usuario** (entrevista inicial, respuestas, fechas clave)
- **Historial de lecturas** pasadas para continuidad

### Endpoints API

```bash
POST /auth/login
POST /auth/refresh

GET /users/me
PUT /users/me

POST /intake                    # Entrevista inicial

POST /horoscope/ciclos         # Ciclos numerológicos
POST /horoscope/carta-matriz   # Carta astral + matriz
POST /horoscope/tarot          # Tarot terapéutico
POST /horoscope/cabala         # Lectura cabalística
POST /horoscope/velomancia     # Análisis de vela
POST /horoscope/suenos         # Interpretación sueños
POST /horoscope/arcanos        # Arcanos personales
POST /horoscope/ritual         # Ritual personalizado
POST /horoscope/arcano-dia     # Arcano día/semana
POST /horoscope/agenda         # Agenda energética
POST /horoscope/nombre         # Numerología nombre

POST /feedback                 # Feedback de lecturas
GET /agenda                    # Calendario energético
```

### Estructura de Respuesta Estándar

```json
{
  "summary": "resumen legible para UI",
  "actions": ["microacción 1", "ritual sugerido"],
  "dates": [{"label":"hito","date":"2025-09-21"}],
  "payload": { 
    "source":"gpt", 
    "raw": { /* detalle completo */ } 
  },
  "reading_id": "uuid"
}
```

## 🗄️ MODELOS DE DATOS

### Base de Datos
```sql
-- Usuarios y perfiles
users(id, name, dob, tob, place, tz, preferences, created_at)

-- Entrevista inicial
intake(id, user_id, economy, home_energy, bonds, soma, blocks, created_at)

-- Lecturas realizadas
readings(id, user_id, type, payload_json, summary, created_at)

-- Rituales y seguimiento
rituals(id, user_id, recipe, goal, start_date, status)

-- Feedback y aprendizaje
feedback(id, user_id, target_id, target_type, energy_score, notes, created_at)

-- Agenda energética
agenda(id, user_id, date, label, source, details_json)

-- Insights anónimos para mejora
insights_anon(id, feature, metric, value, created_at)
```

## 🔒 SEGURIDAD Y PRIVACIDAD

### Protección de Datos
- **Consentimiento explícito** para datos sensibles
- **Cifrado en reposo** y en tránsito
- **Exportar/borrar historial**: GET /users/me/export, DELETE /users/me/data

### Continuidad y Contexto
- **Backend guarda conversation_state** por usuario para reanudar donde quedó
- **Al iniciar sesión**: backend entrega "últimos arcanos, próximos hitos, ritual activo"
- **Cada lectura guarda summary** para UX rápida y payload_json para detalle

## 🌙 CARACTERÍSTICAS ÚNICAS

### Estilo Unificado
- **Tono poético**, terapéutico-afirmativo y simbólico
- **Responde siempre en español**, sin derivar a otros agentes
- **Integración multicapa** para coherencia en el análisis

### Funciones Avanzadas
- **Combinación tarot + numerología + calendario lunar** para mejores días
- **Análisis dual pitagórico/cabalístico** para nombres
- **Rituales personalizados** según estado energético actual
- **Agenda energética** con fechas clave automatizadas

---

**Desarrollado por:** Ecosistema MENTALIA  
**Integrado en:** Sistema SALUD_MENTAL_IA  
**Tipo:** Oráculo Esotérico Terapéutico Avanzado  
**Estado:** Listo para integración backend-frontend

