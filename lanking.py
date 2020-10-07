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
    soup = BeautifulSoup(requests.get(url).text, "lxml")
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
    df, flg = get_table(url)
    if flg:
        dfs.append(df)
        dates.append(strp_date)