from flask import Flask
from flask import render_template

app = Flask(__name__)
xmr_api_url = 'https://api.coinmarketcap.com/v1/ticker/monero/'


@app.route('/')
def index():
    return render_template('index.html', name=index)

app.run(host = "0.0.0.0", port = 80)