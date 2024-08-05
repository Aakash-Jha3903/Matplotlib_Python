import matplotlib.pyplot as plt
import numpy as np

products = ["Mouse", "Keyborad", "Laptop", "Mobile", "Headphone"]
price = [101, 110, 103, 115, 100]
quantity=[30, 60, 40, 80, 90]
plt.plot(products, price, label='Price')
plt.plot(products, quantity, label='Quantity', linestyle='--')
plt.legend()
plt.show()