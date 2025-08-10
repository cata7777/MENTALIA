# Despliegue Mentalia Server

## Requisitos
- Docker y docker-compose instalados
- Puerto 80 disponible (la API se sirve internamente en el puerto 5000)

## Uso
1. Clona este entorno al servidor
2. Coloca los archivos de Mentalia en esta carpeta
3. Ejecuta:

```bash
chmod +x start_all.sh
./start_all.sh
```

4. Accede a:
- `http://<ip-servidor>/` para dashboard
- `http://<ip-servidor>/api/chat` para API mentalia
