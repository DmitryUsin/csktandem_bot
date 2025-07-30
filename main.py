import os
from flask import Flask, request
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    # Простая логика: бот отвечает на /start
    if text == "/start":
        send_message(chat_id, "Привет! Я обучающий бот. Готов к работе.")
    else:
        send_message(chat_id, "Напиши /start, чтобы начать.")

    return {"ok": True}

def send_message(chat_id, text):
    requests.post(URL, json={
        "chat_id": chat_id,
        "text": text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
