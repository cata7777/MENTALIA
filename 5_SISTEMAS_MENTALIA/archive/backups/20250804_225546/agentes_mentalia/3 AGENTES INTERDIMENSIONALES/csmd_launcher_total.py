
import os
import sys

# -----------------------
# 1. ACTIVAR CSMD BASE
# -----------------------
print("🔧 [1] Activando núcleo CSMD base...")
os.system("python ./CLOM_anterior_integrado_CSMD_logfix/clom_extensiones/launch_clom.py")

# -----------------------
# 2. INTEGRAR IA MISTRAL
# -----------------------
print("\n🤖 [2] Integrando IA Mistral...")
os.system("python ./mistral_client.py")

# -----------------------
# 3. LANZAR INTERFAZ CLI
# -----------------------
print("\n💬 [3] Lanzando CLI con IA y entorno CSMD...")
os.system("python ./clom_real_cli_extendido.py")
