from matplotlib import pyplot as plt
import numpy as np

data1 = np.random.randn(1000)
data2 = np.random.randn(1000) + 2
plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Multiple Histograms')
plt.legend()
plt.show()
