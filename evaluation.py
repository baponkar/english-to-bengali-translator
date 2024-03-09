from nltk.translate.bleu_score import corpus_bleu

def calculate_bleu_score(reference_corpus, predicted_corpus):
    return corpus_bleu(reference_corpus, predicted_corpus)

# Example usage:
bleu_score = calculate_bleu_score(reference_corpus, predicted_corpus)

