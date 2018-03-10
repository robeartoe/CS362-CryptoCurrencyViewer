import requests

# def getPrices():

def getCoinList():
    r = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
    # print(r.json())
    return r.json()

def rateLimit():
    r = requests.get('https://min-api.cryptocompare.com/stats/rate/hour/limit')
    print(r.json())

getCoinList()
