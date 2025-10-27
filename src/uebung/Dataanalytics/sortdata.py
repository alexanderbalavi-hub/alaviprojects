import pandas as pd
import numpy as np
from pandas import DataFrame,Series

#define a series object with unsorted values
series_obj = pd.Series([12,27,13,1,5,7,9])
#sort the series object in ascending order
series_obj = series_obj.sort_values()
print(series_obj)

#define a series object with unsorted strings
series_obj_2 = pd.Series(['banana','apple','orange','kiwi','mango'])
series_obj_2 = series_obj_2.sort_values()
print(series_obj_2)


