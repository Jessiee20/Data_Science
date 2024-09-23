import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

# Download stopwords if not already available
nltk.download('stopwords')

# Load dataset from CSV file
def load_data(file_path):
    data = pd.read_csv("C:/Users/jessi/Desktop/FODS/feedback.csv")
    return data['feedback'].dropna()

# Preprocess the text data
def preprocess_text(feedback):
    stop_words = set(stopwords.words('english'))
    processed_feedback = []
    
    for comment in feedback:
        # Convert to lowercase
        comment = comment.lower()
        
        # Remove punctuation
        comment = comment.translate(str.maketrans('', '', string.punctuation))
        
        # Tokenize and remove stop words
        words = comment.split()
        words = [word for word in words if word not in stop_words]
        
        processed_feedback.extend(words)
    
    return processed_feedback

# Calculate the frequency distribution of words
def calculate_word_frequencies(words):
    return Counter(words)

# Display the top N most frequent words
def display_top_words(frequencies, N):
    top_words = frequencies.most_common(N)
    for word, freq in top_words:
        print(f"{word}: {freq}")
    return top_words

# Plot a bar graph of the top N most frequent words
def plot_word_frequencies(top_words):
    words, frequencies = zip(*top_words)
    
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies)
    plt.xlabel('Words')
    plt.ylabel('Frequencies')
    plt.title(f'Top {len(words)} Most Frequent Words')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to run the program
def main():
    # Load data from CSV
    file_path = 'data.csv'  # Ensure this path points to your actual data file
    feedback_data = load_data(file_path)
    
    # Preprocess the feedback data
    words = preprocess_text(feedback_data)
    
    # Calculate word frequencies
    word_frequencies = calculate_word_frequencies(words)
    
    # Get user input for top N words
    N = int(input("Enter the number of top frequent words to display: "))
    
    # Display and plot the top N frequent words
    top_words = display_top_words(word_frequencies, N)
    plot_word_frequencies(top_words)

if __name__ == "__main__":
    main()
