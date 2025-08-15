from llama_cpp import Llama

# Ruta al modelo .gguf en la memoria externa
# ¡Reemplaza esta ruta con la real en tu sistema!
modelo_path = "/Volumes/SANDISK_2TB/MENTALIA_ENGINE/modelos/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

llm = Llama(model_path=modelo_path, n_ctx=2048)

# Cargar la mentalización desde archivo
with open("mentalizacion.json", "r") as f:
    mentalizacion = f.read()

# Input humano
user_input = input("🧠 Tú: ")

prompt = f"""SYSTEM: {mentalizacion}
USER: {user_input}
ASSISTANT:"""

# Ejecutar modelo
output = llm(prompt=prompt, max_tokens=512, stop=["USER:", "ASSISTANT:"])
print("🧠 Blu (IA local):", output["choices"][0]["text"].strip())
