
# Pandas読み込み
import pandas as pd
# csvのファイル名
csv_path = 'titanic.csv'
# データフレーム読込
df_titanic = pd.read_csv(csv_path, header=0)




'''
データを作ってみよう
まず最初にPandasをインポートし、適当にデータフレーム形式のデータを作る
'''

import pandas as pd

df_sample =\
pd.DataFrame([["day1","day2","day1","day2","day1","day2"],
              ["A","B","A","B","C","C"],
              [100,150,200,150,100,50],
              [120,160,100,180,110,80]] ).T  #とりあえず適当なデータを作ります

df_sample.columns = ["day_no","class","score1","score2"]  #カラム名を付ける
df_sample.index   = [11,12,13,14,15,16]  #インデックス名を付ける
print(df_sample)

#◆Column / Index Access
#特定の列やインデックス番号にアクセス
#col_index_access.py
'''
df_sample.columns   #列名を取得 
df_sample.index     #インデックス名を取得
'''

df_sample.columns = ["day_no","class","point1","point2"]   # カラム名を上書き
df_sample.index   = [1,2,3,4,5,6]   # インデックス名を上書きする

print(df_sample)
# Renameメソッドを使う
df_sample.rename(columns={'score1': 'point1'})  #対応関係を辞書型で入れてやる

#◆データの構造を確認する
#データの概要を見てみる

# 行数の確認
len(df_sample)

# 次元数の確認
df_sample.shape #（行数、列数）の形で返す

# カラム情報の一覧
df_sample.info() #カラム名とその型の一覧

# 各列の基礎統計量の確認
# Rでいうところのsummary()
df_sample.describe() # 平均、分散、4分位など

# head / tail
df_sample.head(10) #先頭10行を確認
df_sample.tail(10) #先頭10行を確認

#データをいじってみよう
#データから特定の列だけを選択する
#datacheck.py
#組み込み関数__get_item___を使った選択
df_sample["day_no"] #列名を書いて指定
df_sample[["day_no","point1"]] #複数列を選択する場合にはリスト表記を使う

# locを使った列選択
# 文法 ：iloc[rows, columns]の形で書く
# 列だけでなく行も同時にSubsettingできる
df_sample.loc[:,"day_no"]  # 行は全てを選択するために「:」を入れている。
df_sample.loc[:,["day_no","point1"]] #複数列を選択する場合にはリスト表記を使う     

# ilocを使った列選択
# 文法 ：iloc[rows番号, columns番号]の形で書く
df_sample.iloc[:,0]  # 番号で選択
df_sample.iloc[:,0:2] #複数で連番の場合。リスト表記でも行ける

'''
# ixを使った列選択
# 列名と列番号両方が使える。基本これを使っておけば良い感
df_sample.ix[:,"day_no"] # なお、単列選択の場合には結果はPandas.Series Object
df_sample.ix[:,["day_no","score1"]] # 複数列選択の場合には結果はPandas.Dataframeになる

df_sample.ix[0:4,"score1"] # 行は番号で、列は列名で選択することもできる


series_bool = [True,False,True,False]
df_sample.ix[:,series_bool]  #また、Booleanの配列でも選択できる


#列名の部分一致による選択
#R DplyrにはSelect(Contains()）という、列名部分一致選択のための便利スキームがある
#Pandasにはそれに該当する機能はないため、少し工程を踏む必要がある

score_select = pd.Series(df_sample.columns).str.contains("score") # "score"を列名に含むかどうかの論理判定
df_sample.ix[:,np.array(score_select)]   # 論理配列を使って列選択
'''

#◆Subsetting
#条件文に基づいたデータの部分選択を行います

## Pythonのデフォルトの表記
## データフレーム[Booleanの配列を入れる]
df_sample[df_sample.day_no == "day1"]  # day_no列がday1のデータのみを選択
series_bool = [True,False,True,False,True,False]
df_sample[series_bool] # データフレーム自身の列以外も当然条件に使える


##Pandasのqueryメソッドを使った場合の表記
df_sample.query("day_no == 'day1'")  
     # データフレーム名を2度書く必要が無いため、すっきりする
     # 条件式はStr形式で入れてやらなければならないことに注意

df_sample.query("day_no == 'day1'|day_no == 'day2'")
     # 複数条件の場合は、or条件の "|" もしくは and条件の "&"を間に入れてやる

select_condition = "day1"
#df_sample.query("day_no == select_condition")  # ☓ doesn't work
        # 抽出の条件式はstr表記なので、変数名を直接入れると反応しない

df_sample.query("day_no == @select_condition")  # ◯ it works
        # 変数を使いたい場合には、変数名のアタマに@をつけると、変数名として認識する


## indexを使ってSubsetting
df_sample.query("index == 11 ")  # 普通にindexと書いてやれば動く
df_sample.query("index  in [11,12] ") #　or条件には、「in」も使える

#◆Sorting
#データの並び替えを行います。

df_sample.sort_values("point1")  # Score1の値で昇順でソート
df_sample.sort_values(["point1","point2"])  # point1とpoint2の値で昇順でソート


df_sample.sort_values("point1",ascending=False)  #point1の値で降順でソート
#◆pandas.concat
#データの結合による、レコードや列の追加を行います。 

#concat.py
# 行の追加
#追加したいデータを適当に作ります。データフレーム同士の結合を考えます。
#df_sampleにインデックス「17」をもつレコード追加する場合を想定してみます。 

df_addition_row =\
    pd.DataFrame([["day1","A",100,180]])  #df_sampleと同じ列構造を持つDFを作成
df_addition_row.columns =["day_no","class","score1","score2"]  #同じ列名を付ける
df_addition_row.index   =[17] #インデックスをふる

pd.concat([df_sample,df_addition_row],axis=0)  #結合を行う =rbind
# 第一引数：結合するDFを[]表記で指定する。
# 第二引数：Axis=0で縦方向の結合であることを指定する。


# 列の追加
# Score1、Score2に加えて、Score3の列を追加することを考えます。
# 追加したいデータを適当に作ります。データフレーム同士の結合を考えます。

df_addition_col = pd.DataFrame([[120,160,100,180,110,80]]).T #df_sampleと同じ行数を持つDFを作成

df_addition_col.columns =["score3"] #列名は結合後にもそのまま使われる
df_addition_col.index   = [11,12,13,14,15,16] 
         #注意！！ pandas.concatは結合するもの同士のインデックスが同じ構造でないと、思ったような作用をしません！（後述）


pd.concat([df_sample,df_addition_col],axis=1) #axis=1は横方向の結合を指定します。


# インデックスについて
# 新しいデータのインデックスが結合先と違う場合、データは互い違いな形で結合されます。
# 下記を試してみて下さい

df_addition_col = pd.DataFrame([[120,160,100,180,110,80]]).T

df_addition_col.columns =["score3"]
df_addition_col.index   = [11,12,13,21,22,23]   #一部はもとのデータとインデックスが一致するが、一部は一致しない


pd.concat([df_sample,df_addition_col],axis=1)  # 結果は....
