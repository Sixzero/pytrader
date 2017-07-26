import ccxt


hitbtc = ccxt.hitbtc ({ 'verbose': True })
bitmex = ccxt.bitmex ()
huobi  = ccxt.huobi ()
# exmo   = ccxt.exmo ({
#     'apiKey': 'YOUR_PUBLIC_API_KEY',
#     'secret': 'YOUR_SECRET_PRIVATE_KEY',
# })

hitbtc_products = hitbtc.load_products ()

print (hitbtc.id, hitbtc_products)
print (bitmex.id, bitmex.load_products ())
print (huobi.id,  huobi.load_products ())

print (hitbtc.fetch_order_book (hitbtc.symbols[0]))
print (bitmex.fetch_ticker ('BTC/USD'))
print (huobi.fetch_trades ('LTC/CNY'))

# print (exmo.fetch_balance ())

# sell one BTC/USD for market price and receive $ right now
# print (exmo.id, exmo.create_market_sell_order ('BTC/USD', 1))

# limit buy BTC/EUR, you pay €2500 and receive 1 BTC when the order is closed
# print (exmo.id, exmo.create_limit_buy_order ('BTC/EUR', 1, 2500.00))