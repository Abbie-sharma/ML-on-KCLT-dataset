import pandas as pd
import numpy as np
#np.random.seed(1234)
df = pd.read_csv(('KCLT.csv'))
boxplot = df.boxplot(column=['actual_mean_temp', 'actual_min_temp', 'actual_max_temp'])
#df.show()
