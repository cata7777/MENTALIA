# ☁️ Deploy MENTALIA on RunPod

Este directorio contiene la configuración necesaria para desplegar el ecosistema completo de **MENTALIA** en [RunPod](https://www.runpod.io/) o en cualquier host con Docker.

## 🔧 Prerrequisitos
- Docker y docker-compose instalados
- Variables de entorno configuradas:

```bash
export OPENAI_API_KEY="..."
export OPENAI_API_BASE="..."   # opcional si usas endpoint personalizado
export DB_PASSWORD="..."
export SECRET_KEY="..."
export JWT_SECRET_KEY="..."
export MINSAL_API_KEY="..."     # para módulos clínicos
export HL7_ENDPOINT="..."
export FONASA_API_KEY="..."
export LEGAL_API_KEY="..."      # para despacho legal
export CHILECOMPRA_API="..."
export SENCE_API_KEY="..."      # para formación laboral
export OTEC_CERT="..."
export ND_PROFILES_API="..."    # perfiles neurodivergentes
export GRAFANA_PASSWORD="..."   # acceso al monitoreo
```

## 🚀 Inicio rápido

```bash
cd RUNPOD_DEPLOY
./start_mentalia_runpod.sh
```

El script construye las imágenes, ejecuta migraciones y levanta todos los servicios definidos en [`docker-compose.yml`](docker-compose.yml).

## 🌐 URLs de acceso

- **MENTALIA UNIVERSE:** http://localhost:5000
- **CHAT MENTALIA:** http://localhost:5001
- **HIPERFOCO.COM:** http://localhost:5002
- **Agendas Clínicas:** http://localhost:5003
- **Despacho Legal:** http://localhost:5004
- **Formación Laboral:** http://localhost:5005
- **Mental-IA ND:** http://localhost:5006
- **API Gateway:** http://localhost:5100
- **Monitoreo (Grafana):** http://localhost:3000

## 🧹 Apagado

```bash
docker-compose down --remove-orphans
```

Los logs de inicio se almacenan en `logs/` y el monitoreo continuo se escribe en `logs/monitoring.log`.

