import pandas as pd
import numpy as np
from pandas import DataFrame,Series

#define first dataframe
DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
#define second dataframe
DF_obj_2 = pd.DataFrame(np.arange(15).reshape(5,3))
#define first series object
series_obj2 = pd.Series(np.arange(7))
#define second series object
series_obj3 = pd.Series(np.arange(3))
#delete 3rd row of series_obj2
series_obj2.drop(2)
#delete 2nd row of dataframe DF_obj
DF_obj.drop(1)
#delete 2nd column of dataframe DF_obj
DF_obj.drop(1,axis=1)
print(DF_obj.drop(1,axis=1))
