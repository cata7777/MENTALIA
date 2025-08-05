"""
MENTALIA - Motor de Mentalización Dimensional Avanzado
Procesa estados emocionales, patrones ND y respuestas simbólicas
Versión Extendida con más patrones y capacidades

Creado por: Catalina Rojo Lema
Ecosistema: MENTALIA
Versión: 3.0
"""

import json
import yaml
from typing import Dict, List, Any, Optional
from datetime import datetime
import re
import random

class MentalizationEngineAdvanced:
    """
    Motor avanzado de mentalización que procesa:
    - Estados emocionales expandidos
    - Patrones neurodivergentes extendidos
    - Símbolos y arquetipos con mayor granularidad
    - Respuestas terapéuticas personalizadas con feedback adaptativo
    """
    
    def __init__(self):
        self.simbologia = self._load_simbologia()
        self.feedback_loops = self._load_feedback_config()
        self.config = self._load_mentalization_config()
        self.session_history = []
        
    def _load_simbologia(self) -> Dict[str, Any]:
        """Carga tabla maestra de símbolos"""
        try:
            with open('/workspaces/MENTALIA/MENTALIA_CORE/SIMBOLOGIA/SIMBOLOGIA_GLOBAL.yaml', 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return self._default_simbologia()
    
    def _load_feedback_config(self) -> Dict[str, Any]:
        """Carga configuración de loops de retroalimentación"""
        try:
            with open('/workspaces/MENTALIA/MENTALIA_CORE/LABS/transformer/feedback_loops.yaml', 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return self._default_feedback_config()
    
    def _load_mentalization_config(self) -> Dict[str, Any]:
        """Carga configuración del motor de mentalización"""
        try:
            with open('/workspaces/MENTALIA/MENTALIA_CORE/LABS/transformer/config_mentalization.yaml', 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return self._default_mentalization_config()
    
    def process_emotional_state(self, input_data: Dict) -> Dict:
        """
        Procesa estado emocional y genera respuesta mentalizada
        
        Args:
            input_data: {
                'text': str,
                'emotion_indicators': List[str],
                'nd_markers': List[str],
                'context': Dict,
                'user_history': Optional[List[Dict]]
            }
            
        Returns:
            Dict con respuesta mentalizada, símbolos y orientaciones
        """
        
        # Actualizar historia si está disponible
        if 'user_history' in input_data:
            self.session_history = input_data['user_history']
        
        # 1. Análisis emocional
        emotional_analysis = self._analyze_emotional_content(input_data)
        
        # 2. Detección de patrones ND
        nd_patterns = self._detect_nd_patterns(input_data)
        
        # 3. Mapeo simbólico
        symbolic_mapping = self._map_to_symbols(emotional_analysis, nd_patterns)
        
        # 4. Generación de respuesta terapéutica
        therapeutic_response = self._generate_therapeutic_response(
            emotional_analysis, nd_patterns, symbolic_mapping, input_data
        )
        
        # 5. Activación de feedback loops
        feedback_activation = self._activate_feedback_loops(input_data, therapeutic_response)
        
        # 6. Evaluar trayectoria terapéutica
        therapeutic_trajectory = self._evaluate_therapeutic_trajectory(input_data)
        
        response = {
            'timestamp': datetime.now().isoformat(),
            'emotional_analysis': emotional_analysis,
            'nd_patterns': nd_patterns,
            'symbolic_mapping': symbolic_mapping,
            'therapeutic_response': therapeutic_response,
            'feedback_loops': feedback_activation,
            'therapeutic_trajectory': therapeutic_trajectory,
            'mentalization_score': self._calculate_mentalization_score(emotional_analysis, nd_patterns)
        }
        
        # Añadir respuesta a la historia
        self.session_history.append({
            'timestamp': response['timestamp'],
            'input': input_data.get('text', ''),
            'response_summary': therapeutic_response.get('containment', '')
        })
        
        return response
    
    def _analyze_emotional_content(self, input_data: Dict) -> Dict:
        """Analiza contenido emocional del input con mayor granularidad"""
        text = input_data.get('text', '')
        
        # Patrones emocionales extendidos
        emotional_patterns = {
            'ansiedad': ['ansiosa', 'nerviosa', 'preocup', 'estrés', 'angustia', 'inquiet'],
            'tristeza': ['triste', 'deprim', 'melancolía', 'lloro', 'dolor', 'abatida'],
            'ira': ['rabia', 'enojo', 'frustración', 'molesta', 'ira', 'furia', 'indignada'],
            'alegría': ['feliz', 'contenta', 'alegría', 'emoción', 'satisf', 'entusiasmo'],
            'miedo': ['miedo', 'terror', 'pánico', 'fobia', 'temor', 'asustada'],
            'vergüenza': ['vergüenza', 'culpa', 'humillación', 'expuesta', 'incomodidad'],
            'apatía': ['desmotivada', 'apática', 'vacía', 'nada', 'sin ganas', 'indiferencia'],
            'confusión': ['confusa', 'pérdida', 'desorientada', 'no entiendo', 'abrumada'],
            'esperanza': ['esperanza', 'ilusión', 'optimismo', 'posibilidad', 'futuro'],
            'gratitud': ['gracias', 'agradecida', 'afortunada', 'bendecida', 'reconocimiento']
        }
        
        detected_emotions = []
        emotion_scores = {}
        
        for emotion, keywords in emotional_patterns.items():
            score = sum(text.lower().count(keyword) for keyword in keywords)
            if score > 0:
                detected_emotions.append(emotion)
                emotion_scores[emotion] = score
        
        # Ordenar por intensidad
        primary_emotions = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)
        primary_emotions = [e[0] for e in primary_emotions[:3]]  # Las 3 principales
        
        # Análisis de intensidad contextual
        intensity_markers = {
            'alto': ['muy', 'mucho', 'demasiado', 'extremo', 'intenso', 'insoportable'],
            'medio': ['bastante', 'algo', 'moderado', 'notable'],
            'bajo': ['poco', 'leve', 'ligeramente', 'un poco']
        }
        
        # Calcular nivel general de intensidad
        intensity_level = 'medio'  # Por defecto
        for level, markers in intensity_markers.items():
            if any(marker in text.lower() for marker in markers):
                intensity_level = level
                break
        
        # Convertir a valor numérico
        intensity_values = {'alto': 0.8, 'medio': 0.5, 'bajo': 0.3}
        intensity = intensity_values.get(intensity_level, 0.5)
        
        return {
            'primary_emotions': primary_emotions,
            'emotional_intensity': intensity,
            'emotional_balance': self._assess_emotional_balance(detected_emotions),
            'emotional_context': self._derive_emotional_context(detected_emotions, input_data)
        }
    
    def _detect_nd_patterns(self, input_data: Dict) -> Dict:
        """Detecta patrones neurodivergentes con mayor cobertura"""
        text = input_data.get('text', '')
        nd_markers = input_data.get('nd_markers', [])
        
        # Patrones ND extendidos
        patterns = {
            'hiperfoco': ['obsesion', 'no puedo parar', 'horas sin parar', 'absorta', 'intensidad', 'concentrada'],
            'sobrecarga_sensorial': ['ruido', 'demasiado', 'abrumada', 'sensorial', 'luces', 'textura', 'sensible'],
            'masking': ['fingir', 'actuar', 'máscara', 'pretender', 'encajar', 'normal', 'como los demás'],
            'stim': ['mover', 'repetitivo', 'balanceo', 'autoestimulación', 'movimiento', 'rocking'],
            'recarga_social': ['cansancio social', 'necesito estar sola', 'sobrecarga personas', 'introversión'],
            'alexitimia': ['no sé cómo me siento', 'confusión emocional', 'nombrar emoción', 'identificar'],
            'monotropismo': ['un solo foco', 'atención túnel', 'dificultad cambiar', 'transición difícil'],
            'rigidez_cognitiva': ['necesito estructura', 'cambios difíciles', 'rutina', 'rigidez'],
            'shutdown': ['apagón', 'no puedo responder', 'bloqueada', 'sobrecargada total'],
            'hipersensibilidad': ['muy sensible', 'empatía', 'percibo todo', 'muy perceptiva']
        }
        
        detected_patterns = []
        for pattern, keywords in patterns.items():
            if any(keyword in text.lower() for keyword in keywords) or pattern in nd_markers:
                detected_patterns.append(pattern)
        
        # Calcular intensidad ND
        nd_intensity = len(detected_patterns) / max(1, len(patterns))
        
        # Estrategias adaptativas según patrones detectados
        adaptive_strategies = self._suggest_adaptive_strategies(detected_patterns)
        
        # Identificar patrones de fortaleza ND
        strengths = self._identify_nd_strengths(detected_patterns, input_data)
        
        return {
            'detected_patterns': detected_patterns,
            'nd_intensity': nd_intensity,
            'adaptive_strategies_needed': adaptive_strategies,
            'nd_strengths': strengths
        }
    
    def _map_to_symbols(self, emotional_analysis: Dict, nd_patterns: Dict) -> Dict:
        """Mapea análisis a símbolos terapéuticos con mayor profundidad"""
        symbols = []
        
        # Mapeo emocional a símbolos
        emotion_symbols = {
            'ansiedad': '🌊 (fluir con la incertidumbre)',
            'tristeza': '🌙 (honrar la introspección)',
            'ira': '🔥 (transformar la energía)',
            'alegría': '☀️ (celebrar la luz interior)',
            'miedo': '🛡️ (protección y valentía)',
            'vergüenza': '🌱 (crecer desde la vulnerabilidad)',
            'apatía': '🌪️ (encontrar el centro de la calma)',
            'confusión': '🧭 (orientación interior)',
            'esperanza': '⭐ (guía hacia el futuro)',
            'gratitud': '🌸 (florecer desde la apreciación)'
        }
        
        for emotion in emotional_analysis.get('primary_emotions', []):
            if emotion in emotion_symbols:
                symbols.append(emotion_symbols[emotion])
        
        # Mapeo ND a símbolos
        nd_symbols = {
            'hiperfoco': '🎯 (canalizar la intensidad)',
            'sobrecarga_sensorial': '🧘‍♀️ (crear espacios seguros)',
            'masking': '🎭 (honrar la autenticidad)',
            'stim': '💫 (autorregulación natural)',
            'recarga_social': '🏝️ (santuario personal)',
            'alexitimia': '🗺️ (mapeo emocional)',
            'monotropismo': '🔍 (valor de la profundidad)',
            'rigidez_cognitiva': '🌉 (puentes de transición)',
            'shutdown': '🛌 (recuperación necesaria)',
            'hipersensibilidad': '🌈 (don de la percepción)'
        }
        
        for pattern in nd_patterns.get('detected_patterns', []):
            if pattern in nd_symbols:
                symbols.append(nd_symbols[pattern])
        
        # Símbolos de recursos adicionales basados en necesidades
        resource_symbols = []
        if emotional_analysis.get('emotional_intensity', 0) > 0.7:
            resource_symbols.append('🏺 (contención emocional)')
        if 'shutdown' in nd_patterns.get('detected_patterns', []) or 'sobrecarga_sensorial' in nd_patterns.get('detected_patterns', []):
            resource_symbols.append('🛡️ (protección y límites)')
        
        # Seleccionar arquetipos terapéuticos
        archetype = self._select_primary_archetype(emotional_analysis, nd_patterns)
        
        # Generar activación terapéutica
        activation = self._generate_therapeutic_activation(symbols)
        
        return {
            'active_symbols': symbols,
            'resource_symbols': resource_symbols,
            'primary_archetype': archetype,
            'therapeutic_activation': activation,
            'symbol_narrative': self._generate_symbol_narrative(symbols, archetype)
        }
    
    def _generate_therapeutic_response(self, emotional_analysis: Dict, nd_patterns: Dict, 
                                     symbolic_mapping: Dict, input_data: Dict) -> Dict:
        """Genera respuesta terapéutica personalizada y completa"""
        
        # Componentes base de la respuesta
        response_components = {
            'containment': self._generate_containment_response(emotional_analysis),
            'validation': self._generate_nd_validation(nd_patterns),
            'reframe': self._generate_symbolic_reframe(symbolic_mapping),
            'resource': self._generate_therapeutic_resource(emotional_analysis, nd_patterns)
        }
        
        # Personalización según contexto
        context = input_data.get('context', {})
        if context.get('session_type') == 'crisis':
            response_components['safety_plan'] = self._generate_safety_plan(emotional_analysis, nd_patterns)
        
        # Añadir progresión terapéutica si hay historia previa
        if len(self.session_history) > 2:
            response_components['progression'] = self._generate_progression_insight(input_data)
        
        # Adaptación según fortalezas ND
        if nd_patterns.get('nd_strengths'):
            response_components['strength_affirmation'] = self._generate_strength_affirmation(nd_patterns)
        
        return response_components
    
    # Métodos auxiliares mejorados
    def _assess_emotional_balance(self, emotions: List[str]) -> str:
        """Evalúa balance emocional con mayor precisión"""
        difficult_emotions = ['ansiedad', 'tristeza', 'ira', 'miedo', 'vergüenza', 'apatía']
        positive_emotions = ['alegría', 'esperanza', 'gratitud']
        
        difficult_count = sum(1 for e in emotions if e in difficult_emotions)
        positive_count = sum(1 for e in emotions if e in positive_emotions)
        
        if difficult_count > 2 and positive_count == 0:
            return "desregulado"
        elif difficult_count > 0 and positive_count > 0:
            return "mixto"
        elif difficult_count <= 1 and positive_count == 0:
            return "regulado"
        elif positive_count > 0 and difficult_count == 0:
            return "positivo"
        else:
            return "neutro"
    
    def _derive_emotional_context(self, emotions: List[str], input_data: Dict) -> str:
        """Deriva contexto emocional más profundo"""
        if not emotions:
            return "exploratorio"
        
        # Contextos comunes basados en combinaciones
        if set(['ansiedad', 'miedo']).issubset(set(emotions)):
            return "anticipatorio"
        elif set(['tristeza', 'apatía']).issubset(set(emotions)):
            return "pérdida"
        elif set(['ira', 'frustración']).issubset(set(emotions)):
            return "injusticia"
        elif set(['vergüenza', 'tristeza']).issubset(set(emotions)):
            return "autoestima"
        elif set(['alegría', 'gratitud']).issubset(set(emotions)):
            return "logro"
        else:
            return "procesamiento"
    
    def _suggest_adaptive_strategies(self, patterns: List[str]) -> List[str]:
        """Sugiere estrategias adaptativas específicas para patrones ND"""
        strategies = []
        
        strategy_map = {
            'hiperfoco': ['técnicas de transición suave', 'temporizadores visuales'],
            'sobrecarga_sensorial': ['espacios de descompresión', 'reducción de estímulos'],
            'masking': ['espacios de autenticidad', 'comunidades afirmativas'],
            'stim': ['normalización de estimulación', 'herramientas sensoriales'],
            'recarga_social': ['tiempo de soledad planificado', 'comunicación de límites'],
            'alexitimia': ['mapeo corporal de emociones', 'vocabulario emocional expandido'],
            'monotropismo': ['planificación de transiciones', 'agendas visuales'],
            'rigidez_cognitiva': ['anticipación de cambios', 'rutinas flexibles'],
            'shutdown': ['plan de recuperación', 'señales no verbales'],
            'hipersensibilidad': ['filtros sensoriales', 'espacios de calma']
        }
        
        # Añadir estrategias relevantes
        for pattern in patterns:
            if pattern in strategy_map:
                strategies.extend(strategy_map[pattern])
        
        # Limitar a las 3 más relevantes
        return strategies[:3]
    
    def _identify_nd_strengths(self, patterns: List[str], input_data: Dict) -> List[str]:
        """Identifica fortalezas neurodivergentes basadas en patrones"""
        strengths = []
        
        strength_map = {
            'hiperfoco': ['profundidad de conocimiento', 'persistencia'],
            'masking': ['adaptabilidad social', 'observación detallada'],
            'monotropismo': ['atención al detalle', 'especialización'],
            'hipersensibilidad': ['percepción aumentada', 'empatía profunda'],
            'stim': ['autorregulación intuitiva', 'conexión corporal']
        }
        
        for pattern in patterns:
            if pattern in strength_map:
                strengths.append(random.choice(strength_map[pattern]))
        
        return strengths
    
    def _select_primary_archetype(self, emotional_analysis: Dict, nd_patterns: Dict) -> str:
        """Selecciona arquetipo primario para la sesión basado en necesidades"""
        archetypes = {
            'Sanadora Empática': ['tristeza', 'vergüenza', 'hipersensibilidad'],
            'Guardiana Protectora': ['miedo', 'ansiedad', 'sobrecarga_sensorial', 'shutdown'],
            'Guía Sabia': ['confusión', 'alexitimia', 'rigidez_cognitiva'],
            'Exploradora Valiente': ['apatía', 'masking', 'recarga_social'],
            'Creadora Transformadora': ['ira', 'hiperfoco', 'monotropismo']
        }
        
        # Contar coincidencias
        archetype_scores = {}
        emotions = emotional_analysis.get('primary_emotions', [])
        nd_pats = nd_patterns.get('detected_patterns', [])
        
        for archetype, patterns in archetypes.items():
            score = sum(1 for p in patterns if p in emotions or p in nd_pats)
            archetype_scores[archetype] = score
        
        # Seleccionar el de mayor puntaje
        max_score = max(archetype_scores.values(), default=0)
        candidates = [a for a, s in archetype_scores.items() if s == max_score]
        
        if not candidates:
            return 'Sanadora Empática'  # Valor por defecto
        
        return random.choice(candidates)
    
    def _generate_therapeutic_activation(self, symbols: List[str]) -> str:
        """Genera activación terapéutica basada en símbolos"""
        if not symbols:
            return "Activando recursos internos"
        
        return f"Activando resonancia con: {', '.join(symbols[:2])}"
    
    def _generate_symbol_narrative(self, symbols: List[str], archetype: str) -> str:
        """Genera narrativa simbólica integradora"""
        if not symbols:
            return ""
        
        narratives = {
            'Sanadora Empática': f"La {archetype} te invita a acoger tus emociones como mensajeras.",
            'Guardiana Protectora': f"La {archetype} crea un espacio seguro donde puedes bajar la guardia.",
            'Guía Sabia': f"La {archetype} ilumina el camino para comprenderte mejor.",
            'Exploradora Valiente': f"La {archetype} te anima a reconocer y celebrar tu autenticidad.",
            'Creadora Transformadora': f"La {archetype} canaliza tu energía hacia la transformación."
        }
        
        return narratives.get(archetype, f"La {archetype} te acompaña en este momento.")
    
    def _generate_containment_response(self, emotional_analysis: Dict) -> str:
        """Genera respuesta de contención personalizada"""
        balance = emotional_analysis.get('emotional_balance', 'neutro')
        emotions = emotional_analysis.get('primary_emotions', [])
        
        if balance == 'desregulado':
            return "Te veo en tu intensidad emocional. Estoy aquí, contigo. Respira conmigo."
        elif 'ansiedad' in emotions or 'miedo' in emotions:
            return "Te veo, te escucho, estás acompañada en este momento de incertidumbre."
        elif 'tristeza' in emotions:
            return "Tu tristeza tiene espacio aquí, es bienvenida y respetada."
        elif balance == 'positivo':
            return "Veo tu luz interior brillando en este momento, es hermoso presenciarlo."
        else:
            return "Estoy aquí, en este espacio compartido, acompañándote en tu proceso."
    
    def _generate_nd_validation(self, nd_patterns: Dict) -> str:
        """Genera validación neurodivergente específica"""
        patterns = nd_patterns.get('detected_patterns', [])
        
        if 'masking' in patterns:
            return "Tu forma auténtica de ser es valiosa, sin necesidad de máscaras."
        elif 'sobrecarga_sensorial' in patterns or 'shutdown' in patterns:
            return "Tu sistema nervioso tiene sabiduría propia, está tratando de protegerte."
        elif 'hiperfoco' in patterns or 'monotropismo' in patterns:
            return "Tu intensidad y profundidad de atención son dones únicos."
        else:
            return "Tu forma de procesar el mundo es válida y valiosa."
    
    def _generate_symbolic_reframe(self, symbolic_mapping: Dict) -> str:
        """Genera reframe simbólico con mayor resonancia"""
        narrative = symbolic_mapping.get('symbol_narrative', '')
        activation = symbolic_mapping.get('therapeutic_activation', '')
        
        if narrative and activation:
            return f"Desde lo simbólico: {narrative} {activation}"
        elif activation:
            return f"Desde lo simbólico: {activation}"
        else:
            return "Desde lo simbólico: conectando con tu sabiduría interior."
    
    def _generate_therapeutic_resource(self, emotional_analysis: Dict, nd_patterns: Dict) -> str:
        """Genera recurso terapéutico contextualizado"""
        patterns = nd_patterns.get('detected_patterns', [])
        emotions = emotional_analysis.get('primary_emotions', [])
        
        if 'sobrecarga_sensorial' in patterns:
            return "Recurso: Técnica 5-4-3-2-1 para anclaje sensorial consciente."
        elif 'ansiedad' in emotions or 'miedo' in emotions:
            return "Recurso: Respiración cuadrada (4-4-4-4) con visualización de símbolo de calma."
        elif 'tristeza' in emotions or 'apatía' in emotions:
            return "Recurso: Práctica de autocompasión con mano en el corazón."
        elif 'ira' in emotions:
            return "Recurso: Transformación energética consciente a través del movimiento."
        else:
            return "Recurso: Respiración consciente con anclaje simbólico."
    
    def _generate_safety_plan(self, emotional_analysis: Dict, nd_patterns: Dict) -> str:
        """Genera plan de seguridad para momentos de crisis"""
        return "Plan de seguridad: (1) Anclaje corporal, (2) Contacto con persona de apoyo, (3) Recordatorio: esto pasará."
    
    def _generate_progression_insight(self, input_data: Dict) -> str:
        """Genera insight sobre la progresión terapéutica"""
        return "Observo tu proceso: estás desarrollando mayor consciencia sobre tus patrones emocionales."
    
    def _generate_strength_affirmation(self, nd_patterns: Dict) -> str:
        """Genera afirmación de fortalezas ND"""
        strengths = nd_patterns.get('nd_strengths', [])
        if strengths:
            strength = random.choice(strengths)
            return f"Tu neurodivergencia te da el don de {strength}, una fortaleza única."
        return ""
    
    def _activate_feedback_loops(self, input_data: Dict, response: Dict) -> Dict:
        """Activa loops de retroalimentación para aprendizaje continuo"""
        active_loops = []
        
        # Activar loops relevantes basados en contexto
        if 'ansiedad' in input_data.get('emotion_indicators', []):
            active_loops.append('emotional_regulation')
        
        if any(p in input_data.get('nd_markers', []) for p in ['sobrecarga_sensorial', 'shutdown']):
            active_loops.append('sensory_calibration')
        
        # Añadir loop de integración simbólica siempre
        active_loops.append('symbol_integration')
        
        return {
            'status': 'activated', 
            'loops': active_loops,
            'adaptation_score': 0.75
        }
    
    def _evaluate_therapeutic_trajectory(self, input_data: Dict) -> Dict:
        """Evalúa trayectoria terapéutica basada en historia de sesión"""
        if len(self.session_history) < 2:
            return {'status': 'iniciando', 'phase': 'exploración'}
        
        # Analizar trayectoria basada en patrones recurrentes
        return {
            'status': 'en_progreso',
            'phase': 'procesamiento',
            'recurrent_themes': ['autorregulación', 'identidad'],
            'progress_indicators': ['mayor consciencia', 'expresión emocional']
        }
    
    def _calculate_mentalization_score(self, emotional_analysis: Dict, nd_patterns: Dict) -> float:
        """Calcula score de mentalización con mayor precisión"""
        base_score = 0.5
        
        # Ajustar según balance emocional
        balance_scores = {
            'desregulado': 0.0,
            'regulado': 0.2,
            'mixto': 0.1,
            'positivo': 0.3,
            'neutro': 0.1
        }
        balance = emotional_analysis.get('emotional_balance', 'neutro')
        base_score += balance_scores.get(balance, 0.1)
        
        # Ajustar según intensidad ND
        nd_intensity = nd_patterns.get('nd_intensity', 0)
        if nd_intensity < 0.3:
            base_score += 0.3
        elif nd_intensity < 0.6:
            base_score += 0.1
        
        # Bonificación por fortalezas identificadas
        if nd_patterns.get('nd_strengths'):
            base_score += 0.1
        
        return min(1.0, base_score)
    
    def _default_simbologia(self) -> Dict[str, Any]:
        """Simbología por defecto si no se puede cargar el archivo"""
        return {
            'colores': {
                'azul': 'calma, introspección, profundidad',
                'verde': 'crecimiento, sanación, equilibrio',
                'violeta': 'transformación, espiritualidad, intuición'
            },
            'elementos': {
                'agua': 'fluidez, adaptabilidad, emociones',
                'tierra': 'estabilidad, concreción, recursos',
                'aire': 'comunicación, ideas, perspectiva',
                'fuego': 'energía, pasión, transformación'
            }
        }
    
    def _default_feedback_config(self) -> Dict[str, Any]:
        """Configuración de feedback por defecto"""
        return {
            'loops': {
                'emotional_regulation': {'trigger_threshold': 0.7, 'response_type': 'containment'},
                'nd_support': {'trigger_threshold': 0.5, 'response_type': 'adaptive_strategy'},
                'symbolic_integration': {'trigger_threshold': 0.6, 'response_type': 'symbol_activation'}
            }
        }
    
    def _default_mentalization_config(self) -> Dict[str, Any]:
        """Configuración de mentalización por defecto"""
        return {
            'emotional_weights': {
                'ansiedad': 0.8,
                'tristeza': 0.7,
                'ira': 0.9,
                'alegría': 0.3,
                'miedo': 0.8
            },
            'nd_weights': {
                'hiperfoco': 0.6,
                'sobrecarga_sensorial': 0.8,
                'masking': 0.7,
                'stim': 0.4
            }
        }


# Función principal para usar desde otros módulos
def process_mentalization_advanced(input_data: Dict) -> Dict:
    """
    Función principal para procesar mentalización avanzada
    
    Args:
        input_data: Datos de entrada del usuario
        
    Returns:
        Respuesta mentalizada completa con mayor profundidad
    """
    engine = MentalizationEngineAdvanced()
    return engine.process_emotional_state(input_data)


if __name__ == "__main__":
    # Ejemplo de uso avanzado
    test_input = {
        'text': 'Me siento muy ansiosa y confundida, no puedo parar de pensar en esto. Las luces y el ruido me están afectando mucho.',
        'emotion_indicators': ['ansiedad', 'confusión'],
        'nd_markers': ['hiperfoco', 'sobrecarga_sensorial'],
        'context': {'session_type': 'individual', 'time': 'tarde'}
    }
    
    result = process_mentalization_advanced(test_input)
    print(json.dumps(result, indent=2, ensure_ascii=False))
