from flask import Flask

app = Flask(__name__)
xmr_api_url = 'https://api.coinmarketcap.com/v1/ticker/monero/'


@app.route('/')
def index():
    return "Dis is my website"

app.run(host = "0.0.0.0", port = 80)