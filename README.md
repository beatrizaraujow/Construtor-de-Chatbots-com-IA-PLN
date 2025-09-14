# Construtor de Chatbots com IA/PLN

Descrição
---------
Este projeto é um protótipo de um "Construtor de Chatbots" que permite:
- Criar e editar intents (nome, exemplos de utterances, respostas).
- Treinar um classificador NLU simples (TF-IDF + LogisticRegression).
- Testar conversas via API e via interface web.
- Exemplo de integração com Telegram (polling) e instruções para Twilio/WhatsApp.

Estrutura do projeto
--------------------
- app/
  - main.py                -> API (FastAPI) para CRUD de intents, treino e chat
  - model_trainer.py       -> Treinamento do modelo NLU
  - nlu.py                 -> Envolve carregamento do modelo e predição
- data/
  - intents.json           -> Intents iniciais de exemplo
- frontend/
  - index.html
  - app.js
  - style.css
- bots/
  - telegram_bot.py        -> Exemplo de integração com Telegram (usa backend)
- scripts/
  - package.sh             -> Script para gerar chatbot_builder.zip
- requirements.txt
- README.md
- LICENSE

Requisitos
----------
- Python 3.8+
- Node.js não é necessário (frontend é estático)
- Para integração com Telegram: token do bot
- Para WhatsApp (Twilio): conta Twilio e configuração separada (instruções abaixo)

Instalação rápida
-----------------
1. Crie um ambiente virtual e instale dependências:
   python -m venv venv
   source venv/bin/activate  # linux/mac
   venv\Scripts\activate     # windows

   pip install -r requirements.txt

2. Inicie a API:
   uvicorn app.main:app --reload --port 8000

3. Abra o frontend:
   - Abra `frontend/index.html` no navegador (ele interage com `http://localhost:8000`).

Usos principais
---------------
- Gerenciar intents:
  - GET /api/intents
  - POST /api/intents  (enviar JSON com array de intents para substituir)
- Treinar:
  - POST /api/train
- Chat:
  - POST /api/chat  (payload: {"text":"..."}), retorna resposta do chatbot.

Treino e modelo
---------------
O modelo é um pipeline TF-IDF + LogisticRegression. Dados de treino ficam em `data/intents.json`.
Ao treinar, o arquivo `app/model.joblib` será criado.

Telegram
--------
1. Crie um bot no BotFather e obtenha o TOKEN.
2. Defina a variável de ambiente TELEGRAM_TOKEN ou altere diretamente no arquivo `bots/telegram_bot.py`.
3. Execute:
   python bots/telegram_bot.py
O script faz polling e encaminha mensagens ao backend `http://localhost:8000/api/chat`.

Empacotar em ZIP
----------------
- Torne o script executável e rode:
  chmod +x scripts/package.sh
  ./scripts/package.sh
Isto criará `chatbot_builder.zip` contendo todo o projeto.

Observações e próximos passos
----------------------------
- Este protótipo usa um NLU simples; para produção recomenda-se Rasa, Dialogflow ou modelos transformer (BERT). 
- Para suporte por voz, integre Web Speech API (frontend) e engines TTS (gTTS/pyttsx3) no backend.
- Integrações: Slack SDK, Twilio (WhatsApp) e webhook-based bots podem ser adicionados facilmente.
