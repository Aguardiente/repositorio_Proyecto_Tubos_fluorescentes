# -*- coding: utf_8 -*-
import sqlite3

con=sqlite3.connect('bd_tubos.db')
cursor = con.cursor()
print ("base de datos creada y abierta")

cursor.execute('''CREATE TABLE TUBO
	(ID INT PRIMARY KEY NOT NULL,
	NOMBRE			TEXT NOT NULL,
	PATRON			TEXT NOT NULL,
	CANTIDAD 		INT  NOT NULL)''')

print("tabla creada")

cursor.execute("INSERT INTO TUBO (ID, NOMBRE, PATRON, CANTIDAD) \
	VALUES (1,'OSRAM','OSRAM',0)")
cursor.execute("INSERT INTO TUBO (ID, NOMBRE, PATRON, CANTIDAD) \
	VALUES (2,'NARVA','ÔÇÿ_Vll_VI.IÔÇÿ|ald-be!.d6',0)")	
cursor.execute("INSERT INTO TUBO (ID, NOMBRE, PATRON, CANTIDAD) \
	VALUES (3,'PHILIPS','PHILIPS',0)")
con.commit()
print("datos registrados")

con.close()
