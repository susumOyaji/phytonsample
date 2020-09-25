#再び必要なモジュールのインストール
import seaborn as sns
import matplotlib as inline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
from selenium import webdriver
import requests
import json
import pandas as pd

#%matplotlib inline
import matplotlib.pyplot as plt

#csvファイルの読み込み
train=pd.read_csv("stockPriceData.csv")
train.head()
df = pd.read_csv('stockPriceData.csv')
ooo = df[:0]
del(ooo['date'])
del(ooo['year'])
del(ooo['month'])
del(ooo['day'])
meigara_name = "レオパレス21"
ppp = [meigara_name + '：前日比', meigara_name + '：翌日比']
kkk = ooo.columns
zzz = kkk.drop(ppp)
vars(zzz)

#機械学習の準備
features=['6138 ダイジェット工業(株)', '5009 富士興産(株)', '6185 ＳＭＮ(株)','3667 (株)ｅｎｉｓｈ', ]

x=train[features]
y=train[meigara_name + "：翌日比"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.27)

#モデリングと予測
model=RandomForestRegressor(n_estimators=1000)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

#結果の表示
testUpDown=[]
for test in y_test:
    if test>0:
        testUpDown.append(1)
else:
    testUpDown.append(-1)
predUpDown=[]
for pred in y_pred:
    if pred>0:
        predUpDown.append(1)
else:
    predUpDown.append(-1)
print("確率："+str(metrics.accuracy_score(testUpDown,predUpDown)*100)+"%")

#特徴量のグラフの出力
feature_imp = pd.Series(model.feature_importances_,index=features).sort_values(ascending=False)
print(feature_imp)
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.figure(figsize=(30,50))
plt.show()

#Slackへ
slackURL="https://hooks.slack.com/services/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"
def send_slack(content):
    payload={

        "text":content,

        "username":"PythonStockForecast",

        "icon_emoji":":snake:"

    }

    data=json.dumps(payload)

    requests.post(slackURL,data)

send_slack(resultNotification)