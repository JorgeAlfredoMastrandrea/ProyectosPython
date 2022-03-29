# esta libreria utiliza las conexiones a la base de datos y además
# gestiona los scripts para ejecutarlos, las bases son invocadas desde el proyecto principal
import mysql.connector

# Set cursor para cada base
def SetCursor(db):
    print("...poniendo el cursor en base : ", db.database)
    cursor = db.cursor()
    return cursor

def SeleccionarDatos(db , cursor , scriptSelect):
    print("...ejecutando script SELECT contra : ", db.database)
    cursor.execute(scriptSelect)
    resultado = cursor.fetchall()
    #db.close()
    return resultado

def InsertarDatos(db , cursor , resultado , scriptInsert):
    print("...ejecutando script INSERT contra : ", db.database)
    cursor.executemany(scriptInsert, resultado)
    db.commit()

def LimpiarTabla(db , cursor , tabla):
    print("...limpiando tabla : " + tabla)
    queryTruncate = "TRUNCATE TABLE " + tabla
    cursor.execute(queryTruncate)
    db.commit()
    
def CerrarBase(db):
    print("...cerrando conexión a : " + db.database)
    db.close()
    
def CrearTabla(db , cursor , queryCrear):
    print(f"...creando tabla en base de datos {db.database}")
    cursor.execute(queryCrear)
    db.commit()
    
def EjecutarScript(db , cursor , queryParajecutar):
    print(f"...ejecutando un script en la base {db.database}")
    cursor.execute(queryParajecutar)
    db.commit()
    

    


    
    