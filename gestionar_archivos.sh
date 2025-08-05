#!/bin/bash
# 🚀 SCRIPT PARA GESTIONAR ARCHIVOS CONSOLIDADOS MENTALIA

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m' 
NC='\033[0m'

echo -e "${BLUE}🌌 MENTALIA - Gestión de Archivos Consolidados${NC}"
echo "=============================================="

# 1. Mostrar estructura actual
echo -e "${GREEN}📁 Estructura actual:${NC}"
ls -la consolidated/

echo ""

# 2. Crear archivo ZIP descargable
echo -e "${GREEN}📦 Creando archivo descargable...${NC}"
zip -r "MENTALIA_CONSOLIDATED_$(date +%Y%m%d).zip" consolidated/
echo "✅ Archivo creado: MENTALIA_CONSOLIDATED_$(date +%Y%m%d).zip"

echo ""

# 3. Mostrar estado Git
echo -e "${GREEN}📋 Estado Git:${NC}"
git status --porcelain

echo ""

# 4. Opciones de backup
echo -e "${GREEN}💾 Opciones de respaldo:${NC}"
echo "1. Backup en Escritorio:"
echo "   cp -r consolidated/ ~/Desktop/MENTALIA_CONSOLIDATED/"
echo ""
echo "2. Subir a GitHub:"
echo "   git add ."
echo "   git commit -m '🚀 Consolidación MENTALIA 2025'"
echo "   git push origin main"
echo ""
echo "3. Crear release:"
echo "   git tag v2025.1.0"
echo "   git push origin v2025.1.0"

echo ""
echo -e "${GREEN}🎉 ¡Tu ecosistema MENTALIA está consolidado y listo!${NC}"
