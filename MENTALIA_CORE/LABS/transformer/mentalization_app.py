"""
MENTALIA - Ejemplo de Aplicación del Motor de Mentalización
Muestra cómo integrar el motor de mentalización en aplicaciones reales

Creado por: Catalina Rojo Lema
Ecosistema: MENTALIA
Versión: 1.0
"""

import json
import sys
from pathlib import Path
import argparse

# Asegurarse de que podemos importar desde MENTALIA_CORE
sys.path.append('/workspaces/MENTALIA')
sys.path.append('/workspaces/MENTALIA/MENTALIA_CORE/LABS/transformer')

try:
    from MENTALIA_CORE.LABS.transformer.mentalization_engine_v2 import process_mentalization_advanced
except ImportError:
    try:
        from mentalization_engine_v2 import process_mentalization_advanced
    except ImportError:
        print("ERROR: No se pudo importar el motor de mentalización.")
        print("Asegúrate de que el script se ejecuta desde el directorio correcto.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Procesador de Mentalización MENTALIA')
    parser.add_argument('--text', type=str, help='Texto para analizar')
    parser.add_argument('--emotions', type=str, help='Indicadores emocionales (separados por comas)')
    parser.add_argument('--nd', type=str, help='Marcadores neurodivergentes (separados por comas)')
    parser.add_argument('--session', type=str, default='individual', help='Tipo de sesión (individual, grupo, crisis)')
    parser.add_argument('--output', type=str, help='Archivo de salida para el resultado JSON')
    parser.add_argument('--examples', action='store_true', help='Mostrar ejemplos de uso')
    
    args = parser.parse_args()
    
    if args.examples:
        show_examples()
        return
    
    # Si no hay texto, pedir interactivamente
    if not args.text:
        print("\n=== MENTALIA - Procesador de Mentalización ===")
        print("Ingresa tu texto para análisis (termina con una línea vacía):")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        text = "\n".join(lines)
    else:
        text = args.text
    
    # Preparar los datos de entrada
    emotion_indicators = args.emotions.split(",") if args.emotions else []
    nd_markers = args.nd.split(",") if args.nd else []
    
    input_data = {
        'text': text,
        'emotion_indicators': emotion_indicators,
        'nd_markers': nd_markers,
        'context': {'session_type': args.session, 'time': 'n/a'}
    }
    
    # Procesar con el motor de mentalización
    result = process_mentalization_advanced(input_data)
    
    # Guardar o mostrar el resultado
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\nResultado guardado en: {args.output}")
    else:
        print("\n=== RESPUESTA MENTALIZADA ===")
        print_therapeutic_response(result)
    
    print("\nPara ver el resultado completo en formato JSON, usa la opción --output")

def print_therapeutic_response(result):
    """Imprime una versión formateada y legible de la respuesta terapéutica"""
    response = result.get('therapeutic_response', {})
    symbols = result.get('symbolic_mapping', {}).get('active_symbols', [])
    
    print("\n🫂 CONTENCIÓN:")
    print(f"  {response.get('containment', '')}")
    
    print("\n✨ VALIDACIÓN:")
    print(f"  {response.get('validation', '')}")
    
    if response.get('strength_affirmation'):
        print("\n💪 FORTALEZAS:")
        print(f"  {response.get('strength_affirmation', '')}")
    
    print("\n🌈 SÍMBOLOS ACTIVOS:")
    for symbol in symbols:
        print(f"  {symbol}")
    
    print("\n🔄 REFRAME SIMBÓLICO:")
    print(f"  {response.get('reframe', '')}")
    
    print("\n🧰 RECURSO:")
    print(f"  {response.get('resource', '')}")
    
    if response.get('safety_plan'):
        print("\n🛡️ PLAN DE SEGURIDAD:")
        print(f"  {response.get('safety_plan', '')}")
    
    if response.get('progression'):
        print("\n📈 PROGRESIÓN:")
        print(f"  {response.get('progression', '')}")

def show_examples():
    """Muestra ejemplos de uso del script"""
    print("\n=== EJEMPLOS DE USO ===")
    print("\n1. Análisis interactivo básico:")
    print("   python mentalization_app.py")
    
    print("\n2. Análisis con texto directo:")
    print('   python mentalization_app.py --text "Me siento muy ansiosa por la presentación de mañana"')
    
    print("\n3. Análisis con indicadores emocionales y ND:")
    print('   python mentalization_app.py --text "No puedo concentrarme con tanto ruido" --emotions "ansiedad,frustración" --nd "sobrecarga_sensorial"')
    
    print("\n4. Análisis en contexto de crisis:")
    print('   python mentalization_app.py --text "No puedo más, todo es demasiado" --session "crisis"')
    
    print("\n5. Guardar resultado en archivo:")
    print('   python mentalization_app.py --text "..." --output "resultado.json"')

if __name__ == "__main__":
    main()
