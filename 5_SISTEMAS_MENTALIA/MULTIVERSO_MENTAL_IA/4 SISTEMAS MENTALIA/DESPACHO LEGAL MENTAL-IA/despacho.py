"""
Rutas API para el Despacho Digital Integral
Endpoints para interactuar con todas las IAs especializadas
"""

from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.despacho_integral import (
    DespachoDigitalIntegral, ClienteDespacho, CasoIntegral, 
    DashboardDespacho, TipoServicio
)
from src.models.ia_legal import IALegalCertificada
from src.models.ia_contadora import IAContadoraCertificada
from datetime import datetime
import json

despacho_bp = Blueprint('despacho', __name__)


@despacho_bp.route('/status', methods=['GET'])
def status_despacho():
    """Estado general del despacho"""
    try:
        despacho = DespachoDigitalIntegral.query.first()
        if not despacho:
            # Crear despacho por defecto
            despacho = DespachoDigitalIntegral()
            db.session.add(despacho)
            db.session.commit()
        
        return jsonify({
            'success': True,
            'despacho': {
                'nombre': despacho.nombre_despacho,
                'rut': despacho.rut_despacho,
                'estado': despacho.estado_operativo,
                'servicios_activos': despacho.get_servicios_activos(),
                'ias_disponibles': despacho.get_ias_disponibles()
            }
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@despacho_bp.route('/consulta-integral', methods=['POST'])
def consulta_integral():
    """Endpoint principal para consultas integrales"""
    try:
        data = request.get_json()
        
        # Validar datos requeridos
        if not data.get('consulta'):
            return jsonify({'success': False, 'error': 'Consulta requerida'}), 400
        
        if not data.get('cliente_rut'):
            return jsonify({'success': False, 'error': 'RUT del cliente requerido'}), 400
        
        # Obtener o crear despacho
        despacho = DespachoDigitalIntegral.query.first()
        if not despacho:
            despacho = DespachoDigitalIntegral()
            db.session.add(despacho)
            db.session.commit()
        
        # Obtener o crear cliente
        cliente = ClienteDespacho.query.filter_by(rut=data['cliente_rut']).first()
        if not cliente:
            cliente = ClienteDespacho(
                despacho_id=despacho.id,
                rut=data['cliente_rut'],
                nombre_completo=data.get('cliente_nombre', 'Cliente Anónimo'),
                email=data.get('cliente_email', 'cliente@email.com'),
                telefono=data.get('cliente_telefono', ''),
                tipo_cliente=data.get('tipo_cliente', 'PERSONA_NATURAL')
            )
            db.session.add(cliente)
            db.session.commit()
        
        # Procesar consulta integral
        resultado = despacho.procesar_consulta_integral(
            consulta=data['consulta'],
            cliente_id=cliente.id,
            tipo_servicio_solicitado=data.get('tipo_servicio')
        )
        
        return jsonify({
            'success': True,
            'resultado': resultado,
            'cliente': {
                'id': cliente.id,
                'nombre': cliente.nombre_completo,
                'rut': cliente.rut
            }
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@despacho_bp.route('/servicios-disponibles', methods=['GET'])
def servicios_disponibles():
    """Lista todos los servicios disponibles"""
    try:
        servicios = [
            {
                'codigo': TipoServicio.LEGAL_GENERAL.value,
                'nombre': 'Asesoría Legal General',
                'descripcion': 'Consultas jurídicas generales usando LEXCODE',
                'ia_especializada': 'IA Legal General'
            },
            {
                'codigo': TipoServicio.DEFENSA_NINEZ_MUJERES.value,
                'nombre': 'Defensa Niñez y Mujeres',
                'descripcion': 'Especialización en violencia intrafamiliar y derechos del menor',
                'ia_especializada': 'IA Defensa Especializada'
            },
            {
                'codigo': TipoServicio.LEY_KARIM_ISAPRES.value,
                'nombre': 'Ley Karim e ISAPRES',
                'descripcion': 'Conflictos con ISAPRES y preexistencias médicas',
                'ia_especializada': 'IA Salud Legal'
            },
            {
                'codigo': TipoServicio.LEY_QUIEBRAS.value,
                'nombre': 'Ley de Quiebras',
                'descripcion': 'Reorganización empresarial y procedimientos concursales',
                'ia_especializada': 'IA Concursal'
            },
            {
                'codigo': TipoServicio.CONTABLE_GENERAL.value,
                'nombre': 'Servicios Contables',
                'descripcion': 'Contabilidad general y estados financieros',
                'ia_especializada': 'IA Contadora Certificada'
            },
            {
                'codigo': TipoServicio.AUDITORIA_FINANCIERA.value,
                'nombre': 'Auditoría Financiera',
                'descripcion': 'Auditorías y dictámenes financieros',
                'ia_especializada': 'IA Auditora'
            },
            {
                'codigo': TipoServicio.COMPLIANCE_SII.value,
                'nombre': 'Compliance SII',
                'descripcion': 'Cumplimiento tributario y declaraciones SII',
                'ia_especializada': 'IA Tributaria'
            },
            {
                'codigo': TipoServicio.CONSULTORIA_INTEGRAL.value,
                'nombre': 'Consultoría Integral',
                'descripcion': 'Asesoría multidisciplinaria legal-contable',
                'ia_especializada': 'IA Coordinadora'
            }
        ]
        
        return jsonify({
            'success': True,
            'servicios': servicios,
            'total_servicios': len(servicios)
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@despacho_bp.route('/dashboard', methods=['GET'])
def dashboard():
    """Dashboard con estadísticas del despacho"""
    try:
        despacho = DespachoDigitalIntegral.query.first()
        if not despacho:
            return jsonify({'success': False, 'error': 'Despacho no encontrado'}), 404
        
        estadisticas = DashboardDespacho.generar_estadisticas_generales(despacho.id)
        reporte_financiero = DashboardDespacho.generar_reporte_financiero(despacho.id)
        
        return jsonify({
            'success': True,
            'dashboard': {
                'estadisticas_generales': estadisticas,
                'reporte_financiero': reporte_financiero,
                'fecha_actualizacion': datetime.utcnow().isoformat()
            }
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@despacho_bp.route('/casos', methods=['GET'])
def listar_casos():
    """Lista casos del despacho con filtros opcionales"""
    try:
        # Parámetros de filtro
        estado = request.args.get('estado')
        tipo_servicio = request.args.get('tipo_servicio')
        cliente_id = request.args.get('cliente_id')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        
        # Construir query
        query = CasoIntegral.query
        
        if estado:
            query = query.filter_by(estado=estado)
        if tipo_servicio:
            query = query.filter_by(tipo_servicio=tipo_servicio)
        if cliente_id:
            query = query.filter_by(cliente_id=cliente_id)
        
        # Paginación
        casos_paginados = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        casos_data = []
        for caso in casos_paginados.items:
            casos_data.append({
                'id': caso.id,
                'numero_caso': caso.numero_caso,
                'tipo_servicio': caso.tipo_servicio,
                'estado': caso.estado,
                'prioridad': caso.prioridad,
                'cliente': {
                    'id': caso.cliente.id,
                    'nombre': caso.cliente.nombre_completo,
                    'rut': caso.cliente.rut
                },
                'ia_utilizada': caso.ia_utilizada,
                'fecha_inicio': caso.fecha_inicio.isoformat() if caso.fecha_inicio else None,
                'fecha_cierre': caso.fecha_cierre.isoformat() if caso.fecha_cierre else None,
                'costo_estimado': caso.costo_estimado,
                'costo_real': caso.costo_real
            })
        
        return jsonify({
            'success': True,
            'casos': casos_data,
            'paginacion': {
                'page': page,
                'per_page': per_page,
                'total': casos_paginados.total,
                'pages': casos_paginados.pages,
                'has_next': casos_paginados.has_next,
                'has_prev': casos_paginados.has_prev
            }
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@despacho_bp.route('/casos/<int:caso_id>', methods=['GET'])
def detalle_caso(caso_id):
    """Detalle completo de un caso"""
    try:
        caso = CasoIntegral.query.get(caso_id)
        if not caso:
            return jsonify({'success': False, 'error': 'Caso no encontrado'}), 404
        
        return jsonify({
            'success': True,
            'caso': {
                'id': caso.id,
                'numero_caso': caso.numero_caso,
                'tipo_servicio': caso.tipo_servicio,
                'consulta_original': caso.consulta_original,
                'respuesta_generada': caso.respuesta_generada,
                'estado': caso.estado,
                'prioridad': caso.prioridad,
                'cliente': {
                    'id': caso.cliente.id,
                    'nombre': caso.cliente.nombre_completo,
                    'rut': caso.cliente.rut,
                    'email': caso.cliente.email,
                    'telefono': caso.cliente.telefono
                },
                'ia_utilizada': caso.ia_utilizada,
                'fecha_inicio': caso.fecha_inicio.isoformat() if caso.fecha_inicio else None,
                'fecha_cierre': caso.fecha_cierre.isoformat() if caso.fecha_cierre else None,
                'costo_estimado': caso.costo_estimado,
                'costo_real': caso.costo_real,
                'seguimientos': caso.get_seguimientos(),
                'documentos_generados': caso.get_documentos_generados()
            }
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@despacho_bp.route('/casos/<int:caso_id>/seguimiento', methods=['POST'])
def agregar_seguimiento(caso_id):
    """Agrega seguimiento a un caso"""
    try:
        data = request.get_json()
        
        if not data.get('descripcion'):
            return jsonify({'success': False, 'error': 'Descripción requerida'}), 400
        
        caso = CasoIntegral.query.get(caso_id)
        if not caso:
            return jsonify({'success': False, 'error': 'Caso no encontrado'}), 404
        
        caso.agregar_seguimiento(
            descripcion=data['descripcion'],
            usuario=data.get('usuario', 'SISTEMA')
        )
        
        return jsonify({
            'success': True,
            'mensaje': 'Seguimiento agregado exitosamente',
            'seguimientos': caso.get_seguimientos()
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@despacho_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    """Lista clientes del despacho"""
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        
        clientes_paginados = ClienteDespacho.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        clientes_data = []
        for cliente in clientes_paginados.items:
            # Contar casos del cliente
            total_casos = CasoIntegral.query.filter_by(cliente_id=cliente.id).count()
            casos_activos = CasoIntegral.query.filter_by(
                cliente_id=cliente.id
            ).filter(
                CasoIntegral.estado.in_(['PENDIENTE', 'EN_PROCESO'])
            ).count()
            
            clientes_data.append({
                'id': cliente.id,
                'rut': cliente.rut,
                'nombre_completo': cliente.nombre_completo,
                'email': cliente.email,
                'telefono': cliente.telefono,
                'tipo_cliente': cliente.tipo_cliente,
                'estado_cuenta': cliente.estado_cuenta,
                'fecha_registro': cliente.fecha_registro.isoformat(),
                'estadisticas': {
                    'total_casos': total_casos,
                    'casos_activos': casos_activos
                }
            })
        
        return jsonify({
            'success': True,
            'clientes': clientes_data,
            'paginacion': {
                'page': page,
                'per_page': per_page,
                'total': clientes_paginados.total,
                'pages': clientes_paginados.pages,
                'has_next': clientes_paginados.has_next,
                'has_prev': clientes_paginados.has_prev
            }
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@despacho_bp.route('/clientes', methods=['POST'])
def crear_cliente():
    """Crea un nuevo cliente"""
    try:
        data = request.get_json()
        
        # Validar datos requeridos
        if not data.get('rut'):
            return jsonify({'success': False, 'error': 'RUT requerido'}), 400
        if not data.get('nombre_completo'):
            return jsonify({'success': False, 'error': 'Nombre completo requerido'}), 400
        if not data.get('email'):
            return jsonify({'success': False, 'error': 'Email requerido'}), 400
        
        # Verificar que no exista cliente con mismo RUT
        cliente_existente = ClienteDespacho.query.filter_by(rut=data['rut']).first()
        if cliente_existente:
            return jsonify({'success': False, 'error': 'Cliente ya existe con ese RUT'}), 400
        
        # Obtener despacho
        despacho = DespachoDigitalIntegral.query.first()
        if not despacho:
            despacho = DespachoDigitalIntegral()
            db.session.add(despacho)
            db.session.commit()
        
        # Crear cliente
        cliente = ClienteDespacho(
            despacho_id=despacho.id,
            rut=data['rut'],
            nombre_completo=data['nombre_completo'],
            email=data['email'],
            telefono=data.get('telefono', ''),
            direccion=data.get('direccion', ''),
            tipo_cliente=data.get('tipo_cliente', 'PERSONA_NATURAL')
        )
        
        db.session.add(cliente)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'mensaje': 'Cliente creado exitosamente',
            'cliente': {
                'id': cliente.id,
                'rut': cliente.rut,
                'nombre_completo': cliente.nombre_completo,
                'email': cliente.email,
                'fecha_registro': cliente.fecha_registro.isoformat()
            }
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@despacho_bp.route('/generar-documento', methods=['POST'])
def generar_documento():
    """Genera documento legal usando IA Legal"""
    try:
        data = request.get_json()
        
        if not data.get('tipo_documento'):
            return jsonify({'success': False, 'error': 'Tipo de documento requerido'}), 400
        
        if not data.get('datos'):
            return jsonify({'success': False, 'error': 'Datos del documento requeridos'}), 400
        
        # Obtener IA Legal
        ia_legal = IALegalCertificada.query.first()
        if not ia_legal:
            ia_legal = IALegalCertificada()
            db.session.add(ia_legal)
            db.session.commit()
        
        # Generar documento
        documento_generado = ia_legal.generar_documento_legal(
            tipo_documento=data['tipo_documento'],
            datos=data['datos']
        )
        
        return jsonify({
            'success': True,
            'documento': documento_generado,
            'tipo_documento': data['tipo_documento'],
            'fecha_generacion': datetime.utcnow().isoformat()
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@despacho_bp.route('/auditoria-contable', methods=['POST'])
def realizar_auditoria():
    """Realiza auditoría contable usando IA Contadora"""
    try:
        data = request.get_json()
        
        if not data.get('estados_financieros'):
            return jsonify({'success': False, 'error': 'Estados financieros requeridos'}), 400
        
        # Obtener IA Contadora
        ia_contadora = IAContadoraCertificada.query.first()
        if not ia_contadora:
            ia_contadora = IAContadoraCertificada()
            db.session.add(ia_contadora)
            db.session.commit()
        
        # Realizar validaciones
        validaciones = ia_contadora.validar_estados_financieros(data['estados_financieros'])
        
        # Generar dictamen
        dictamen = ia_contadora.generar_dictamen_auditoria(
            data['estados_financieros'], validaciones
        )
        
        return jsonify({
            'success': True,
            'validaciones': validaciones,
            'dictamen': dictamen,
            'fecha_auditoria': datetime.utcnow().isoformat()
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@despacho_bp.route('/estadisticas-ia', methods=['GET'])
def estadisticas_ia():
    """Estadísticas de uso de las IAs"""
    try:
        # Contar consultas por tipo de IA
        casos = CasoIntegral.query.all()
        
        uso_ias = {}
        for caso in casos:
            if caso.ia_utilizada:
                uso_ias[caso.ia_utilizada] = uso_ias.get(caso.ia_utilizada, 0) + 1
        
        # Estadísticas de IAs
        total_ias_legales = IALegalCertificada.query.count()
        total_ias_contadoras = IAContadoraCertificada.query.count()
        
        return jsonify({
            'success': True,
            'estadisticas': {
                'uso_por_ia': uso_ias,
                'ias_registradas': {
                    'legal': total_ias_legales,
                    'contadora': total_ias_contadoras
                },
                'total_casos_procesados': len(casos),
                'ia_mas_utilizada': max(uso_ias.items(), key=lambda x: x[1])[0] if uso_ias else None
            }
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

