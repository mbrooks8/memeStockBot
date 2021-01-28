import re
import time
from collections import defaultdict
from datetime import datetime

import praw
import requests
from praw.models import MoreComments

from redditParser import RedditParser
import passwords
import polygonWrapper

# Reddit Parser Examples
reddit = praw.Reddit(
    client_id=passwords.client_id,
    client_secret=passwords.client_secret,
    user_agent=passwords.user_agent
)
rparser = RedditParser(reddit)

subreddits = ["stocks", "SPACs", "wallstreetbets", "options"]
rparser.getRedditStockData(subreddits, printMe="all",
                           limit=10000, time_filter="day")


# Polygon Wrapper Examples
stocks = polygonWrapper.PolygonAPI(passwords.polygonAPIKey)

# Polygon Websocket API example
stocks.websocket_client.start()
stocks.websocket_client.subscribe("T.MSFT", "T.AAPL", "T.AMD", "T.NVDA")
time.sleep(1)
stocks.websocket_client.close_connection()

# Polygon Rest API example
resp = stocks.rest_client.stocks_equities_daily_open_close(
    "AAPL", "2018-03-02")
print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")

temp = stocks.rest_client.reference_market_status()
print(temp.market)
