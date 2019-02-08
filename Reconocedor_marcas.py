from difflib import SequenceMatcher as SM

from PIL import Image

import pytesseract

s1 = 'Hola Mundo'
s2 = 'Hola Mundo cruel'
print(SM(None, s1, s2).ratio())

s1 = 'Hola Mundo'
s2 = 'Hola Mundo!'
print(SM(None, s1, s2).ratio())

print('jaja')

im = Image.open("example_01.png")
texto = pytesseract.image_to_string(im)
print(texto)
