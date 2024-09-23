import numpy as np
sales_data = np.array([20000, 25000, 30000, 40000])
total_sales = np.sum(sales_data)
q1_sales = sales_data[0]
q4_sales = sales_data[3]
percentage_increase = ((q4_sales - q1_sales) / q1_sales) * 100
print("Total sales for the year:", total_sales)
print("Percentage increase from Q1 to Q4:", percentage_increase, "%")
