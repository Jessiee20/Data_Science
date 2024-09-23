# Step 1: Import necessary libraries
from collections import Counter
import string

# Step 2: Define a function to preprocess and count word frequencies
def count_word_frequencies(file_path):
    try:
        # Step 3: Read the text document
        with open(file_path, 'r') as file:
            text = file.read()

        # Step 4: Preprocess the text
        # Convert to lowercase and remove punctuation
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Split text into words
        words = text.split()

        # Step 5: Count the frequency of each word using Counter
        word_count = Counter(words)

        # Display the frequency distribution
        for word, count in word_count.items():
            print(f'{word}: {count}')

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

# Step 6: Specify the path to the text document and call the function
file_path = 'sample_text.txt'
count_word_frequencies(file_path)
