import os
import json
import requests
from typing import List, Optional

CHILECOMPRA_API_URL = "https://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json"


def buscar_licitaciones(
    keywords: Optional[List[str]] = None,
    fecha_desde: Optional[str] = None,
    fecha_hasta: Optional[str] = None,
    estado: Optional[str] = None,
    api_key: Optional[str] = None,
    pagina: int = 1,
) -> List[dict]:
    """Consulta licitaciones desde la API de ChileCompra.

    Parameters
    ----------
    keywords : list[str], optional
        Palabras clave para filtrar por nombre o descripci\u00f3n.
    fecha_desde : str, optional
        Fecha de publicaci\u00f3n inicial en formato YYYY-MM-DD.
    fecha_hasta : str, optional
        Fecha de publicaci\u00f3n final en formato YYYY-MM-DD.
    estado : str, optional
        Estado de la licitaci\u00f3n ("publicada", "cerrada", etc).
    api_key : str, optional
        Ticket de autenticaci\u00f3n de la API.
    pagina : int
        N\u00famero de p\u00e1gina a consultar.

    Returns
    -------
    list[dict]
        Listado de licitaciones filtradas.
    """

    params = {"pagina": pagina}
    if api_key:
        params["ticket"] = api_key
    if estado:
        params["estado"] = estado
    if fecha_desde:
        params["fecha"] = fecha_desde
    if fecha_hasta:
        params["fechaHasta"] = fecha_hasta

    response = requests.get(CHILECOMPRA_API_URL, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    licitaciones = data.get("Listado", [])

    if keywords:
        lowered = [k.lower() for k in keywords]
        filtered = []
        for lic in licitaciones:
            texto = f"{lic.get('Nombre', '')} {lic.get('Descripcion', '')}".lower()
            if any(k in texto for k in lowered):
                filtered.append(lic)
        licitaciones = filtered

    return licitaciones


def guardar_resultados(ruta: str, data: List[dict]) -> None:
    """Guarda resultados en archivo JSON."""
    with open(ruta, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
