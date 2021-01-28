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

reddit = praw.Reddit(
    client_id=passwords.client_id,
    client_secret=passwords.client_secret,
    user_agent=passwords.user_agent
)
rparser = RedditParser(reddit)

# subreddits = ["stocks", "SPACs", "wallstreetbets", "options"]
# rparser.getRedditStockData(subreddits, printMe="all",
#                            limit=10000, time_filter="day")


stocks = polygonWrapper.PolygonAPI(passwords.polygonAPIKey)

stocks.websocket_client.subscribe("T.MSFT", "T.AAPL", "T.AMD", "T.NVDA")
time.sleep(1)
stocks.websocket_client.close_connection()
