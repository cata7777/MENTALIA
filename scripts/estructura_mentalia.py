import os
import json
from pathlib import Path

# Mapeo simbólico por SIP
SIMBOLOS = {
    "MULTIVERSO": "🌌",
    "MENTALIZACION": "🧠",
    "AGENTES": "💫",
    "SISTEMAS": "🪐",
    "RRI": "🛡️"
}


def clasificar(nombre):
    nombre_up = nombre.upper()
    for clave, emoji in SIMBOLOS.items():
        if clave in nombre_up:
            return f"{emoji} {nombre}"
    return f"📁 {nombre}"


def recorrer(base_path):
    estructura = []
    for root, dirs, files in os.walk(base_path):
        nivel = Path(root).relative_to(base_path)
        carpetas = [clasificar(d) for d in dirs]
        archivos = [f for f in files]
        estructura.append({
            "ruta": str(nivel),
            "carpetas": carpetas,
            "archivos": archivos
        })
    return estructura


if __name__ == "__main__":
    base_path = Path(".")  # desde raíz del repo
    estructura = recorrer(base_path)

    # Guardar README simbólico
    with open("README_MENTALIA_STRUCTURE.md", "w", encoding="utf-8") as f:
        f.write("# 🌐 ESTRUCTURA MENTALIA\n\n")
        for item in estructura:
            f.write(f"\n## {item['ruta']}\n")
            for c in item["carpetas"]:
                f.write(f"- {c}\n")
            for a in item["archivos"]:
                f.write(f"  - 📄 {a}\n")

    # Guardar JSON estructural
    with open("estructura_universal.json", "w", encoding="utf-8") as f:
        json.dump(estructura, f, indent=2, ensure_ascii=False)

    print("✅ Estructura generada correctamente.")
