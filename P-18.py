# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Creating the dataset
data = {
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    '%fat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Calculating the mean, median, and standard deviation for 'age' and '%fat'
age_mean = df['age'].mean()
age_median = df['age'].median()
age_std = df['age'].std()

fat_mean = df['%fat'].mean()
fat_median = df['%fat'].median()
fat_std = df['%fat'].std()

print(f"Mean of age: {age_mean}, Median of age: {age_median}, Std dev of age: {age_std}")
print(f"Mean of %fat: {fat_mean}, Median of %fat: {fat_median}, Std dev of %fat: {fat_std}")

# Drawing all plots in a single figure
fig, axs = plt.subplots(3, 2, figsize=(15, 15))

# Boxplot for 'age'
sns.boxplot(y=df['age'], ax=axs[0, 0])
axs[0, 0].set_title('Boxplot of Age')

# Boxplot for '%fat'
sns.boxplot(y=df['%fat'], ax=axs[0, 1])
axs[0, 1].set_title('Boxplot of %fat')

# Scatter plot
axs[1, 0].scatter(df['age'], df['%fat'], color='b', marker='o')
axs[1, 0].set_title('Scatter plot of Age vs %fat')
axs[1, 0].set_xlabel('Age')
axs[1, 0].set_ylabel('%fat')
axs[1, 0].grid(True)

# Q-Q plot for 'age'
stats.probplot(df['age'], dist="norm", plot=axs[1, 1])
axs[1, 1].set_title('Q-Q plot for Age')

# Q-Q plot for '%fat'
stats.probplot(df['%fat'], dist="norm", plot=axs[2, 0])
axs[2, 0].set_title('Q-Q plot for %fat')

# Hide the empty subplot
axs[2, 1].axis('off')

plt.tight_layout()
plt.show()
