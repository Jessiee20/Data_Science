# Step 1: Import necessary libraries
import pandas as pd

# Step 2: Sample sales data (assuming you have a Pandas DataFrame)
# Example data
data = {
    'customer_id': [101, 102, 103, 104, 105, 106, 107],
    'age': [25, 30, 22, 30, 25, 40, 22],
    'purchase_amount': [100, 150, 200, 50, 120, 300, 80]
}

# Step 3: Create the DataFrame
df = pd.DataFrame(data)

# Step 4: Calculate the frequency distribution of customer ages
age_distribution = df['age'].value_counts()

# Step 5: Display the frequency distribution
print("Frequency Distribution of Customer Ages:")
print(age_distribution)
