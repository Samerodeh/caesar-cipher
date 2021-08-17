import nltk 
from nltk.corpus import words, names
import re

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
    text = ''
    percentage = 100

    if not plain_text_phrase:
        return 

    for numeric_shift in range(0,26):
        word = decrypt(plain_text_phrase, numeric_shift)
        words = word.split()
        count_words = 0
        for word in words:
            check_word = re.sub(r"[^a-zA-Z]+", " ", word).lower()
            if check_word in word_list:
                count_words += 1
        words_percentage = int(count_words / len(words) * 100)

        if words_percentage > percentage:
            percentage = words_percentage
            text = word

    return text


if __name__=="__main__":

   sam = "Samer Odeh"
   print(f"\n{encrypt(sam, 6)}")
   print(f"\n{crack(sam)}\n")
   print(f"{decrypt(sam, 0)}\n")