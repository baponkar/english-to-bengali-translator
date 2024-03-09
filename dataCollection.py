import requests
from bs4 import BeautifulSoup

def scrape_parallel_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    english_sentences = []
    bengali_sentences = []

    for item in soup.find_all('div', class_='parallel'):
        english_sentence = item.find('div', class_='english').text.strip()
        bengali_sentence = item.find('div', class_='bengali').text.strip()

        english_sentences.append(english_sentence)
        bengali_sentences.append(bengali_sentence)

    return english_sentences, bengali_sentences

# Example usage:
english_data, bengali_data = scrape_parallel_data('https://example.com/parallel-data')

