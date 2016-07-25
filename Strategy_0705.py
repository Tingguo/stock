import tushare as ts
import math
import numpy as np
import pandas as pd
import xlsxwriter


all_codes = pd.read_csv('SH_A_CODES.xlsx')
all_codes = list(all_codes[0].values)
result = []
for code in all_codes:
    data = ts.get_hist_data(code, start='2016-06-05', end='2016-07-18')
    if type(data) == pd.core.frame.DataFrame:
        print code
        # data = data.iloc[::-1]
        opens = data['open'].values
        highs = data['high'].values
        closes = data['close'].values
        lows = data['low'].values
        volumes = data['volume'].values
        ma5 = data['ma5'].values
        if len(ma5) > 15 and ma5.argmin()>=2 and ma5.argmin()<=4:
            print '*************'
            print code
            print '*************'
            result.append(code)
            # tmp = ma5[4:8] - ma5[3:7]
            # if min(tmp) > 0:
            #     tmp1 = sum(lows[2:9])/8
            #     tmp2 = sum(highs[0:9])/10
            #     if highs[0] > tmp2 and lows[2] < tmp1:
            #         print '*************'
            #         print code
            #         print '*************'
            #         result.append(code)

# execfile('C:\\Users\\guo090\\tguo\\STOCK\\NewStart\\stock_project\\stock_project\\Strategy_0705.py')