import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#lese eine csv datei ein

address = 'c:/Users/em75ir1/OneDrive - Volkswagen AG/Save/Dokumente/Training/Programmieren/programming-foundations-esst-3159482-cs-main/Kapitel_01_bis_09/code/src/Dataanalytics/mtcars.csv'

cars = pd.read_csv(address)
cars.head()

cars.columns = ['car names' , 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

cars.head()
print(cars.head())

#generiere einen Dataframe aus den eingelesenen Daten
DF_obj = DataFrame(cars)
print(DF_obj)
