import configparser
import urllib
import sqlite3
from contextlib import closing
from sqlite3 import Error

import datetime
import os.path
import zipfile
import csv
from sklearn.ensemble import RandomForestClassifier

lscode=[];
ltday=[];



def main():
   database = "stockdatadase.db"

    # create a database connection
   conn = create_connection(database)
   
   with conn:
      #delete_task(conn, 2)
      #delete_all_tasks(conn)
      learn_db_init(database)



def learn_db_init(db_file):
   #dbname = 'stockdatabase.db'
   with closing(sqlite3.connect(db_file)) as conn:
      con = conn.cursor()

      # executeメソッドでSQL文を実行する
      # ここでは、もしusersテーブルが存在していたら、一旦削除します。
      drop_table = '''drop table if exists users'''
      con.execute(drop_table)
      # ここでは、もしusersテーブルが存在していなかったら、作成します。
      create_table = '''create table if not exists users (id int, name varchar(64), age int, gender varchar(32))'''
      con.execute(create_table)

      # SQL文に値をセットする場合は，Pythonのformatメソッドなどは使わずに，
      # セットしたい場所に?を記述し，executeメソッドの第2引数に?に当てはめる値を
      # タプルで渡す．
      sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
      user = (1, '高橋', 34, 'male')
      con.execute(sql, user)

      # 一度に複数のSQL文を実行したいときは，タプルのリストを作成した上で
      # executemanyメソッドを実行する
      insert_sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
      # タプルデータの配列
      users = [
          (2, '斎藤', 23, 'male'),
          (3, '井上', 34, 'mail'),
          (4, '水谷', 32, 'female'),
          (5, '小林', 19, 'male')
      ]
      con.executemany(insert_sql, users)
      conn.commit()

      select_sql = 'select * from users'
      for row in con.execute(select_sql):
          print(row)

   return con


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn




def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_tasks(con):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM tasks'
    cur = con.cursor()
    cur.execute(sql)
    conn.commit()






def learn_db_init():
   # データベースに接続する
   conn = sqlite3.connect('example.db')#example.dbと同名のファイルがなければ，ファイルが作成されます   
   c = conn.cursor()#


   # レコードを生年月日の降順で取得する
   for row in c.execute('SELECT * FROM users ORDER BY birtyday DESC'):
      print(row)

   # データベースへのアクセスが終わったら close する
   conn.close()





   # データベースに接続する
   conn = sqlite3.connect('example.db')
   c = conn.cursor()
   # テーブルの作成
   c.execute('''CREATE TABLE users(id real, name text, birtyday text)''')

   # データの挿入
   c.execute("INSERT INTO users VALUES (1, '煌木 太郎', '2001-01-01')")
   c.execute("INSERT INTO users VALUES (2, '学習 次郎', '2006-05-05')")
   c.execute("INSERT INTO users VALUES (3, '牌存 花子', '2017-09-10')")

   # 挿入した結果を保存（コミット）する
   conn.commit()

   # データベースへのアクセスが終わったら close する
   conn.close()


























   conn = sqlite3.connect("N255.csv");
   c = conn.cursor();
   query = "select scode from chrt group by scode order by scode";
   #c.execute('query')
   for row in c:
      lscode.append(row[0]);
   query = "select tday from chrt group by tday order by tday"; 
   c.execute(query)
   for row in c:
      ltday.append(row[0]);
   conn.close();


def rnd_forest(ltree_scode,tscode,tdate):#株価予想
   
   conn = sqlite3.connect("chart.db");
   c = conn.cursor();

   ltra_x=[];    
   ltra_y=[];
   ltest_x=[];

   dp = -1;
   for i in range(0,len(ltday)):
      if ltday[i]==tdate:
         dp=i;
         break;
   if dp-102 < 0:  #&lt:#0:
      return 0;

   whe="";
   for sc in ltree_scode:
      if whe!="":
         whe = whe + "or";
      whe = whe + "(scode='"+sc+"')";

   lr={};
   lbr={};
   for s in ltree_scode:
      lr[s]=-1;
      lbr[s]=-1;   
   for d in range(dp-102,dp,1):      
      query = "select scode,val from chrt where (tday='%s')and(%s) order by scode" % \
            (ltday[d],whe);
      c.execute(query);
      for row in c:
         lr[row[0]]=row[1];      

      if d > dp-102:      
         lx=[];
         for s in ltree_scode:
            if lr[s] < lbr[s]:
               lx.append(-1);
            else:
               lx.append(1);   
            lbr[s]=lr[s];
         if d==dp-1:
            ltest_x=lx;            
         else:
            ltra_x.append(lx); 

      for s in ltree_scode:
         if lr[s] > 0:
            lbr[s]=lr[s];


   query = "select tday,val from chrt where (scode='%s')and(tday>='%s')and(tday<'%s') order by tday" % \
            (tscode,ltday[dp-101],ltday[dp]);
   c.execute(query)
   r=-1;
   for row in c:
      if r>0:
         if r < row[1]:
            ltra_y.append(1);
         else:
            ltra_y.append(-1);
      r=row[1];

   conn.close();

   classifier = RandomForestClassifier(n_estimators=len(ltree_scode), random_state=0,max_depth=5);
   classifier.fit(ltra_x,ltra_y);
   ret = classifier.predict([ltest_x]);

   return ret;      
   print(tdate,ret); 
#--------------------------------------------------------------------------------------------------
#learn_db_init();


if __name__ == '__main__':
    main()
    

letf=["1309","1313","1314","1322","1326","1343","1543","1548","1551","1633","1671","1673","1678","1681","1682","1693","1698","1699"];
ans=rnd_forest(letf,'6758',"2017-03-07");  