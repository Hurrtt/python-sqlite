from createTables import conexion
import sqlite3

def agregar_tarea():
    try:
        connection = conexion()
        if not connection:
            print("no se pudo conectar a la base de datos...")
            return
        description = input("Agregue una descripcion de la tarea: ")
        query = ('''INSERT INTO tareas (DESCRIPCION, ESTATUS) VALUES (?, 0)''')
        connection.execute(query, (description,))
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print(f"Error al agregar la tarea: {e}")
    finally:
        connection.close()

def tareas_pendientes():
    try:
        connection = conexion()
        cursor = connection.cursor()
        if not connection:
            print("No se pudo conectar a la base de datos")
            return
        query = "SELECT * FROM tareas WHERE ESTATUS = 0"
        cursor.execute(query)
        lista = cursor.fetchall()
        for i in lista:
            print(i)
    except sqlite3.Error as e:
        print(f"Error al consultar: {e}")
    finally:
        connection.close()

def complete():
    try:
        connection = conexion()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM tareas WHERE ESTATUS = 0")
        pendientes = cursor.fetchall()
        for tareas in pendientes:
            print(tareas)
        tarea_completada = int(input("Ingrese el ID de la tarea que completo: "))
        query = "UPDATE tareas SET ESTATUS = 1 WHERE ID = ?"
        connection.execute(query, (tarea_completada, ))
        connection.commit()

    except sqlite3.Error as e:
        print(f"Error inesperado: {e}")
    finally:
        connection.close()

def eliminar_tareas():
    try:
        connection = conexion()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tareas")
        all_tareas = cursor.fetchall()
        for tareas in all_tareas:
            print(tareas)
        delete = int(input("Ingrese el ID de la tarea que desea eliminar: "))
        query = "DELETE FROM tareas WHERE ID = ?"
        connection.execute(query, (delete,))
        connection.commit()

    except sqlite3.Error as e:
        print(f"Error inesperado: {e}")
    finally:
        connection.close()

def menu():
    print("Ingrese una opcion: \n1-Agregar tarea \n2-Ver tareas pendientes \n3-Marcar tarea completada \n4-Eliminar tarea \n5-Salir")
    opc = input()
    while opc != '5':
        if opc == '1':
            agregar_tarea()
        if opc == '2':
            tareas_pendientes()
        if opc == '3':
            complete()
        if opc == '4':
            eliminar_tareas()
        if opc == '5':
            print("Hasta luego")
        else:
            print("Elija una opcion valida...")
            return menu()
menu()