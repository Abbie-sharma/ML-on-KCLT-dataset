import matplotlib.pyplot as plt
import numpy as np

# data to plot
n_groups = 3
minn = (df['actual_mean_temp'].min(), df['actual_min_temp'].min(), df['actual_max_temp'].min())
maxx = (df['actual_mean_temp'].max(),df['actual_min_temp'].max(),df['actual_max_temp'].max())

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, minn, bar_width,
alpha=opacity,
color='b',
label='Min')

rects2 = plt.bar(index + bar_width, maxx, bar_width, alpha=opacity,color='r',label='Max')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Weather')
plt.xticks(index + bar_width, ('Actual_mean_temp', 'Actual_min_temp', 'Actual_max_temp'))
plt.legend()

plt.tight_layout()
plt.show()
