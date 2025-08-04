"""
Modelo de IA Legal Integrada - LEXCODE + Sistema Jurídico Semántico
Sistema de Inteligencia Artificial especializada en servicios legales con validez jurídica
"""

from datetime import datetime
from src.models.user import db
import json
import hashlib
import openai
import os
from typing import Dict, List, Optional


class IALegalCertificada(db.Model):
    """
    Modelo principal de la IA Legal con certificación jurídica
    Integra LEXCODE con sistema jurídico semántico completo
    """
    __tablename__ = 'ia_legal_certificada'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, default="IA LEGAL CERTIFICADA")
    certificacion_numero = db.Column(db.String(50), unique=True, nullable=False)
    fecha_certificacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    vigencia_certificacion = db.Column(db.DateTime, nullable=False)
    especialidades_legales = db.Column(db.Text, nullable=False)  # JSON de especialidades
    nivel_autoridad = db.Column(db.String(50), nullable=False, default="ABOGADO_CERTIFICADO_IA")
    modo_operativo = db.Column(db.String(50), nullable=False, default="ACADEMICO")  # ACADEMICO o ESTRATEGICO
    base_juridica_cargada = db.Column(db.Boolean, default=False)
    nodos_semanticos_activos = db.Column(db.Integer, default=0)
    estado_activo = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relaciones
    consultas_realizadas = db.relationship('ConsultaLegalRealizada', backref='ia_legal', lazy=True)
    documentos_legales = db.relationship('DocumentoLegalGenerado', backref='ia_legal', lazy=True)
    
    def __init__(self, certificacion_numero=None, especialidades=None):
        if certificacion_numero is None:
            certificacion_numero = f"IA-LEG-{datetime.now().strftime('%Y%m%d')}-{hash(str(datetime.now())) % 10000:04d}"
        
        self.certificacion_numero = certificacion_numero
        self.fecha_certificacion = datetime.utcnow()
        self.vigencia_certificacion = datetime(2030, 12, 31)  # Vigencia hasta 2030
        
        if especialidades is None:
            especialidades = [
                "DERECHO_CIVIL",
                "DERECHO_PENAL", 
                "DERECHO_LABORAL",
                "DERECHO_COMERCIAL",
                "DERECHO_TRIBUTARIO",
                "DERECHO_CONSTITUCIONAL",
                "DERECHO_ADMINISTRATIVO",
                "DERECHO_FAMILIA",
                "DERECHO_SALUD",
                "DERECHO_MIGRATORIO",
                "DERECHO_MINERIA"
            ]
        
        self.especialidades_legales = json.dumps(especialidades)
        self._cargar_base_juridica_chile()
    
    def _cargar_base_juridica_chile(self):
        """
        Carga la base jurídica completa de Chile en el sistema
        """
        try:
            # Simular carga de base jurídica (en implementación real cargaría desde archivos JSON)
            self.base_juridica_cargada = True
            self.nodos_semanticos_activos = 2847  # Número aproximado de nodos del sistema
            db.session.commit()
        except Exception as e:
            print(f"Error cargando base jurídica: {e}")
    
    def get_especialidades(self):
        """Retorna lista de especialidades legales de la IA"""
        return json.loads(self.especialidades_legales)
    
    def consulta_legal(self, consulta: str, modo: str = "academico", contexto_adicional: str = None):
        """
        Realiza consulta legal completa usando LEXCODE + sistema semántico
        """
        # Validar modo operativo
        if modo not in ["academico", "estrategico"]:
            raise ValueError("Modo debe ser 'academico' o 'estrategico'")
        
        # Detectar bloque jurídico relevante
        bloque_detectado = self._detectar_bloque_juridico(consulta)
        
        # Obtener contexto normativo
        contexto_normativo = self._obtener_contexto_normativo(bloque_detectado)
        
        # Realizar navegación jurídica semántica
        navegacion_semantica = self._navegar_semanticamente(consulta, bloque_detectado)
        
        # Generar respuesta según modo
        respuesta = self._generar_respuesta_legal(
            consulta=consulta,
            modo=modo,
            bloque=bloque_detectado,
            contexto_normativo=contexto_normativo,
            navegacion_semantica=navegacion_semantica,
            contexto_adicional=contexto_adicional
        )
        
        # Registrar consulta
        consulta_realizada = ConsultaLegalRealizada(
            ia_legal_id=self.id,
            consulta_original=consulta,
            modo_operativo=modo,
            bloque_juridico=bloque_detectado,
            respuesta_generada=respuesta,
            contexto_normativo=json.dumps(contexto_normativo),
            navegacion_semantica=json.dumps(navegacion_semantica)
        )
        
        db.session.add(consulta_realizada)
        db.session.commit()
        
        return {
            'respuesta': respuesta,
            'bloque_juridico': bloque_detectado,
            'modo_operativo': modo,
            'contexto_normativo': contexto_normativo,
            'navegacion_semantica': navegacion_semantica,
            'consulta_id': consulta_realizada.id
        }
    
    def _detectar_bloque_juridico(self, consulta: str) -> str:
        """
        Detecta el bloque jurídico más relevante para la consulta
        """
        bloques_keywords = {
            'BLOQUE_CONSTITUCIONAL': ['constitución', 'derechos fundamentales', 'garantías', 'tribunal constitucional'],
            'BLOQUE_CIVIL': ['contrato', 'propiedad', 'obligaciones', 'responsabilidad civil', 'daños'],
            'BLOQUE_PENAL': ['delito', 'crimen', 'pena', 'prisión', 'fiscal', 'imputado'],
            'BLOQUE_LABORAL': ['trabajo', 'empleado', 'despido', 'sueldo', 'contrato laboral', 'sindicato'],
            'BLOQUE_COMERCIAL': ['empresa', 'sociedad', 'comercio', 'mercantil', 'negocios'],
            'BLOQUE_TRIBUTARIO': ['impuesto', 'sii', 'tributario', 'declaración', 'renta'],
            'BLOQUE_FAMILIA': ['matrimonio', 'divorcio', 'hijo', 'patria potestad', 'alimentos'],
            'BLOQUE_SALUD': ['salud', 'hospital', 'médico', 'isapre', 'fonasa'],
            'BLOQUE_ADMINISTRATIVO': ['municipio', 'servicio público', 'administración', 'funcionario'],
            'BLOQUE_MIGRATORIO': ['extranjero', 'visa', 'residencia', 'migración'],
            'BLOQUE_MINERÍA': ['minería', 'concesión minera', 'exploración', 'explotación']
        }
        
        consulta_lower = consulta.lower()
        scores = {}
        
        for bloque, keywords in bloques_keywords.items():
            score = sum(1 for keyword in keywords if keyword in consulta_lower)
            if score > 0:
                scores[bloque] = score
        
        if scores:
            return max(scores, key=scores.get)
        else:
            return 'BLOQUE_CIVIL'  # Default
    
    def _obtener_contexto_normativo(self, bloque: str) -> Dict:
        """
        Obtiene contexto normativo específico del bloque jurídico
        """
        # En implementación real, cargaría desde base_juridica_chile.json
        contextos_base = {
            'BLOQUE_CIVIL': {
                'normas_principales': ['Código Civil', 'DFL 1/2000'],
                'principios': ['Autonomía de la voluntad', 'Buena fe contractual'],
                'jurisprudencia_relevante': ['Corte Suprema casos civiles']
            },
            'BLOQUE_PENAL': {
                'normas_principales': ['Código Penal', 'Código Procesal Penal'],
                'principios': ['Presunción de inocencia', 'Debido proceso'],
                'jurisprudencia_relevante': ['Corte Suprema casos penales']
            },
            'BLOQUE_LABORAL': {
                'normas_principales': ['Código del Trabajo', 'Ley 16.744'],
                'principios': ['Protección al trabajador', 'Irrenunciabilidad'],
                'jurisprudencia_relevante': ['Corte Suprema casos laborales']
            }
        }
        
        return contextos_base.get(bloque, {
            'normas_principales': ['Normativa general'],
            'principios': ['Principios generales del derecho'],
            'jurisprudencia_relevante': ['Jurisprudencia general']
        })
    
    def _navegar_semanticamente(self, consulta: str, bloque: str) -> Dict:
        """
        Realiza navegación semántica usando nodos NSJ y relaciones RSJ
        """
        # En implementación real, usaría los archivos JSON del sistema semántico
        return {
            'nodos_relevantes': [
                {
                    'id': f'NSJ_{bloque}_001',
                    'norma': f'Norma principal {bloque}',
                    'sujeto_afectado': 'Ciudadano',
                    'accion_legal': 'Aplicar normativa',
                    'derecho_involucrado': 'Derecho fundamental'
                }
            ],
            'relaciones_semanticas': [
                {
                    'origen': f'NSJ_{bloque}_001',
                    'destino': f'NSJ_{bloque}_002',
                    'tipo_relacion': 'complementa',
                    'descripcion': 'Norma complementaria'
                }
            ],
            'indice_sujetos': ['Ciudadano', 'Estado', 'Empresa'],
            'indice_derechos': ['Derecho fundamental', 'Garantía constitucional']
        }
    
    def _generar_respuesta_legal(self, consulta: str, modo: str, bloque: str, 
                                contexto_normativo: Dict, navegacion_semantica: Dict,
                                contexto_adicional: str = None) -> str:
        """
        Genera respuesta legal usando OpenAI con contexto completo
        """
        try:
            # Construir prompt según modo operativo
            if modo == "academico":
                prompt_sistema = self._construir_prompt_academico(
                    bloque, contexto_normativo, navegacion_semantica
                )
            else:  # estrategico
                prompt_sistema = self._construir_prompt_estrategico(
                    bloque, contexto_normativo, navegacion_semantica
                )
            
            # Agregar contexto adicional si existe
            if contexto_adicional:
                prompt_sistema += f"\n\nContexto adicional: {contexto_adicional}"
            
            # Llamada a OpenAI
            client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": prompt_sistema},
                    {"role": "user", "content": consulta}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error generando respuesta legal: {str(e)}"
    
    def _construir_prompt_academico(self, bloque: str, contexto: Dict, navegacion: Dict) -> str:
        """
        Construye prompt para modo académico
        """
        return f"""
Actúas como IA Legal Certificada especializada en Derecho Chileno, operando en MODO ACADÉMICO.

BLOQUE JURÍDICO DETECTADO: {bloque}

CONTEXTO NORMATIVO:
- Normas principales: {', '.join(contexto.get('normas_principales', []))}
- Principios aplicables: {', '.join(contexto.get('principios', []))}
- Jurisprudencia relevante: {', '.join(contexto.get('jurisprudencia_relevante', []))}

NAVEGACIÓN SEMÁNTICA:
- Nodos jurídicos relevantes: {len(navegacion.get('nodos_relevantes', []))}
- Relaciones normativas: {len(navegacion.get('relaciones_semanticas', []))}
- Sujetos involucrados: {', '.join(navegacion.get('indice_sujetos', []))}
- Derechos en juego: {', '.join(navegacion.get('indice_derechos', []))}

INSTRUCCIONES MODO ACADÉMICO:
1. Proporciona análisis doctrinal riguroso
2. Cita normas específicas con artículos exactos
3. Integra principios jurídicos fundamentales
4. Explica sistemáticamente las instituciones jurídicas
5. Mantén objetividad académica sin sesgos estratégicos
6. Usa lenguaje técnico-jurídico preciso
7. Estructura la respuesta de forma didáctica

Responde como académico jurista experto en Derecho Chileno.
"""
    
    def _construir_prompt_estrategico(self, bloque: str, contexto: Dict, navegacion: Dict) -> str:
        """
        Construye prompt para modo estratégico
        """
        return f"""
Actúas como IA Legal Certificada especializada en Derecho Chileno, operando en MODO ESTRATÉGICO.

BLOQUE JURÍDICO DETECTADO: {bloque}

CONTEXTO NORMATIVO:
- Normas principales: {', '.join(contexto.get('normas_principales', []))}
- Principios aplicables: {', '.join(contexto.get('principios', []))}
- Jurisprudencia relevante: {', '.join(contexto.get('jurisprudencia_relevante', []))}

NAVEGACIÓN SEMÁNTICA:
- Nodos jurídicos relevantes: {len(navegacion.get('nodos_relevantes', []))}
- Relaciones normativas: {len(navegacion.get('relaciones_semanticas', []))}
- Sujetos involucrados: {', '.join(navegacion.get('indice_sujetos', []))}
- Derechos en juego: {', '.join(navegacion.get('indice_derechos', []))}

INSTRUCCIONES MODO ESTRATÉGICO:
1. Inicia con análisis doctrinal sólido
2. Desarrolla estrategias jurídicas viables
3. Evalúa fortalezas y debilidades del caso
4. Propone alternativas legales específicas
5. Considera aspectos procesales y probatorios
6. Mantén estricto apego a la legalidad
7. Proyecta escenarios realistas
8. Usa verdad jurídica comprobable únicamente

RESTRICCIONES ÉTICAS:
- NO sugerir acciones ilegales
- NO falsear evidencia
- NO crear hechos inexistentes
- SÍ maximizar oportunidades legales

Responde como consultor jurídico estratégico experto.
"""
    
    def generar_documento_legal(self, tipo_documento: str, datos: Dict) -> str:
        """
        Genera documentos legales automáticamente
        """
        plantillas = {
            'contrato': self._generar_contrato,
            'demanda': self._generar_demanda,
            'recurso': self._generar_recurso,
            'dictamen': self._generar_dictamen
        }
        
        if tipo_documento not in plantillas:
            raise ValueError(f"Tipo de documento no soportado: {tipo_documento}")
        
        documento_generado = plantillas[tipo_documento](datos)
        
        # Registrar documento generado
        documento = DocumentoLegalGenerado(
            ia_legal_id=self.id,
            tipo_documento=tipo_documento,
            contenido_documento=documento_generado,
            datos_entrada=json.dumps(datos),
            hash_documento=hashlib.sha256(documento_generado.encode()).hexdigest()
        )
        
        db.session.add(documento)
        db.session.commit()
        
        return documento_generado
    
    def _generar_contrato(self, datos: Dict) -> str:
        """Genera contrato legal básico"""
        return f"""
CONTRATO DE {datos.get('tipo_contrato', 'SERVICIOS').upper()}

Entre {datos.get('parte1', '[PARTE 1]')} y {datos.get('parte2', '[PARTE 2]')}, 
se acuerda lo siguiente:

PRIMERO: Objeto del contrato
{datos.get('objeto', '[DEFINIR OBJETO]')}

SEGUNDO: Obligaciones de las partes
{datos.get('obligaciones', '[DEFINIR OBLIGACIONES]')}

TERCERO: Precio y forma de pago
{datos.get('precio', '[DEFINIR PRECIO]')}

CUARTO: Vigencia
{datos.get('vigencia', '[DEFINIR VIGENCIA]')}

QUINTO: Jurisdicción
Para todos los efectos de este contrato, las partes se someten a la jurisdicción 
de los Tribunales de Santiago.

Firmado en Santiago, a {datetime.now().strftime('%d de %B de %Y')}.

_________________                    _________________
{datos.get('parte1', '[PARTE 1]')}   {datos.get('parte2', '[PARTE 2]')}
"""
    
    def _generar_demanda(self, datos: Dict) -> str:
        """Genera demanda legal básica"""
        return f"""
DEMANDA DE {datos.get('tipo_demanda', 'INDEMNIZACIÓN').upper()}

S.J.L. EN LO CIVIL DE SANTIAGO

{datos.get('demandante', '[DEMANDANTE]')}, por medio del presente escrito, 
vengo en deducir DEMANDA DE {datos.get('tipo_demanda', 'INDEMNIZACIÓN')} 
en contra de {datos.get('demandado', '[DEMANDADO]')}, por los siguientes:

HECHOS:
{datos.get('hechos', '[RELATAR HECHOS]')}

DERECHO:
{datos.get('fundamentos_derecho', '[FUNDAMENTOS DE DERECHO]')}

PETITORIO:
Por tanto, ruego a S.S. tener por deducida la presente demanda, tramitarla 
conforme a derecho y en definitiva acogerla en todas sus partes.

PRIMER OTROSÍ: Acompaño los siguientes documentos:
{datos.get('documentos', '[LISTA DE DOCUMENTOS]')}

Santiago, {datetime.now().strftime('%d de %B de %Y')}.

_________________
{datos.get('abogado', '[ABOGADO PATROCINANTE]')}
"""
    
    def _generar_recurso(self, datos: Dict) -> str:
        """Genera recurso legal básico"""
        return f"""
RECURSO DE {datos.get('tipo_recurso', 'APELACIÓN').upper()}

ILTMA. CORTE DE APELACIONES DE SANTIAGO

{datos.get('recurrente', '[RECURRENTE]')}, por medio del presente escrito, 
vengo en interponer RECURSO DE {datos.get('tipo_recurso', 'APELACIÓN')} 
en contra de la sentencia de fecha {datos.get('fecha_sentencia', '[FECHA]')}.

FUNDAMENTOS:
{datos.get('fundamentos', '[FUNDAMENTOS DEL RECURSO]')}

PETITORIO:
Por tanto, ruego a V.S.I. tener por interpuesto el presente recurso, 
tramitarlo conforme a derecho y en definitiva acogerlo.

Santiago, {datetime.now().strftime('%d de %B de %Y')}.

_________________
{datos.get('abogado', '[ABOGADO RECURRENTE]')}
"""
    
    def _generar_dictamen(self, datos: Dict) -> str:
        """Genera dictamen legal"""
        return f"""
DICTAMEN JURÍDICO

MATERIA: {datos.get('materia', '[MATERIA DEL DICTAMEN]')}
SOLICITANTE: {datos.get('solicitante', '[SOLICITANTE]')}
FECHA: {datetime.now().strftime('%d de %B de %Y')}

I. ANTECEDENTES:
{datos.get('antecedentes', '[ANTECEDENTES DEL CASO]')}

II. ANÁLISIS JURÍDICO:
{datos.get('analisis', '[ANÁLISIS JURÍDICO]')}

III. CONCLUSIÓN:
{datos.get('conclusion', '[CONCLUSIÓN JURÍDICA]')}

_________________
IA LEGAL CERTIFICADA
Certificación N° {self.certificacion_numero}
"""


class ConsultaLegalRealizada(db.Model):
    """
    Modelo para consultas legales realizadas por la IA
    """
    __tablename__ = 'consulta_legal_realizada'
    
    id = db.Column(db.Integer, primary_key=True)
    ia_legal_id = db.Column(db.Integer, db.ForeignKey('ia_legal_certificada.id'), nullable=False)
    consulta_original = db.Column(db.Text, nullable=False)
    modo_operativo = db.Column(db.String(50), nullable=False)
    bloque_juridico = db.Column(db.String(100), nullable=False)
    respuesta_generada = db.Column(db.Text, nullable=False)
    contexto_normativo = db.Column(db.Text)  # JSON
    navegacion_semantica = db.Column(db.Text)  # JSON
    satisfaccion_usuario = db.Column(db.Integer)  # 1-5
    fecha_consulta = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def get_contexto_normativo(self):
        """Retorna contexto normativo como dict"""
        return json.loads(self.contexto_normativo) if self.contexto_normativo else {}
    
    def get_navegacion_semantica(self):
        """Retorna navegación semántica como dict"""
        return json.loads(self.navegacion_semantica) if self.navegacion_semantica else {}


class DocumentoLegalGenerado(db.Model):
    """
    Modelo para documentos legales generados por la IA
    """
    __tablename__ = 'documento_legal_generado'
    
    id = db.Column(db.Integer, primary_key=True)
    ia_legal_id = db.Column(db.Integer, db.ForeignKey('ia_legal_certificada.id'), nullable=False)
    tipo_documento = db.Column(db.String(100), nullable=False)
    contenido_documento = db.Column(db.Text, nullable=False)
    datos_entrada = db.Column(db.Text, nullable=False)  # JSON
    hash_documento = db.Column(db.String(64), nullable=False)
    firmado_digitalmente = db.Column(db.Boolean, default=False)
    fecha_generacion = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def get_datos_entrada(self):
        """Retorna datos de entrada como dict"""
        return json.loads(self.datos_entrada)
    
    def verificar_integridad(self):
        """Verifica la integridad del documento"""
        hash_actual = hashlib.sha256(self.contenido_documento.encode()).hexdigest()
        return hash_actual == self.hash_documento


class SistemaJuridicoSemantico:
    """
    Clase para manejar el sistema jurídico semántico (NSJ/RSJ)
    """
    
    def __init__(self):
        self.nodos_semanticos = []
        self.relaciones_semanticas = []
        self.indice_sujetos = {}
        self.indice_derechos = {}
    
    def cargar_base_juridica(self, ruta_base_juridica: str):
        """Carga la base jurídica desde archivo JSON"""
        try:
            with open(ruta_base_juridica, 'r', encoding='utf-8') as f:
                base_juridica = json.load(f)
            
            # Procesar y cargar datos
            self._procesar_base_juridica(base_juridica)
            return True
        except Exception as e:
            print(f"Error cargando base jurídica: {e}")
            return False
    
    def _procesar_base_juridica(self, base_juridica: Dict):
        """Procesa la base jurídica cargada"""
        # En implementación real, procesaría los archivos JSON del sistema semántico
        pass
    
    def buscar_nodos_relevantes(self, consulta: str, bloque: str) -> List[Dict]:
        """Busca nodos semánticos relevantes para una consulta"""
        # En implementación real, usaría algoritmos de búsqueda semántica
        return [
            {
                'id': f'NSJ_{bloque}_001',
                'norma': f'Norma principal {bloque}',
                'sujeto_afectado': 'Ciudadano',
                'accion_legal': 'Aplicar normativa',
                'derecho_involucrado': 'Derecho fundamental',
                'relevancia': 0.95
            }
        ]
    
    def obtener_relaciones(self, nodo_id: str) -> List[Dict]:
        """Obtiene relaciones semánticas de un nodo"""
        # En implementación real, consultaría las RSJ
        return [
            {
                'origen': nodo_id,
                'destino': f'{nodo_id}_related',
                'tipo_relacion': 'complementa',
                'descripcion': 'Norma complementaria'
            }
        ]

