from data import getStock_C
from featureGeneration import addFeatures
from machineLearning import Classify
from preprocess import Prep
from CV import CV
from performance import Portfolio,MarketIntradayPortfolio
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from pylab import *
from datetime import datetime
import tushare as ts

# get all codes
all_codes = ts.get_today_all()
# all_codes = pd.read_csv('SH_A_CODES.xlsx')
all_codes = all_codes['code'].values
result = []
for code in all_codes:
    Train = getStock_C(code, '2005-01-01', '2016-07-22')
    if len(Train) < 2000:
        continue
    else:
        Train = addFeatures(Train)
        Train.drop('ADOSC', axis=1)
        X_train, y_train, X_test, y_test = Prep(Train, datetime(2016, 7, 22))
        clf = LDA()
        y_pred = clf.fit(X_train, y_train).predict(X_test)
        if y_pred > 0:
            result.append(code)
            print code

open("result.txt", "w").write("\n".joint("".join(item)) for item in result)
        
