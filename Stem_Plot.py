from matplotlib import pyplot as plt
import numpy as np

# Stem plots are useful for visualizing data points along a baseline, with lines (stems) extending from the baseline to the data points. 
# This type of plot is particularly useful for displaying discrete data points.

x = np.linspace(0.1, 2 * np.pi, 10)
y = np.sin(x)
plt.stem(x, y, linefmt='--')
plt.title('Basic Stem Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()