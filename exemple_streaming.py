#https://pypi.org/project/websocket_client/


# Comme t'es chaud sur le streaming et je comprends, voilà un exemple que je viens d'apprendre, ça récupère le cours de certaines actions et crypto en temps réel.


# avant de lancer le script il faut installer websocket : pip install websocket-client sur le terminal, si çça marche pas je passe t'expliquer le bordel des environnements python

import websocket
import datetime
import json


api_key = 'cl0205hr01qhjei2vk5gcl0205hr01qhjei2vk60'

def on_message(ws, message):
    
    message = json.loads(message)
    data = message['data']
    print(json.dumps(data, indent=4)) # added line to print parsed JSON data


def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"GOOGL"}')
    ws.send('{"type":"subscribe","symbol":"MSFT"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=" + api_key ,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
