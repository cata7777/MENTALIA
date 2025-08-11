# ChileCompra Scraper

Este m\u00f3dulo permite consultar autom\u00e1ticamente licitaciones del portal [mercadopublico.cl](https://www.mercadopublico.cl) mediante una peque\u00f1a API en Flask.

## Uso con Docker

1. Defina la variable de entorno `CHILECOMPRA_API_KEY` con el ticket de acceso provisto por ChileCompra.
2. Construya la imagen y levante el servicio:

```bash
docker-compose up --build
```

El contenedor expone el puerto `8000`.

### Endpoint `/api/chilecompra`

Realice peticiones GET con los siguientes par\u00e1metros opcionales:

- `keywords`: palabras separadas por comas para filtrar por nombre o descripci\u00f3n.
- `fecha_desde`: fecha inicial `YYYY-MM-DD`.
- `fecha_hasta`: fecha final `YYYY-MM-DD`.
- `estado`: estado de la licitaci\u00f3n (ej. `publicada` o `cerrada`).
- `pagina`: n\u00famero de p\u00e1gina seg\u00fan la API.
- `save`: si vale `true`, guarda los resultados en `chilecompra_results.json`.
- `file`: nombre del archivo donde guardar (opcional).

Ejemplo:

```
http://localhost:8000/api/chilecompra?keywords=inteligencia+artificial,salud+mental&estado=publicada&save=true
```

El resultado es un JSON con el listado de licitaciones encontradas.

## Ejecuci\u00f3n local sin Docker

Instale dependencias:

```bash
pip install -r requirements.txt
```

Luego ejecute:

```bash
python -m backend.app
```

El servidor qued\u00f3 disponible en `http://localhost:8000`.
