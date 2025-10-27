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
#concat series objects
pd.concat([series_obj2,series_obj3])
#concat dataframe objects
pd.concat([DF_obj,DF_obj_2])
print(pd.concat([DF_obj,DF_obj_2]))


