import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
# Pandas読み込み
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from IPython.display import display, HTML, Image



##############################################################################################

# 学習させてみよう

# まずは株価は上がるか下がるかを機械学習で予測できればゴールなので、
# 「株価はいくら上がるか（下がるか）」までは予測できなくていいので、
# 上がったか下がったかだけを学習させやすいように説明用にデーターを作っていきます。
# 実際には本物の株価データーを使って学習させていくのですが、今ここで学習過程を説明するためにここでは仮のデーターを作っていきます。

train_X = np.array([1.0, 1.1, 1.2, 1.3, 1.4])
train_y = np.array([1])
plt.plot([1, 2, 3, 4, 5], train_X)
#これは今なにしているかというと、機械学習に学習させるデーターを作っています。
#株価はいくら上がるか下がるかは予想しなくていいので、上がったか下がったかだけ学習させればいいので、そのようにデーターを作りました。
#どういうことかというと、
#train_X = np.array([1.0, 1.1, 1.2, 1.3, 1.4])
#この部分。これは最初の株価と比べて1日後に1.1倍、２日後に1.2倍、４日後には1.4倍になったというデーターを作っています。
#仮に最初が1000円だとしたら次の日は1100円、次の次の日は1200円、と増えていってる計算ですね。
#最初が980円だと、次の日はその1.1倍で1078円、1.2倍で1176円と推移していきますね。そういうのが計算しやすいように、何円であるかは関係なくして、1から始めて何倍、何倍と動いているかだけをデーターにしているのです。

#それに対し、次の部分、
#train_y = np.array([1])
#これは、６日後には株価が上がったのか下がったのか、上がっていれば1、下がっていれば0を答えとして教えています。

#なんども言いますが、今回の予想ではいくら上がったかを予想しなくていいので、上がったか下がったかだけの結果を教えています。
#こうやって、問題と答えの二つの変数を作って機械学習に教えてやります。
#機械には5日間分のデーターだけと、６日目の答えだけを与えるわけですね。こうすることによって、今日を含む過去5日間の値動きのデーターだけを与えると６日目つまり明日の結果が予想できるようになるのです。

#作った問題集を機械学習に教えてやります。
clf = DecisionTreeClassifier()
clf = clf.fit(train_X.reshape(1, -1), train_y)#学習
#これでパイソン君は問題と答えを覚えました。それではさっそく本番で予測してもらいます。


test_X = np.array([1.5, 1.6, 1.7, 1.8, 1.9])
#5日間、こういう動き方をする株価だったら、６日後には株価は上がっているのでしょうか？それとも下がっているのでしょうか？

clf.predict(test_X.reshape(1, -1))#評価用データを使って予測
print('[1.5, 1.6, 1.7, 1.8, 1.9] 予測してもらう時にはこうします。: %d' %train_y)
#予測してもらう時にはこうします。
# 結果は,array([1])と表示されました。

#上がるか下がるかを1か0かで教えたので、予想結果も上がると予想するなら1、下がると予想するなら0と教えてくれるようになります。
#結果は1。上がります！機械学習、賢い！

#なんとなくわかってきましたでしょうか。どんどんやってみます。(学習)
train_X = np.array([1.0, 0.9, 0.8, 0.7, 0.6])
train_y = np.array([0])
plt.plot([1, 2, 3, 4, 5], train_X)
clf.predict(test_X.reshape(1, -1))
print('[1.0, 0.9, 0.8, 0.7, 0.6]5日間かけて下がり続けた : %d' %train_y) #array([0])


#1.0, 0.9, 0.8, 0.7, 0.6と、5日間かけて下がり続けた結果、６日後にも株価が下がったパターン。これを学習させたうえで、
#2.0, 1.9, 1.8, 1.7, 1.6と5日間動けば６日後にはどうなるのか。


clf = clf.fit(train_X.reshape(1, -1), train_y)
test_X = np.array([2.0, 1.9, 1.8, 1.7, 1.6])
clf.predict(test_X.reshape(1, -1))
print('[2.0, 1.9, 1.8, 1.7, 1.6] : %d' %train_y) #array([0])

#下がる！やばい！賢すぎる！！！！
#おもしろい！！！どんどんいこう！！！

train_X = np.array([1.0, 0.5, 1.0, 0.5, 1.0])
train_y = np.array([0]) # 下がって上がると次は下がる
plt.plot([1, 2, 3, 4, 5], train_X)
clf = clf.fit(train_X.reshape(1, -1), train_y)
print('[1.0, 0.5, 1.0, 0.5, 1.0] : %d' %train_y)

train_X = np.array([0.5, 1.0, 0.5, 1.0, 0.5])
train_y = np.array([1]) # 上がって下がると次は上がる
plt.plot([1, 2, 3, 4, 5], train_X)
clf = clf.fit(train_X.reshape(1, -1), train_y)
print('[0.5, 1.0, 0.5, 1.0, 0.5] : %d' %train_y)


#学習させた結果！！
# 上がって下がると次はどうなるのか！？
test_X = np.array([0.7, 1.1, 0.7, 1.1, 0.7])
clf.predict(test_X.reshape(1, -1)) 
print('[0.7, 1.1, 0.7, 1.1, 0.7] : %d' %train_y) #array([1])

test_X = np.array([0.7, 1.1, 1.2, 1.3, 1.7])
clf.predict(test_X.reshape(1, -1)) 
print('[0.7, 1.1, 1.2, 1.3, 1.7] : %d' %train_y) #array([1])











'''
#if文, 100より大きいかの判定
num = 98
if num > 100: #>
    print(num, "は100より大きい")
elif num < 100:
    print(num, "は100より小さい")
else:
    print(num, "は１００です")
 
#出力結果: 98は100より小さい
'''
#よくできたすごいぞおおおおおおおぉぉぉぉぉ！！！！
#というわけで実際に作った、過去の株価から教師データーを作るソースコードがこちら。

# リターンインデックス
def get_ret_index(close):
    # データーが昇順（日付が過去が上になって最新が一番下）になっている前提
    returns = pd.Series(close).pct_change() # 騰落率を求める
    ret_index = (1 + returns).cumprod() # 累積積を求める
    ret_index.iloc[0] = 1 # 最初の値を 1.0 にする
    return ret_index
# 学習データーの作成
def train_data(arr, step):
    train_X = []
    train_y = []
    for i in range(0, len(arr) - step):
        end = i + step
        data = arr.iloc[i:end]
        close = data['adj_close']
        feature = get_ret_index(close)
        if close.iloc[-1] < arr['adj_close'].iloc[end]: # その翌日、株価は上がったか？
            # 上がっていれば１
            res = 1
        else:
            # 下がっていれば０
            res = 0
        train_X.append(feature.values)
        train_y.append(res)
    return np.array(train_X), np.array(train_y)



#ももももうこれ株買いに行けるんちゃちゃちゃちゃうか？
#待て。落ち着け。


'''
過去のデーターが大量にある。 ←ここまではいいです。
過去のデーターを使って、教師データーという問題集を大量に作れる。 ←ここまでもいいです。
問題集を大量に作れるので、機械にたくさん学習させられる。 ←「はい！ブー！過学習知らないのかよ！ばーかばーか」って山田君に言われたけど放っておこう。
学習した結果が正しいか、誰がわかるの？ ←ファッ！？


どういうこと？結果に従って、株を買えばいいんじゃないの？と思ったんですが、もし学習した結果が正しくなかったらお金を失いますよね。どうしましょう。
ここから途中のソースコードを保存していないので一気にいきますが、学習用問題データーとは別に検証用テストデーターを作らないといけないですよね。
株価なんていう複雑な動きをするデーターに、本物そっくりなテストデーターなんて作れるもんなんでしょうか？
ここで先人たちは、本物のデーターから無作為にテストデーターを抽出しておいて、学習用データーとはわけておくという引くくらい賢い解決策を講じています。そんな賢いこと思いつく人……機械学習なんていらんくらい頭いいやん……。
というわけで、例えば過去のデーターの2/3を学習用データーに使って、残りの1/3のデーターを使いテストして正解率を出せば、機械学習が最適に学習できたかわかるというわけですね。何遍も言うけど賢すぎて引く。


こんな賢いやりかたですが、まだデメリットがあります。
それは、できるだけデーターは学習用につかうほうもテスト用に使う方も大量に用意したい。せっかく用意したデーターを、学習用にもテスト用にも減らしたくない！っていうんです。用意したデーターをぜんぶ学習用に使いたいし、でもテストもしたいと言うんですね。えーい！わがままな！お前は２歳児か！！
これにはさすがに「そんなわがままいう子、お母さんしりません！勝手にしなさい！」と言いたかったところなんですが、なんと方法があるっていうです。用意したデーターを全部学習用にも使えてテストもできるっていう、機械学習開発者のわがままを全て満たしてくれる方法が。
それが交差検証法っていって、交差検証法のなかでもいくつかやり方があるんですが、今回やるのは学習用データーを何分割かして（例えば５分割）、ひとつをテスト用データーにつかい残りを教師用データーとしてもちいながら、テスト用データーを変えながら5回繰り返す、というやり方です。
図で説明するとわかりやすいんですが、わざわざ説明図を書くのも面倒なので、もうそのままソースコードのせます。ライブラリにそのものの機能が提供されているのでそれを使えば実際に使いながら試せたりします。
'''

#scores = cross_val_score(clf, train_X, train_y, cv=5)
#mean = scores.mean()

# meanで学習結果の正解率まで求められる。
# なんだろう、ツールの頭が良すぎて相対的に自分の頭の悪さが浮き彫りになってくるように思えて、アンニュイな気分になる。

'''
そろそろ山田君の声にも耳を傾けた方がいい
山田君って何て言ってたっけ。てか山田君って誰？
山田君「ばーかばーか」
↑
ああー！あのときの。
私がバカってのは事実なんだから別にいいんじゃない？いい気分はしないけど。
山田君「過学習知らないのかよ！ばーかばーか」
↑
過学習…だと…！？
ああ、うん、過学習ね。えっと、うん。
オライリー社から出ている実践 機械学習システムでも一番最初に触れるのが、この未学習と過学習のジレンマでして、未学習つまり学習させなさすぎても正しい答えは得られないし、過学習つまり詰め込みすぎてもガチガチに頭が固くなってしまって未知のデーターに対して柔軟に答えを得られなくなるんですね。人間と同じで、ここが機械学習の面白いところです。
ではどうすればいいかというと、学習量を変えて総当たりで結果を求めて、一番正解率が高かった学習量を採用すればいいのではないかと考えて、次のようなコードを書きました。
'''

def get_params(ccode, last_date, db):
    '''
    決定木に最適なパラメーターを総当たりで取得します。
    '''
    _top_mean = 0
    _data_length = 0
    _step = 0
    _min_samples_leaf = 0
    _max_depth = 0
    for data_length in range(30, 40, 10):
        for step in range(4, 12):
            for min_samples_leaf in range(1, 7):
                for max_depth in range(2, 8):
                    clf, train_X, train_y = lean(ccode, last_date, db, data_length, step, min_samples_leaf, max_depth)
                    scores = cross_val_score(clf, train_X, train_y, cv=5)
                    mean = scores.mean()
                    del clf
                    if _top_mean < mean:
                        _top_mean = mean
                        _data_length = data_length
                        _step = step
                        _min_samples_leaf = min_samples_leaf
                        _max_depth = max_depth
#     print("{}%, length:{}, step:{}, leaf: {}, depth: {}".format(int(_top_mean * 100), _data_length, _step, _min_samples_leaf, _max_depth))
    return _top_mean, _data_length, _step, _min_samples_leaf, _max_depth

'''
盛大にネストしてますがそこはご容赦を。

例えば、上のほうに書いてある解説では５日分の問題データーを作っていますが、ここを7日分にすればどうでしょう？10日分では？過去300日のデーターをつかって５日分の量で予想させるのと、100日のデーターを使って７日分の量で予想させるのと、どちらが正解率が高いでしょうか？仮に答えが求まったとしても、ある銘柄だけに使えるパラメーターであって、他の銘柄にも使えるでしょうか？そういったものを全て総当たりで調べています。


こんな感じでシステムでは予想をしていくわけですが、このシステムでミソなのは、調べた結果、この機械学習で予想しにくい銘柄はばっさり切り捨てていることです。

今回は、予想しにくい銘柄の予想精度をあげることが目的ではなく、これだけたくさんある銘柄の中から予想しやすい銘柄を見つけ出していくことが目的だからです。

次に湧き上がる疑問が、「こんなに簡単な予想結果で、果たして本当に実用になるのだろうか」ですね。それは冒頭で書いたように「予測で出た結果に従って株を買い続けるとどうなるのか」というポイントになりますので、次回以降からしっかりシミュレーションしていけばいいわけです。

シミュレーションしてみて、だめならだめで別の方法試せばいいわけで。


いかがでしたでしょうか？

次回からは実際にシミュレーションの方法を書いていきます。自分の手法は全てオープンにしましたしソースコードまで公開したので、何かしらの参考にされて実際にもう自分で開発を進めている方ももしかしたらいるかもしれません。もし参考になりそうだと思うなら、ぜひ試してみてください。もしかしたらこれを読んだ方の中からは「こんなさんざん既出な方法、みんな試してると思うし少なくとも俺は試してるし実際役に立たなかったよ」という方もいるかもしれません。そういう情報が集まって、自分の中の機械学習の技術が全体的に高まるのであれば、これほど技術者冥利に尽きることはありません。

こうして話題になることが、若くて貧しくて愚かだったあの頃、今日こそ現場で死ぬかもと思いながらも技術に夢を持ち続けて現場仕事とプログラミングを覚えていたあの頃の自分へのプレゼントになることでしょう。

株価もおもしろいけど機械学習で小説もかいてみたいよね、ってことで自然言語処理の入門書なんかも読んでたりします
'''






##############################################################################################
# csvのファイル名
csv_path = 'foo.csv'
# データフレーム読込
#data = pd.read_csv(csv_path, header=0)



data = np.loadtxt('foo.csv', delimiter=',', dtype=float)
print(data)

#data.columns = ["day_no","class","score1"]  #カラム名を付ける
#data.index = [11, 12, 13, 14, 15,16]  #インデックス名を付ける
#labels = data['day_no'] # 目的変数を取り出す

# 説明変数の格納,要因とした気温と天気のデータ
#1行目と２行目をスライスを使って配列xに格納しています。
# 説明変数の格納
x = data[:,0:2] # 目的変数を取り出す,すべての行の0~1列
print('説明変数を出力\n',x)

#目的変数の格納
y = data[:, 2:3].ravel()
print("目的変数を出力\n", y)


#学習用データと評価用データに分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
print("学習用の目的変数を出力-y_train\n", y_train)
print("評価用の目的変数を出力-y_test\n", y_test)
print("学習用の説明変数を出力-x_train\n", x_train)
print("評価用の説明変数を出力-x_test\n", x_test)



from sklearn.ensemble import RandomForestRegressor
#モデルに決定木を選択
clf = tree.DecisionTreeClassifier()
#clf = RandomForestRegressor()

#学習
clf.fit(x_train, y_train)


#評価用データを使って予測
predict = clf.predict(x_test)
print("評価結果を出力\n", predict)
print("正解率を出力\n", accuracy_score(y_test, predict))






'''
features = preprocessing.minmax_scale(data[:,1:])  # 説明変数を取り出した上でスケーリング
#print(features)
# X,yをそれぞれランダムに、学習データとテストデータに分ける（学習：テスト = 0.8：0.2）
x_train, x_test, y_train, y_test = train_test_split(features, labels.ravel(), test_size=0.8) # トレーニングデータとテストデータに分割




# 学習データを使ってモデルを構築する
from sklearn.ensemble import RandomForestRegressor

regr = RandomForestRegressor()
regr.fit(x_train, y_train)
regr.predict(x_test)#テストデータを使った予測です。



#正解率（accuracy）、適合率（precision）、再現率（recall）を出したい場合は、
from sklearn.metrics import accuracy_score, precision_score, recall_score
#from sklearn.ensemble import RandomForestClassifier

predict = regr.predict(x_test)
print(accuracy_score(y_test, predict), precision_score(y_test, predict), recall_score(y_test, predict))


#print(x_train)
#print(y_train)


#print('')



# テストデータのyの予測値を求める
y_predicted = regr.predict(x_test)

# 実際のyの値と予測値を比較して、テストデータに関するR2決定係数を確認する
from sklearn import metrics
R2test = metrics.r2_score(y_test, y_predicted)
print(R2test)
'''




#print(clf.predict(x_test))

#from sklearn.metrics import accuracy_score, precision_score, recall_score

#predict = clf.predict(x_test)
#print(accuracy_score(y_test, predict), precision_score(y_test, predict), recall_score(y_test, predict))