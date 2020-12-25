'''
Request Format：
http://x.x.x.x:xxxx/data?pair=BTC-PERP&side=buy&size=0.001

Parameters：
:param pair: the trading pair to query
:param side: the trading side, should only be buy or sell
:param size: the amount of the order for the trading pair
'''
import json

from flask import Flask, request, abort

from FTX.client import Client

from config import *

# Global Variables
app = Flask(__name__)
client = Client(API_KEY, API_SECRET) # Subaccount

@app.route("/")
def home():
    return '正常運作'

@app.route("/data", methods=['POST'])
def trade():
    if request.method == 'POST':
        # Convert the string data from tradingview into a python dict
        data = json.loads(request.get_data(as_text=True))

        # Trade
        response = client.set_private_create_order(data['pair'], data['side'], None, 'market', data['size'])
        # print (response)
        
        return str(response), 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()