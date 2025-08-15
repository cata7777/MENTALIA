"""
MENTALIA - Motor de Mentalización Dimensional
Procesa estados emocionales, patrones ND y respuestas simbólicas

Creado por: Catalina Rojo Lema
Ecosistema: MENTALIA
Versión: 2.0
"""

import json
import yaml
from typing import Dict, List, Any, Optional
from datetime import datetime
import re

class MentalizationEngine:
    """
    Motor central de mentalización que procesa:
    - Estados emocionales
    - Patrones neurodivergentes  
    - Símbolos y arquetipos
    - Respuestas terapéuticas contextualizadas
    """
    
    def __init__(self):
        self.simbologia = self._load_simbologia()
        self.feedback_loops = self._load_feedback_config()
        self.config = self._load_mentalization_config()
        
    def _load_simbologia(self) -> Dict:
        """Carga tabla maestra de símbolos"""
        try:
            with open('/workspaces/MENTALIA/MENTALIA_CORE/SIMBOLOGIA/SIMBOLOGIA_GLOBAL.yaml', 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return self._default_simbologia()
    
    def _load_feedback_config(self) -> Dict:
        """Carga configuración de loops de retroalimentación"""
        try:
            with open('/workspaces/MENTALIA/MENTALIA_CORE/LABS/transformer/feedback_loops.yaml', 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return self._default_feedback_config()
    
    def _load_mentalization_config(self) -> Dict:
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
                'context': Dict
            }
            
        Returns:
            Dict con respuesta mentalizada, símbolos y orientaciones
        """
        
        # 1. Análisis emocional
        emotional_analysis = self._analyze_emotional_content(input_data)
        
        # 2. Detección de patrones ND
        nd_patterns = self._detect_nd_patterns(input_data)
        
        # 3. Mapeo simbólico
        symbolic_mapping = self._map_to_symbols(emotional_analysis, nd_patterns)
        
        # 4. Generación de respuesta terapéutica
        therapeutic_response = self._generate_therapeutic_response(
            emotional_analysis, nd_patterns, symbolic_mapping
        )
        
        # 5. Activación de feedback loops
        feedback_activation = self._activate_feedback_loops(input_data, therapeutic_response)
        
        return {
            'timestamp': datetime.now().isoformat(),
            'emotional_analysis': emotional_analysis,
            'nd_patterns': nd_patterns,
            'symbolic_mapping': symbolic_mapping,
            'therapeutic_response': therapeutic_response,
            'feedback_loops': feedback_activation,
            'mentalization_score': self._calculate_mentalization_score(emotional_analysis, nd_patterns)
        }
    
    def _analyze_emotional_content(self, input_data: Dict) -> Dict:
        """Analiza contenido emocional del input"""
        text = input_data.get('text', '')
        
        # Patrones emocionales básicos
        emotional_patterns = {
            'ansiedad': ['ansiosa', 'nerviosa', 'preocup', 'estrés', 'angustia'],
            'tristeza': ['triste', 'deprim', 'melancolía', 'lloro', 'dolor'],
            'ira': ['rabia', 'enojo', 'frustración', 'molesta', 'ira'],
            'alegría': ['feliz', 'contenta', 'alegría', 'emoción', 'satisf'],
            'miedo': ['miedo', 'terror', 'pánico', 'fobia', 'temor']
        }
        
        detected_emotions = []
        for emotion, keywords in emotional_patterns.items():
            if any(keyword in text.lower() for keyword in keywords):
                detected_emotions.append(emotion)
        
        return {
            'primary_emotions': detected_emotions[:2],  # Las 2 principales
            'emotional_intensity': self._calculate_emotional_intensity(text),
            'emotional_balance': self._assess_emotional_balance(detected_emotions)
        }
    
    def _detect_nd_patterns(self, input_data: Dict) -> Dict:
        """Detecta patrones neurodivergentes"""
        text = input_data.get('text', '')
        nd_markers = input_data.get('nd_markers', [])
        
        patterns = {
            'hiperfoco': ['obsesion', 'no puedo parar', 'horas sin parar', 'absorta'],
            'sobrecarga_sensorial': ['ruido', 'demasiado', 'abrumada', 'sensorial'],
            'masking': ['fingir', 'actuar', 'máscara', 'pretender'],
            'stim': ['mover', 'repetitivo', 'balanceo', 'autoestimulación']
        }
        
        detected_patterns = []
        for pattern, keywords in patterns.items():
            if any(keyword in text.lower() for keyword in keywords):
                detected_patterns.append(pattern)
        
        return {
            'detected_patterns': detected_patterns,
            'nd_intensity': len(detected_patterns) / len(patterns),
            'adaptive_strategies_needed': self._suggest_adaptive_strategies(detected_patterns)
        }
    
    def _map_to_symbols(self, emotional_analysis: Dict, nd_patterns: Dict) -> Dict:
        """Mapea análisis a símbolos terapéuticos"""
        symbols = []
        
        # Mapeo emocional a símbolos
        emotion_symbols = {
            'ansiedad': '🌊 (fluir con la incertidumbre)',
            'tristeza': '🌙 (honrar la introspección)',
            'ira': '🔥 (transformar la energía)',
            'alegría': '☀️ (celebrar la luz interior)',
            'miedo': '🛡️ (protección y valentía)'
        }
        
        for emotion in emotional_analysis.get('primary_emotions', []):
            if emotion in emotion_symbols:
                symbols.append(emotion_symbols[emotion])
        
        # Mapeo ND a símbolos
        nd_symbols = {
            'hiperfoco': '🎯 (canalizar la intensidad)',
            'sobrecarga_sensorial': '🧘‍♀️ (crear espacios seguros)',
            'masking': '🎭 (honrar la autenticidad)',
            'stim': '💫 (autorregulación natural)'
        }
        
        for pattern in nd_patterns.get('detected_patterns', []):
            if pattern in nd_symbols:
                symbols.append(nd_symbols[pattern])
        
        return {
            'active_symbols': symbols,
            'primary_archetype': self._select_primary_archetype(emotional_analysis, nd_patterns),
            'therapeutic_activation': self._generate_therapeutic_activation(symbols)
        }
    
    def _generate_therapeutic_response(self, emotional_analysis: Dict, nd_patterns: Dict, symbolic_mapping: Dict) -> Dict:
        """Genera respuesta terapéutica personalizada"""
        
        response_components = {
            'containment': self._generate_containment_response(emotional_analysis),
            'validation': self._generate_nd_validation(nd_patterns),
            'reframe': self._generate_symbolic_reframe(symbolic_mapping),
            'resource': self._generate_therapeutic_resource(emotional_analysis, nd_patterns)
        }
        
        return response_components
    
    def _default_simbologia(self) -> Dict:
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
    
    def _default_feedback_config(self) -> Dict:
        """Configuración de feedback por defecto"""
        return {
            'loops': {
                'emotional_regulation': {'trigger_threshold': 0.7, 'response_type': 'containment'},
                'nd_support': {'trigger_threshold': 0.5, 'response_type': 'adaptive_strategy'},
                'symbolic_integration': {'trigger_threshold': 0.6, 'response_type': 'symbol_activation'}
            }
        }
    
    def _default_mentalization_config(self) -> Dict:
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
    
    # Métodos auxiliares (implementación básica)
    def _calculate_emotional_intensity(self, text: str) -> float:
        """Calcula intensidad emocional del texto"""
        intensity_markers = ['muy', 'mucho', 'demasiado', 'extremo', 'intenso']
        return min(1.0, sum(1 for marker in intensity_markers if marker in text.lower()) * 0.2)
    
    def _assess_emotional_balance(self, emotions: List[str]) -> str:
        """Evalúa balance emocional"""
        if len(emotions) > 2:
            return 'desregulado'
        elif len(emotions) == 0:
            return 'neutro'
        else:
            return 'regulado'
    
    def _suggest_adaptive_strategies(self, patterns: List[str]) -> List[str]:
        """Sugiere estrategias adaptativas para patrones ND"""
        strategies = []
        if 'hiperfoco' in patterns:
            strategies.append('técnicas de transición')
        if 'sobrecarga_sensorial' in patterns:
            strategies.append('espacios de descompresión')
        return strategies
    
    def _select_primary_archetype(self, emotional_analysis: Dict, nd_patterns: Dict) -> str:
        """Selecciona arquetipo primario para la sesión"""
        return 'Sanadora Empática'  # Simplificado por ahora
    
    def _generate_therapeutic_activation(self, symbols: List[str]) -> str:
        """Genera activación terapéutica basada en símbolos"""
        return f"Activando resonancia con: {', '.join(symbols)}"
    
    def _generate_containment_response(self, emotional_analysis: Dict) -> str:
        """Genera respuesta de contención"""
        return "Te veo, te escucho, estás acompañada en este momento."
    
    def _generate_nd_validation(self, nd_patterns: Dict) -> str:
        """Genera validación neurodivergente"""
        return "Tu forma de procesar el mundo es válida y valiosa."
    
    def _generate_symbolic_reframe(self, symbolic_mapping: Dict) -> str:
        """Genera reframe simbólico"""
        return f"Desde lo simbólico: {symbolic_mapping.get('therapeutic_activation', '')}"
    
    def _generate_therapeutic_resource(self, emotional_analysis: Dict, nd_patterns: Dict) -> str:
        """Genera recurso terapéutico"""
        return "Recurso: Respiración consciente con anclaje simbólico."
    
    def _activate_feedback_loops(self, input_data: Dict, response: Dict) -> Dict:
        """Activa loops de retroalimentación"""
        return {'status': 'activated', 'loops': ['emotional_regulation']}
    
    def _calculate_mentalization_score(self, emotional_analysis: Dict, nd_patterns: Dict) -> float:
        """Calcula score de mentalización"""
        base_score = 0.5
        if emotional_analysis.get('emotional_balance') == 'regulado':
            base_score += 0.2
        if nd_patterns.get('nd_intensity', 0) < 0.5:
            base_score += 0.2
        return min(1.0, base_score)


# Función principal para usar desde otros módulos
def process_mentalization(input_data: Dict) -> Dict:
    """
    Función principal para procesar mentalización
    
    Args:
        input_data: Datos de entrada del usuario
        
    Returns:
        Respuesta mentalizada completa
    """
    engine = MentalizationEngine()
    return engine.process_emotional_state(input_data)


if __name__ == "__main__":
    # Ejemplo de uso
    test_input = {
        'text': 'Me siento muy ansiosa, no puedo parar de pensar en esto',
        'emotion_indicators': ['ansiedad', 'rumiación'],
        'nd_markers': ['hiperfoco'],
        'context': {'session_type': 'individual', 'time': 'tarde'}
    }
    
    result = process_mentalization(test_input)
    print(json.dumps(result, indent=2, ensure_ascii=False))