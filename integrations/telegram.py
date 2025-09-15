# Integração básica com Telegram Bot API
import requests

def send_telegram_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    return requests.post(url, json=payload)
