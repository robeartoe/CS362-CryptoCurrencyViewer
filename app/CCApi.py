import requests
from operator import itemgetter

def getCoinList():
    r = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')
    someDict = r.json()
    someDict = someDict["Data"]

    # someDict = list(someDict['Data'].values()) #A list of dicts.
    # sortedDict = sorted(someDict,key=itemgetter("SortOrder")) #This is now a list of dicts. From most to least popular.
    # print(sortedDict)
    # print(type(someDict))

    return someDict

def getPrices(currentPage,CoinList):
    CoinList = list(CoinList.values()) #A list of dicts.
    prices = []

    for index in range((currentPage-1)*40,currentPage*40):
        prices.append(CoinList[index]["Symbol"])

    prices = ','.join(prices)
    # print(prices)

    payload = {"fsyms":prices,"tsyms":"USD,BTC","extraParams":"studentCurrencyWebViewer"}
    r = requests.get('https://min-api.cryptocompare.com/data/pricemulti',params = payload)
    # print(r.status_code)
    # print(r.json())
    return r.json()

def rateLimit():
    r = requests.get('https://min-api.cryptocompare.com/stats/rate/hour/limit')
    print(r.json())

# This function will make several API calls to get info for this particular coin.
# To be used in the detailed coin page.
def getFullInfo(coin):
    pass

# rateLimit()
test = getCoinList()
getPrices(1,test)

#               <!-- <p>{{currencyPrices[currencies[item].Symbol]["USD"]}}</p> -->
