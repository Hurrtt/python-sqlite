import sqlite3

conexion = sqlite3.connect("DataBase.db")

cursor = conexion.cursor()


#creamos nuestra tabla de usuarios, una vez creada eliminamos el bloque de codigo
"""
conexion.execute(''' 
                 CREATE TABLE usuarios 
                 (ID INT PRIMAREY KEY NOT NULL,
                 LOGIN CHAR(50) NOT NULL,
                 NOMBRE CHAR(50) NOT NULL,
                 APELLIDOS CHAR(50) NOT NULL)''')
"""

#Ejemplo de un insert
"""conexion.execute('''
                 INSERT INTO usuarios (ID, LOGIN, NOMBRE, APELLIDOS) VALUES(1, 'Hurrtt', 'Erik', 'Garcia')''')
conexion.commit()
conexion.close()
"""
"""
conexion.execute('''
                 INSERT INTO usuarios (ID, LOGIN, NOMBRE, APELLIDOS) VALUES(2 ,'Crypt', 'Ethan', 'Fernandez')''')
conexion.commit()
conexion.close()
"""
"""
conexion.execute( "UPDATE usuarios SET APELLIDOS = 'Garcia' WHERE ID = 1")
"""
"""
conexion.execute("DELETE FROM usuarios WHERE ID = 2")
"""
"""
cursor.execute("SELECT * FROM usuarios")
filas = cursor.fetchall()

conexion.commit()
conexion.close()
for fila in filas:
    print(fila)

"""


print("Registro completado")