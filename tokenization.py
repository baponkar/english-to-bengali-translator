from tokenizers import BertWordPieceTokenizer

def tokenize_data(english_sentences, bengali_sentences):
    tokenizer = BertWordPieceTokenizer()
    tokenizer.train(english_sentences + bengali_sentences)
    
    tokenized_english_sentences = [tokenizer.encode(sentence).tokens for sentence in 
english_sentences]
    tokenized_bengali_sentences = [tokenizer.encode(sentence).tokens for sentence in 
bengali_sentences]

    return tokenized_english_sentences, tokenized_bengali_sentences

# Example usage:
english_data, bengali_data = tokenize_data(english_data, bengali_data)

