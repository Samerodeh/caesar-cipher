from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    actual = encrypt("Samer Odeh", 6)
    expected = "ygskx ujkn"
    assert actual == expected

def test_decrypt():
    actual = decrypt("ygskx ujkn", 6)
    expected = "Samer Odeh"
    assert actual == expected 

def test_crack():
    text = " Samer Odeh "
    actual = crack(text)
    expected = "Samer Odeh"
    assert actual == expected
