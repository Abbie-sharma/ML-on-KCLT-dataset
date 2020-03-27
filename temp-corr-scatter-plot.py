import numpy
import pandas
names = ['actual_mean_temp','actual_min_temp','actual_max_temp','average_min_temp','average_max_temp','record_min_temp','record_max_temp']
#data = pandas.read_csv(KCLT.csv, names=names)
correlations = df.corr()
# plot correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()
from pandas.plotting import scatter_matrix
scatter_matrix(df, figsize=[20,20])
plt.show()
