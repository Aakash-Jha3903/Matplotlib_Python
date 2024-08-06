import matplotlib.pyplot as plt
import numpy as np

products = ["Mouse", "Keyborad", "Laptop", "Mobile", "Headphone"]
price = [101, 110, 103, 115, 100]
quantity=[30, 60, 40, 80, 90]

plt.subplot(2, 1, 1)  #(rows, columns, index) - first subplot
plt.plot(products, price, label='Price')
plt.title('Price')

plt.subplot(2, 1, 2)  #(rows, columns, index) - second subplot
plt.plot(products, quantity, label='Quantity')
plt.title('Quantity')

plt.tight_layout()

plt.show()