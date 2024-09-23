import numpy as np
from scipy import stats

# Example data for conversion rates
# Assuming you have the conversion rates for each visitor in both groups
# Group A: conversion rates for visitors who experienced design A
# Group B: conversion rates for visitors who experienced design B

# Replace the arrays below with your actual conversion rate data
group_A = np.array([0, 1, 0, 1, 0, 1, 0, 0, 1, 1])  # 0 = no conversion, 1 = conversion
group_B = np.array([0, 0, 1, 1, 0, 0, 0, 1, 1, 1])

# Perform two-sample t-test (independent samples)
t_stat, p_value = stats.ttest_ind(group_A, group_B)

# Print the results
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Significance level
alpha = 0.05

# Check if the difference is statistically significant
if p_value < alpha:
    print("There is a statistically significant difference between the two groups.")
else:
    print("There is no statistically significant difference between the two groups.")
