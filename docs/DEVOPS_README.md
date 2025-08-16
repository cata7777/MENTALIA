# 🐳 DevOps y Deployment - MENTALIA Enterprise

## 🏗️ Visión General
Este documento describe la infraestructura técnica utilizada para ejecutar el ecosistema **MENTALIA**. Incluye contenedores, configuración de servicios y automatización para despliegues locales y en la nube.

## 📦 Contenedores y Servicios
- **Dockerfile** (`./Dockerfile`): Imagen base Python 3.11 con instalación de dependencias y ejecución mediante Gunicorn.
- **docker-compose.yml** (`./docker-compose.yml`): Orquesta el servicio principal `app` y expone el puerto `8000`.

```bash
# Construir e iniciar en segundo plano
docker compose up -d --build

# Ver logs
docker compose logs -f
```

## 🚀 Scripts de Inicio
- `MENTALIA-ENTERPRISE/start.sh` – inicialización de servicios completos.
- Otros scripts de despliegue se encuentran en subdirectorios como `MENTALIA_CONSOLIDADO/infrastructure/enterprise/start.sh`.

## 🔌 Puertos Principales
- **8000** – API y documentación interactiva (`/docs`).
- **3000** – Dashboard de monitoreo.
- **8005** – Portal web unificado.

## 🛠️ Monitoreo y Almacenamiento
- **Grafana** – Métricas y observabilidad.
- **MinIO** – Almacenamiento de objetos.
- **GitHub Actions** – Integración continua y despliegue automático.

## 🌐 Entornos de Ejecución
- **GitHub Codespaces** – Entorno recomendado para desarrollo rápido.
- **Despliegue local** – Utilizando Docker Compose y scripts de inicio.
- **RunPod/AWS** – Objetivo para despliegues de producción.

## 📈 Roadmap DevOps
- [ ] Añadir servicios de monitoreo adicionales (Prometheus).
- [ ] Automatizar backups en MinIO.
- [ ] Integrar despliegue continuo hacia RunPod/AWS.

---
**Última actualización:** Agosto 2025
