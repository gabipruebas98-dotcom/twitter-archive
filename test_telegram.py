
import os
import requests

token = os.environ["TG_TOKEN"]
chat_id = os.environ["TG_CHAT"]

response = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    data={
        "chat_id": chat_id,
        "text": "✅ Prueba exitosa: el bot de Telegram está conectado al proyecto twitter-archive."
    },
    timeout=20,
)

response.raise_for_status()
print("Mensaje enviado correctamente a Telegram.")
