# Integração básica com Twilio WhatsApp
from twilio.rest import Client

def send_whatsapp_message(account_sid, auth_token, from_, to, body):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body,
        from_=from_,
        to=to
    )
    return message.sid
