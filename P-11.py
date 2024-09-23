import matplotlib.pyplot as plt
import numpy as np

# Step 1: Import necessary libraries
# Already done above

# Step 2: Create sample data
days = np.arange(1, 31)  # Days from 1 to 30
sales = np.random.randint(100, 800, size=len(days))  # Simulated sales data between 100 and 800

# Step 3: Create the figure and subplots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(15, 10))  # 2 rows and 2 columns of subplots

# Step 4: Generate each plot and position them

# Line plot (Top Left - 1st plot)
axs[0, 0].plot(days, sales, marker='o', color='b', linestyle='-', label='Sales')
axs[0, 0].set_title('Line Plot: Product Sales Over Time (1 Month)')
axs[0, 0].set_xlabel('Day of the Month')
axs[0, 0].set_ylabel('Number of Sales')
axs[0, 0].set_ylim(100, 800)  # Adjust y-axis scale
axs[0, 0].set_xticks(np.arange(1, 31, 5))  # Fewer ticks on x-axis (every 5 days)
axs[0, 0].legend()
axs[0, 0].grid(True)

# Scatter plot (Top Right - 2nd plot)
axs[0, 1].scatter(days, sales, color='r', label='Sales')
axs[0, 1].set_title('Scatter Plot: Sales Over Time (1 Month)')
axs[0, 1].set_xlabel('Day of the Month')
axs[0, 1].set_ylabel('Number of Sales')
axs[0, 1].set_ylim(100, 800)  # Adjust y-axis scale
axs[0, 1].set_xticks(np.arange(1, 31, 5))  # Fewer ticks on x-axis (every 5 days)
axs[0, 1].legend()
axs[0, 1].grid(True)

# Bar plot (Bottom Left - 3rd plot)
axs[1, 0].bar(days, sales, color='green')
axs[1, 0].set_title('Bar Plot: Product Sales (1 Month)')
axs[1, 0].set_xlabel('Day of the Month')
axs[1, 0].set_ylabel('Number of Sales')
axs[1, 0].set_ylim(100, 800)  # Adjust y-axis scale
axs[1, 0].set_xticks(np.arange(1, 31, 5))  # Fewer ticks on x-axis (every 5 days)
axs[1, 0].grid(axis='y')

# Remove the unused bottom-right plot
fig.delaxes(axs[1, 1])

# Step 5: Display the plots in a merged form
plt.tight_layout()  # Adjust spacing between plots
plt.show()
