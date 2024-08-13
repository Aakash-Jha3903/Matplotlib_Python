import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [10, 15, 13, 17, 20]

x2 = [1, 2, 3, 4, 5]
y2 = [20, 25, 23, 27, 30]

plt.scatter(x1, y1, color='blue', label='Group 1')
plt.scatter(x2, y2, color='red', label='Group 2')

plt.legend()
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Multiple Scatter Plots')
plt.show()