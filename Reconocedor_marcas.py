from difflib import SequenceMatcher as SM
from PIL import Image
import pytesseract
from cv2 import *
#import uuid
import sqlite3
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#import win32api
#CONEXION
db=sqlite3.connect('bd_tubos.db')
cursor = db.cursor()
#CAPTURA
#state_right = win32api.GetKeyState(0x02)
namedWindow("webcam")
vc = VideoCapture(0);

while True:
	#b = win32api.GetKeyState(0x02)
    next, im = vc.read()
    #plt.imshow(im)
    imshow("webcam", im)
    #if b != state_right:
    if waitKey(32) >= 0:  
        break;
#PREPROCESAMIENTO
#CROPEADO
#im = im.crop((1, 1, 98, 33)) 
#REDIMENSIONADO
#basewidth = 300         valor a redimensionar
#img = Image.open('somepic.jpg')
#wpercent = (basewidth/float(img.size[0]))
#hsize = int((float(img.size[1])*float(wpercent)))
#img = img.resize((basewidth,hsize), Image.ANTIALIAS)
#CONVERSION A GRAYSCALE
#img = color.rgb2gray(io.imread('image.png'))
#AUMENTAR CONTRASTE
#img = cv2.imread('Dog.jpg', 1)
#cv2.imshow("img",img) 
#lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#cv2.imshow("lab",lab)
#l, a, b = cv2.split(lab)
#cv2.imshow('l_channel', l)
#cv2.imshow('a_channel', a)
#cv2.imshow('b_channel', b)
#clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
#cl = clahe.apply(l)
#cv2.imshow('CLAHE output', cl)
#limg = cv2.merge((cl,a,b))
#cv2.imshow('limg', limg)
#final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
#cv2.imshow('final', final)
#PREPROCESAMIENTO TERMINADO
#im.save('_0.png') 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#im = Image.open("NARVA.jpg")
texto = pytesseract.image_to_string(im)
print(texto.encode("utf-8")), "\n"
cursor.execute("SELECT * FROM tubo WHERE id =1")
for row in cursor.fetchall():
	cmpAnterior=SM(None, row[2], texto).ratio()
	id_tubo=row[0]
	cantidad_tubo=row[3]
#RECONOCIENDO	
cursor.execute("SELECT * FROM tubo")
for row in cursor.fetchall():
    cmpNuevo=SM(None, row[2], texto).ratio()
    if cmpNuevo > cmpAnterior:
    	cmpAnterior=cmpNuevo
    	id_tubo=row[0]
    	cantidad_tubo=row[3]
qry="UPDATE tubo SET cantidad = %s WHERE id = %s " %(cantidad_tubo+1, id_tubo)
cursor.execute(qry)
db.commit()
#MOSTRAR RESULTADOS
cursor.execute("SELECT * FROM tubo")
for i in cursor:
	print "ID = ", i[0]
	print "NOMBRE = ", i[1]
	print "PATRON = ", i[2].encode("utf-8")
	print "CANTIDAD = ", i[3], "\n"

db.close()