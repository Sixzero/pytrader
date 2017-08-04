import ccxt
import os
import json
from pprint import pprint

with open('keys.json') as data_file:
    keys = json.load(data_file)
# pprint(keys)


API_KEY = keys.get('POLONIEX_API_KEY', None)
print(API_KEY)
API_SECRET = keys.get('POLONIEX_API_SECRET', None)
print(API_SECRET)

hitbtc = ccxt.hitbtc ({ 'verbose': True })
bitmex = ccxt.bitmex ()
huobi  = ccxt.poloniex ({
    'apiKey': API_KEY,
    'secret': API_SECRET,}
)
# exmo   = ccxt.exmo ({
#     'apiKey': 'YOUR_PUBLIC_API_KEY',
#     'secret': 'YOUR_SECRET_PRIVATE_KEY',
# })


# print (hitbtc.id, hitbtc.load_products ())
# print (bitmex.id, bitmex.load_products ())
# print (huobi.id,  huobi.load_products ())

# print (hitbtc.fetch_order_book (hitbtc.symbols[0]))
# print (bitmex.fetch_ticker ('BTC/USD'))
# print (huobi.fetch_trades ('LTC/CNY'))

# print (exmo.fetch_balance ())

# sell one BTC/USD for market price and receive $ right now
# print (exmo.id, exmo.create_market_sell_order ('BTC/USD', 1))

# limit buy BTC/EUR, you pay €2500 and receive 1 BTC when the order is closed
# print (exmo.id, exmo.create_limit_buy_order ('BTC/EUR', 1, 2500.00))