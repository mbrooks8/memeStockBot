# memeStockBot
Lets get those tendies.

# Setup
```
pip install -r requirements.txt
```
## Passwords.py file should look like this:
 client_id = ""<br />
 client_secret = ""<br />
 user_agent = ""<br />
 polygonAPIKey = ""

## Reddit
 Documentation:<br />
 PRAW: https://praw.readthedocs.io/en/latest/code_overview/praw_models.html
 
### To get reddit passwords file info:
 - Log into your reddit account
 - Go to https://www.reddit.com/prefs/apps/
 - Create Another App
 - Set the name to be anything
 - set the type to be script
 - Put anything you want in description / about url / redirect uri
 - save the "personal use script" as client_id into passwords.py
 - save the "secret" as client_secret into passwords.py
 - Set user_agent to whatever you want

## Polygon
 Documentation: <br />
 Rest API: https://polygon.io/docs<br />
 Websocket: https://polygon.io/docs/websockets/getting-started

### To get the polygon api key:
- Sign up with a live account for https://alpaca.markets/, you need to be a US citizen.
- Once you log in, on the right click View under Your API Keys
- Copy the API Key ID as your polygon api key
