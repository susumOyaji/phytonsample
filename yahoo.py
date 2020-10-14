#!pip install yahoo_finance_api2

import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
from datetime import datetime



'''
my_share = share.Share('6758.T')
symbol_data = None

try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,7,share.FREQUENCY_TYPE_MINUTE,1)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)

print(symbol_data)
'''



my_share = share.Share('6758.T')
symbol_data = None

try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,1,share.FREQUENCY_TYPE_MINUTE,1)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)

print(symbol_data.keys())
date = symbol_data["timestamp"]
print(len(date))



old_date = date[0]
now_date = date[301]


old_time = datetime.utcfromtimestamp(old_date/1000)
now_time = datetime.utcfromtimestamp(now_date/1000)

price = symbol_data["close"]
old_price = price[0]
now_price = price[301]
print(str(old_time) + "の時の株価： " + str(old_price))
print(str(now_time) + "の時の株価： " + str(now_price))
print('{:.2f}'.format(now_price - old_price))


my_share = share.Share('6758.T')
symbol_data = None

try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,1,share.FREQUENCY_TYPE_MINUTE,5)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)

print(symbol_data)

price = symbol_data["close"]
old_price = price[0]
now_price = price[69]