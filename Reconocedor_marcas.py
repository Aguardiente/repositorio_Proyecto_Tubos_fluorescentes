#  -*- coding: utf-8 -*-
from difflib import SequenceMatcher as SM
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
#im = Image.open("test.png")
im = Image.open("pruebaTUBO.jpg")
#im = Image.open("pruebaTextoBN.jpg")
#im = Image.open("pruebaTexto.jpg")
texto = pytesseract.image_to_string(im)
#print(texto.encode("utf-8"))
s1 = 'PHILIPS'
s2 = texto
print(SM(None, s1, s2).ratio())