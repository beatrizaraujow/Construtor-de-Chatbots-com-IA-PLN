# Integração básica com Slack API
import requests

def send_slack_message(token, channel, text):
    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel, "text": text}
    return requests.post(url, headers=headers, json=payload)
