import re

def preprocess_data(english_sentences, bengali_sentences):
    # Remove special characters and extra whitespaces
    english_sentences = [re.sub(r'[^a-zA-Z0-9\s]', '', sentence) for sentence in 
english_sentences]
    bengali_sentences = [re.sub(r'[^\u0980-\u09FF\s]', '', sentence) for sentence in 
bengali_sentences]

    # Convert to lowercase
    english_sentences = [sentence.lower() for sentence in english_sentences]
    bengali_sentences = [sentence.lower() for sentence in bengali_sentences]

    return english_sentences, bengali_sentences

# Example usage:
english_data, bengali_data = preprocess_data(english_data, bengali_data)

