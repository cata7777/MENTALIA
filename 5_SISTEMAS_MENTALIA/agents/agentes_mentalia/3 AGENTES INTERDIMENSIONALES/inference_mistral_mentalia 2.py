from llama_cpp import Llama
import json

# Ruta al modelo GGUF
modelo_path = "/Volumes/MENTALIA/MODELS/mistral-7b-instruct-v0.2.Q5_K_M.gguf"

# Cargar el modelo
llm = Llama(model_path=modelo_path, n_ctx=2048)

# Intentar cargar mentalización
try:
    with open("mentalizacion.json", "r") as f:
        mentalizacion = f.read().strip()
except FileNotFoundError:
    mentalizacion = "Eres una inteligencia artificial local diseñada para asistir al usuario con precisión, lógica y sin decoraciones innecesarias. Responde de forma clara, estructurada y útil."

# Entrada del usuario
user_input = input("🧠 Tú: ")

# Generar prompt
prompt = f"SYSTEM: {mentalizacion}\nUSER: {user_input}\nASSISTANT:"

# Ejecutar modelo
output = llm(prompt=prompt, max_tokens=512, stop=["USER:", "ASSISTANT:"])
print("🧠 Blu (IA local):", output["choices"][0]["text"].strip())
