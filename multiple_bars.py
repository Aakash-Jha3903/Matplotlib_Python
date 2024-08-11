import matplotlib.pyplot as plt
import numpy as np

products = ["Mouse", "Keyborad", "Laptop", "Mobile", "Headphone"]
price = [101, 110, 103, 115, 100]
quantity=[30, 60, 40, 80, 90]
width=0.3

products_index = np.arange(len(products))
products_index_set = [j+width for j in products_index]
plt.bar(products_index, price, color='red', width=width, label='Price')
plt.bar(products_index_set, quantity, color='blue', width=width, label='Quantity')
plt.xticks(products_index+width/2, products, rotation=20)
plt.legend()
plt.show()