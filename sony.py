import ConfigParser
import urllib
import sqlite3
import datetime
import os.path
import zipfile
import csv
from sklearn.ensemble import RandomForestClassifier

lscode=[];
ltday=[];

def learn_db_init():

   conn = sqlite3.connect("chart.db");
   c = conn.cursor();
   query = "select scode from chrt group by scode order by scode";
   c.execute(query)
   for row in c:
      lscode.append(row[0]);
   query = "select tday from chrt group by tday order by tday"; 
   c.execute(query)
   for row in c:
      ltday.append(row[0]);
   conn.close();

def rnd_forest(ltree_scode,tscode,tdate):

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
   if dp-102 &lt:#0:
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

      if d &gt; dp-102:      
         lx=[];
         for s in ltree_scode:
            if lr[s] &lt; lbr[s]:
               lx.append(-1);
            else:
               lx.append(1);   
            lbr[s]=lr[s];
         if d==dp-1:
            ltest_x=lx;            
         else:
            ltra_x.append(lx); 

      for s in ltree_scode:
         if lr[s] &gt; 0:
            lbr[s]=lr[s];


   query = "select tday,val from chrt where (scode='%s')and(tday>='%s')and(tday<'%s') order by tday" % \
            (tscode,ltday[dp-101],ltday[dp]);
   c.execute(query)
   r=-1;
   for row in c:
      if r>0:
         if r &lt; row[1]:
            ltra_y.append(1);
         else:
            ltra_y.append(-1);
      r=row[1];

   conn.close();

   classifier = RandomForestClassifier(n_estimators=len(ltree_scode), random_state=0,max_depth=5);
   classifier.fit(ltra_x,ltra_y);
   ret = classifier.predict([ltest_x]);

   return ret;      
   print tdate,ret; 
#--------------------------------------------------------------------------------------------------
learn_db_init();
letf=["1309","1313","1314","1322","1326","1343","1543","1548","1551","1633","1671","1673","1678","1681","1682","1693","1698","1699"];
ans=rnd_forest(letf,'6758',"2017-03-07");  