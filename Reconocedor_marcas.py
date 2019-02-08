from difflib import SequenceMatcher as SM
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract'
im = Image.open("pruebaTUBO.jpg")
texto = pytesseract.image_to_string(im)
print(texto)

s1 = 'PHILIPS'
s2 = texto
print(SM(None, s1, s2).ratio())