import matplotlib.pyplot as plt


products = ["Mouse", "Keyborad", "Laptop", "Mobile", "Headphone"]
price = [101, 110, 103, 115, 100]
#plt.bar(products, price)
#plt.bar(products, price, color='red', width=0.5)
plt.bar(products, price, color=['r', 'g', 'y'], width=0.5)
#plt.barh(products, price, color=['r', 'g', 'y'])
bars = plt.bar(products, price, color=['r', 'g', 'y'], width=0.5)
plt.xlabel('Products')
plt.ylabel('Price')
plt.title('Products Bar Plot')
plt.grid(axis='x', linestyle='--')
plt.grid(axis='y', linestyle=':')
# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontsize=15)
plt.show()