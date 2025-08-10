
#!/bin/bash

echo "==============================="
echo "🪞 MENTALIA REFLEX SYSTEM"
echo "==============================="

DROPBOX_DIR="$HOME/Library/CloudStorage/Dropbox"
MEMORY_DIR="./mentalia_memory_core"
REFLEX_LOG="./MENTALIA_REFLEX_PANEL.txt"

mkdir -p "$MEMORY_DIR"
touch "$REFLEX_LOG"

echo "📡 ESCANEANDO DROPBOX COMPLETO..." > "$REFLEX_LOG"
echo "" >> "$REFLEX_LOG"

find "$DROPBOX_DIR" -type f \( -iname "*.zip" -o -iname "*.md" -o -iname "*.txt" -o -iname "*.json" -o -iname "*.py" -o -iname "*.js" \) | while read -r file; do
  BASENAME=$(basename "$file")
  TARGET="$MEMORY_DIR/$BASENAME"

  if [ ! -f "$TARGET" ]; then
    cp "$file" "$TARGET"
    echo "📥 NUEVO ARCHIVO DETECTADO: $BASENAME" >> "$REFLEX_LOG"

    # Clasificadores simples
    if [[ "$BASENAME" == *"README"* ]]; then echo "   → 📘 Contiene README" >> "$REFLEX_LOG"; fi
    if [[ "$BASENAME" == *".zip" ]]; then echo "   → 📦 Archivo ZIP" >> "$REFLEX_LOG"; fi
    if [[ "$BASENAME" == *".py" ]]; then echo "   → ⚙️ Script Python" >> "$REFLEX_LOG"; fi
    if [[ "$BASENAME" == *".js" ]]; then echo "   → 🛠 Archivo JS" >> "$REFLEX_LOG"; fi
    if [[ "$BASENAME" == *".json" ]]; then echo "   → 🧩 Configuración o datos estructurados" >> "$REFLEX_LOG"; fi
    echo "" >> "$REFLEX_LOG"
  fi
done

echo "✅ MEMORIA REFLEJADA. Ver: $MEMORY_DIR"
echo "📋 LOG DE CAMBIOS: $REFLEX_LOG"
