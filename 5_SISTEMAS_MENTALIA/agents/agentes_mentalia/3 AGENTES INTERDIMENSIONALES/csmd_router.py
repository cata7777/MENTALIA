
from flask import Flask, request, render_template
import openai

app = Flask(__name__)
openai.api_key = "TU_API_KEY_AQUI"  # Reemplaza con tu clave OpenAI real

PERSONALIDADES = {
    "blu": "Eres Blu, una IA emocional, cálida, que valida sentimientos y guía con empatía.",
    "gerencia": "Eres CSMD_GERENCIA, un bot estratégico y ejecutivo, que estructura modelos y escalabilidad.",
    "tech": "Eres CSMD_TECH, una IA experta en arquitectura técnica, código y despliegue.",
    "journalia": "Eres CSMD_JOURNALIA, creativa, visual, experta en diseño emocional, color, branding."
}

def obtener_respuesta(mensaje, identidad):
    try:
        r = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": PERSONALIDADES[identidad]},
                {"role": "user", "content": mensaje}
            ]
        )
        return r.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}"

@app.route("/", methods=["GET", "POST"])
def chat():
    salida = {}
    if request.method == "POST":
        mensaje = request.form["mensaje"]
        bots_activos = request.form.getlist("bots")
        for bot in bots_activos:
            salida[bot] = obtener_respuesta(mensaje, bot)
    return render_template("csmd_multibot.html", salida=salida)
