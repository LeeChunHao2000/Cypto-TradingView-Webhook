import requests

print (requests.post('http://127.0.0.1:5000/data', json={'pair': 'BTC-PERP', 'side': 'buy', 'size': 0.0001}).text)