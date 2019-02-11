from difflib import SequenceMatcher as SM
from PIL import Image
import pytesseract
import pymysql
import cv2
import uuid
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
db = pymysql.connect("Localhost","root","","bd_fluorescentes")
cursor = db.cursor()
#cap = cv2.VideoCapture(0)
#leido, frame = cap.read()
#if leido == True:
#	nombre_foto = str(uuid.uuid4()) + ".png" # uuid4 regresa un objeto, no una cadena. Por eso lo convertimos
#	cv2.imwrite(nombre_foto, frame)
#	print("Foto tomada correctamente con el nombre {}".format(nombre_foto))
#else:
#	print("Error al acceder a la cámara")
#cap.release()
im = Image.open("pruebaTUBO.jpg")
texto = pytesseract.image_to_string(im)
#print(texto.encode("utf-8"))
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