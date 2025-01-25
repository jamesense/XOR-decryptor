import string
import re
import nltk
from nltk.corpus import words


english_words = set(words.words()) #NLTK dictionary for words

def contains_english_words(text):
    cleaned_text = ''.join([char if char in string.ascii_letters + ' ' else ' ' for char in text])
    words_in_text = re.findall(r'\b[a-zA-Z]{3,}\b', cleaned_text)
    return any(word.lower() in english_words for word in words_in_text)

def clean_text(text):
    return ''.join([char if char in string.printable else ' ' for char in text])

encrypted_strings = input("Enter XOR encrypted string(s) separated by commas (if multiple): ").split(',')

for key in range(1, 256):
    for encrypted in encrypted_strings:
        decrypted = ''.join(chr(ord(char) ^ key) for char in encrypted)
        cleaned_decrypted = clean_text(decrypted)
        if contains_english_words(cleaned_decrypted):
            print(f"Key {key}: {cleaned_decrypted}")
