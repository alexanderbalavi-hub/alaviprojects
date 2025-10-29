import pandas as pd
import numpy as np
import numpy.random as randn
import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams
import scipy
from scipy.stats import pearsonr

adress = "src/uebung/Dataanalytics/mtcars.csv"
cars = pd.read_csv(adress)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.set_index('car_names', inplace=True) #ignore car_names as this is a string and not needed for the correlation
print(cars)

cars.corr() #gives out the peasron correltation koefficient matrix. R = 1 high correlation, R = -1 high anti correlation, R = 0 no correlation
print(cars.corr())

