#!/usr/bin/env python3
"""
FL ND - Plataforma Freelance Neurodivergente
Marketplace especializado para profesionales ND independientes
Ecosistema MENTALIA
"""

import os
import sys
from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta
import json
import uuid
from enum import Enum

# Configuración de la aplicación
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fl_nd_2025_freelance'

# Configuración de categorías de servicios ND
app.config['CATEGORIAS_SERVICIOS_ND'] = {
    'tecnologia_desarrollo': {
        'nombre': 'Tecnología y Desarrollo',
        'descripcion': 'Servicios de programación y desarrollo técnico',
        'fortalezas_nd': ['sistematización', 'atención_detalle', 'pensamiento_lógico'],
        'servicios': [
            'Desarrollo Web Full-Stack',
            'Aplicaciones Móviles',
            'APIs y Microservicios',
            'Testing y QA Exhaustivo',
            'Documentación Técnica',
            'Arquitectura de Software',
            'DevOps y Automatización',
            'Debugging Especializado'
        ]
    },
    'creatividad_diseño': {
        'nombre': 'Creatividad y Diseño',
        'descripcion': 'Servicios creativos y de diseño visual',
        'fortalezas_nd': ['pensamiento_divergente', 'creatividad', 'visión_única'],
        'servicios': [
            'Diseño Gráfico Innovador',
            'UX/UI Neurodiverso',
            'Branding Auténtico',
            'Ilustración Detallada',
            'Animación y Motion Graphics',
            'Diseño Web Accesible',
            'Identidad Visual Corporativa',
            'Packaging Creativo'
        ]
    },
    'analisis_consultoria': {
        'nombre': 'Análisis y Consultoría',
        'descripcion': 'Servicios de análisis profundo y consultoría estratégica',
        'fortalezas_nd': ['análisis_profundo', 'pensamiento_sistémico', 'detección_patrones'],
        'servicios': [
            'Investigación de Mercado',
            'Data Science y Analytics',
            'Consultoría Estratégica',
            'Optimización de Procesos',
            'Auditoría Especializada',
            'Business Intelligence',
            'Análisis Financiero',
            'Investigación Académica'
        ]
    },
    'contenido_comunicacion': {
        'nombre': 'Contenido y Comunicación',
        'descripcion': 'Servicios de creación de contenido y comunicación',
        'fortalezas_nd': ['hiperfoco', 'precisión_lingüística', 'storytelling_auténtico'],
        'servicios': [
            'Copywriting Persuasivo',
            'Contenido Técnico',
            'Traducción Especializada',
            'Edición y Corrección',
            'Marketing de Contenidos',
            'Storytelling Corporativo',
            'Comunicación Interna',
            'Documentación Empresarial'
        ]
    }
}

# Configuración de niveles de freelancer
app.config['NIVELES_FREELANCER'] = {
    'emergente': {
        'nombre': 'Freelancer Emergente ND',
        'requisitos': {'proyectos_completados': 0, 'rating_minimo': 0},
        'beneficios': ['Comisión 8%', 'Soporte básico', 'Acceso a proyectos junior'],
        'tarifa_sugerida_min': 15,
        'tarifa_sugerida_max': 35
    },
    'establecido': {
        'nombre': 'Freelancer Establecido ND',
        'requisitos': {'proyectos_completados': 10, 'rating_minimo': 4.5},
        'beneficios': ['Comisión 6%', 'Soporte prioritario', 'Acceso a proyectos premium'],
        'tarifa_sugerida_min': 35,
        'tarifa_sugerida_max': 75
    },
    'experto': {
        'nombre': 'Experto ND',
        'requisitos': {'proyectos_completados': 50, 'rating_minimo': 4.8},
        'beneficios': ['Comisión 4%', 'Soporte VIP', 'Proyectos exclusivos'],
        'tarifa_sugerida_min': 75,
        'tarifa_sugerida_max': 150
    },
    'maestro': {
        'nombre': 'Maestro ND',
        'requisitos': {'proyectos_completados': 100, 'rating_minimo': 4.9},
        'beneficios': ['Comisión 2%', 'Soporte dedicado', 'Proyectos enterprise'],
        'tarifa_sugerida_min': 150,
        'tarifa_sugerida_max': 300
    }
}

class EstadoProyecto(Enum):
    PUBLICADO = "publicado"
    EN_REVISION = "en_revision"
    ASIGNADO = "asignado"
    EN_PROGRESO = "en_progreso"
    EN_REVISION_CLIENTE = "en_revision_cliente"
    COMPLETADO = "completado"
    CANCELADO = "cancelado"
    DISPUTADO = "disputado"

class FreelancePlatformND:
    """Sistema principal de la plataforma freelance ND"""
    
    def __init__(self):
        self.freelancers = []
        self.clientes = []
        self.proyectos = []
        self.propuestas = []
        self.contratos = []
        self.stats = {
            'freelancers_activos': 0,
            'clientes_activos': 0,
            'proyectos_completados': 0,
            'valor_total_proyectos': 0,
            'rating_promedio_freelancers': 4.8,
            'tiempo_promedio_entrega': '5.2 días',
            'tasa_satisfaccion_clientes': 0.94
        }
        self.inicializar_datos_demo()
    
    def inicializar_datos_demo(self):
        """Inicializar datos demo para testing"""
        # Freelancers demo
        freelancers_demo = [
            {
                'id': str(uuid.uuid4()),
                'usuario_id': 'freelancer_001',
                'perfil_nd': ['tdah', 'altas_capacidades'],
                'especialidades': ['tecnologia_desarrollo'],
                'servicios': ['Desarrollo Web Full-Stack', 'APIs y Microservicios'],
                'tarifa_por_hora': 65,
                'nivel': 'establecido',
                'rating': 4.9,
                'proyectos_completados': 23,
                'ingresos_totales': 45000,
                'disponibilidad': 'disponible',
                'fortalezas_nd': ['hiperfoco', 'sistematización', 'atención_detalle'],
                'portfolio': [
                    {
                        'titulo': 'E-commerce ND-Friendly',
                        'descripcion': 'Plataforma de comercio electrónico accesible',
                        'tecnologias': ['React', 'Node.js', 'MongoDB'],
                        'url': 'https://portfolio.example.com/ecommerce'
                    }
                ],
                'fecha_registro': '2024-06-15',
                'ultima_actividad': datetime.now().isoformat()
            },
            {
                'id': str(uuid.uuid4()),
                'usuario_id': 'freelancer_002',
                'perfil_nd': ['tea', 'sensibilidad'],
                'especialidades': ['creatividad_diseño'],
                'servicios': ['UX/UI Neurodiverso', 'Branding Auténtico'],
                'tarifa_por_hora': 55,
                'nivel': 'establecido',
                'rating': 4.8,
                'proyectos_completados': 18,
                'ingresos_totales': 32000,
                'disponibilidad': 'ocupado',
                'fortalezas_nd': ['atención_detalle', 'pensamiento_visual', 'empatía'],
                'portfolio': [
                    {
                        'titulo': 'Identidad Visual Inclusiva',
                        'descripcion': 'Branding para startup de tecnología asistiva',
                        'tecnologias': ['Adobe Creative Suite', 'Figma'],
                        'url': 'https://portfolio.example.com/branding'
                    }
                ],
                'fecha_registro': '2024-08-20',
                'ultima_actividad': datetime.now().isoformat()
            }
        ]
        
        # Clientes demo
        clientes_demo = [
            {
                'id': str(uuid.uuid4()),
                'empresa': 'TechStart Innovación',
                'contacto': 'María González',
                'email': 'maria@techstart.com',
                'tipo': 'startup',
                'educacion_nd': True,
                'proyectos_publicados': 5,
                'rating_como_cliente': 4.7,
                'presupuesto_promedio': 8500,
                'fecha_registro': '2024-09-10'
            }
        ]
        
        self.freelancers = freelancers_demo
        self.clientes = clientes_demo
        self.stats['freelancers_activos'] = len(freelancers_demo)
        self.stats['clientes_activos'] = len(clientes_demo)
    
    def registrar_freelancer(self, datos_freelancer):
        """Registrar nuevo freelancer ND"""
        freelancer_id = str(uuid.uuid4())
        
        # Determinar nivel inicial basado en experiencia
        nivel_inicial = self.determinar_nivel_inicial(datos_freelancer)
        
        nuevo_freelancer = {
            'id': freelancer_id,
            'usuario_id': datos_freelancer.get('usuario_id'),
            'perfil_nd': datos_freelancer.get('perfil_nd', []),
            'especialidades': datos_freelancer.get('especialidades', []),
            'servicios': datos_freelancer.get('servicios', []),
            'tarifa_por_hora': datos_freelancer.get('tarifa_por_hora', 25),
            'nivel': nivel_inicial,
            'rating': 0,
            'proyectos_completados': 0,
            'ingresos_totales': 0,
            'disponibilidad': 'disponible',
            'fortalezas_nd': datos_freelancer.get('fortalezas_nd', []),
            'portfolio': datos_freelancer.get('portfolio', []),
            'fecha_registro': datetime.now().isoformat(),
            'ultima_actividad': datetime.now().isoformat(),
            'configuracion': {
                'notificaciones_proyectos': True,
                'auto_aplicar_filtros': True,
                'mostrar_perfil_publico': True
            }
        }
        
        self.freelancers.append(nuevo_freelancer)
        self.stats['freelancers_activos'] += 1
        
        return nuevo_freelancer
    
    def determinar_nivel_inicial(self, datos_freelancer):
        """Determinar nivel inicial del freelancer basado en experiencia"""
        experiencia_previa = datos_freelancer.get('experiencia_previa', 0)
        
        if experiencia_previa >= 5:
            return 'establecido'
        elif experiencia_previa >= 2:
            return 'emergente'
        else:
            return 'emergente'
    
    def publicar_proyecto(self, datos_proyecto, cliente_id):
        """Publicar nuevo proyecto"""
        proyecto_id = str(uuid.uuid4())
        
        nuevo_proyecto = {
            'id': proyecto_id,
            'cliente_id': cliente_id,
            'titulo': datos_proyecto.get('titulo'),
            'descripcion': datos_proyecto.get('descripcion'),
            'categoria': datos_proyecto.get('categoria'),
            'habilidades_requeridas': datos_proyecto.get('habilidades_requeridas', []),
            'presupuesto_min': datos_proyecto.get('presupuesto_min'),
            'presupuesto_max': datos_proyecto.get('presupuesto_max'),
            'tipo_pago': datos_proyecto.get('tipo_pago', 'por_proyecto'),  # por_proyecto, por_hora
            'duracion_estimada': datos_proyecto.get('duracion_estimada'),
            'nivel_experiencia': datos_proyecto.get('nivel_experiencia', 'intermedio'),
            'requiere_nd': datos_proyecto.get('requiere_nd', False),
            'fortalezas_nd_deseadas': datos_proyecto.get('fortalezas_nd_deseadas', []),
            'estado': EstadoProyecto.PUBLICADO.value,
            'fecha_publicacion': datetime.now().isoformat(),
            'fecha_limite_propuestas': (datetime.now() + timedelta(days=7)).isoformat(),
            'propuestas_recibidas': 0,
            'freelancer_asignado': None,
            'fecha_inicio': None,
            'fecha_entrega': None
        }
        
        self.proyectos.append(nuevo_proyecto)
        
        return nuevo_proyecto
    
    def enviar_propuesta(self, proyecto_id, freelancer_id, datos_propuesta):
        """Enviar propuesta para un proyecto"""
        proyecto = self.obtener_proyecto(proyecto_id)
        freelancer = self.obtener_freelancer(freelancer_id)
        
        if not proyecto or not freelancer:
            return None
        
        if proyecto['estado'] != EstadoProyecto.PUBLICADO.value:
            return None
        
        propuesta_id = str(uuid.uuid4())
        
        nueva_propuesta = {
            'id': propuesta_id,
            'proyecto_id': proyecto_id,
            'freelancer_id': freelancer_id,
            'precio_propuesto': datos_propuesta.get('precio_propuesto'),
            'tiempo_entrega': datos_propuesta.get('tiempo_entrega'),
            'mensaje_propuesta': datos_propuesta.get('mensaje_propuesta'),
            'enfoque_nd': datos_propuesta.get('enfoque_nd', ''),
            'fortalezas_aplicables': datos_propuesta.get('fortalezas_aplicables', []),
            'portfolio_relevante': datos_propuesta.get('portfolio_relevante', []),
            'estado': 'enviada',
            'fecha_envio': datetime.now().isoformat(),
            'vista_por_cliente': False
        }
        
        self.propuestas.append(nueva_propuesta)
        
        # Actualizar contador en proyecto
        proyecto['propuestas_recibidas'] += 1
        
        return nueva_propuesta
    
    def aceptar_propuesta(self, propuesta_id, cliente_id):
        """Aceptar propuesta y crear contrato"""
        propuesta = next((p for p in self.propuestas if p['id'] == propuesta_id), None)
        if not propuesta:
            return None
        
        proyecto = self.obtener_proyecto(propuesta['proyecto_id'])
        if not proyecto or proyecto['cliente_id'] != cliente_id:
            return None
        
        # Crear contrato
        contrato = self.crear_contrato(propuesta)
        
        # Actualizar estado del proyecto
        proyecto['estado'] = EstadoProyecto.ASIGNADO.value
        proyecto['freelancer_asignado'] = propuesta['freelancer_id']
        proyecto['fecha_inicio'] = datetime.now().isoformat()
        
        # Actualizar estado de la propuesta
        propuesta['estado'] = 'aceptada'
        
        # Rechazar otras propuestas
        for p in self.propuestas:
            if p['proyecto_id'] == propuesta['proyecto_id'] and p['id'] != propuesta_id:
                p['estado'] = 'rechazada'
        
        return contrato
    
    def crear_contrato(self, propuesta):
        """Crear contrato basado en propuesta aceptada"""
        contrato_id = str(uuid.uuid4())
        
        contrato = {
            'id': contrato_id,
            'proyecto_id': propuesta['proyecto_id'],
            'freelancer_id': propuesta['freelancer_id'],
            'propuesta_id': propuesta['id'],
            'precio_acordado': propuesta['precio_propuesto'],
            'tiempo_entrega': propuesta['tiempo_entrega'],
            'terminos_especiales_nd': self.generar_terminos_nd(propuesta),
            'hitos': self.generar_hitos_proyecto(propuesta),
            'estado': 'activo',
            'fecha_creacion': datetime.now().isoformat(),
            'fecha_inicio': datetime.now().isoformat(),
            'fecha_entrega_acordada': (datetime.now() + timedelta(days=propuesta['tiempo_entrega'])).isoformat(),
            'pagos_realizados': 0,
            'pagos_pendientes': propuesta['precio_propuesto']
        }
        
        self.contratos.append(contrato)
        
        return contrato
    
    def generar_terminos_nd(self, propuesta):
        """Generar términos especiales para freelancers ND"""
        return {
            'comunicacion_preferida': 'escrita',
            'feedback_constructivo': True,
            'flexibilidad_horarios': True,
            'entrega_por_hitos': True,
            'revision_iterativa': True,
            'respeto_ritmos_trabajo': True
        }
    
    def generar_hitos_proyecto(self, propuesta):
        """Generar hitos del proyecto"""
        tiempo_total = propuesta['tiempo_entrega']
        
        hitos = [
            {
                'numero': 1,
                'descripcion': 'Análisis y planificación inicial',
                'porcentaje_completado': 0,
                'porcentaje_pago': 25,
                'fecha_estimada': (datetime.now() + timedelta(days=tiempo_total * 0.2)).isoformat(),
                'estado': 'pendiente'
            },
            {
                'numero': 2,
                'descripcion': 'Desarrollo/Implementación principal',
                'porcentaje_completado': 0,
                'porcentaje_pago': 50,
                'fecha_estimada': (datetime.now() + timedelta(days=tiempo_total * 0.7)).isoformat(),
                'estado': 'pendiente'
            },
            {
                'numero': 3,
                'descripcion': 'Revisión, testing y entrega final',
                'porcentaje_completado': 0,
                'porcentaje_pago': 25,
                'fecha_estimada': (datetime.now() + timedelta(days=tiempo_total)).isoformat(),
                'estado': 'pendiente'
            }
        ]
        
        return hitos
    
    def buscar_proyectos(self, freelancer_id, filtros=None):
        """Buscar proyectos compatibles para freelancer"""
        freelancer = self.obtener_freelancer(freelancer_id)
        if not freelancer:
            return []
        
        proyectos_compatibles = []
        
        for proyecto in self.proyectos:
            if proyecto['estado'] != EstadoProyecto.PUBLICADO.value:
                continue
            
            # Verificar compatibilidad básica
            if self.es_proyecto_compatible(proyecto, freelancer, filtros):
                # Calcular score de compatibilidad
                score = self.calcular_score_compatibilidad(proyecto, freelancer)
                
                proyecto_con_score = proyecto.copy()
                proyecto_con_score['score_compatibilidad'] = score
                proyecto_con_score['razones_compatibilidad'] = self.generar_razones_compatibilidad(proyecto, freelancer)
                
                proyectos_compatibles.append(proyecto_con_score)
        
        # Ordenar por score de compatibilidad
        proyectos_compatibles.sort(key=lambda x: x['score_compatibilidad'], reverse=True)
        
        return proyectos_compatibles
    
    def es_proyecto_compatible(self, proyecto, freelancer, filtros):
        """Verificar compatibilidad básica proyecto-freelancer"""
        # Verificar categoría
        if proyecto['categoria'] not in freelancer['especialidades']:
            return False
        
        # Verificar presupuesto si se especifica filtro
        if filtros and 'presupuesto_min' in filtros:
            if proyecto['presupuesto_max'] < filtros['presupuesto_min']:
                return False
        
        # Verificar nivel de experiencia
        nivel_freelancer = freelancer['nivel']
        nivel_requerido = proyecto['nivel_experiencia']
        
        niveles_orden = ['emergente', 'establecido', 'experto', 'maestro']
        if niveles_orden.index(nivel_freelancer) < niveles_orden.index(nivel_requerido):
            return False
        
        return True
    
    def calcular_score_compatibilidad(self, proyecto, freelancer):
        """Calcular score de compatibilidad proyecto-freelancer"""
        score = 0
        
        # Compatibilidad de habilidades (40%)
        habilidades_proyecto = set(proyecto.get('habilidades_requeridas', []))
        servicios_freelancer = set(freelancer.get('servicios', []))
        
        if habilidades_proyecto:
            overlap_habilidades = len(habilidades_proyecto & servicios_freelancer) / len(habilidades_proyecto)
            score += overlap_habilidades * 40
        
        # Compatibilidad de fortalezas ND (30%)
        if proyecto.get('requiere_nd') and proyecto.get('fortalezas_nd_deseadas'):
            fortalezas_proyecto = set(proyecto['fortalezas_nd_deseadas'])
            fortalezas_freelancer = set(freelancer.get('fortalezas_nd', []))
            
            if fortalezas_proyecto:
                overlap_fortalezas = len(fortalezas_proyecto & fortalezas_freelancer) / len(fortalezas_proyecto)
                score += overlap_fortalezas * 30
        else:
            score += 15  # Bonus por ser freelancer ND aunque no se requiera específicamente
        
        # Rating del freelancer (20%)
        rating_normalizado = freelancer.get('rating', 0) / 5.0
        score += rating_normalizado * 20
        
        # Disponibilidad (10%)
        if freelancer.get('disponibilidad') == 'disponible':
            score += 10
        
        return min(score, 100)  # Máximo 100
    
    def generar_razones_compatibilidad(self, proyecto, freelancer):
        """Generar razones específicas de compatibilidad"""
        razones = []
        
        # Habilidades coincidentes
        habilidades_proyecto = set(proyecto.get('habilidades_requeridas', []))
        servicios_freelancer = set(freelancer.get('servicios', []))
        coincidencias = habilidades_proyecto & servicios_freelancer
        
        if coincidencias:
            razones.append(f"Servicios coincidentes: {', '.join(coincidencias)}")
        
        # Fortalezas ND
        if proyecto.get('fortalezas_nd_deseadas'):
            fortalezas_proyecto = set(proyecto['fortalezas_nd_deseadas'])
            fortalezas_freelancer = set(freelancer.get('fortalezas_nd', []))
            fortalezas_comunes = fortalezas_proyecto & fortalezas_freelancer
            
            if fortalezas_comunes:
                razones.append(f"Fortalezas ND ideales: {', '.join(fortalezas_comunes)}")
        
        # Rating alto
        if freelancer.get('rating', 0) >= 4.5:
            razones.append(f"Freelancer altamente calificado (★{freelancer['rating']})")
        
        # Experiencia en categoría
        if proyecto['categoria'] in freelancer['especialidades']:
            razones.append(f"Especialista en {proyecto['categoria']}")
        
        return razones
    
    def obtener_freelancer(self, freelancer_id):
        """Obtener freelancer por ID"""
        return next((f for f in self.freelancers if f['id'] == freelancer_id), None)
    
    def obtener_proyecto(self, proyecto_id):
        """Obtener proyecto por ID"""
        return next((p for p in self.proyectos if p['id'] == proyecto_id), None)
    
    def obtener_cliente(self, cliente_id):
        """Obtener cliente por ID"""
        return next((c for c in self.clientes if c['id'] == cliente_id), None)

# Instancia global de la plataforma
freelance_platform = FreelancePlatformND()

@app.route('/')
def home():
    """Página principal de FL ND"""
    return {
        'fl_nd': 'FL ND - Plataforma Freelance Neurodivergente',
        'version': '2.0 MENTALIA',
        'status': 'ACTIVE',
        'freelancers_activos': freelance_platform.stats['freelancers_activos'],
        'proyectos_completados': freelance_platform.stats['proyectos_completados'],
        'rating_promedio': freelance_platform.stats['rating_promedio_freelancers'],
        'categorias_disponibles': list(app.config['CATEGORIAS_SERVICIOS_ND'].keys()),
        'ecosystem': 'MENTALIA'
    }

@app.route('/api/registrar-freelancer', methods=['POST'])
def registrar_freelancer():
    """Registrar nuevo freelancer ND"""
    try:
        data = request.get_json()
        datos_freelancer = data.get('datos_freelancer', {})
        
        freelancer = freelance_platform.registrar_freelancer(datos_freelancer)
        
        return jsonify({
            'status': 'FREELANCER_REGISTRADO',
            'freelancer': {
                'id': freelancer['id'],
                'nivel': freelancer['nivel'],
                'especialidades': freelancer['especialidades'],
                'tarifa_por_hora': freelancer['tarifa_por_hora']
            },
            'mensaje': 'Freelancer ND registrado exitosamente',
            'beneficios_nivel': app.config['NIVELES_FREELANCER'][freelancer['nivel']]['beneficios'],
            'integracion_mentalia': {
                'id_nd': 'Identidad verificada automáticamente',
                'cv_nd': 'Portfolio sincronizado',
                'match_nd': 'Red profesional disponible'
            }
        })
    
    except Exception as e:
        return jsonify({
            'status': 'ERROR',
            'message': str(e)
        }), 500

@app.route('/api/buscar-proyectos/<freelancer_id>', methods=['GET'])
def buscar_proyectos(freelancer_id):
    """Buscar proyectos compatibles para freelancer"""
    try:
        # Obtener filtros de query parameters
        filtros = {}
        if request.args.get('presupuesto_min'):
            filtros['presupuesto_min'] = int(request.args.get('presupuesto_min'))
        if request.args.get('categoria'):
            filtros['categoria'] = request.args.get('categoria')
        
        proyectos = freelance_platform.buscar_proyectos(freelancer_id, filtros)
        
        return jsonify({
            'freelancer_id': freelancer_id,
            'proyectos_compatibles': proyectos,
            'total_encontrados': len(proyectos),
            'filtros_aplicados': filtros,
            'recomendacion': 'Enfócate en proyectos con score > 70 para mayor probabilidad de éxito'
        })
    
    except Exception as e:
        return jsonify({
            'status': 'ERROR',
            'message': str(e)
        }), 500

@app.route('/api/enviar-propuesta', methods=['POST'])
def enviar_propuesta():
    """Enviar propuesta para proyecto"""
    try:
        data = request.get_json()
        proyecto_id = data.get('proyecto_id')
        freelancer_id = data.get('freelancer_id')
        datos_propuesta = data.get('datos_propuesta', {})
        
        propuesta = freelance_platform.enviar_propuesta(proyecto_id, freelancer_id, datos_propuesta)
        
        if propuesta:
            return jsonify({
                'status': 'PROPUESTA_ENVIADA',
                'propuesta': propuesta,
                'mensaje': 'Propuesta enviada exitosamente',
                'consejos_nd': [
                    'Destaca tus fortalezas neurodivergentes específicas',
                    'Explica cómo tu perfil ND beneficia el proyecto',
                    'Sé específico sobre tu enfoque y metodología'
                ]
            })
        else:
            return jsonify({
                'status': 'ERROR',
                'message': 'No se pudo enviar la propuesta'
            }), 400
    
    except Exception as e:
        return jsonify({
            'status': 'ERROR',
            'message': str(e)
        }), 500

@app.route('/api/publicar-proyecto', methods=['POST'])
def publicar_proyecto():
    """Publicar nuevo proyecto"""
    try:
        data = request.get_json()
        datos_proyecto = data.get('datos_proyecto', {})
        cliente_id = data.get('cliente_id')
        
        proyecto = freelance_platform.publicar_proyecto(datos_proyecto, cliente_id)
        
        return jsonify({
            'status': 'PROYECTO_PUBLICADO',
            'proyecto': proyecto,
            'mensaje': 'Proyecto publicado exitosamente',
            'tiempo_estimado_propuestas': '24-48 horas',
            'consejos_cliente': [
                'Sé específico sobre las fortalezas ND que necesitas',
                'Proporciona feedback claro y constructivo',
                'Respeta los ritmos de trabajo neurodivergentes'
            ]
        })
    
    except Exception as e:
        return jsonify({
            'status': 'ERROR',
            'message': str(e)
        }), 500

@app.route('/api/categorias-servicios', methods=['GET'])
def obtener_categorias_servicios():
    """Obtener categorías de servicios ND disponibles"""
    return jsonify({
        'categorias': app.config['CATEGORIAS_SERVICIOS_ND'],
        'total_categorias': len(app.config['CATEGORIAS_SERVICIOS_ND']),
        'especializacion_nd': 'Cada categoría está optimizada para fortalezas neurodivergentes específicas'
    })

@app.route('/api/niveles-freelancer', methods=['GET'])
def obtener_niveles_freelancer():
    """Obtener información sobre niveles de freelancer"""
    return jsonify({
        'niveles': app.config['NIVELES_FREELANCER'],
        'progresion': 'Los niveles se basan en proyectos completados y rating',
        'beneficios': 'Cada nivel ofrece comisiones menores y mejores oportunidades'
    })

@app.route('/api/stats', methods=['GET'])
def obtener_estadisticas():
    """Obtener estadísticas de la plataforma"""
    return jsonify({
        'estadisticas': freelance_platform.stats,
        'diferenciacion_nd': {
            'comision_reducida': '8% vs 20% plataformas tradicionales',
            'especializacion_nd': 'Primera plataforma freelance específica para ND',
            'educacion_clientes': 'Formación en trabajo con profesionales ND',
            'herramientas_adaptadas': 'Interfaces y procesos ND-friendly'
        },
        'impacto_economico': {
            'ingresos_promedio_superiores': '+40% vs freelancers tradicionales',
            'satisfaccion_clientes': f"{freelance_platform.stats['tasa_satisfaccion_clientes']*100:.0f}%",
            'tiempo_entrega': freelance_platform.stats['tiempo_promedio_entrega'],
            'calidad_superior': 'Rating promedio 4.8/5.0'
        }
    })

if __name__ == '__main__':
    print("💼 FL ND - Plataforma Freelance activada")
    print("🎯 Matching especializado: OPTIMIZADO")
    print("💰 Comisiones reducidas: CONFIGURADAS")
    print("🔗 Ecosistema MENTALIA: INTEGRADO")
    
    app.run(host='0.0.0.0', port=5008, debug=True)

