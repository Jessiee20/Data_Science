import numpy as np
sales_data = np.array([[10, 25, 250],  
                       [5,  30, 150],  
                       [8,  20, 160]]) 
prices = sales_data[:, 1]
average_price = np.mean(prices)
print("Average price of all products sold:", average_price)
