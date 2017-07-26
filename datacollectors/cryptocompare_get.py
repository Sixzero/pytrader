import requests
import json
from pprint import pprint
import datetime
    # datetime.datetime.fromtimestamp(1452672000)

r = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
coins = r.json()
# for coin in not coins['Data']:

pprint(coins)
# coinList = coins['Data']
coinList = ['BTC', 'ETH', 'NMR', 'VERI', 'LTC', 'BCN', 'DGB', 'DGB', 'DGB', 'OMG', 'PAY']
# pprint(coins)
counter = 0
for coin in coinList :
    # pprint(r.json())
    # get_url = f'https://min-api.cryptocompare.com/data/histohour?fsym={coin}&tsym=USD&limit=2000&aggregate=1&extraParams=your_app_name'
    get_url = f'https://min-api.cryptocompare.com/data/histohour?fsym={coin}&tsym=USD&limit=2000&aggregate=1&extraParams=my_crypto_bot'
    r = requests.get(get_url).json()

    counter += 1
    print(f"{counter}/{len(coinList )} Response: {r['Response']} Url: {get_url}")

    # print(r.json())
    with open(f'coins_hour_v2/{coin}.txt', 'w') as outfile:
        json.dump(r, outfile)

