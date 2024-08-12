import matplotlib.pyplot as plt

products = ["Mouse", "Keyborad", "Laptop", "Mobile", "Headphone"]
price = [101, 110, 103, 115, 100]
#plt.scatter(products, price)
sizes = [20, 50, 80, 200, 500]  # Marker sizes
colors = ['red', 'green', 'blue', 'cyan', 'magenta']  # Marker colors
plt.scatter(products, price, s=sizes, c=colors)
# Annotate specific points
for i, txt in enumerate(['A', 'B', 'C', 'D', 'E']):
    plt.annotate(txt, (products[i], price[i]))
plt.show()