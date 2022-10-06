from flask import Flask
from flask import render_template
from markupsafe import escape
from requests import Request, Session
import json




app = Flask(__name__)
apikey = 'dce91ae3-620f-4117-a56b-3a4943835a3f'
# https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=328&convert=CHF&CMC_PRO_API_KEY=dce91ae3-620f-4117-a56b-3a4943835a3f
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'id':'328',
  'convert':'CHF'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apikey,
}

session = Session()
session.headers.update(headers)
response = session.get(url, params=parameters)
data = json.loads(response.text)
xmrprice = str(data['data']['328']['quote']['CHF']['price'])[:7]

@app.route('/')
def index():
    return f'XMR Price (CHF): {escape(xmrprice)}'

app.run(host = "0.0.0.0", port = 80)