import numpy as np 
import matplotlib.pyplot as plt


# Step plots are useful for visualizing data that changes at discrete intervals. 
# They are often used to represent data that changes in steps, like digital signals.

x = np.linspace(0, 10, 11)
y = np.sin(x)
plt.step(x, y, where='mid', linestyle='--', color='g')
plt.fill_between(x, y, step='mid', alpha=0.2)
plt.title('Basic Step Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()