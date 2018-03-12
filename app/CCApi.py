import requests
from operator import itemgetter

def getCoinList():
    r = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')
    someDict = r.json()
    someDict = someDict["Data"]

    return someDict

    # someDict = list(someDict['Data'].values()) #A list of dicts.
    # sortedDict = sorted(someDict,key=itemgetter("SortOrder")) #This is now a list of dicts. From most to least popular.
    # print(sortedDict)
    # print(type(someDict))


def getPrices(currentPage,CoinList):
    CoinList = list(CoinList.values()) #A list of dicts.
    # prices = []
    #
    # for index in range((currentPage-1)*40,currentPage*40):
    #     prices.append(CoinList[index]["Symbol"])
    #
    # prices = ','.join(prices)
    #
    # payload = {"fsyms":prices,"tsyms":"USD,BTC","extraParams":"studentCurrencyWebViewer"}
    # r = requests.get('https://min-api.cryptocompare.com/data/pricemulti',params = payload)
    # # print(r.status_code)
    # # print(r.json())

    payload = {"start":,"limit":50}
    r = requests.get('https://api.coinmarketcap.com/ticker')
    

    return r.json()

def rateLimit():
    r = requests.get('https://min-api.cryptocompare.com/stats/rate/hour/limit')
    print(r.json())

# This function will make several API calls to get info for this particular coin.
# To be used in the detailed coin page.
def getFullInfo(coin):
    payload = {"fsyms":coin,"tsyms":"USD,BTC","extraParams":"studentCurrencyWebViewer"}
    r = requests.get('https://min-api.cryptocompare.com/data/pricemultifull')
    return r.json()

# rateLimit()
# test = getCoinList()
# getPrices(1,test)
