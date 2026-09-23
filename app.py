import os
from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "Bot attivo!", 200

if _name_ == '_main_':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
