import nltk 
from nltk.corpus import words, names, jeita
import re

from nltk.corpus.reader.chasen import test

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

word_list = words.words()
name_list = names.words() 

def encrypt(plain_text_phrase, numeric_shift):
    ciphertext = ''
    for i in range(len(plain_text_phrase)):
        text = plain_text_phrase[i]
        new_text = text.lower()
        if new_text == " ":
            ciphertext += ' '
        elif text.isalpha():
            ciphertext += chr((ord(new_text) + numeric_shift - 97) % 26 + 97)

    return ciphertext

def decrypt(plain_text_phrase, numeric_shift):
    return encrypt(plain_text_phrase, numeric_shift * -1)


def crack(plain_text_phrase):

    text = {}
    test = 1
    percentage = 100

    if not plain_text_phrase:
        return None

    for i in range(0, 26):
        count_words = 0
        phrase = decrypt(plain_text_phrase, test)
        phrase1 = phrase.split()

        for word in phrase1:
            if word in word_list or word in name_list:
                count_words += 1

        percentage = int(count_words / len(phrase1) * 100)
        text[test] = percentage
        test += 1

    crackKey = max(text, key = text.get)
    return decrypt(plain_text_phrase, crackKey)


if __name__ == "__main__":

   sam = "Samer Odeh"
   print(f"\n{encrypt(sam, 6)}\n")
   print(f"\n{decrypt(sam, 0)}\n")
   print(f"\n{crack(encrypt(sam, 3))}\n")