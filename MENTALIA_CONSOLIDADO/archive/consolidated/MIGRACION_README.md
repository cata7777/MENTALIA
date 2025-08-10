# 🚀 MIGRACIÓN A ARQUITECTURA CONSOLIDADA MENTALIA

## Pasos de Migración

### 1. Preparación
```bash
cd consolidated
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configuración de Base de Datos
```bash
export DATABASE_URL="postgresql://mentalia:password@localhost/mentalia_unified"
export REDIS_URL="redis://localhost:6379/0"
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 3. Migración de Datos
```bash
python scripts/migrate_data.py
```

### 4. Despliegue con Docker
```bash
docker-compose up -d
```

### 5. Verificación
```bash
./scripts/health_check.sh
```

## URLs de Acceso Post-Migración

- **HIPERFOCO:** http://localhost:5000/hiperfoco
- **Universe:** http://localhost:5000/universe  
- **Chat:** http://localhost:5000/chat
- **API:** http://localhost:5000/api

## Rollback

En caso de problemas, los backups están en: `backups/TIMESTAMP/`
