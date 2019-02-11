from difflib import SequenceMatcher as SM
from PIL import Image
import pytesseract
import pymysql
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
db = pymysql.connect("Localhost","root","","bd_fluorescentes")
cursor = db.cursor()
im = Image.open("pruebaTUBO.jpg")
texto = pytesseract.image_to_string(im)
#print(texto.encode("utf-8"))
#s1 = 'PHILIPS'
cmpAnterior=SM(None, 'CD & P', texto).ratio()
#cmpNuevo=""
id_tubo=1 #debe recojerse de la bd
cantidad_tubo=0 #debe recojerse de la bd
cursor.execute("SELECT * FROM marca_prueba")
for row in cursor.fetchall():
    cmpNuevo=SM(None, row[1], texto).ratio()
    if cmpNuevo > cmpAnterior:
    	cmpAnterior=cmpNuevo
    	id_tubo=row[0]
    	cantidad_tubo=row[2]
    else:
     	id_tubo=24
qry="UPDATE marca_prueba SET cantidad_marca = %s WHERE id_marca = %s " %(cantidad_tubo+1, id_tubo)
print(qry)
cursor.execute(qry)
db.commit()