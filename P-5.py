import numpy as np
fuel_efficiency = np.array([20, 25, 30, 35, 40, 45])
average_efficiency = np.mean(fuel_efficiency)
model1_efficiency = fuel_efficiency[1]  
model2_efficiency = fuel_efficiency[4] 
percentage_improvement = ((model2_efficiency - model1_efficiency) / model1_efficiency) * 100
print("Average fuel efficiency of all car models:", average_efficiency, "mpg")
print("Percentage improvement from model 1 to model 2:", percentage_improvement, "%")
