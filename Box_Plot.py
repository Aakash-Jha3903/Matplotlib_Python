from matplotlib import pyplot as plt
import numpy as np
# Box plots, also known as box-and-whisker plots, are a standardized way of displaying the distribution of data based on a five-number summary: 
# minimum, first quartile (Q1), median, third quartile (Q3), and maximum. They are useful for identifying outliers and understanding the spread and skewness of data.

np.random.seed(10)
data = np.random.normal(100, 10, 200)
plt.boxplot(data)
plt.title('Basic Box Plot')
plt.ylabel('Values')
plt.show()