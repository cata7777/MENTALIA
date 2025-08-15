#!/bin/bash
echo "🚀 Iniciando MENTALIA Enterprise..."
cd deployment
docker-compose up -d
echo "✅ Listo en:"
echo "  - Web: http://localhost:8005"
echo "  - Grafana: http://localhost:3000 (admin/admin123)" -la
