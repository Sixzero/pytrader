# pip3 install https://github.com/s4w3d0ff/python-poloniex/archive/v0.4.6.zip


from poloniex import Poloniex
polo = Poloniex()

# Ticker:
print(polo('returnTicker')['BTC_ETH'])
# or
print(polo.returnTicker()['BTC_ETH'])

# Public trade history:
print(polo.marketTradeHist('BTC_ETH'))

# Basic Private Setup (Api key/secret required):
import poloniex
polo = poloniex.Poloniex('your-Api-Key-Here-xxxx','yourSecretKeyHere123456789')
# or
polo.key = 'your-Api-Key-Here-xxxx'
polo.secret = 'yourSecretKeyHere123456789'

# Get all your balances

balance = polo.returnBalances()
print("I have %s ETH!" % balance['ETH'])
# or
balance = polo('returnBalances')
print("I have %s BTC!" % balance['BTC'])

# Private trade history:

print(polo.returnTradeHistory('BTC_ETH'))

