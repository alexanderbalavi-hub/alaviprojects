import numpy as np
import pandas as pd

# Create a Series object with 8 rows using numpy arange
data = np.arange(8)
series = pd.Series(data)

print(series)
newseries = series[3]
print(newseries)
