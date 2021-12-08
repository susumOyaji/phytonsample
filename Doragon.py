# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def get_table(url):
    soup = BeautifulSoup(requests.get(url).text, "lxml")
    if len(soup.body.find_all('tr')) > 20:
        start_line = [i  for i in range(14,20) if soup.body.find_all('tr')[i].text.splitlines()[1] == '順位']
        items = [v.text.splitlines() for i, v in enumerate(soup.body.find_all('tr')) if i > start_line[0]]
        cols = ['', '順位','コード', '名称', '市場','日付','終値','前日比（円）','前日比（%）','5日平均比出来高急増率','出来高','高値','安値']
        df = pd.DataFrame(np.array(items[0]).reshape(1,-1),columns=cols)
        print(items[0])
        for i in range(1,200):
            df_add = pd.DataFrame(np.array(items[i]).reshape(1,-1),columns=cols)
            df = pd.concat([df, df_add],axis = 0)
        return df,True
    else:
        print('休場')
        return np.nan, False
    
st_date = '2019/01/01'
end_date = '2019/07/31'
st_date = datetime.strptime(st_date, '%Y/%m/%d')
end_date = datetime.strptime(end_date, '%Y/%m/%d')

dfs = []

while st_date <= end_date:
    date = datetime.strftime(st_date, '%Y/%m/%d' )
    print(date)
    url = 'https://www.kabudragon.com/ranking/{}/dekizou200.html'.format(date)
    st_date = st_date + timedelta(days = 1)
    
    df, flg = get_table(url)
    if flg:
        dfs.append(df)
        
#複数ページのデータを1つのデータフレームにする
df = pd.concat(dfs).reset_index(drop = True)

#初登場の日付のみに絞る
df = df.drop(df[df.duplicated(subset = 'コード')].index,axis=0)

#初登場の日付をdatetimeの日付にする
df['date'] = [datetime.strptime('2019/' + i.split('(')[0],'%Y/%m/%d') for i in df['日付']]

#対象の期間の指定
target_start = '2019/07/01'
target_end = '2019/07/31'

data = df[(df['date']>=target_start) & (df['date']<=target_end)]
output = data.loc[:,['コード', '名称', '市場', 'date']]
output = output.rename(columns = {'コード':'code', '名称':'name','市場':'market'}).set_index('date', drop = True)
print(output)