import numpy as np
house_data = np.array([[3, 2000, 350000], 
                       [5, 3000, 500000], 
                       [4, 2500, 400000], 
                       [6, 4000, 750000]])
houses_with_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]
sale_prices = houses_with_more_than_4_bedrooms[:, 2]
average_sale_price = np.mean(sale_prices)
print("Average sale price of houses with more than four bedrooms:", average_sale_price)
