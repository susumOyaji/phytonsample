#再び必要なモジュールのインストール
import seaborn as sns
import matplotlib as inline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
from selenium import webdriver
import requests
import json

#csvファイルの読み込み
train=pd.read_csv("stockPriceData.csv")
train.head()
df = pd.read_csv('stockPriceData.csv')
ooo = df[:0]
del(ooo['date'])
del(ooo['year'])
del(ooo['month'])
del(ooo['day'])
ppp = [meigara_name + '：前日比', meigara_name + '：翌日比']
kkk = ooo.columns
zzz = kkk.drop(ppp)
vars(zzz)

#機械学習の準備
features=['6138 ダイジェット工業(株)', '5009 富士興産(株)', '6185 ソネット・メディア・ネットワークス(株)',

        '3667 (株)ｅｎｉｓｈ', '9265 ヤマシタヘルスケアホールディングス(株)', '7238 曙ブレーキ工業(株)',

        '4463 日華化学(株)', '7191 (株)イントラスト', '3627 ネオス(株)',

        '3561 (株)力の源ホールディングス', '7730 マニー(株)', '2809 キユーピー(株)',

        '7475 アルビス(株)', '6189 (株)グローバルキッズＣＯＭＰＡＮＹ', '2424 (株)ブラス',

        '3932 (株)アカツキ', '3877 中越パルプ工業(株)', '9716 (株)乃村工藝社', '8349 (株)東北銀行',

        '9325 (株)ファイズ', '4680 (株)ラウンドワン', '7504 (株)高速',

        '8798 (株)アドバンスクリエイト', '4320 (株)ＣＥホールディングス', '7888 三光合成(株)',

        '8585 (株)オリエントコーポレーション', '3677 (株)システム情報',

        '5698 (株)エンビプロ・ホールディングス', '1726 (株)ビーアールホールディングス',

        '6330 東洋エンジニアリング(株)', '3771 (株)システムリサーチ',

        '8028 ユニー・ファミリーマートホールディングス(株)', '8589 (株)アプラスフィナンシャル',

        '6274 ヤマハモーターロボティクスホールディングス(株)', '7823 (株)アートネイチャー',

        '4369 (株)トリケミカル研究所', '8515 アイフル(株)', '3918 ＰＣＩホールディングス(株)',

        '3030 (株)ハブ', '7199 プレミアグループ(株)', '3992 (株)ニーズウェル', '2009 鳥越製粉(株)',

        '6740 (株)ジャパンディスプレイ', '7455 (株)三城ホールディングス',

        '7735 (株)ＳＣＲＥＥＮホールディングス', '6753 シャープ(株)', '2931 (株)ユーグレナ',

        '7481 尾家産業(株)']

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