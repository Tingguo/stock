# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 09:42:16 2016

@author: tguo
"""

#import urllib.parse
#import urllib.request
import urllib2
from urllib2 import Request
from bs4 import BeautifulSoup

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

All_code = []

stockTypes = {
           '001': '国债现货',
           '110': '企业债券',  
           '120': '企业债券',
           '129': '可转换债券',
           '100': '可转换债券',
           '201': '国债回购',
           '310': '基金',
           '500': '基金',  
           '550': '企业债券',
           '710': '转配股',
           '701': '转配股再配股',
           '711': '转配股再配股',
           '720': '红利',  
           '735': '新基金申购',  
           '737': '新股配售',
           '300': '创业板',  
           '600': '沪市A股',  
           '601': '沪市A股',
           '603': '沪市A股',
           '900': '沪市B股',
           '000': '深市A股',
           '002': '中小板',
           '200': '深市B股',
           '730': '新股申购',
           '700': '沪市配股',
           '080': '深市配股',
           '580': '沪市权证',
           '031': '深市权证',
           '18':'深交所基金',
           '50':'上交所基金',
           '16':'深交所基金',
           '51':'上交所基金',
           '15':'深交所基金',
 }
 
#获取网页请求信息
url = 'http://quote.eastmoney.com/stocklist.html'
req = Request(url)
response = urllib2.urlopen(req)
responseContent = response.read()
soup = BeautifulSoup(responseContent,from_encoding="gb18030")
index = [5,9]
j = 4

for j in index:
    content = soup.find(id="quotesearch").contents[j]
    for string in content.strings:
        if len(string) > 10:
            str1 = string.split('(')
            stockType = '其他类型'
            stockName = str1[0]
            stockCode = str1[1][0:6]
            startCode = stockCode[0:3]
            if startCode in stockTypes:
                stockType = stockTypes.get(startCode)
            else:
                startCode1 = stockCode[0:2]
                if startCode1 in stockTypes:
                    stockType = stockTypes.get(startCode1)
            #print(stockName+':'+stockCode+':'+stockType)
            if startCode == '600' or startCode == '601' or startCode == '603':
                All_code.append(stockCode)

# generate excel file
workbook = xlsxwriter.Workbook('SH_A_CODES.xlsx')
worksheet = workbook.add_worksheet('result')
row = 0
col = 0

for i in All_code:
    worksheet.write(row,col,i)    
    row += 1
workbook.close()


# execfile('C:\\Users\\guo090\\tguo\\STOCK\\NewStart\\stock_project\\stock_project\\Strategy_test.py')