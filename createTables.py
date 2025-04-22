import sqlite3


def conexion():
    try:
        conec = sqlite3.connect('DBgestor.db')
        cursor = conec.cursor()
        cursor.execute('''
                      SELECT name
                      FROM sqlite_master
                      WHERE type = 'table' AND name = "tareas";''')
        filas = cursor.fetchone()
        if not filas:
            conec.execute('''
                 CREATE TABLE tareas 
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DESCRIPCION TEXT,
                ESTATUS INT NOT NULL)''')
            conec.commit()
            print("Las tablas se crearon")
        return conec
    except sqlite3.Error as e:
        print(f"Ocurrio un error indesperado: {e}")
        return None
    

conexion()






