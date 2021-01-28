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


