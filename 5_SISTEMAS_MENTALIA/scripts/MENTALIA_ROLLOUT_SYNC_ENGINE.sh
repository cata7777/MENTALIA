
#!/bin/bash

echo "==============================="
echo "🧠 MENTALIA ROLLOUT SYNC ENGINE"
echo "==============================="

DROPBOX_DIR="$HOME/Library/CloudStorage/Dropbox"
LOG_FILE="./MENTALIA_SYNC_LOG.txt"
MEMORY_DIR="./mentalia_memory_core"

mkdir -p "$MEMORY_DIR"
touch "$LOG_FILE"

find "$DROPBOX_DIR" -type f \( -iname "*.zip" -o -iname "*.md" -o -iname "*.txt" -o -iname "*.json" -o -iname "*.py" -o -iname "*.js" \) | while read -r file; do
  TARGET="$MEMORY_DIR/$(basename "$file")"
  if [ ! -f "$TARGET" ]; then
    cp "$file" "$TARGET"
    echo "🧠 INTEGRADO: $(basename "$file")" >> "$LOG_FILE"
  fi
done

echo "✅ ROLLOUT MEMORIA ACTUALIZADA. Ver: $MEMORY_DIR"
