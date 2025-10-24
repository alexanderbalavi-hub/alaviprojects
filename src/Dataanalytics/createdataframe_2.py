import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#erstellt einen DataFrame (Tabelle) mit 36 Werten in einer 6x6 Matrix (6 Spalten und 6 Zeilen)
np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape(6,6),index=['r1','r2','r3','r4','r5','r6'],columns=['c1','c2','c3','c4','c5','c6'])
print(DF_obj)

#einzelne Spalten und Zeilen ausgeben
#hier geben spalte 1,2 und zeile 1,2 aus
location = DF_obj.loc[['r1','r2'],['c1','c2']]
print(location)

#einen Bereich ausgeben lassen von row 3 bis row4
area = DF_obj[2:4]
print(area)

#Werte kleiner 0.2 als boolean auswerten
filter = DF_obj < 0.2
print(filter)