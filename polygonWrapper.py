import time
from polygon import WebSocketClient, STOCKS_CLUSTER, RESTClient
import datetime

class PolygonAPI:
    def __init__(self, key):
        self.key = key
        self.websocket_client = WebSocketClient(
            STOCKS_CLUSTER, key, self.my_custom_process_message)
        self.websocket_client.run_async()
        self.rest_client = RESTClient(key)

    def my_custom_process_message(self, message):
        print("this is my custom message processing", message)

    def my_custom_error_handler(self, ws, error):
        print("this is my custom error handler", error)

    def my_custom_close_handler(self, ws):
        print("this is my custom close handler")
    
    def ts_to_datetime(self, ts) -> str:
        return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')

    
