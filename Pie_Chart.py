from matplotlib import pyplot as plt

labels = ['Mouse', 'Keyboard', 'Laptop', 'Mobile', 'Headphone']
sizes = [30, 60, 40, 80, 90]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0, 0.1, 0, 0, 0)
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True)
plt.title('Basic Pie Chart')
plt.axis('equal')
plt.legend(labels, loc='upper right')
plt.show()