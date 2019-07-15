import numpy as np
np.random.seed(19680801)
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
for color in ['tab:orange', 'tab:green']:
     x, y = np.random.rand(2, 5)
     ax.scatter(x, y, c=color, label=color,
               alpha=0.8, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()