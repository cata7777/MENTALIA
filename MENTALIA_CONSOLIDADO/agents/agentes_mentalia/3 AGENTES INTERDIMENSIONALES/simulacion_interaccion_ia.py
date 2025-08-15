
from ia_bridge.mistral_client import mistral_client  # Asumiendo que ya existe y está importable

class IAConnector:
    def __init__(self, mistral_api):
        self.api = mistral_api

    def enviar_instruccion(self, instruccion: str, contexto: dict = None):
        payload = {
            "prompt": f"[CLOM] {instruccion}",
            "contexto": contexto or {}
        }
        respuesta = self.api.enviar(payload)  # Simula uso del cliente real
        return respuesta.get("respuesta", "[IA] Sin respuesta procesada")

    def validar_respuesta(self, respuesta: str):
        return "[VALIDADO]" if "error" not in respuesta.lower() else "[ALERTA]"

if __name__ == "__main__":
    ia = IAConnector(mistral_api=mistral_client)
    consulta = "¿Cómo debería comportarse un CLOM base cuando detecta un AST inválido?"
    respuesta = ia.enviar_instruccion(consulta)
    print("[IA DICE]", respuesta)
    print("Validación:", ia.validar_respuesta(respuesta))
