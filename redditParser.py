import requests
import re
import praw
from collections import defaultdict
from collections import Counter
from praw.models import MoreComments
import time
from datetime import datetime


class RedditParser:
    def __init__(self, reddit):
        self.tickerDict = self.getTickerDict()
        self.reddit = reddit

    def getTickerDict(self):
        tickerDict = {}
        with open("tickerSymbols.csv", "r") as f:
            for line in f:
                tickerDict[line.replace("\n", "")] = 0

        with open("NYSE.txt", "r") as f:
            for line in f:
                tickerDict[line.split("	")[0]] = 0
        return tickerDict

    def getTickerSymbols(self, stuff, tickerDict):
        tickers = re.findall(r"\b[A-Z][A-Z]+\b", stuff)
        tempList = []
        for ticker in tickers:
            if ticker in tickerDict:
                tempList.append(ticker)
        return tempList

    def removeBadSymbols(self, myDict, filter=0):
        tempList = []
        for thing in myDict:
            if myDict[thing] < filter:
                tempList.append(thing)

        badSymbols = ["CEO", "DD", "FOR", "DO", "HAS", "TO", "RSI", "ETF", "EV", "USA", "EDIT", "AI", "AM", "PM",
                      "TIME", "HI", "PPP", "LINK", "EOD", "ARE", "IM", "ALL", "IF", "AT",
                      "CA", "IT", "IRS", "ROTH", "MOST", "HUGE", "MY", "HERO", "MORE", "FULL", "IMO", "ONE"]
        for thing in tempList + badSymbols:
            myDict.pop(thing, None)
        return myDict

    def getTickerSymbolsFromPost(self, submission):
        tickerSymbols = []
        tickerSymbols += self.getTickerSymbols(
            submission.title, self.tickerDict)
        # Post Text
        tickerSymbols += self.getTickerSymbols(
            submission.selftext, self.tickerDict)
        # Post comments
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            tickerSymbols += self.getTickerSymbols(
                top_level_comment.body, self.tickerDict)
        return tickerSymbols

    def getRedditStockData(self, subreddit, printMe="all", minOccurances=2, time_filter="week", searchQuery="DD", limit=100, window = None):
        window.evaluate_js("setProgressBar('1')")
        for sub in subreddit:
            tickers = defaultdict(int)
            if printMe:
                print("Summary for: %s" % sub)
                print("Search Query:", searchQuery)
                print("Minimum Occurances:", minOccurances)
                print("Time Filter:", time_filter)
            if(window):
                window.evaluate_js("setProgressBar('10')")
            for submission in self.reddit.subreddit(sub).search(searchQuery, time_filter=time_filter):
                if "?" not in submission.title and len(submission.selftext) > 200:
                    if printMe == "all":
                        try:
                            print("Title:", submission.title,
                                  datetime.fromtimestamp(submission.created))
                            print("Length:", len(submission.selftext))
                            print("Link:", submission.url)
                        except Exception as e:
                            print(e)
                    symbols = self.getTickerSymbolsFromPost(submission)
                    if printMe == "all":
                        print("Symbols in this post:", symbols, "\n")
                    for ticker in symbols:
                        tickers[ticker] += 1
            if(window):
                window.evaluate_js("setProgressBar('50')")
            self.removeBadSymbols(tickers, filter=minOccurances)
            if(window):
                window.evaluate_js("setProgressBar('90')")
            if printMe:
                print("Ticker summary for: %s" % sub)
                print(Counter(tickers).most_common(limit))
                # print({k: v for k, v in sorted(tickers.items(), key=lambda item: item[1], reverse=True)})
                print("\n")
            if(window):
                window.evaluate_js("setProgressBar('100')")
