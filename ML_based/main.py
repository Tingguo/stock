from data import getStock_A, getStock_C
from featureGeneration import addFeatures
from machineLearning import Classify
from preprocess import Prep
from CV import CV
from performance import Portfolio, MarketIntradayPortfolio
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from pylab import *
from datetime import datetime

HS300 = getStock_C('000300')