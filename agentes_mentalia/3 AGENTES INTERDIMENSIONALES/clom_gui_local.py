
import subprocess
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from ia_bridge.mistral_client import IAConnector, mistral_client

# Lanzar núcleo CSMD desde carpeta anterior
print("🧠 Iniciando núcleo CSMD...")
subprocess.Popen(["python", "CLOM_anterior_integrado_CSMD_logfix/clom_extensiones/launch_clom.py"])
time.sleep(3)

# Inicializar IAConnector con mentalización CSMD
print("🔗 Conectando IA real (Ollama)...")
clom_ia = IAConnector(mistral_client)
contexto_csmd = {
    "estructura": "CLOM base estructurado por AST y GMF",
    "modo": "mentalizado_clom_base",
    "protocolo": "ninguno"
}

# Interfaz GUI básica
class CLOMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CLOM CSMD Local")
        self.output = ScrolledText(root, width=100, height=30, wrap=tk.WORD)
        self.output.pack(padx=10, pady=10)
        self.entry = tk.Entry(root, width=100)
        self.entry.pack(padx=10, pady=(0,10))
        self.entry.bind("<Return>", self.enviar)

    def enviar(self, event=None):
        entrada = self.entry.get().strip()
        print(f"➡️ Entrada del usuario: {entrada}")
        if not entrada:
            return
        self.output.insert(tk.END, f">> {entrada}\n")
        try:
            respuesta = clom_ia.enviar_instruccion(entrada, contexto_csmd)
            print(f"🧠 Respuesta IA: {respuesta}")
            self.output.insert(tk.END, f"{respuesta}\n\n")
        except Exception as e:
            error_msg = f"[ERROR GUI] {str(e)}"
            print(error_msg)
            self.output.insert(tk.END, f"{error_msg}\n\n")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    print("🚀 Lanzando interfaz gráfica...")
    root = tk.Tk()
    app = CLOMApp(root)
    root.mainloop()
