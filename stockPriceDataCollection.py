#BM Pythonで作る株価予測SlackBot

#import vital tools
from selenium import webdriver
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#%matplotlib inline

#browser open (chrome)
browser=webdriver.Chrome()

#ready for scraping
columnNames=[]
ETFComparisonsTable=[]
for num in range(0,48):
    browser.get("https://kabuoji3.com/stock/")
    stockSearch=browser.find_element_by_class_name("form_inputs")
    stockSearchForm=stockSearch.find_element_by_class_name("form_txt")
    stockSearchForm.send_keys("ETF")
    btnClick=browser.find_element_by_class_name("btn_submit")
    btnClick.click()

    #choose a stock out of list
    stockClick=browser.find_elements_by_class_name("clickable")
    stockClick[num].find_element_by_tag_name("a").click()

    stockTable=browser.find_element_by_class_name("table_wrap")
    stockLine=stockTable.find_elements_by_tag_name("tr")

    #price scraping with calculation
    if len(stockLine)==302:
        ETFComparisons=[]
        for i in range(2,152):
            stockETFPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
            stockETFPriceBefore=stockLine[i].find_elements_by_tag_name("td")
            ETFComparison=float(stockETFPriceAfter[6].text)-float(stockETFPriceBefore[6].text)
            ETFComparisons.append(ETFComparison)

        stockETFPriceAfter=stockLine[151].find_elements_by_tag_name("td")
        stockETFPriceBefore=stockLine[153].find_elements_by_tag_name("td")
        ETFComparison=float(stockETFPriceAfter[6].text)-float(stockETFPriceBefore[6].text)
        ETFComparisons.append(ETFComparison)

        for i in range(154,302):
            stockETFPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
            stockETFPriceBefore=stockLine[i].find_elements_by_tag_name("td")
            ETFComparison=float(stockETFPriceAfter[6].text)-float(stockETFPriceBefore[6].text)
            ETFComparisons.append(ETFComparison)

        ETFComparisonsTable.append(ETFComparisons)

        #pick up title
        stockTitleBox=browser.find_element_by_class_name("base_box_ttl")
        stockTitle=stockTitleBox.find_element_by_class_name("jp").text
        columnNames.append(stockTitle)

#making ETF table
ETFTable=pd.DataFrame(ETFComparisonsTable)
ETFTable=ETFTable.T
ETFTable.columns=columnNames
#checking ETF table
ETF.head()


#date scraping
browser.get("https://kabuoji3.com/stock/{}/".format(4307))
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")
dates=[]
for i in range(1,152):
    stockDate=stockLine[i].find_elements_by_tag_name("td")
    stockDate=stockDate[0].text
    dates.append(stockDate)
for i in range(153,302):
    stockDate=stockLine[i].find_elements_by_tag_name("td")
    stockDate=stockDate[0].text
    dates.append(stockDate)
df_date=pd.DataFrame()
df_date["date"]=dates
df_date["year"]=df_date["date"].apply(lambda x:int(x.split("-")[0]))
df_date["month"]=df_date["date"].apply(lambda x:int(x.split("-")[1]))
df_date["day"]=df_date["date"].apply(lambda x:int(x.split("-")[2]))
df_date.head()


#stock scraping (comparison with yesterday)
browser.get("https://kabuoji3.com/stock/{}/".format(4307))
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")
targetStockComparisons=[]
for i in range(2,152):
    targetStockPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
    targetStockPriceBefore=stockLine[i].find_elements_by_tag_name("td")
    targetStockComparison=float(targetStockPriceAfter[6].text)-float(targetStockPriceBefore[6].text)
    targetStockComparisons.append(targetStockComparison)
targetStockPriceAfter=stockLine[151].find_elements_by_tag_name("td")
targetStockPriceBefore=stockLine[153].find_elements_by_tag_name("td")
targetStockComparison=float(targetStockPriceAfter[6].text)-float(targetStockPriceBefore[6].text)
targetStockComparisons.append(targetStockComparison)
for i in range(154,302):
    targetStockPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
    targetStockPriceBefore=stockLine[i].find_elements_by_tag_name("td")
    targetStockComparison=float(targetStockPriceAfter[6].text)-float(targetStockPriceBefore[6].text)
    targetStockComparisons.append(targetStockComparison)
df=pd.DataFrame(targetStockComparisons)
df.columns=["(株)野村総合研究所：前日比"]
df.head()


#add table
stockPriceTable=pd.concat([df_date,ETFTable],axis=1)
stockPriceTable=pd.concat([stockPriceTable,df],axis=1)
stockPriceTable.head()

#prepare for making target values
df_next=df.copy()
df_next.columns=["(株)野村総合研究所：翌日比"]

#date scraping for target values
browser.get("https://kabuoji3.com/stock/{}/".format(4307))
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")
dates=[]
for i in range(2,152):
    stockDate=stockLine[i].find_elements_by_tag_name("td")
    stockDate=stockDate[0].text
    dates.append(stockDate)
for i in range(153,302):
    stockDate=stockLine[i].find_elements_by_tag_name("td")
    stockDate=stockDate[0].text
    dates.append(stockDate)
df_date2=pd.DataFrame()
df_date2["date"]=dates

#making target values table
df_next=pd.concat([df_date2,df_next],axis=1)
df_next.index=df_date2["date"]

#prepare for complete table
table=stockPriceTable[1:299].copy()
table.index=table["date"]

#making complete table
table["(株)野村総合研究所：翌日比"]=df_next["(株)野村総合研究所：翌日比"]
table.tail()

#making csv file
table.to_csv("stockPriceData.csv", index=False)
