from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # Aqui você integraria com Rasa/Dialogflow para PLN
    response = {'reply': 'Resposta simulada do chatbot.'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
