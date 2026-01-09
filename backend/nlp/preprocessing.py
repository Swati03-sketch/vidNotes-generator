import re
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from nltk.tokenize import sent_tokenize

# clean the text by removing extra spaces and unwanted characters
def preprocess_text(text: str):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)            # remove whitespaces
    text = re.sub(r"[^\w\s]", "", text)         # remove punctuations 
    return text.strip()

# Tokenization of text into sentences
def tokenize_text(text: str):
    return sent_tokenize(text)
