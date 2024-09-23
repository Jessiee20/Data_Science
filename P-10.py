import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [5000, 6000, 5500, 7000, 6500, 8000, 7500, 8500, 9000, 9500, 10000, 10500]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.plot(months, sales, marker='o', linestyle='-', color='b', label='Monthly Sales')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales')
ax1.set_title('Monthly Sales Data - Line Plot')
ax1.legend()
ax1.grid(True)
ax2.bar(months, sales, color='c', edgecolor='black')
ax2.set_xlabel('Month')
ax2.set_ylabel('Sales')
ax2.set_title('Monthly Sales Data - Bar Plot')
ax2.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
