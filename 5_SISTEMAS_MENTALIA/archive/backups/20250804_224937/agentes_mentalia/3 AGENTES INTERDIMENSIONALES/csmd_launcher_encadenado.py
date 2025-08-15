
import subprocess
import time

print("🔧 [1] Activando núcleo CSMD base...")
subprocess.Popen(["python", "./CLOM_anterior_integrado_CSMD_logfix/clom_extensiones/launch_clom.py"])
time.sleep(3)

print("\n🤖 [2] Integrando IA Mistral...")
subprocess.Popen(["python", "mistral_client.py"])
time.sleep(2)

print("\n💬 [3] Lanzando CLI con IA y entorno CSMD...")
subprocess.Popen(["python", "clom_real_cli_extendido.py"])
