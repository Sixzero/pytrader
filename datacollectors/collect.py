
import ccxt
import time
import sys
import json
import ccxt_collector

import threading
from arctic import Arctic
from datetime import datetime as dt
import pandas as pd


# Connect to the mongo-host / cluster
mongo_host = "127.0.0.1 "
store = Arctic(mongo_host)

exchange_name = "bittrex"


def get_library_for_exchange(exchange_name):
    store_libraries = store.list_libraries()
    if not exchange_name in store_libraries:
        store.initialize_library(exchange_name)
    return store[exchange_name]


markets = {}


# instantiate all markets
for id in ccxt.markets:
    market = getattr(ccxt, id)
    markets[id] = market({'verbose': False})

# load the api keys from config
with open('./keys.json') as file:
    config = json.load(file)

# set up api keys appropriately
tuples = list(ccxt.Market.keysort(config).items())
for (id, params) in tuples:
    options = list(params.items())
    for key in params:
        setattr(markets[id], key, params[key])

# ccxt_collector.get_valid_symbols(markets)

# move gdax to sandbox
# markets['gdax'].urls['api'] = 'https://api-public.sandbox.gdax.com'

# ------------------------------------------------------------------------------

proxies = [
    '',
    'https://cors-anywhere.herokuapp.com/',
    'https://crossorigin.me/',
    'https://galvanize-cors-proxy.herokuapp.com/',
    'http://jsonp.herokuapp.com/',
    'http://dry-sierra-94326.herokuapp.com/',
    # 'http://cors-proxy.htmldriven.com/?url=', # we don't want this for now
]

if __name__ == "__main__":

    bittrex = markets["bittrex"]
    library = get_library_for_exchange(bittrex.id)
    logger = ccxt_collector.Logger(bittrex, library, proxies)
    th = threading.Thread(target=logger.logger_every_X_mins, args=())
    th.start()


    # tuples = list(ccxt.Market.keysort(markets).items())
    # print("tuples", tuples)
    # print("markets", markets)
    # loggers = []
    # for (id, params) in tuples[:-1]:
    #     library = get_library_for_exchange(id)
    #     market = markets[id]
    #     logger = ccxt_collector.Logger(market, library, proxies)
    #     th = threading.Thread(target=logger.logger_every_mins, args=())
    #     th.start()
    #     loggers.append(logger)

    try:
        time.sleep(130)
    except KeyboardInterrupt:
        print('Exiting by user KeyboardInterrupt.')
        pass
    finally:
        # for l in loggers:
        #     l.mNeedRun = False
        sys.exit(0)
