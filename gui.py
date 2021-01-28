import webview

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
subreddits = ["stocks", "SPACs", "wallstreetbets", "options"]
window = None
#API that we expose to javascript
class Api:
    def __init__(self):
        ''''''

    def startParser(self):
        rparser.getRedditStockData(subreddits, printMe="all",
                           limit=10000, time_filter="day", window=window)
        print("parsing complete")

api = Api()
window = webview.create_window('Meme Stock', './webResources/index.html',js_api=api)
webview.start(debug=True,http_server=False,gui="cef")