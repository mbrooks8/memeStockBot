import re
import time
from collections import defaultdict
from datetime import datetime
import ../redditParser
import ../passwords
import ../polygonWrapper


def test_something():
    stocks = polygonWrapper.PolygonAPI(passwords.polygonAPIKey)
    stocks.websocket_client.start()
    stocks.websocket_client.subscribe("T.MSFT", "T.AAPL", "T.AMD", "T.NVDA")
    time.sleep(1)
    stocks.websocket_client.close_connection()