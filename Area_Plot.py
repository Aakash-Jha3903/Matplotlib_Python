import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.fill_between(x, y1, color='skyblue', alpha=0.5, label='sin(x)')
plt.fill_between(x, y2, color='lightgreen', alpha=0.5, label='cos(x)')
plt.title('Basic Area Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()