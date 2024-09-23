import matplotlib.pyplot as plt

# Step 2: Prepare the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [30, 32, 35, 37, 40, 42, 43, 41, 38, 35, 32, 30]  # Monthly temperature values
rainfall = [78, 56, 34, 20, 10, 5, 2, 3, 12, 40, 60, 80]  # Monthly rainfall values

# Step 3: Create a line plot for temperature
plt.figure(figsize=(10, 5))  # Setting figure size for clear visibility
plt.subplot(1, 2, 1)  # Create a subplot with 1 row and 2 columns, position 1
plt.plot(months, temperature, marker='o', color='r', linestyle='-', label='Temperature')
plt.title('Monthly Temperature')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()

# Step 4: Create a scatter plot for rainfall
plt.subplot(1, 2, 2)  # Position 2 in the 1x2 grid
plt.scatter(months, rainfall, color='b', label='Rainfall')
plt.title('Monthly Rainfall')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.legend()

# Step 5: Display the plots
plt.tight_layout()  # Adjust the layout to prevent overlap
plt.show()
