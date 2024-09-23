# Step 1: Import necessary libraries
import pandas as pd

# Step 2: Sample user interaction data (assuming a Pandas DataFrame)
# Example data
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7],
    'likes': [10, 20, 10, 30, 20, 10, 40]
}

# Step 3: Create the DataFrame
df = pd.DataFrame(data)

# Step 4: Calculate the frequency distribution of likes
likes_distribution = df['likes'].value_counts()

# Step 5: Display the frequency distribution
print("Frequency Distribution of Likes:")
print(likes_distribution)
