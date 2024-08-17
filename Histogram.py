from matplotlib import pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
#plt.hist(data, bins=5, orientation='vertical')
plt.hist(data, bins=5, orientation='vertical', color='skyblue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
plt.show()