# coding=utf-8

import ccxt
import time
import sys
import json

import argparse
import threading
from pprint import pprint

# ------------------------------------------------------------------------------
# string coloring functions

def style(s, style): return style + str(s) + '\033[0m'


def green(s): return style(s, '\033[92m')


def blue(s): return style(s, '\033[94m')


def yellow(s): return style(s, '\033[93m')


def red(s): return style(s, '\033[91m')


def pink(s): return style(s, '\033[95m')


def bold(s): return style(s, '\033[1m')


def underline(s): return style(s, '\033[4m')


# print a colored string
def dump(*args):
    print(' '.join([str(arg) for arg in args]))


# ------------------------------------------------------------------------------

def test_market_symbol_orderbook(market, symbol):
    delay = int(market.rateLimit / 1000)
    time.sleep(delay)
    dump(green(market.id), green(symbol), 'fetching order book...')
    orderbook = market.fetch_order_book(symbol)
    dump(green(market.id), green(symbol), 'order book',
         orderbook['datetime'],
         'bid: ' + str(orderbook['bids'][0][0] if len(orderbook['bids']) else 'N/A'),
         'bidVolume: ' + str(orderbook['bids'][0][1] if len(orderbook['bids']) else 'N/A'),
         'ask: ' + str(orderbook['asks'][0][0] if len(orderbook['asks']) else 'N/A'),
         'askVolume: ' + str(orderbook['asks'][0][1] if len(orderbook['asks']) else 'N/A'),
         )


def test_market_symbol_ticker(market, symbol):
    delay = int(market.rateLimit / 1000)
    time.sleep(delay)
    dump(green(market.id), green(symbol), 'fetching ticker...')
    ticker = market.fetch_ticker(symbol)
    dump(green(market.id), green(symbol), 'ticker',
         ticker['datetime'],
         'high: ' + str(ticker['high']),
         'low: ' + str(ticker['low']),
         'bid: ' + str(ticker['bid']),
         'ask: ' + str(ticker['ask']),
         'volume: ' + str(ticker['quoteVolume']),
         )


def test_market_symbol(market, symbol):
    dump(green('SYMBOL: ' + symbol))
    test_market_symbol_ticker(market, symbol)
    if market.id == 'coinmarketcap':
        dump(green(market.fetchGlobal()))
    else:
        test_market_symbol_orderbook(market, symbol)


def get_stats_from_coinmarketcap():
    coinmarketcap_market = ccxt.coins()
    coinmarketcap_market.load_products()
    keys = list(coinmarketcap_market.products.keys())
    dump(green('MARKET: ' + coinmarketcap_market.id), keys)




def get_valid_symbols(markets):
    excluded_symbols = ["/USD",
                        "USD/",
                        "EUR/",
                        "/EUR",
                        "AUD/",
                        "/CHF",
                        "/CNY",
                        "/JPY",
                        "/MXN",
                        "/RUB",
                        '/GBP',
                        '/CAD',
                        '/AUD',
                        '/AED',
                        '/BGN',
                        '/CZK',
                        '/DKK',
                        '/HKD',
                        '/HRK',
                        '/HUF',
                        '/ILS',
                        '/INR',
                        '/MUR',
                        '/NOK',
                        '/NZD',
                        '/PLN',
                        '/RON',
                        '/SEK',
                        '/SGD',
                        '/THB',
                        '/TRY',
                        '/ZAR',
                        ]
    symbols = []
    bittrex = markets["bittrex"]
    # bittrex.proxy = 'https://crossorigin.me/'
    print("Ok start")
    products = bittrex.load_products()
    print("Ok loaded")
    keys = list(bittrex.products.keys())
    print(keys)
    for k in keys:
        if any(k.find(excluded_symbol) >= 0 for excluded_symbol in excluded_symbols):
            continue
        if not k in symbols:
            symbols.append(k)
    get_ticks(bittrex, ['PAY/BTC', ]) # 'ETH/BTC',
    pprint(dir(ccxt.bittrex()))
    # pprint(bittrex.publicGetTicker())
    assert 0
    for market_id in markets:
        th = threading.Thread(target=get_ticks, args=(markets[market_id], symbols))
        th.start()
    # print("symbols", symbols)
    time.sleep(10)
    assert 0


def get_ticks(market, symbols):
    products = market.load_products()
    keys = list(market.products.keys())
    for k in symbols:
        if k in keys:
            # print(f"market.fetch_ticker( {k} ) ")
            # print(market.fetch_ticker(k))
            # print(market.fetch_order_book(k))
            # pprint(market.fetch_trades(k))
            time.sleep(1)


def test_market(market):
    delay = 2
    products = market.load_products()
    keys = list(market.products.keys())
    dump(green('MARKET: ' + market.id), keys)
    # ..........................................................................
    # public API

    symbols = ['LTC/BTC', 'DOGE/BTC', 'VTC/BTC', 'PPC/BTC', 'FTC/BTC', 'RDD/BTC', 'NXT/BTC', 'DASH/BTC', 'POT/BTC', 'BLK/BTC',
     'EMC2/BTC', 'MYR/BTC', 'AUR/BTC', 'EFL/BTC', 'GLD/BTC', 'SLR/BTC', 'PTC/BTC', 'GRS/BTC', 'NLG/BTC', 'RBY/BTC',
     'XWC/BTC', 'MONA/BTC', 'THC/BTC', 'ENRG/BTC', 'ERC/BTC', 'NAUT/BTC', 'VRC/BTC', 'CURE/BTC', 'XBB/BTC', 'XMR/BTC',
     'CLOAK/BTC', 'START/BTC', 'KORE/BTC', 'XDN/BTC', 'TRUST/BTC', 'NAV/BTC', 'XST/BTC', 'BTCD/BTC', 'VIA/BTC',
     'UNO/BTC', 'PINK/BTC', 'IOC/BTC', 'CANN/BTC', 'SYS/BTC', 'NEOS/BTC', 'DGB/BTC', 'BURST/BTC', 'EXCL/BTC',
     'SWIFT/BTC', 'DOPE/BTC', 'BLOCK/BTC', 'ABY/BTC', 'BYC/BTC', 'XMG/BTC', 'BLITZ/BTC', 'BAY/BTC', 'BTS/BTC',
     'FAIR/BTC', 'SPR/BTC', 'VTR/BTC', 'XRP/BTC', 'GAME/BTC', 'COVAL/BTC', 'NXS/BTC', 'XCP/BTC', 'BITB/BTC', 'GEO/BTC',
     'FLDC/BTC', 'GRC/BTC', 'FLO/BTC', 'NBT/BTC', 'MUE/BTC', 'XEM/BTC', 'CLAM/BTC', 'DMD/BTC', 'GAM/BTC', 'SPHR/BTC',
     'OK/BTC', 'SNRG/BTC', 'PKB/BTC', 'CPC/BTC', 'AEON/BTC', 'ETH/BTC', 'GCR/BTC', 'TX/BTC', 'BCY/BTC', 'EXP/BTC',
     'INFX/BTC', 'OMNI/BTC', 'AMP/BTC', 'AGRS/BTC', 'XLM/BTC', 'BTA/BTC', 'BTC/BITCNY', 'CLUB/BTC', 'VOX/BTC',
     'EMC/BTC', 'FCT/BTC', 'MAID/BTC', 'EGC/BTC', 'SLS/BTC', 'RADS/BTC', 'DCR/BTC', 'SEC/BTC', 'BSD/BTC', 'XVG/BTC',
     'PIVX/BTC', 'XVC/BTC', 'MEME/BTC', 'STEEM/BTC', '2GIVE/BTC', 'LSK/BTC', 'PDC/BTC', 'BRK/BTC', 'DGD/BTC', 'DGD/ETH',
     'WAVES/BTC', 'RISE/BTC', 'LBC/BTC', 'SBD/BTC', 'BRX/BTC', 'DRACO/BTC', 'ETC/BTC', 'ETC/ETH', 'STRAT/BTC',
     'UNB/BTC', 'SYNX/BTC', 'TRIG/BTC', 'EBST/BTC', 'VRM/BTC', 'SEQ/BTC', 'XAUR/BTC', 'SNGLS/BTC', 'REP/BTC',
     'SHIFT/BTC', 'ARDR/BTC', 'XZC/BTC', 'ANS/BTC', 'ZEC/BTC', 'ZCL/BTC', 'IOP/BTC', 'DAR/BTC', 'GOLOS/BTC', 'HKG/BTC',
     'UBQ/BTC', 'KMD/BTC', 'GBG/BTC', 'SIB/BTC', 'ION/BTC', 'LMC/BTC', 'QWARK/BTC', 'CRW/BTC', 'SWT/BTC', 'TIME/BTC',
     'MLN/BTC', 'ARK/BTC', 'DYN/BTC', 'TKS/BTC', 'MUSIC/BTC', 'DTB/BTC', 'INCNT/BTC', 'GBYTE/BTC', 'GNT/BTC', 'NXC/BTC',
     'EDG/BTC', 'LGD/BTC', 'TRST/BTC', 'GNT/ETH', 'REP/ETH', 'WINGS/ETH', 'WINGS/BTC', 'RLC/BTC', 'GNO/BTC', 'GUP/BTC',
     'LUN/BTC', 'GUP/ETH', 'RLC/ETH', 'LUN/ETH', 'SNGLS/ETH', 'GNO/ETH', 'APX/BTC', 'TKN/BTC', 'TKN/ETH', 'HMQ/BTC',
     'HMQ/ETH', 'ANT/BTC', 'TRST/ETH', 'ANT/ETH', 'SC/BTC', 'BAT/ETH', 'BAT/BTC', 'ZEN/BTC', '1ST/BTC', 'QRL/BTC',
     '1ST/ETH', 'QRL/ETH', 'CRB/BTC', 'CRB/ETH', 'LGD/ETH', 'PTOY/BTC', 'PTOY/ETH', 'MYST/BTC', 'MYST/ETH', 'CFI/BTC',
     'CFI/ETH', 'BNT/BTC', 'BNT/ETH', 'NMR/BTC', 'NMR/ETH', 'TIME/ETH', 'LTC/ETH', 'XRP/ETH', 'SNT/BTC', 'SNT/ETH',
     'DCT/BTC', 'XEL/BTC', 'MCO/BTC', 'MCO/ETH', 'ADT/BTC', 'ADT/ETH', 'FUN/BTC', 'FUN/ETH', 'PAY/BTC', 'PAY/ETH',
     'MTL/BTC', 'MTL/ETH', 'STORJ/BTC', 'STORJ/ETH', 'ADX/BTC', 'ADX/ETH', 'DASH/ETH', 'SC/ETH', 'ZEC/ETH', 'OMG/BTC',
     'OMG/ETH', 'CVC/BTC', 'CVC/ETH', 'PART/BTC', 'QTUM/BTC', 'QTUM/ETH', 'XMR/ETH', 'XEM/ETH', 'XLM/ETH', 'ANS/ETH',
     'BCC/ETH', 'BCC/BTC', 'WAVES/ETH', 'STRAT/ETH', 'DGB/ETH', 'FCT/ETH', 'BTS/ETH']

    for s in symbols:
        if s in keys:
            print(u"Ye {s} in keys.")
            if s.find('.d') < 0:
                print(u"So run!")

                test_market_symbol(market, s)


    # ..........................................................................
    # private API

    if (not hasattr(market, 'apiKey') or (len(market.apiKey) < 1)):
        return

    # balance = market.fetch_balance()
    # dump(green(market.id), 'balance', balance)
    # time.sleep (delay)

    amount = 1
    price = 0.0161

    # marketBuy = market.create_market_buy_order (symbol, amount)
    # print (marketBuy)
    # time.sleep (delay)

    # marketSell = market.create_market_sell_order (symbol, amount)
    # print (marketSell)
    # time.sleep (delay)

    # limitBuy = market.create_limit_buy_order (symbol, amount, price)
    # print (limitBuy)
    # time.sleep (delay)

    # limitSell = market.create_limit_sell_order (symbol, amount, price)
    # print (limitSell)
    # time.sleep (delay)


# ------------------------------------------------------------------------------


import datetime
class Logger():
    mNeedRun = True
    def __init__(self, market, library, proxies = None):
        if proxies:
            self.proxies = proxies
        else:
            self.proxies = [""]
        self.library = library
        self.market = market

    def logger_every_X_mins(self, minutes=2):
        last_date = datetime.datetime.now()
        last_date = last_date.replace(second=58)
        symbols = ['PAY/BTC']
        self.save_trade_history(self.market, symbols)
        while self.mNeedRun:
            while datetime.datetime.now() < last_date:
                time.sleep(1)
                if not self.mNeedRun:
                    return
            self.save_trade_history(self.market, symbols)
            # get_ticks(self.market, ['PAY/BTC', ])  # 'ETH/BTC',
            # self.try_all_proxies()
            last_date = last_date + datetime.timedelta(minutes=minutes)


    def save_trade_history(self, market, symbols):
        import pandas as pd
        products = market.load_products()
        keys = list(market.products.keys())

        for k in symbols:
            if k in keys:
                response = market.fetch_trades(k)
                df = pd.DataFrame(response['result'])
                df.reindex(index=df.index[::-1])
                df = df.sort_values('Id')
                lastDF = self.library.read(k).data
                lastDF = lastDF.sort_values('Id')
                # merged = df
                print( list(df))
                merged = pd.merge_ordered(df, lastDF, how='outer', on=list(df))
                self.library.write(k, merged)
                print(merged)
                print("Data size:", merged.shape)
                time.sleep(1)

    def try_all_proxies(self):
        current_proxy = 0
        max_retries = len(self.proxies)
        # a special case for ccex
        if self.market.id == 'ccex':
            currentProxy = 1
        for num_retries in range(0, max_retries):
            try:
                self.market.proxy = self.proxies[current_proxy]
                current_proxy = (current_proxy + 1) % len(self.proxies)
                test_market(self.market)
                break
            except ccxt.DDoSProtectionError as e:
                dump(yellow(type(e).__name__), e.args)
            except ccxt.TimeoutError as e:
                dump(yellow(type(e).__name__), str(e))
            except ccxt.MarketNotAvailableError as e:
                dump(yellow(type(e).__name__), e.args)
            except ccxt.EndpointError as e:
                dump(yellow(type(e).__name__), e.args)
            except ccxt.MarketError as e:
                dump(yellow(type(e).__name__), e.args)
            except ccxt.AuthenticationError as e:
                dump(yellow(type(e).__name__), str(e))