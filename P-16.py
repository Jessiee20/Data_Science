from collections import Counter
import re

# Small input dataset of customer reviews
reviews = [
    "Good product.",
    "Bad quality.",
    "Product is good."
]

# Function to clean and tokenize reviews
def clean_and_tokenize(review):
    # Remove special characters and convert to lowercase
    review = re.sub(r'[^\w\s]', '', review.lower())
    # Tokenize the review (split by whitespace)
    return review.split()

# Combine all reviews into one text
all_reviews = ' '.join(reviews)

# Clean and tokenize the combined reviews
words = clean_and_tokenize(all_reviews)

# Calculate frequency distribution using Counter
word_frequency = Counter(words)

# Print the frequency distribution
for word, freq in word_frequency.items():
    print(f'{word}: {freq}')
