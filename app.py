import os
import requests
from flask import Flask, request

app = Flask(_name_)

@app.route('/', methods=['POST', 'GET'])
def webhook():
    return "Bot attivo!", 200

if _name_ == '_main_':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
