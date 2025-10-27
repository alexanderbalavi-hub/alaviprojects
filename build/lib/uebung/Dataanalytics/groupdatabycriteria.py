import pandas as pd
import numpy as np
from pandas import DataFrame,Series

#define a dataset for a vehicles and their power
data = {
    'Vehicle': ['Car', 'Truck', 'Bike', 'Car', 'Truck', 'Bike', 'Car'],
    'Power': [150, 300, 20, 200, 350, 25, 180]
}
#Create a DataFrame from the dataset
DF_obj = pd.DataFrame(data)
print("Original DataFrame:", DF_obj)
# Group by 'Vehicle' and calculate the mean power
gr=DF_obj.groupby('Vehicle').mean()
print(gr)
# Group by 'Vehicle' and calculate the minimum power
gr2=DF_obj.groupby('Vehicle').min() 
print(gr2)
# Group by 'Vehicle' and calculate the maximum power
gr3=DF_obj.groupby('Vehicle').max()
print(gr3)
# Group by 'Vehicle' and calculate the sum of power
gr4=DF_obj.groupby('Vehicle').sum()
print(gr4)
# Group by 'Vehicle' and count the number of entries
gr5=DF_obj.groupby('Vehicle').count()
print(gr5)
# Group by 'Vehicle' and get descriptive statistics
gr6=DF_obj.groupby('Vehicle').describe()
print(gr6)
# Group by 'Vehicle' and get the size of each group
gr7=DF_obj.groupby('Vehicle').size()
print(gr7)
