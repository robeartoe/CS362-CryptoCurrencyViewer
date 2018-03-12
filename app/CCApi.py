import requests
from operator import itemgetter

def getCoinList():
    r = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')
    someDict = r.json()
    someDict = someDict["Data"]
    return someDict

def getPrices(currentPage):
    payload = {"start": (currentPage-1)*50,"limit":50}
    r = requests.get('https://api.coinmarketcap.com/v1/ticker',params=payload)
    return r.json() #Returns a list of dicts.

def rateLimitCC():
    r = requests.get('https://min-api.cryptocompare.com/stats/rate/hour/limit')
    print(r.json())

# To be used in the detailed coin page.
def getFullInfo(coin):
    payload = {"fsyms":coin,"tsyms":"USD,BTC","extraParams":"studentCurrencyWebViewer"}
    r = requests.get('https://min-api.cryptocompare.com/data/pricemultifull')
    return r.json()

# rateLimit()
# test = getCoinList()
# getPrices(1,test)
