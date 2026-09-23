import os
import requests
from flask import Flask, request

app = Flask(__name__)

# Inserisci qui sotto i tuoi dati di Telegram
TELEGRAM_BOT_TOKEN = "8666558779:AAFYe9nRQZ2DEbQBvjnAtTLapQg3to57A2A"
TELEGRAM_CHAT_ID = "1266021878"

@app.route('/')
def home():
    return "Bot Telegram per TradingView attivo!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    # Riceve i dati inviati da TradingView (in formato testo o JSON)
    data = request.get_data(as_text=True)
    
    if data:
        # Costruisce il messaggio da mandare su Telegram
        url = f"https://api.telegram.org/bot{8666558779:AAFYe9nRQZ2DEbQBvjnAtTLapQg3to57A2A}/sendMessage"
        payload = {
            "chat_id": "1266021878",
            "text": f"🚨 Segnale TradingView:\n{data}",
            "parse_mode": "HTML"
        }
        requests.post(url, json=payload)
        return "Messaggio inviato a Telegram", 200
    
    return "Nessun dato ricevuto", 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
