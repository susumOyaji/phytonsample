# -*- coding: utf-8 -*-
# ライブラリのインポート
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 各ページのランキング表をデータフレーム化する関数
def get_table(url):
    urlName = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code="+url
    soup = BeautifulSoup(requests.get(urlName).text, 'html.parser')
    if len(soup.body.find_all('tr')) > 20:
        start_line = [i  for i in range(14,20) if soup.body.find_all('tr')[i].text.splitlines()[1] == '順位']
        items = [v.text.splitlines() for i, v in enumerate(soup.body.find_all('tr')) if i > start_line[0]]
        cols = ['', '順位','コード', '名称', '市場','日付','終値','前日比（円）','前日比（%）','値上がり','出来高','高値','安値']
        df = pd.DataFrame(np.array(items[0]).reshape(1,-1),columns=cols)
        print(items[0])
        for i in range(1,200):
            df_add = pd.DataFrame(np.array(items[i]).reshape(1,-1),columns=cols)
            df = pd.concat([df, df_add],axis = 0)
        df['値上がり率(円)']  = [v.split('+')[1] for v in df['値上がり']]
        df['値上がり率(%）']  = [v.split('+')[-1] for v in df['値上がり']]
        df = df.drop('値上がり', axis = 1)
        return df,True
    else:
        print('休場')
        return np.nan, False

# ランキングの推移を可視化したい日付（開始と終わり）を設定
date = '2019/01/01'
end_date = '2019/05/19'
dfs = []
dates = []
while date !=  end_date:
    strp_date = datetime.strptime(date, '%Y/%m/%d') + timedelta(days = 1)
    date = datetime.strftime(strp_date, '%Y/%m/%d' )
    print(date)
    url = 'https://www.kabudragon.com/ranking/{}/yl_age200.html'.format(date)
    #url = "https://kabuoji3.com/ranking/?date=2019-07-05&type=1&market=3"  #リストから銘柄を選択
    df, flg = get_table(url)
    if flg:
        dfs.append(df)
        dates.append(strp_date)

# 対象期間でランキングに入った銘柄コードの辞書作成
dic = {}
for df in dfs:
    keys = df['コード']
    values = df['名称']
    buf = dict(zip(keys, values))
    dic.update(buf)

# ランキング推移可視化
for k, v in dic.items():
    code = k
    name = v

    rankings = []
    close = []
    day_inc_rate = []
    volume = []
    inc_rate = []
    for df in dfs:
        if len(df[df['コード'] == code]['順位']) != 1:
            rankings.append(-201)
            close.append(-1)
            day_inc_rate.append(-100)
            volume.append(-1)
            inc_rate.append(-1)

        else:
            rankings.append(int(df[df['コード'] == code]['順位'].values[0])*-1)
            close.append(float(df[df['コード'] == code]['終値'].values[0].replace(',', '')))
            day_inc_rate.append(float(df[df['コード'] == code]['前日比（%）'].values[0].replace('%', '')))
            volume.append(float(df[df['コード'] == code]['出来高'].values[0].replace(',', '')))
            inc_rate.append(float(df[df['コード'] == code]['値上がり率(%）'].values[0].replace('%', '')))

    fig, ax1 = plt.subplots(figsize =(20,3))
    ax1.plot(dates, rankings,'o-')
    ax2 = ax1.twinx()
    # ax2.plot(np.arange(len(rankings)), close,'o-')
    # ax2.plot(np.arange(len(rankings)), day_inc_rate,'o-')
    # ax2.plot(np.arange(len(rankings)), volume,'o-')
    ax2.plot(dates, inc_rate,'o-',color = 'orange')
    plt.title([code, name])
    ax1.set_ylim(-201,0)
    ax2.set_ylim(0,1000)
    plt.show()