"""
Modelo del Despacho Digital Integral
Sistema unificado que integra todas las IAs especializadas (Legal, Contable, etc.)
"""

from datetime import datetime
from src.models.user import db
from src.models.ia_legal import IALegalCertificada, ConsultaLegalRealizada
from src.models.ia_contadora import IAContadoraCertificada, AuditoriaAutomatizada
import json
import hashlib
from enum import Enum
from typing import Dict, List, Optional, Union


class TipoServicio(Enum):
    """Tipos de servicios disponibles en el despacho"""
    LEGAL_GENERAL = "legal_general"
    DEFENSA_NINEZ_MUJERES = "defensa_ninez_mujeres"
    LEY_KARIM_ISAPRES = "ley_karim_isapres"
    LEY_QUIEBRAS = "ley_quiebras"
    CONTABLE_GENERAL = "contable_general"
    AUDITORIA_FINANCIERA = "auditoria_financiera"
    COMPLIANCE_SII = "compliance_sii"
    CONSULTORIA_INTEGRAL = "consultoria_integral"


class DespachoDigitalIntegral(db.Model):
    """
    Modelo principal del Despacho Digital Integral
    Coordina todas las IAs especializadas
    """
    __tablename__ = 'despacho_digital_integral'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_despacho = db.Column(db.String(200), nullable=False, default="DESPACHO DIGITAL INTEGRAL")
    rut_despacho = db.Column(db.String(12), unique=True, nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    servicios_activos = db.Column(db.Text, nullable=False)  # JSON lista de servicios
    ias_disponibles = db.Column(db.Text, nullable=False)  # JSON de IAs activas
    estado_operativo = db.Column(db.String(50), default="ACTIVO")
    fecha_constitucion = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relaciones
    clientes = db.relationship('ClienteDespacho', backref='despacho', lazy=True)
    casos_activos = db.relationship('CasoIntegral', backref='despacho', lazy=True)
    
    def __init__(self, rut_despacho=None, nombre=None):
        if rut_despacho is None:
            rut_despacho = f"77.{datetime.now().strftime('%Y%m%d')}.{hash(str(datetime.now())) % 1000:03d}-K"
        
        self.rut_despacho = rut_despacho
        self.nombre_despacho = nombre or "DESPACHO DIGITAL INTEGRAL"
        self.direccion = "Av. Providencia 1234, Santiago, Chile"
        self.telefono = "+56 2 2345 6789"
        self.email = "contacto@despachodigital.cl"
        
        # Servicios disponibles por defecto
        servicios_default = [
            TipoServicio.LEGAL_GENERAL.value,
            TipoServicio.DEFENSA_NINEZ_MUJERES.value,
            TipoServicio.LEY_KARIM_ISAPRES.value,
            TipoServicio.LEY_QUIEBRAS.value,
            TipoServicio.CONTABLE_GENERAL.value,
            TipoServicio.AUDITORIA_FINANCIERA.value,
            TipoServicio.COMPLIANCE_SII.value,
            TipoServicio.CONSULTORIA_INTEGRAL.value
        ]
        
        self.servicios_activos = json.dumps(servicios_default)
        
        # IAs disponibles
        ias_default = {
            "ia_legal_general": {"activa": True, "especialidad": "Derecho General"},
            "ia_defensa_ninez": {"activa": True, "especialidad": "Defensa Niñez y Mujeres"},
            "ia_ley_karim": {"activa": True, "especialidad": "Ley Karim e ISAPRES"},
            "ia_quiebras": {"activa": True, "especialidad": "Ley de Quiebras"},
            "ia_contadora": {"activa": True, "especialidad": "Contabilidad General"},
            "ia_auditora": {"activa": True, "especialidad": "Auditoría Financiera"},
            "ia_coordinadora": {"activa": True, "especialidad": "Coordinación Integral"}
        }
        
        self.ias_disponibles = json.dumps(ias_default)
    
    def get_servicios_activos(self) -> List[str]:
        """Retorna lista de servicios activos"""
        return json.loads(self.servicios_activos)
    
    def get_ias_disponibles(self) -> Dict:
        """Retorna diccionario de IAs disponibles"""
        return json.loads(self.ias_disponibles)
    
    def procesar_consulta_integral(self, consulta: str, cliente_id: int, 
                                 tipo_servicio_solicitado: str = None) -> Dict:
        """
        Procesa una consulta integral determinando qué IA especializada debe responder
        """
        # Determinar tipo de servicio si no se especifica
        if not tipo_servicio_solicitado:
            tipo_servicio_solicitado = self._determinar_tipo_servicio(consulta)
        
        # Obtener o crear cliente
        cliente = ClienteDespacho.query.get(cliente_id)
        if not cliente:
            raise ValueError(f"Cliente {cliente_id} no encontrado")
        
        # Crear caso integral
        caso = CasoIntegral(
            despacho_id=self.id,
            cliente_id=cliente_id,
            tipo_servicio=tipo_servicio_solicitado,
            consulta_original=consulta,
            estado="EN_PROCESO"
        )
        
        db.session.add(caso)
        db.session.flush()  # Para obtener el ID
        
        # Procesar según tipo de servicio
        resultado = self._procesar_por_tipo_servicio(
            consulta, tipo_servicio_solicitado, caso.id, cliente
        )
        
        # Actualizar caso con resultado
        caso.respuesta_generada = resultado.get('respuesta', '')
        caso.ia_utilizada = resultado.get('ia_utilizada', '')
        caso.estado = "COMPLETADO"
        
        db.session.commit()
        
        return {
            'caso_id': caso.id,
            'tipo_servicio': tipo_servicio_solicitado,
            'ia_utilizada': resultado.get('ia_utilizada'),
            'respuesta': resultado.get('respuesta'),
            'recomendaciones': resultado.get('recomendaciones', []),
            'servicios_adicionales': self._sugerir_servicios_adicionales(tipo_servicio_solicitado),
            'costo_estimado': self._calcular_costo_servicio(tipo_servicio_solicitado)
        }
    
    def _determinar_tipo_servicio(self, consulta: str) -> str:
        """
        Determina automáticamente el tipo de servicio basado en la consulta
        """
        consulta_lower = consulta.lower()
        
        # Palabras clave por tipo de servicio
        keywords_servicios = {
            TipoServicio.DEFENSA_NINEZ_MUJERES.value: [
                'violencia', 'mujer', 'niño', 'niña', 'menor', 'abuso', 'maltrato',
                'violencia intrafamiliar', 'pensión alimenticia', 'custodia', 'visitas'
            ],
            TipoServicio.LEY_KARIM_ISAPRES.value: [
                'isapre', 'fonasa', 'salud', 'ley karim', 'preexistencia', 'cobertura',
                'plan de salud', 'bonificación', 'reembolso', 'prestación médica'
            ],
            TipoServicio.LEY_QUIEBRAS.value: [
                'quiebra', 'insolvencia', 'reorganización', 'liquidación', 'deudas',
                'acreedor', 'síndico', 'convenio', 'cesación de pagos'
            ],
            TipoServicio.CONTABLE_GENERAL.value: [
                'contabilidad', 'balance', 'estado financiero', 'impuesto', 'declaración',
                'facturación', 'boleta', 'libro', 'registro contable'
            ],
            TipoServicio.AUDITORIA_FINANCIERA.value: [
                'auditoría', 'revisión', 'dictamen', 'control interno', 'riesgo',
                'cumplimiento', 'verificación', 'análisis financiero'
            ]
        }
        
        # Calcular scores
        scores = {}
        for tipo_servicio, keywords in keywords_servicios.items():
            score = sum(1 for keyword in keywords if keyword in consulta_lower)
            if score > 0:
                scores[tipo_servicio] = score
        
        if scores:
            return max(scores, key=scores.get)
        else:
            return TipoServicio.LEGAL_GENERAL.value  # Default
    
    def _procesar_por_tipo_servicio(self, consulta: str, tipo_servicio: str, 
                                   caso_id: int, cliente: 'ClienteDespacho') -> Dict:
        """
        Procesa la consulta usando la IA especializada correspondiente
        """
        if tipo_servicio == TipoServicio.LEGAL_GENERAL.value:
            return self._procesar_legal_general(consulta, cliente)
        
        elif tipo_servicio == TipoServicio.DEFENSA_NINEZ_MUJERES.value:
            return self._procesar_defensa_ninez_mujeres(consulta, cliente)
        
        elif tipo_servicio == TipoServicio.LEY_KARIM_ISAPRES.value:
            return self._procesar_ley_karim_isapres(consulta, cliente)
        
        elif tipo_servicio == TipoServicio.LEY_QUIEBRAS.value:
            return self._procesar_ley_quiebras(consulta, cliente)
        
        elif tipo_servicio in [TipoServicio.CONTABLE_GENERAL.value, 
                               TipoServicio.AUDITORIA_FINANCIERA.value]:
            return self._procesar_contable_auditoria(consulta, tipo_servicio, cliente)
        
        else:
            return self._procesar_consultoria_integral(consulta, cliente)
    
    def _procesar_legal_general(self, consulta: str, cliente: 'ClienteDespacho') -> Dict:
        """Procesa consulta legal general usando LEXCODE"""
        # Buscar o crear IA Legal
        ia_legal = IALegalCertificada.query.first()
        if not ia_legal:
            ia_legal = IALegalCertificada()
            db.session.add(ia_legal)
            db.session.commit()
        
        # Realizar consulta legal
        resultado = ia_legal.consulta_legal(
            consulta=consulta,
            modo="estrategico",  # Modo estratégico por defecto para clientes
            contexto_adicional=f"Cliente: {cliente.nombre_completo}, RUT: {cliente.rut}"
        )
        
        return {
            'ia_utilizada': 'IA Legal General (LEXCODE)',
            'respuesta': resultado['respuesta'],
            'bloque_juridico': resultado['bloque_juridico'],
            'recomendaciones': [
                'Revisar documentación relacionada',
                'Considerar asesoría presencial si es necesario',
                'Evaluar costos y beneficios de acciones legales'
            ]
        }
    
    def _procesar_defensa_ninez_mujeres(self, consulta: str, cliente: 'ClienteDespacho') -> Dict:
        """Procesa consulta especializada en defensa de niñez y mujeres"""
        # IA especializada en defensa de niñez y mujeres
        contexto_especializado = """
        Especialización en:
        - Violencia intrafamiliar y de género
        - Derechos del niño y adolescente
        - Pensiones alimenticias y cuidado personal
        - Medidas de protección
        - Procedimientos especiales de familia
        """
        
        # Usar IA Legal con contexto especializado
        ia_legal = IALegalCertificada.query.first()
        if not ia_legal:
            ia_legal = IALegalCertificada()
            db.session.add(ia_legal)
            db.session.commit()
        
        resultado = ia_legal.consulta_legal(
            consulta=consulta,
            modo="estrategico",
            contexto_adicional=f"{contexto_especializado}\nCliente: {cliente.nombre_completo}"
        )
        
        return {
            'ia_utilizada': 'IA Defensa Niñez y Mujeres',
            'respuesta': resultado['respuesta'],
            'recomendaciones': [
                'Evaluar medidas de protección urgentes',
                'Documentar evidencia de violencia si aplica',
                'Considerar apoyo psicológico especializado',
                'Revisar derechos de menores involucrados'
            ]
        }
    
    def _procesar_ley_karim_isapres(self, consulta: str, cliente: 'ClienteDespacho') -> Dict:
        """Procesa consulta especializada en Ley Karim e ISAPRES"""
        contexto_especializado = """
        Especialización en:
        - Ley Karim (Ley 21.309) sobre preexistencias
        - Conflictos con ISAPRES y FONASA
        - Cobertura de prestaciones médicas
        - Reembolsos y bonificaciones
        - Procedimientos ante Superintendencia de Salud
        """
        
        ia_legal = IALegalCertificada.query.first()
        if not ia_legal:
            ia_legal = IALegalCertificada()
            db.session.add(ia_legal)
            db.session.commit()
        
        resultado = ia_legal.consulta_legal(
            consulta=consulta,
            modo="estrategico",
            contexto_adicional=f"{contexto_especializado}\nCliente: {cliente.nombre_completo}"
        )
        
        return {
            'ia_utilizada': 'IA Ley Karim e ISAPRES',
            'respuesta': resultado['respuesta'],
            'recomendaciones': [
                'Revisar contrato de salud vigente',
                'Documentar historial médico relevante',
                'Evaluar reclamo ante Superintendencia',
                'Calcular perjuicios económicos'
            ]
        }
    
    def _procesar_ley_quiebras(self, consulta: str, cliente: 'ClienteDespacho') -> Dict:
        """Procesa consulta especializada en Ley de Quiebras"""
        contexto_especializado = """
        Especialización en:
        - Ley de Reorganización y Liquidación (Ley 20.720)
        - Procedimientos concursales
        - Reorganización empresarial
        - Liquidación de activos
        - Derechos de acreedores
        """
        
        ia_legal = IALegalCertificada.query.first()
        if not ia_legal:
            ia_legal = IALegalCertificada()
            db.session.add(ia_legal)
            db.session.commit()
        
        resultado = ia_legal.consulta_legal(
            consulta=consulta,
            modo="estrategico",
            contexto_adicional=f"{contexto_especializado}\nCliente: {cliente.nombre_completo}"
        )
        
        return {
            'ia_utilizada': 'IA Ley de Quiebras',
            'respuesta': resultado['respuesta'],
            'recomendaciones': [
                'Evaluar viabilidad de reorganización',
                'Analizar masa de acreedores',
                'Revisar activos disponibles',
                'Considerar alternativas extrajudiciales'
            ]
        }
    
    def _procesar_contable_auditoria(self, consulta: str, tipo_servicio: str, 
                                   cliente: 'ClienteDespacho') -> Dict:
        """Procesa consulta contable o de auditoría"""
        # Buscar o crear IA Contadora
        ia_contadora = IAContadoraCertificada.query.first()
        if not ia_contadora:
            ia_contadora = IAContadoraCertificada()
            db.session.add(ia_contadora)
            db.session.commit()
        
        if tipo_servicio == TipoServicio.AUDITORIA_FINANCIERA.value:
            # Simular datos financieros para auditoría
            estados_financieros = {
                'activos': {'efectivo': 100000, 'cuentas_por_cobrar': 50000},
                'pasivos': {'cuentas_por_pagar': 30000, 'prestamos': 20000},
                'patrimonio': {'capital': 100000}
            }
            
            validaciones = ia_contadora.validar_estados_financieros(estados_financieros)
            dictamen = ia_contadora.generar_dictamen_auditoria(estados_financieros, validaciones)
            
            return {
                'ia_utilizada': 'IA Contadora Certificada (Auditoría)',
                'respuesta': f"Auditoría realizada. Dictamen: {dictamen['opinion']}",
                'validaciones': validaciones,
                'dictamen': dictamen,
                'recomendaciones': dictamen.get('recomendaciones', [])
            }
        
        else:  # Contabilidad general
            return {
                'ia_utilizada': 'IA Contadora Certificada',
                'respuesta': f"Consulta contable procesada: {consulta}",
                'recomendaciones': [
                    'Mantener registros contables actualizados',
                    'Realizar conciliaciones mensuales',
                    'Preparar declaraciones tributarias oportunamente'
                ]
            }
    
    def _procesar_consultoria_integral(self, consulta: str, cliente: 'ClienteDespacho') -> Dict:
        """Procesa consulta de consultoría integral"""
        return {
            'ia_utilizada': 'IA Coordinadora Integral',
            'respuesta': f"Consultoría integral para: {consulta}. Se requiere análisis multidisciplinario.",
            'recomendaciones': [
                'Evaluar aspectos legales y contables',
                'Considerar impacto tributario',
                'Analizar riesgos operacionales',
                'Desarrollar plan de implementación'
            ]
        }
    
    def _sugerir_servicios_adicionales(self, tipo_servicio_actual: str) -> List[str]:
        """Sugiere servicios adicionales basados en el servicio actual"""
        sugerencias = {
            TipoServicio.LEGAL_GENERAL.value: [
                TipoServicio.CONTABLE_GENERAL.value,
                TipoServicio.CONSULTORIA_INTEGRAL.value
            ],
            TipoServicio.DEFENSA_NINEZ_MUJERES.value: [
                TipoServicio.LEGAL_GENERAL.value
            ],
            TipoServicio.LEY_KARIM_ISAPRES.value: [
                TipoServicio.LEGAL_GENERAL.value
            ],
            TipoServicio.LEY_QUIEBRAS.value: [
                TipoServicio.CONTABLE_GENERAL.value,
                TipoServicio.AUDITORIA_FINANCIERA.value
            ],
            TipoServicio.CONTABLE_GENERAL.value: [
                TipoServicio.AUDITORIA_FINANCIERA.value,
                TipoServicio.COMPLIANCE_SII.value
            ]
        }
        
        return sugerencias.get(tipo_servicio_actual, [])
    
    def _calcular_costo_servicio(self, tipo_servicio: str) -> Dict:
        """Calcula costo estimado del servicio"""
        costos_base = {
            TipoServicio.LEGAL_GENERAL.value: {'consulta': 50000, 'hora': 80000},
            TipoServicio.DEFENSA_NINEZ_MUJERES.value: {'consulta': 40000, 'hora': 70000},
            TipoServicio.LEY_KARIM_ISAPRES.value: {'consulta': 60000, 'hora': 90000},
            TipoServicio.LEY_QUIEBRAS.value: {'consulta': 80000, 'hora': 120000},
            TipoServicio.CONTABLE_GENERAL.value: {'consulta': 30000, 'hora': 50000},
            TipoServicio.AUDITORIA_FINANCIERA.value: {'consulta': 100000, 'hora': 150000}
        }
        
        return costos_base.get(tipo_servicio, {'consulta': 50000, 'hora': 80000})


class ClienteDespacho(db.Model):
    """
    Modelo para clientes del despacho digital
    """
    __tablename__ = 'cliente_despacho'
    
    id = db.Column(db.Integer, primary_key=True)
    despacho_id = db.Column(db.Integer, db.ForeignKey('despacho_digital_integral.id'), nullable=False)
    rut = db.Column(db.String(12), unique=True, nullable=False)
    nombre_completo = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    tipo_cliente = db.Column(db.String(50), default="PERSONA_NATURAL")  # PERSONA_NATURAL, EMPRESA
    servicios_contratados = db.Column(db.Text)  # JSON
    historial_casos = db.Column(db.Text)  # JSON
    estado_cuenta = db.Column(db.String(50), default="AL_DIA")
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    casos = db.relationship('CasoIntegral', backref='cliente', lazy=True)
    
    def get_servicios_contratados(self) -> List[str]:
        """Retorna servicios contratados como lista"""
        return json.loads(self.servicios_contratados) if self.servicios_contratados else []
    
    def get_historial_casos(self) -> List[Dict]:
        """Retorna historial de casos como lista"""
        return json.loads(self.historial_casos) if self.historial_casos else []


class CasoIntegral(db.Model):
    """
    Modelo para casos integrales del despacho
    """
    __tablename__ = 'caso_integral'
    
    id = db.Column(db.Integer, primary_key=True)
    despacho_id = db.Column(db.Integer, db.ForeignKey('despacho_digital_integral.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente_despacho.id'), nullable=False)
    numero_caso = db.Column(db.String(50), unique=True, nullable=False)
    tipo_servicio = db.Column(db.String(100), nullable=False)
    consulta_original = db.Column(db.Text, nullable=False)
    respuesta_generada = db.Column(db.Text)
    ia_utilizada = db.Column(db.String(100))
    estado = db.Column(db.String(50), default="PENDIENTE")  # PENDIENTE, EN_PROCESO, COMPLETADO, CERRADO
    prioridad = db.Column(db.String(20), default="NORMAL")  # BAJA, NORMAL, ALTA, URGENTE
    costo_estimado = db.Column(db.Float)
    costo_real = db.Column(db.Float)
    fecha_inicio = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_cierre = db.Column(db.DateTime)
    documentos_generados = db.Column(db.Text)  # JSON
    seguimientos = db.Column(db.Text)  # JSON
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.numero_caso:
            self.numero_caso = f"CASO-{datetime.now().strftime('%Y%m%d')}-{hash(str(datetime.now())) % 10000:04d}"
    
    def agregar_seguimiento(self, descripcion: str, usuario: str = "SISTEMA"):
        """Agrega seguimiento al caso"""
        seguimientos = json.loads(self.seguimientos) if self.seguimientos else []
        
        nuevo_seguimiento = {
            'fecha': datetime.utcnow().isoformat(),
            'usuario': usuario,
            'descripcion': descripcion
        }
        
        seguimientos.append(nuevo_seguimiento)
        self.seguimientos = json.dumps(seguimientos)
        db.session.commit()
    
    def get_seguimientos(self) -> List[Dict]:
        """Retorna lista de seguimientos"""
        return json.loads(self.seguimientos) if self.seguimientos else []
    
    def get_documentos_generados(self) -> List[Dict]:
        """Retorna lista de documentos generados"""
        return json.loads(self.documentos_generados) if self.documentos_generados else []


class DashboardDespacho:
    """
    Clase para generar dashboard del despacho
    """
    
    @staticmethod
    def generar_estadisticas_generales(despacho_id: int) -> Dict:
        """Genera estadísticas generales del despacho"""
        despacho = DespachoDigitalIntegral.query.get(despacho_id)
        if not despacho:
            return {}
        
        # Contar casos por estado
        casos_pendientes = CasoIntegral.query.filter_by(
            despacho_id=despacho_id, estado="PENDIENTE"
        ).count()
        
        casos_en_proceso = CasoIntegral.query.filter_by(
            despacho_id=despacho_id, estado="EN_PROCESO"
        ).count()
        
        casos_completados = CasoIntegral.query.filter_by(
            despacho_id=despacho_id, estado="COMPLETADO"
        ).count()
        
        # Contar clientes
        total_clientes = ClienteDespacho.query.filter_by(despacho_id=despacho_id).count()
        
        # Servicios más solicitados
        casos = CasoIntegral.query.filter_by(despacho_id=despacho_id).all()
        servicios_count = {}
        for caso in casos:
            servicio = caso.tipo_servicio
            servicios_count[servicio] = servicios_count.get(servicio, 0) + 1
        
        return {
            'casos_pendientes': casos_pendientes,
            'casos_en_proceso': casos_en_proceso,
            'casos_completados': casos_completados,
            'total_casos': casos_pendientes + casos_en_proceso + casos_completados,
            'total_clientes': total_clientes,
            'servicios_mas_solicitados': sorted(
                servicios_count.items(), key=lambda x: x[1], reverse=True
            )[:5],
            'ias_activas': len(despacho.get_ias_disponibles()),
            'servicios_disponibles': len(despacho.get_servicios_activos())
        }
    
    @staticmethod
    def generar_reporte_financiero(despacho_id: int, periodo: str = "mensual") -> Dict:
        """Genera reporte financiero del despacho"""
        # En implementación real, calcularía ingresos, costos, etc.
        return {
            'ingresos_periodo': 2500000,
            'costos_operacionales': 800000,
            'utilidad_bruta': 1700000,
            'margen_utilidad': 68.0,
            'casos_facturados': 45,
            'valor_promedio_caso': 55555,
            'crecimiento_vs_periodo_anterior': 15.5
        }

