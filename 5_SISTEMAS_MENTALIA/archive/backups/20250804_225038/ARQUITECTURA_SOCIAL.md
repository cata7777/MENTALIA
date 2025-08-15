# ARQUITECTURA SOCIAL MULTIMODAL
## Especificaciones Técnicas para Comunicación Social

---

## 🏗️ ARQUITECTURA GENERAL

### Stack Tecnológico Especializado:
```
Frontend Adaptativo:
├── React 18+ (TypeScript) - Interfaz principal
├── Three.js - Simulaciones 3D de interacciones
├── WebRTC - Análisis en tiempo real
├── D3.js - Visualizaciones de progreso social
└── Accessibility APIs - Soporte neurodivergente

Backend Inteligente:
├── Python 3.11 (FastAPI) - API principal
├── TensorFlow/PyTorch - Modelos de IA social
├── OpenCV + MediaPipe - Análisis visual
├── Librosa - Análisis prosódico
└── spaCy + Transformers - NLP emocional

Base de Datos Especializada:
├── PostgreSQL 15 - Datos de usuarios y progreso
├── Neo4j - Grafos de relaciones sociales
├── Redis 7 - Cache de análisis frecuentes
└── InfluxDB - Métricas temporales de progreso

Servicios de IA:
├── Emotion Recognition API
├── Social Context Analyzer
├── Communication Pattern Detector
└── Neurodivergent Profile Adapter
```

---

## 🧠 MODELOS DE IA ESPECIALIZADOS

### 1. Analizador de Microexpresiones Sociales
```python
import cv2
import mediapipe as mp
import tensorflow as tf
import numpy as np

class SocialMicroexpressionAnalyzer:
    """
    Analizador especializado en microexpresiones para contextos sociales
    Optimizado para personas neurodivergentes
    """
    
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=5,  # Análisis grupal
            refine_landmarks=True,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        
        # Modelo entrenado específicamente para contextos sociales
        self.emotion_model = tf.keras.models.load_model('social_emotion_model.h5')
        self.microexpression_detector = tf.keras.models.load_model('microexpression_model.h5')
        
        # Calibración para diferentes neurotipos
        self.neurodivergent_calibration = {
            'autism': {'sensitivity': 1.2, 'context_weight': 0.8},
            'adhd': {'sensitivity': 0.9, 'context_weight': 1.1},
            'typical': {'sensitivity': 1.0, 'context_weight': 1.0}
        }
    
    def analyze_social_emotions(self, frame, user_profile='typical'):
        """
        Analiza emociones en contexto social con calibración por neurotipo
        """
        results = self.face_mesh.process(frame)
        
        if not results.multi_face_landmarks:
            return None
        
        emotions_detected = []
        
        for face_landmarks in results.multi_face_landmarks:
            # Extraer características faciales
            landmarks_array = self.extract_landmark_features(face_landmarks)
            
            # Detectar emoción principal
            emotion_prediction = self.emotion_model.predict(landmarks_array.reshape(1, -1))
            
            # Detectar microexpresiones (cambios sutiles)
            microexpressions = self.detect_microexpressions(landmarks_array)
            
            # Aplicar calibración por neurotipo
            calibration = self.neurodivergent_calibration.get(user_profile, 
                                                            self.neurodivergent_calibration['typical'])
            
            emotions_detected.append({
                'primary_emotion': self.get_emotion_label(emotion_prediction),
                'confidence': float(np.max(emotion_prediction) * calibration['sensitivity']),
                'microexpressions': microexpressions,
                'social_context': self.analyze_social_context(landmarks_array, calibration),
                'interpretation': self.generate_social_interpretation(
                    emotion_prediction, microexpressions, user_profile
                )
            })
        
        return emotions_detected
    
    def detect_microexpressions(self, landmarks_array):
        """
        Detecta microexpresiones específicas relevantes para interacción social
        """
        microexp_prediction = self.microexpression_detector.predict(landmarks_array.reshape(1, -1))
        
        microexpressions = {
            'genuine_smile': microexp_prediction[0][0],
            'fake_smile': microexp_prediction[0][1],
            'confusion': microexp_prediction[0][2],
            'discomfort': microexp_prediction[0][3],
            'interest': microexp_prediction[0][4],
            'boredom': microexp_prediction[0][5],
            'agreement': microexp_prediction[0][6],
            'disagreement': microexp_prediction[0][7]
        }
        
        # Filtrar solo microexpresiones con alta confianza
        significant_microexp = {k: v for k, v in microexpressions.items() if v > 0.7}
        
        return significant_microexp
    
    def generate_social_interpretation(self, emotion, microexpressions, user_profile):
        """
        Genera interpretación social adaptada al perfil del usuario
        """
        primary_emotion = self.get_emotion_label(emotion)
        
        if user_profile == 'autism':
            return self.generate_autism_friendly_interpretation(primary_emotion, microexpressions)
        elif user_profile == 'adhd':
            return self.generate_adhd_friendly_interpretation(primary_emotion, microexpressions)
        else:
            return self.generate_general_interpretation(primary_emotion, microexpressions)
    
    def generate_autism_friendly_interpretation(self, emotion, microexpressions):
        """
        Interpretación específica para personas en el espectro autista
        """
        interpretations = {
            'happy': {
                'genuine_smile': "Esta persona está genuinamente contenta. Es seguro continuar la conversación.",
                'fake_smile': "Esta sonrisa parece forzada. Puede estar siendo cortés pero no necesariamente cómoda.",
                'default': "Esta persona parece contenta, pero observa su lenguaje corporal para más contexto."
            },
            'confused': {
                'confusion': "Esta persona no entiende algo. Considera explicar de manera más clara o preguntar qué necesita aclaración.",
                'default': "Hay confusión. Puede ser útil pausar y verificar comprensión mutua."
            },
            'neutral': {
                'interest': "Aunque su expresión es neutral, muestra signos de interés. Puedes continuar compartiendo.",
                'boredom': "Su expresión neutral puede indicar aburrimiento. Considera cambiar de tema o preguntar sobre sus intereses.",
                'default': "Expresión neutral. No hay señales claras de incomodidad, puedes continuar normalmente."
            }
        }
        
        emotion_interpretations = interpretations.get(emotion, {})
        
        # Buscar microexpresión más relevante
        for microexp, confidence in microexpressions.items():
            if microexp in emotion_interpretations:
                return emotion_interpretations[microexp]
        
        return emotion_interpretations.get('default', "No hay señales claras de incomodidad.")
```

### 2. Detector de Coherencia Comunicacional Social
```python
class SocialCoherenceAnalyzer:
    """
    Analiza coherencia entre diferentes modalidades de comunicación
    Especializado en contextos sociales cotidianos
    """
    
    def __init__(self):
        self.text_analyzer = pipeline("sentiment-analysis", 
                                    model="cardiffnlp/twitter-roberta-base-sentiment-latest")
        self.voice_analyzer = VoiceEmotionAnalyzer()
        self.context_analyzer = SocialContextAnalyzer()
    
    def analyze_communication_coherence(self, text, audio, visual, context):
        """
        Analiza coherencia entre texto, audio y visual en contexto social
        """
        # Análisis individual de cada modalidad
        text_sentiment = self.analyze_text_sentiment(text)
        voice_emotion = self.voice_analyzer.analyze_emotion(audio)
        visual_emotion = visual  # Ya analizado por MicroexpressionAnalyzer
        social_context = self.context_analyzer.analyze_context(context)
        
        # Calcular coherencia
        coherence_score = self.calculate_coherence_score(
            text_sentiment, voice_emotion, visual_emotion
        )
        
        # Detectar incongruencias específicas
        incongruences = self.detect_social_incongruences(
            text_sentiment, voice_emotion, visual_emotion, social_context
        )
        
        # Generar interpretación social
        interpretation = self.generate_social_interpretation(
            coherence_score, incongruences, social_context
        )
        
        return {
            'coherence_score': coherence_score,
            'incongruences': incongruences,
            'interpretation': interpretation,
            'social_guidance': self.generate_social_guidance(incongruences, social_context)
        }
    
    def detect_social_incongruences(self, text_sentiment, voice_emotion, visual_emotion, context):
        """
        Detecta incongruencias específicas relevantes para interacción social
        """
        incongruences = []
        
        # Incongruencia texto-visual
        if text_sentiment['label'] == 'POSITIVE' and visual_emotion.get('primary_emotion') == 'sad':
            incongruences.append({
                'type': 'text_visual_mismatch',
                'description': 'Dice algo positivo pero su expresión parece triste',
                'confidence': 0.8,
                'social_meaning': 'Puede estar ocultando tristeza o malestar'
            })
        
        # Incongruencia voz-contenido
        if 'angry' in voice_emotion and text_sentiment['label'] == 'POSITIVE':
            incongruences.append({
                'type': 'voice_content_mismatch',
                'description': 'Tono de voz molesto pero palabras positivas',
                'confidence': 0.85,
                'social_meaning': 'Posible sarcasmo o molestia contenida'
            })
        
        # Incongruencia contextual
        if context.get('situation') == 'celebration' and visual_emotion.get('primary_emotion') == 'sad':
            incongruences.append({
                'type': 'context_emotion_mismatch',
                'description': 'Emoción no coincide con el contexto social',
                'confidence': 0.75,
                'social_meaning': 'Puede estar pasando por algo personal'
            })
        
        return incongruences
    
    def generate_social_guidance(self, incongruences, context):
        """
        Genera guía social específica basada en incongruencias detectadas
        """
        if not incongruences:
            return {
                'message': 'La comunicación parece coherente. Puedes continuar normalmente.',
                'suggestions': ['Mantén el nivel actual de interacción']
            }
        
        guidance = {
            'message': 'Se detectaron algunas incongruencias en la comunicación.',
            'suggestions': []
        }
        
        for incongruence in incongruences:
            if incongruence['type'] == 'text_visual_mismatch':
                guidance['suggestions'].extend([
                    'Considera preguntar: "¿Estás bien? Pareces un poco triste"',
                    'Ofrece espacio para que expresen cómo se sienten realmente',
                    'No presiones si no quieren hablar'
                ])
            
            elif incongruence['type'] == 'voice_content_mismatch':
                guidance['suggestions'].extend([
                    'Puede haber sarcasmo o molestia. Pregunta para clarificar',
                    'Evita tomar las palabras al pie de la letra',
                    'Considera: "¿Hay algo que te molesta?"'
                ])
            
            elif incongruence['type'] == 'context_emotion_mismatch':
                guidance['suggestions'].extend([
                    'Respeta que puede estar pasando por algo personal',
                    'Ofrece apoyo sin ser intrusivo',
                    'Considera cambiar a un tema más neutral'
                ])
        
        return guidance
```

### 3. Simulador de Interacciones Sociales
```python
class SocialInteractionSimulator:
    """
    Simulador de interacciones sociales para entrenamiento
    """
    
    def __init__(self):
        self.scenario_database = self.load_scenario_database()
        self.personality_models = self.load_personality_models()
        self.response_generator = SocialResponseGenerator()
    
    def create_simulation(self, scenario_type, user_profile, difficulty_level):
        """
        Crea una simulación personalizada
        """
        scenario = self.scenario_database[scenario_type][difficulty_level]
        
        # Adaptar escenario al perfil del usuario
        adapted_scenario = self.adapt_scenario_to_profile(scenario, user_profile)
        
        # Crear personajes virtuales
        virtual_characters = self.create_virtual_characters(adapted_scenario)
        
        return {
            'scenario': adapted_scenario,
            'characters': virtual_characters,
            'learning_objectives': self.define_learning_objectives(scenario_type, user_profile),
            'success_criteria': self.define_success_criteria(scenario_type, difficulty_level)
        }
    
    def process_user_response(self, user_input, simulation_state):
        """
        Procesa respuesta del usuario y genera respuesta del personaje virtual
        """
        # Analizar respuesta del usuario
        user_analysis = self.analyze_user_response(user_input, simulation_state)
        
        # Generar respuesta del personaje virtual
        character_response = self.response_generator.generate_response(
            user_input, simulation_state, user_analysis
        )
        
        # Actualizar estado de la simulación
        updated_state = self.update_simulation_state(
            simulation_state, user_input, character_response, user_analysis
        )
        
        # Generar feedback en tiempo real
        feedback = self.generate_real_time_feedback(user_analysis, simulation_state)
        
        return {
            'character_response': character_response,
            'simulation_state': updated_state,
            'feedback': feedback,
            'progress_metrics': self.calculate_progress_metrics(updated_state)
        }
    
    def load_scenario_database(self):
        """
        Base de datos de escenarios sociales
        """
        return {
            'workplace': {
                'basic': [
                    {
                        'name': 'Presentarse a un nuevo colega',
                        'context': 'Primer día de trabajo, conocer al equipo',
                        'characters': ['colega_amigable', 'supervisor_ocupado'],
                        'objectives': ['hacer_buena_primera_impresion', 'obtener_informacion_basica'],
                        'challenges': ['nervios_primer_dia', 'recordar_nombres']
                    }
                ],
                'intermediate': [
                    {
                        'name': 'Dar feedback constructivo',
                        'context': 'Reunión de equipo, necesitas señalar un problema',
                        'characters': ['colega_defensivo', 'manager_observador'],
                        'objectives': ['comunicar_problema_claramente', 'mantener_relacion_positiva'],
                        'challenges': ['evitar_conflicto', 'ser_asertivo_sin_agredir']
                    }
                ],
                'advanced': [
                    {
                        'name': 'Mediar en conflicto de equipo',
                        'context': 'Dos colegas en desacuerdo, tú debes facilitar solución',
                        'characters': ['colega_frustrado', 'colega_terco', 'manager_estresado'],
                        'objectives': ['encontrar_solucion_mutua', 'mantener_neutralidad'],
                        'challenges': ['manejar_emociones_altas', 'no_tomar_lados']
                    }
                ]
            },
            'social': {
                'basic': [
                    {
                        'name': 'Small talk en una fiesta',
                        'context': 'Fiesta de cumpleaños, conoces pocas personas',
                        'characters': ['anfitrion_ocupado', 'invitado_timido', 'grupo_conversando'],
                        'objectives': ['iniciar_conversacion', 'mantener_dialogo_fluido'],
                        'challenges': ['encontrar_temas_comunes', 'manejar_silencios']
                    }
                ]
            }
        }
```

---

## 🎯 SISTEMA DE PERSONALIZACIÓN NEURODIVERGENTE

### Adaptador de Perfil Neurodivergente:
```python
class NeurodivergentProfileAdapter:
    """
    Adapta la experiencia de la app según el perfil neurodivergente del usuario
    """
    
    def __init__(self):
        self.profile_configurations = {
            'autism': {
                'sensory_preferences': {
                    'visual_stimulation': 'low',
                    'audio_volume': 'adjustable',
                    'animation_speed': 'slow',
                    'color_scheme': 'high_contrast'
                },
                'communication_adaptations': {
                    'literal_interpretation': True,
                    'direct_feedback': True,
                    'detailed_explanations': True,
                    'predictable_structure': True
                },
                'learning_preferences': {
                    'repetition_tolerance': 'high',
                    'pattern_recognition': 'excellent',
                    'detail_focus': 'high',
                    'routine_importance': 'critical'
                }
            },
            'adhd': {
                'attention_management': {
                    'session_length': 'short',
                    'break_frequency': 'high',
                    'gamification': 'high',
                    'immediate_feedback': True
                },
                'engagement_strategies': {
                    'variety': 'high',
                    'interactive_elements': 'many',
                    'progress_visualization': 'immediate',
                    'reward_frequency': 'high'
                }
            },
            'high_sensitivity': {
                'emotional_regulation': {
                    'gentle_feedback': True,
                    'emotional_preparation': True,
                    'safe_space_emphasis': True,
                    'overwhelm_prevention': True
                }
            }
        }
    
    def adapt_interface(self, user_profile):
        """
        Adapta la interfaz según el perfil neurodivergente
        """
        config = self.profile_configurations.get(user_profile, {})
        
        interface_adaptations = {
            'theme': self.select_appropriate_theme(config),
            'layout': self.adapt_layout(config),
            'interaction_patterns': self.adapt_interactions(config),
            'feedback_style': self.adapt_feedback_style(config)
        }
        
        return interface_adaptations
    
    def adapt_learning_content(self, content, user_profile):
        """
        Adapta el contenido de aprendizaje al perfil neurodivergente
        """
        config = self.profile_configurations.get(user_profile, {})
        
        if user_profile == 'autism':
            return self.adapt_for_autism(content, config)
        elif user_profile == 'adhd':
            return self.adapt_for_adhd(content, config)
        elif user_profile == 'high_sensitivity':
            return self.adapt_for_high_sensitivity(content, config)
        
        return content
    
    def adapt_for_autism(self, content, config):
        """
        Adaptaciones específicas para autismo
        """
        adapted_content = content.copy()
        
        # Estructura más predecible
        adapted_content['structure'] = 'highly_structured'
        
        # Explicaciones más detalladas
        adapted_content['explanation_detail'] = 'comprehensive'
        
        # Ejemplos concretos en lugar de abstractos
        adapted_content['examples'] = self.make_examples_concrete(content['examples'])
        
        # Feedback directo y específico
        adapted_content['feedback_style'] = 'direct_specific'
        
        return adapted_content
    
    def adapt_for_adhd(self, content, config):
        """
        Adaptaciones específicas para TDAH
        """
        adapted_content = content.copy()
        
        # Sesiones más cortas
        adapted_content['session_length'] = min(content.get('session_length', 30), 15)
        
        # Más elementos interactivos
        adapted_content['interactivity'] = 'high'
        
        # Gamificación aumentada
        adapted_content['gamification'] = self.add_gamification_elements(content)
        
        # Feedback inmediato
        adapted_content['feedback_frequency'] = 'immediate'
        
        return adapted_content
```

---

## 📊 SISTEMA DE MÉTRICAS Y PROGRESO

### Analizador de Progreso Social:
```python
class SocialProgressAnalyzer:
    """
    Analiza y rastrea el progreso en habilidades sociales
    """
    
    def __init__(self):
        self.metrics_database = InfluxDBClient()
        self.progress_calculator = ProgressCalculator()
        self.goal_tracker = SocialGoalTracker()
    
    def track_interaction_metrics(self, user_id, interaction_data):
        """
        Rastrea métricas de una interacción social
        """
        metrics = {
            'timestamp': datetime.now(),
            'user_id': user_id,
            'interaction_type': interaction_data['type'],
            'duration': interaction_data['duration'],
            'confidence_level': interaction_data['user_confidence'],
            'success_indicators': self.calculate_success_indicators(interaction_data),
            'areas_improved': self.identify_improvements(interaction_data),
            'challenges_faced': self.identify_challenges(interaction_data)
        }
        
        # Guardar en base de datos temporal
        self.metrics_database.write_points([metrics])
        
        # Calcular progreso
        progress_update = self.calculate_progress_update(user_id, metrics)
        
        return progress_update
    
    def calculate_success_indicators(self, interaction_data):
        """
        Calcula indicadores de éxito de la interacción
        """
        indicators = {}
        
        # Duración apropiada de la conversación
        if interaction_data['type'] == 'small_talk':
            target_duration = 180  # 3 minutos
            indicators['duration_appropriateness'] = min(1.0, 
                interaction_data['duration'] / target_duration)
        
        # Reciprocidad en la conversación
        if 'turn_taking' in interaction_data:
            indicators['reciprocity'] = interaction_data['turn_taking']['balance_score']
        
        # Coherencia emocional
        if 'emotional_coherence' in interaction_data:
            indicators['emotional_coherence'] = interaction_data['emotional_coherence']['score']
        
        # Uso apropiado de contacto visual
        if 'eye_contact' in interaction_data:
            indicators['eye_contact_appropriateness'] = interaction_data['eye_contact']['appropriateness_score']
        
        return indicators
    
    def generate_progress_report(self, user_id, timeframe='week'):
        """
        Genera reporte de progreso personalizado
        """
        # Obtener datos del período
        metrics = self.get_user_metrics(user_id, timeframe)
        
        # Calcular tendencias
        trends = self.calculate_trends(metrics)
        
        # Identificar logros
        achievements = self.identify_achievements(metrics)
        
        # Generar recomendaciones
        recommendations = self.generate_recommendations(trends, achievements)
        
        return {
            'period': timeframe,
            'summary': self.generate_summary(trends),
            'achievements': achievements,
            'areas_of_growth': trends['improving_areas'],
            'challenges': trends['challenging_areas'],
            'recommendations': recommendations,
            'next_goals': self.suggest_next_goals(trends, achievements)
        }
```

---

## 🔧 CONFIGURACIÓN DE DESPLIEGUE RUNPOD

### Docker Compose Especializado:
```yaml
version: '3.8'

services:
  # API Principal de Comunicación Social
  comunicacion-social-api:
    build: 
      context: ./backend
      dockerfile: Dockerfile.social
    ports:
      - "8002:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@postgres:5432/comunicacion_social
      - REDIS_URL=redis://redis:6379
      - NEO4J_URL=bolt://neo4j:7687
      - INFLUXDB_URL=http://influxdb:8086
      - GPU_ENABLED=true
      - NEURODIVERGENT_MODELS_PATH=/app/models/neurodivergent
    volumes:
      - ./models:/app/models
      - ./user_data:/app/user_data
    depends_on:
      - postgres
      - redis
      - neo4j
      - influxdb
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  # Frontend Adaptativo
  comunicacion-social-web:
    build:
      context: ./frontend
      dockerfile: Dockerfile.adaptive
    ports:
      - "3002:3000"
    environment:
      - REACT_APP_API_URL=http://comunicacion-social-api:8000
      - REACT_APP_WS_URL=ws://comunicacion-social-api:8000/ws
      - REACT_APP_ACCESSIBILITY_MODE=enhanced
    depends_on:
      - comunicacion-social-api

  # Base de datos de grafos para relaciones sociales
  neo4j:
    image: neo4j:5
    environment:
      - NEO4J_AUTH=neo4j/social_password
      - NEO4J_PLUGINS=["graph-data-science"]
    volumes:
      - neo4j_data:/data
    ports:
      - "7474:7474"
      - "7687:7687"

  # Base de datos temporal para métricas
  influxdb:
    image: influxdb:2.7
    environment:
      - INFLUXDB_DB=social_metrics
      - INFLUXDB_ADMIN_USER=admin
      - INFLUXDB_ADMIN_PASSWORD=social_admin
    volumes:
      - influxdb_data:/var/lib/influxdb2
    ports:
      - "8086:8086"

  # Servicio de simulaciones sociales
  social-simulator:
    build:
      context: ./simulator
      dockerfile: Dockerfile
    environment:
      - SIMULATION_ENGINE=advanced
      - CHARACTER_AI_MODELS=/app/models/characters
    volumes:
      - ./models/characters:/app/models/characters
    depends_on:
      - comunicacion-social-api

  # Servicio de análisis neurodivergente
  neurodivergent-analyzer:
    build:
      context: ./neurodivergent
      dockerfile: Dockerfile
    environment:
      - PROFILE_MODELS_PATH=/app/models/profiles
      - ADAPTATION_ENGINE=enabled
    volumes:
      - ./models/profiles:/app/models/profiles
    depends_on:
      - comunicacion-social-api

volumes:
  neo4j_data:
  influxdb_data:
```

### Nginx Configuration para Comunicación Social:
```nginx
# Configuración específica para Comunicación Social
location /ComunicacionSocial/ {
    # Configuraciones de accesibilidad
    add_header X-Accessibility-Features "neurodivergent-optimized";
    add_header X-Content-Type-Options nosniff;
    
    proxy_pass http://comunicacion-social-web/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    
    # Configuraciones especiales para usuarios neurodivergentes
    proxy_read_timeout 300s;  # Más tiempo para procesamiento
    proxy_send_timeout 300s;
}

location /ComunicacionSocial/api/ {
    proxy_pass http://comunicacion-social-api/api/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    
    # Configuraciones para análisis en tiempo real
    proxy_buffering off;
    proxy_cache off;
}

# WebSocket para análisis en tiempo real
location /ComunicacionSocial/ws/ {
    proxy_pass http://comunicacion-social-api/ws/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    
    # Configuraciones para sesiones largas de entrenamiento
    proxy_read_timeout 3600s;  # 1 hora
    proxy_send_timeout 3600s;
}
```

---

## 🔒 CONSIDERACIONES DE PRIVACIDAD Y ÉTICA

### Protección de Datos Neurodivergentes:
```python
class NeurodivergentDataProtection:
    """
    Protección especializada para datos de usuarios neurodivergentes
    """
    
    def __init__(self):
        self.encryption_key = self.generate_encryption_key()
        self.anonymization_engine = AnonymizationEngine()
        self.consent_manager = ConsentManager()
    
    def protect_sensitive_data(self, user_data):
        """
        Protege datos especialmente sensibles de usuarios neurodivergentes
        """
        # Identificar datos sensibles
        sensitive_fields = [
            'neurodivergent_diagnosis',
            'social_challenges',
            'therapy_history',
            'medication_info',
            'family_dynamics'
        ]
        
        protected_data = user_data.copy()
        
        for field in sensitive_fields:
            if field in protected_data:
                # Encriptar datos sensibles
                protected_data[field] = self.encrypt_field(protected_data[field])
        
        return protected_data
    
    def anonymize_for_research(self, user_data):
        """
        Anonimiza datos para investigación respetando neurodivergencia
        """
        # Remover identificadores directos
        anonymized = self.anonymization_engine.remove_direct_identifiers(user_data)
        
        # Generalizar datos demográficos
        anonymized = self.generalize_demographics(anonymized)
        
        # Preservar patrones importantes para investigación
        anonymized = self.preserve_research_patterns(anonymized)
        
        return anonymized
    
    def ensure_informed_consent(self, user_profile, consent_request):
        """
        Asegura consentimiento informado adaptado al perfil neurodivergente
        """
        if user_profile == 'autism':
            return self.autism_friendly_consent(consent_request)
        elif user_profile == 'adhd':
            return self.adhd_friendly_consent(consent_request)
        else:
            return self.standard_consent(consent_request)
    
    def autism_friendly_consent(self, consent_request):
        """
        Proceso de consentimiento adaptado para autismo
        """
        return {
            'format': 'detailed_structured',
            'language': 'literal_clear',
            'examples': 'concrete_specific',
            'time_to_decide': 'extended',
            'questions_allowed': 'unlimited',
            'withdrawal_process': 'clearly_explained'
        }
```

---

## 📈 MÉTRICAS DE RENDIMIENTO ESPECIALIZADO

### Monitoreo de Accesibilidad:
```python
class AccessibilityMetrics:
    """
    Métricas específicas para accesibilidad neurodivergente
    """
    
    def __init__(self):
        self.metrics_collector = MetricsCollector()
        self.accessibility_analyzer = AccessibilityAnalyzer()
    
    def track_accessibility_usage(self, user_id, session_data):
        """
        Rastrea uso de características de accesibilidad
        """
        accessibility_metrics = {
            'sensory_adjustments_used': session_data.get('sensory_adjustments', []),
            'interface_adaptations_active': session_data.get('adaptations', []),
            'break_frequency': session_data.get('breaks_taken', 0),
            'session_completion_rate': session_data.get('completion_rate', 0),
            'user_satisfaction': session_data.get('satisfaction_score', 0),
            'cognitive_load_indicators': self.calculate_cognitive_load(session_data)
        }
        
        return accessibility_metrics
    
    def calculate_cognitive_load(self, session_data):
        """
        Calcula indicadores de carga cognitiva
        """
        indicators = {
            'task_switching_frequency': session_data.get('task_switches', 0),
            'error_rate': session_data.get('errors', 0) / session_data.get('total_actions', 1),
            'response_time_variance': self.calculate_response_variance(session_data),
            'help_requests': session_data.get('help_requests', 0)
        }
        
        # Calcular score de carga cognitiva
        cognitive_load_score = (
            indicators['task_switching_frequency'] * 0.2 +
            indicators['error_rate'] * 0.3 +
            indicators['response_time_variance'] * 0.3 +
            indicators['help_requests'] * 0.2
        )
        
        return {
            'score': cognitive_load_score,
            'level': self.categorize_cognitive_load(cognitive_load_score),
            'indicators': indicators
        }
```

---

**Esta arquitectura técnica proporciona una base sólida, accesible y éticamente responsable para Comunicación Social Multimodal, optimizada específicamente para usuarios neurodivergentes y su integración perfecta con el ecosistema MENTALIA.**

