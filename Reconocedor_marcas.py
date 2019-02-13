from difflib import SequenceMatcher as SM
from PIL import Image
import pytesseract
import pymysql
import cv2
import uuid
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
db = pymysql.connect("Localhost","root","","bd_fluorescentes")
cursor = db.cursor()
im = Image.open("pruebaPreparado/1.jpg")
texto = pytesseract.image_to_string(im)
print(texto.encode("utf-8"))
cursor.execute("SELECT * FROM marca_prueba_small WHERE id_marca =1")
for row in cursor.fetchall():
	cmpAnterior=SM(None, row[1], texto).ratio()
	id_tubo=row[0]
	cantidad_tubo=row[2]
cursor.execute("SELECT * FROM marca_prueba_small")
for row in cursor.fetchall():
    cmpNuevo=SM(None, row[1], texto).ratio()
    if cmpNuevo > cmpAnterior:
    	cmpAnterior=cmpNuevo
    	id_tubo=row[0]
    	cantidad_tubo=row[2]
qry="UPDATE marca_prueba_small SET cantidad_marca = %s WHERE id_marca = %s " %(cantidad_tubo+1, id_tubo)
cursor.execute(qry)
db.commit()