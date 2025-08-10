from flask import Flask, request, jsonify
from .chilecompra_scraper import buscar_licitaciones, guardar_resultados
import os

app = Flask(__name__)


@app.route("/api/chilecompra", methods=["GET"])
def chilecompra_endpoint():
    keywords_param = request.args.get("keywords")
    keywords = [k.strip() for k in keywords_param.split(",") if k.strip()] if keywords_param else None

    fecha_desde = request.args.get("fecha_desde")
    fecha_hasta = request.args.get("fecha_hasta")
    estado = request.args.get("estado")
    pagina = int(request.args.get("pagina", 1))

    api_key = os.getenv("CHILECOMPRA_API_KEY")

    try:
        licitaciones = buscar_licitaciones(
            keywords=keywords,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
            estado=estado,
            api_key=api_key,
            pagina=pagina,
        )
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

    if request.args.get("save") == "true":
        ruta = request.args.get("file", "chilecompra_results.json")
        guardar_resultados(ruta, licitaciones)

    return jsonify({"results": licitaciones})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
