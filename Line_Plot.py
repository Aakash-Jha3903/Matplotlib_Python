import matplotlib.pyplot as plt
import numpy as np


products = ["Mouse", "Keyborad", "Laptop", "Mobile", "Headphone"]
price = [101, 110, 103, 115, 100]
plt.plot(products, price)
plt.plot(products, price, color='red', linestyle='--', linewidth=2)
plt.plot(products, price, marker='o', markersize=20, markerfacecolor='red')
plt.xlabel('Products')
plt.ylabel('Price')
plt.title('Products Line Plot')
plt.grid(True)
plt.grid(color='gray', linestyle=':')
plt.show()