import time
from polygon import WebSocketClient, STOCKS_CLUSTER, RESTClient
import datetime
import requests

class PolygonAPI:
    def __init__(self, key):
        self.key = key
        self.websocket_client = WebSocketClient(
            STOCKS_CLUSTER, key, self.my_custom_process_message)
        self.rest_client = RESTClient(key)

    def websocket_start(self):
        self.websocket_client.run_async()

    def my_custom_process_message(self, message):
        print("this is my custom message processing", message)

    def my_custom_error_handler(self, ws, error):
        print("this is my custom error handler", error)

    def my_custom_close_handler(self, ws):
        print("this is my custom close handler")
    
    def ts_to_datetime(self, ts) -> str:
        return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')
    
    def check_real_stock(self, symbol):
        try:
            self.rest_client.reference_ticker_details(symbol)
            return True
        except requests.exceptions.HTTPError:
            return False

    
