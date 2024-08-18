import matplotlib.pyplot as plt
import numpy as np

# Adding Density Plot
# Generate random data
data = np.random.randn(10000)

# Create histogram with density plot
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

# Add density plot
density = np.linspace(min(data), max(data), 100)
plt.plot(density, 1/(np.sqrt(2 * np.pi)) * np.exp(-0.5 * density**2), color='r')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram with Density Plot')
plt.show()