# simulacion_con_ia_y_memoria.py

import sys
import json
import datetime

# Agregar la carpeta interna al entorno Python
sys.path.append("CLOM_anterior")

from clom_extensiones.verificador_logico import VerificadorLogico
from ia_bridge.mistral_client import mistral_client

# Manejo de memoria operativa
def actualizar_memoria_operacional(evento, resultado, respuesta_ia):
    ruta = "CLOM_anterior/clom_config/memoria_operacional.json"
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            datos = json.load(f)
    except:
        datos = {"sesion_activa": True, "eventos": []}

    datos["eventos"].append({
        "evento": evento,
        "resultado": resultado,
        "respuesta_ia": respuesta_ia,
        "timestamp": datetime.datetime.now().isoformat()
    })

    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2)

# IA real
class IAConnector:
    def __init__(self, mistral_api):
        self.api = mistral_api

    def enviar_instruccion(self, instruccion: str, contexto: dict = None):
        payload = {"prompt": f"[CLOM] {instruccion}\nContexto: {contexto}", "contexto": contexto or {}}
        return self.api.enviar(payload)["respuesta"]

    def validar_respuesta(self, respuesta: str):
        return "[VALIDADO]" if "válida" in respuesta.lower() else "[ALERTA]"

# Flujo principal
if __name__ == "__main__":
    with open("CLOM_anterior/clom_config/1.Configuracion_Base_CSMD.ast", "r") as f:
        ast_data = f.read()
    with open("CLOM_anterior/clom_config/1.Configuracion_Base_CSMD.json", "r") as f:
        json_data = f.read()
    with open("CLOM_anterior/clom_config/2.GMF_Modulos_Funcionales_Dinamicos.json", "r") as f:
        gmf_data = f.read()

    verificador = VerificadorLogico(ast_data, json_data, gmf_data)
    resultado_diagnostico = verificador.diagnostico()
    print("📊 Diagnóstico:", resultado_diagnostico)

    ia = IAConnector(mistral_api=mistral_client)
    consulta = "¿Es correcto activar un módulo evaluador lógico sobre este JSON si ya fue cargado un AST?"
    respuesta_ia = ia.enviar_instruccion(consulta, contexto={"diagnostico": resultado_diagnostico})
    print("🤖 IA:", respuesta_ia)

    validez = ia.validar_respuesta(respuesta_ia)
    print("✔️ Validación:", validez)

    actualizar_memoria_operacional("consulta_ia_validacion", validez, respuesta_ia)
    print("🧠 Evento guardado en memoria_operacional.json")