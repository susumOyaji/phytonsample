# coding: utf-8
'''
def DataRead():
    with cd.open("./dataset/jpstock/1570_2018.csv", "r", "Shift-JIS", "ignore") as csv_file:
        df = pd.read_csv(csv_file, quotechar='"', header=1, index_col=0)    # convert data frame type by index_col


df_ = df.copy()
df_.index = mdates.date2num(df_.index)
data = df_.reset_index().values

fig = plt.figure(figsize=(12, 4))
ax = fig.add_subplot(1, 1, 1)

mpf.candlestick_ohlc(ax, data, width=2, alpha=1.0, colorup='r', colordown='b')
    ax.plot(df.index, df['close'].rolling(5).mean(),color='g',label="Moving Ave(5)")
    ax.plot(df.index, df['close'].rolling(25).mean(),color='m',label="Moving Ave(25)")
    ax.plot(df.index, df['close'].rolling(50).mean(),color='r',label="Moving Ave(50)")
    plt.scatter(x, y, s=100, marker="v",color='k')

    ax.grid()

    locator = mdates.AutoDateLocator()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))
    plt.legend()
    plt.show()
'''


import sys
import datetime
import pandas as pd
#import pandas.io.data as web
from pandas_datareader import DataReader

class JpStock:
    def base_url(self):
        return ('http://info.finance.yahoo.co.jp/history/'
                '?code={0}.T&{1}&{2}&tm={3}&p={4}')

    def get(self, code, start=None, end=None, interval='d'):
        base = self.base_url()
        start, end = DataReader._sanitize_dates(start, end)
        start = 'sy={0}&sm={1}&sd={2}'.format(start.year, start.month, start.day)
        end = 'ey={0}&em={1}&ed={2}'.format(end.year, end.month, end.day)
        p = 1
        results = []

        if interval not in ['d', 'w', 'm', 'v']:
            raise ValueError(
                "Invalid interval: valid values are 'd', 'w', 'm' and 'v'")

        while True:
            url = base.format(code, start, end, interval, p)
            tables = pd.read_html(url, header=0)
            if len(tables) < 2 or len(tables[1]) == 0:
                break
            results.append(tables[1])
            p += 1
        result = pd.concat(results, ignore_index=True)

        result.columns = [
            'Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
        result['Date'] = pd.to_datetime(result['Date'], format='%Y年%m月%d日')
        result = result.set_index('Date')
        result = result.sort_index()
        return result.asfreq('B')


if __name__ == '__main__':
    argsmin = 2
    version = (3, 0)
   
    if sys.version_info > (version):
        if len(sys.argv) > argsmin:
            try:
                stock = sys.argv[1]
                start = sys.argv[2]

                jpstock = JpStock()
                stock_tse = jpstock.get(int(stock), start=start)
                stock_tse.to_csv("".join(["stock_", stock, ".csv"]))
            except ValueError:
                print("Value Error occured in", stock)
        else:
            print("This program needs at least %(argsmin)s arguments" %
                  locals())
    else:
        print("This program requires python > %(version)s" % locals())
