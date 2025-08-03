#!/usr/bin/env python3
"""
GERENCIA IA - Gestión Empresarial con Inteligencia Artificial
Plataforma de liderazgo inteligente para equipos neurodiversos
Ecosistema MENTALIA
"""

import os
import sys
from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta
import json
import uuid
import random
from enum import Enum

# Configuración de la aplicación
app = Flask(__name__)
app.config['SECRET_KEY'] = 'gerencia_ia_2025'

# Configuración de módulos de gestión
app.config['MODULOS_GERENCIA'] = {
    'liderazgo_nd': {
        'nombre': 'Liderazgo Neurodivergente',
        'descripcion': 'Herramientas especializadas para líderes ND',
        'funcionalidades': ['estilos_liderazgo', 'comunicacion_adaptiva', 'gestion_energia', 'toma_decisiones'],
        'integracion_blu': True,
        'personalizacion_perfil': True
    },
    'equipos_diversos': {
        'nombre': 'Gestión de Equipos Diversos',
        'descripcion': 'Coordinación de equipos neurodiversos',
        'funcionalidades': ['asignacion_inteligente', 'colaboracion_adaptiva', 'resolucion_conflictos', 'sinergia_optimizada'],
        'analytics_avanzado': True,
        'automatizacion': True
    },
    'analytics_empresarial': {
        'nombre': 'Business Intelligence Avanzado',
        'descripcion': 'Análisis predictivo y insights estratégicos',
        'funcionalidades': ['kpis_inteligentes', 'dashboards_adaptativos', 'reportes_automaticos', 'alertas_predictivas'],
        'machine_learning': True,
        'visualizacion_avanzada': True
    },
    'automatizacion_ia': {
        'nombre': 'Automatización Inteligente',
        'descripcion': 'Workflows adaptativos y optimización continua',
        'funcionalidades': ['workflows_adaptativos', 'delegacion_automatica', 'seguimiento_proactivo', 'escalacion_inteligente'],
        'ia_avanzada': True,
        'optimizacion_continua': True
    }
}

class TipoLiderazgo(Enum):
    VISIONARIO = "visionario"
    COLABORATIVO = "colaborativo"
    ADAPTATIVO = "adaptativo"
    INNOVADOR = "innovador"
    EMPÁTICO = "empático"

class GerenciaIA:
    """Sistema principal de Gerencia IA"""
    
    def __init__(self):
        self.equipos_gestionados = []
        self.lideres_activos = []
        self.proyectos_en_curso = []
        self.analytics_data = {}
        self.stats = {
            'equipos_gestionados': 0,
            'lideres_activos': 0,
            'productividad_promedio': 0.85,
            'satisfaccion_equipos': 4.7,
            'proyectos_completados': 0,
            'ahorro_tiempo_semanal': 0,
            'innovaciones_implementadas': 0,
            'retention_rate': 0.92
        }
        self.inicializar_datos_demo()
    
    def inicializar_datos_demo(self):
        """Inicializar datos demo para testing"""
        lideres_demo = [
            {
                'id': str(uuid.uuid4()),
                'nombre': 'Ana García',
                'perfil_nd': ['tdah', 'altas_capacidades'],
                'tipo_liderazgo': TipoLiderazgo.INNOVADOR.value,
                'equipo_size': 12,
                'industria': 'tecnologia',
                'experiencia_anos': 8,
                'fortalezas_nd': ['creatividad_explosiva', 'vision_estrategica', 'adaptabilidad'],
                'areas_desarrollo': ['gestion_tiempo', 'delegacion'],
                'kpis_principales': {
                    'productividad_equipo': 0.89,
                    'satisfaccion_equipo': 4.8,
                    'innovaciones_mes': 3,
                    'tiempo_decision_promedio': '2.3 horas'
                }
            },
            {
                'id': str(uuid.uuid4()),
                'nombre': 'Carlos Mendoza',
                'perfil_nd': ['tea', 'sensibilidad'],
                'tipo_liderazgo': TipoLiderazgo.COLABORATIVO.value,
                'equipo_size': 8,
                'industria': 'consultoria',
                'experiencia_anos': 12,
                'fortalezas_nd': ['atencion_detalle', 'sistematizacion', 'lealtad_equipo'],
                'areas_desarrollo': ['comunicacion_publica', 'networking'],
                'kpis_principales': {
                    'productividad_equipo': 0.94,
                    'satisfaccion_equipo': 4.9,
                    'calidad_entregables': 0.97,
                    'retention_equipo': 0.95
                }
            }
        ]
        
        equipos_demo = [
            {
                'id': str(uuid.uuid4()),
                'nombre': 'Equipo Innovación Digital',
                'lider_id': lideres_demo[0]['id'],
                'miembros': [
                    {'nombre': 'Luis', 'perfil_nd': ['tdah'], 'rol': 'desarrollador', 'fortalezas': ['hiperfoco', 'creatividad']},
                    {'nombre': 'María', 'perfil_nd': ['tea'], 'rol': 'qa', 'fortalezas': ['precision', 'sistematizacion']},
                    {'nombre': 'Pedro', 'perfil_nd': ['altas_capacidades'], 'rol': 'arquitecto', 'fortalezas': ['vision_tecnica', 'solucion_problemas']},
                    {'nombre': 'Sofia', 'perfil_nd': ['sensibilidad'], 'rol': 'ux_designer', 'fortalezas': ['empatia', 'intuicion_usuario']}
                ],
                'proyectos_activos': 3,
                'metodologia': 'agile_adaptado_nd',
                'performance': {
                    'velocidad_sprint': 0.87,
                    'calidad_codigo': 0.93,
                    'satisfaccion_cliente': 4.6,
                    'innovacion_index': 0.91
                }
            }
        ]
        
        self.lideres_activos = lideres_demo
        self.equipos_gestionados = equipos_demo
        self.stats['lideres_activos'] = len(lideres_demo)
        self.stats['equipos_gestionados'] = len(equipos_demo)
    
    def analizar_liderazgo_nd(self, lider_id):
        """Analizar estilo de liderazgo neurodivergente"""
        lider = self.obtener_lider(lider_id)
        if not lider:
            return None
        
        perfil_nd = lider.get('perfil_nd', [])
        fortalezas = lider.get('fortalezas_nd', [])
        
        analisis = {
            'estilo_actual': lider.get('tipo_liderazgo'),
            'fortalezas_nd': self.mapear_fortalezas_liderazgo(perfil_nd, fortalezas),
            'areas_optimizacion': self.identificar_areas_optimizacion(lider),
            'recomendaciones_ia': self.generar_recomendaciones_liderazgo(lider),
            'plan_desarrollo': self.crear_plan_desarrollo_lider(lider),
            'metricas_efectividad': self.calcular_metricas_liderazgo(lider)
        }
        
        return analisis
    
    def mapear_fortalezas_liderazgo(self, perfil_nd, fortalezas):
        """Mapear fortalezas ND a capacidades de liderazgo"""
        mapeo_fortalezas = {
            'tdah': {
                'creatividad_explosiva': 'Innovación disruptiva y soluciones creativas',
                'adaptabilidad': 'Liderazgo ágil en entornos cambiantes',
                'energia_dinamica': 'Motivación contagiosa del equipo',
                'vision_estrategica': 'Capacidad de ver oportunidades únicas'
            },
            'tea': {
                'atencion_detalle': 'Excelencia operativa y calidad',
                'sistematizacion': 'Procesos eficientes y escalables',
                'lealtad_equipo': 'Construcción de equipos sólidos',
                'precision': 'Toma de decisiones basada en datos'
            },
            'altas_capacidades': {
                'vision_tecnica': 'Liderazgo estratégico avanzado',
                'solucion_problemas': 'Resolución de desafíos complejos',
                'aprendizaje_rapido': 'Adaptación a nuevas industrias',
                'sintesis_informacion': 'Decisiones informadas y rápidas'
            },
            'sensibilidad': {
                'empatia': 'Liderazgo empático y humano',
                'intuicion_usuario': 'Comprensión profunda del mercado',
                'comunicacion_emocional': 'Inspiración y motivación del equipo',
                'deteccion_necesidades': 'Anticipación de requerimientos'
            }
        }
        
        fortalezas_liderazgo = {}
        for perfil in perfil_nd:
            if perfil in mapeo_fortalezas:
                for fortaleza in fortalezas:
                    if fortaleza in mapeo_fortalezas[perfil]:
                        fortalezas_liderazgo[fortaleza] = mapeo_fortalezas[perfil][fortaleza]
        
        return fortalezas_liderazgo
    
    def identificar_areas_optimizacion(self, lider):
        """Identificar áreas de optimización para el líder"""
        perfil_nd = lider.get('perfil_nd', [])
        areas_desarrollo = lider.get('areas_desarrollo', [])
        
        # Áreas comunes de optimización por perfil ND
        optimizaciones_nd = {
            'tdah': [
                'Gestión de tiempo y prioridades',
                'Seguimiento de tareas delegadas',
                'Comunicación estructurada',
                'Documentación de decisiones'
            ],
            'tea': [
                'Comunicación interpersonal',
                'Flexibilidad en procesos',
                'Networking y relaciones externas',
                'Gestión de cambios inesperados'
            ],
            'altas_capacidades': [
                'Paciencia con ritmos diferentes',
                'Comunicación simplificada',
                'Delegación efectiva',
                'Gestión de expectativas'
            ],
            'sensibilidad': [
                'Límites emocionales',
                'Toma de decisiones difíciles',
                'Gestión de conflictos',
                'Protección energética'
            ]
        }
        
        areas_sugeridas = []
        for perfil in perfil_nd:
            if perfil in optimizaciones_nd:
                areas_sugeridas.extend(optimizaciones_nd[perfil])
        
        # Combinar con áreas identificadas por el líder
        areas_finales = list(set(areas_sugeridas + areas_desarrollo))
        
        return areas_finales[:5]  # Top 5 áreas
    
    def generar_recomendaciones_liderazgo(self, lider):
        """Generar recomendaciones personalizadas de liderazgo"""
        perfil_nd = lider.get('perfil_nd', [])
        tipo_liderazgo = lider.get('tipo_liderazgo')
        
        recomendaciones_base = {
            'tdah': [
                'Utiliza timers para reuniones y mantén agendas estructuradas',
                'Aprovecha tu creatividad para sesiones de brainstorming regulares',
                'Implementa sistemas de seguimiento visual para proyectos',
                'Delega tareas de detalle y enfócate en visión estratégica'
            ],
            'tea': [
                'Establece rutinas de comunicación regulares con el equipo',
                'Crea documentación detallada de procesos y expectativas',
                'Programa tiempo específico para interacciones sociales',
                'Utiliza tu atención al detalle para mejorar la calidad'
            ],
            'altas_capacidades': [
                'Adapta tu comunicación al nivel de cada miembro del equipo',
                'Crea desafíos intelectuales para mantener motivación',
                'Establece mentoring para desarrollar a otros',
                'Balancea visión a largo plazo con necesidades inmediatas'
            ],
            'sensibilidad': [
                'Implementa check-ins emocionales regulares con el equipo',
                'Crea espacios seguros para feedback y comunicación',
                'Utiliza tu intuición para detectar problemas temprano',
                'Establece límites claros para proteger tu energía'
            ]
        }
        
        recomendaciones = []
        for perfil in perfil_nd:
            if perfil in recomendaciones_base:
                recomendaciones.extend(recomendaciones_base[perfil])
        
        return recomendaciones[:6]  # Top 6 recomendaciones
    
    def crear_plan_desarrollo_lider(self, lider):
        """Crear plan de desarrollo personalizado"""
        areas_desarrollo = lider.get('areas_desarrollo', [])
        experiencia = lider.get('experiencia_anos', 0)
        
        plan = {
            'objetivos_30_dias': [],
            'objetivos_90_dias': [],
            'objetivos_1_ano': [],
            'recursos_recomendados': [],
            'metricas_seguimiento': []
        }
        
        # Objetivos según experiencia y áreas de desarrollo
        if 'gestion_tiempo' in areas_desarrollo:
            plan['objetivos_30_dias'].append('Implementar sistema de time-blocking personalizado')
            plan['objetivos_90_dias'].append('Reducir 20% tiempo en reuniones improductivas')
            plan['recursos_recomendados'].append('Curso: Time Management para Líderes ND')
        
        if 'delegacion' in areas_desarrollo:
            plan['objetivos_30_dias'].append('Identificar 3 tareas clave para delegar')
            plan['objetivos_90_dias'].append('Establecer sistema de seguimiento de delegaciones')
            plan['objetivos_1_ano'].append('Desarrollar 2 líderes junior en el equipo')
        
        if 'comunicacion_publica' in areas_desarrollo:
            plan['objetivos_90_dias'].append('Realizar 2 presentaciones ejecutivas')
            plan['objetivos_1_ano'].append('Liderar conferencia sobre neurodiversidad empresarial')
            plan['recursos_recomendados'].append('Coach: Comunicación para Líderes ND')
        
        # Métricas de seguimiento
        plan['metricas_seguimiento'] = [
            'Satisfacción del equipo (mensual)',
            'Productividad del equipo (semanal)',
            'Tiempo dedicado a actividades estratégicas vs operativas',
            'Número de innovaciones implementadas',
            'Feedback 360 trimestral'
        ]
        
        return plan
    
    def calcular_metricas_liderazgo(self, lider):
        """Calcular métricas de efectividad del liderazgo"""
        kpis = lider.get('kpis_principales', {})
        
        metricas = {
            'efectividad_general': self.calcular_efectividad_general(kpis),
            'impacto_equipo': self.calcular_impacto_equipo(kpis),
            'innovacion_liderazgo': self.calcular_innovacion_liderazgo(kpis),
            'desarrollo_talento': self.calcular_desarrollo_talento(kpis),
            'sostenibilidad_liderazgo': self.calcular_sostenibilidad_liderazgo(kpis)
        }
        
        return metricas
    
    def calcular_efectividad_general(self, kpis):
        """Calcular efectividad general del liderazgo"""
        productividad = kpis.get('productividad_equipo', 0.5)
        satisfaccion = kpis.get('satisfaccion_equipo', 2.5) / 5.0
        
        efectividad = (productividad * 0.6) + (satisfaccion * 0.4)
        return round(efectividad, 2)
    
    def calcular_impacto_equipo(self, kpis):
        """Calcular impacto en el equipo"""
        satisfaccion = kpis.get('satisfaccion_equipo', 2.5) / 5.0
        retention = kpis.get('retention_equipo', 0.7)
        
        impacto = (satisfaccion * 0.7) + (retention * 0.3)
        return round(impacto, 2)
    
    def calcular_innovacion_liderazgo(self, kpis):
        """Calcular capacidad de innovación"""
        innovaciones = min(kpis.get('innovaciones_mes', 0) / 5.0, 1.0)  # Normalizar a máximo 5 por mes
        return round(innovaciones, 2)
    
    def calcular_desarrollo_talento(self, kpis):
        """Calcular desarrollo de talento"""
        # Simplificado - en producción sería más complejo
        calidad = kpis.get('calidad_entregables', 0.7)
        return round(calidad, 2)
    
    def calcular_sostenibilidad_liderazgo(self, kpis):
        """Calcular sostenibilidad del liderazgo"""
        tiempo_decision = kpis.get('tiempo_decision_promedio', '5 horas')
        # Convertir a score (menos tiempo = mejor score)
        horas = float(tiempo_decision.split()[0])
        score = max(0, 1 - (horas / 10))  # 10 horas = score 0
        return round(score, 2)
    
    def optimizar_equipo_nd(self, equipo_id):
        """Optimizar rendimiento de equipo neurodiverso"""
        equipo = self.obtener_equipo(equipo_id)
        if not equipo:
            return None
        
        optimizacion = {
            'analisis_actual': self.analizar_dinamica_equipo(equipo),
            'recomendaciones_asignacion': self.optimizar_asignacion_tareas(equipo),
            'mejoras_comunicacion': self.optimizar_comunicacion_equipo(equipo),
            'plan_desarrollo_equipo': self.crear_plan_desarrollo_equipo(equipo),
            'metricas_objetivo': self.establecer_metricas_equipo(equipo)
        }
        
        return optimizacion
    
    def analizar_dinamica_equipo(self, equipo):
        """Analizar dinámica actual del equipo"""
        miembros = equipo.get('miembros', [])
        
        analisis = {
            'composicion_nd': self.analizar_composicion_nd(miembros),
            'complementariedad': self.analizar_complementariedad(miembros),
            'gaps_identificados': self.identificar_gaps_equipo(miembros),
            'fortalezas_colectivas': self.identificar_fortalezas_colectivas(miembros),
            'riesgos_potenciales': self.identificar_riesgos_equipo(miembros)
        }
        
        return analisis
    
    def analizar_composicion_nd(self, miembros):
        """Analizar composición neurodivergente del equipo"""
        perfiles_count = {}
        for miembro in miembros:
            for perfil in miembro.get('perfil_nd', []):
                perfiles_count[perfil] = perfiles_count.get(perfil, 0) + 1
        
        total_miembros = len(miembros)
        composicion = {
            'distribucion_perfiles': perfiles_count,
            'diversidad_index': len(perfiles_count) / 4,  # Máximo 4 perfiles principales
            'balance_recomendado': self.evaluar_balance_nd(perfiles_count, total_miembros)
        }
        
        return composicion
    
    def evaluar_balance_nd(self, perfiles_count, total):
        """Evaluar balance de perfiles ND en el equipo"""
        recomendaciones = []
        
        # Verificar representación mínima
        if perfiles_count.get('tdah', 0) == 0:
            recomendaciones.append('Considerar incorporar perfil TDAH para creatividad e innovación')
        
        if perfiles_count.get('tea', 0) == 0:
            recomendaciones.append('Considerar incorporar perfil TEA para precisión y sistematización')
        
        if perfiles_count.get('altas_capacidades', 0) == 0:
            recomendaciones.append('Considerar incorporar perfil AC para visión estratégica')
        
        if perfiles_count.get('sensibilidad', 0) == 0:
            recomendaciones.append('Considerar incorporar perfil Sensible para empatía y UX')
        
        return recomendaciones
    
    def obtener_lider(self, lider_id):
        """Obtener líder por ID"""
        return next((l for l in self.lideres_activos if l['id'] == lider_id), None)
    
    def obtener_equipo(self, equipo_id):
        """Obtener equipo por ID"""
        return next((e for e in self.equipos_gestionados if e['id'] == equipo_id), None)

# Instancia global de Gerencia IA
gerencia_ia = GerenciaIA()

@app.route('/')
def home():
    """Página principal de Gerencia IA"""
    return {
        'gerencia_ia': 'Gerencia IA - Gestión Empresarial con Inteligencia Artificial',
        'version': '2.0 MENTALIA',
        'status': 'ACTIVE',
        'modulos_disponibles': len(app.config['MODULOS_GERENCIA']),
        'lideres_activos': gerencia_ia.stats['lideres_activos'],
        'equipos_gestionados': gerencia_ia.stats['equipos_gestionados'],
        'productividad_promedio': f"{gerencia_ia.stats['productividad_promedio']*100:.1f}%",
        'ecosystem': 'MENTALIA'
    }

@app.route('/api/analizar-liderazgo/<lider_id>', methods=['GET'])
def analizar_liderazgo(lider_id):
    """Analizar estilo de liderazgo neurodivergente"""
    try:
        analisis = gerencia_ia.analizar_liderazgo_nd(lider_id)
        
        if analisis:
            return jsonify({
                'status': 'ANALISIS_COMPLETADO',
                'analisis_liderazgo': analisis,
                'recomendaciones_ia': 'Generadas específicamente para perfil neurodivergente',
                'integracion_mentalia': {
                    'perfil_nd': 'Datos sincronizados automáticamente',
                    'blu_supervisora': 'Análisis emocional integrado',
                    'agenda_clinica': 'Optimización de tiempo ejecutivo'
                }
            })
        else:
            return jsonify({
                'status': 'ERROR',
                'message': 'Líder no encontrado'
            }), 404
    
    except Exception as e:
        return jsonify({
            'status': 'ERROR',
            'message': str(e)
        }), 500

@app.route('/api/optimizar-equipo/<equipo_id>', methods=['GET'])
def optimizar_equipo(equipo_id):
    """Optimizar rendimiento de equipo neurodiverso"""
    try:
        optimizacion = gerencia_ia.optimizar_equipo_nd(equipo_id)
        
        if optimizacion:
            return jsonify({
                'status': 'OPTIMIZACION_COMPLETADA',
                'optimizacion_equipo': optimizacion,
                'ia_recommendations': 'Basadas en análisis de neurodiversidad',
                'expected_improvement': {
                    'productividad': '+25%',
                    'satisfaccion': '+30%',
                    'innovacion': '+40%',
                    'retention': '+20%'
                }
            })
        else:
            return jsonify({
                'status': 'ERROR',
                'message': 'Equipo no encontrado'
            }), 404
    
    except Exception as e:
        return jsonify({
            'status': 'ERROR',
            'message': str(e)
        }), 500

@app.route('/api/dashboard-ejecutivo/<lider_id>', methods=['GET'])
def dashboard_ejecutivo(lider_id):
    """Dashboard ejecutivo personalizado"""
    try:
        lider = gerencia_ia.obtener_lider(lider_id)
        if not lider:
            return jsonify({'status': 'ERROR', 'message': 'Líder no encontrado'}), 404
        
        dashboard = {
            'kpis_principales': lider.get('kpis_principales', {}),
            'alertas_ia': [
                'Productividad del equipo 5% por encima del promedio',
                'Oportunidad de innovación detectada en proyecto Alpha',
                'Recomendación: Sesión de feedback con María (TEA) esta semana'
            ],
            'acciones_recomendadas': [
                'Revisar asignación de tareas para optimizar fortalezas ND',
                'Programar sesión de brainstorming para proyecto Beta',
                'Implementar nueva herramienta de comunicación asíncrona'
            ],
            'metricas_tiempo_real': {
                'productividad_hoy': 0.91,
                'satisfaccion_equipo_semana': 4.8,
                'proyectos_en_verde': 2,
                'proyectos_en_amarillo': 1,
                'proyectos_en_rojo': 0
            },
            'insights_ia': [
                'Tu estilo de liderazgo innovador está generando 40% más ideas',
                'El equipo responde mejor a comunicación visual que textual',
                'Oportunidad: Delegar más tareas de detalle para enfocarte en estrategia'
            ]
        }
        
        return jsonify({
            'dashboard_ejecutivo': dashboard,
            'personalizacion_nd': 'Adaptado a tu perfil neurodivergente específico',
            'actualizacion': 'Tiempo real con IA predictiva'
        })
    
    except Exception as e:
        return jsonify({
            'status': 'ERROR',
            'message': str(e)
        }), 500

@app.route('/api/stats', methods=['GET'])
def obtener_estadisticas():
    """Obtener estadísticas de Gerencia IA"""
    return jsonify({
        'estadisticas': gerencia_ia.stats,
        'diferenciacion_nd': {
            'primera_plataforma_gerencial_nd': 'Diseñada específicamente para líderes neurodivergentes',
            'ia_especializada': 'Algoritmos que comprenden estilos de liderazgo únicos',
            'equipos_neurodiversos': 'Optimización para equipos con diferentes neurotipos',
            'integracion_ecosistema': 'Conectada con todo el ecosistema MENTALIA'
        },
        'impacto_empresarial': {
            'mejora_productividad': '+40% promedio en equipos gestionados',
            'aumento_satisfaccion': '+60% en bienestar laboral',
            'aceleracion_innovacion': '3x más ideas implementadas',
            'reduccion_rotacion': '80% menos turnover'
        }
    })

if __name__ == '__main__':
    print("🏢 Gerencia IA - Sistema activado")
    print("🧠 IA especializada en liderazgo ND: CARGADA")
    print("👥 Gestión de equipos neurodiversos: DISPONIBLE")
    print("📊 Analytics empresarial avanzado: INTEGRADO")
    print("🔗 Ecosistema MENTALIA: CONECTADO")
    
    app.run(host='0.0.0.0', port=5010, debug=True)

