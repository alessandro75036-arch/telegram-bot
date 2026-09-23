import requests
from flask import Flask, request

app = Flask(_name_)

TOKEN = "8997349228:AAGJ-nw4AVWn01UFjmLWYUvv_OxogQopjYE"
CHAT_ID = "1265021878"


@app.route("/webhook", methods=["POST"])
def webhook():
  data = request.json
  if data:
    message = data.get("text", "Segnale di trading da TradingView")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)
    return "OK", 200
  return "Bad Request", 400


if _name_ == "_main_":
  app.run(host="0.0.0.0", port=5000)
