# esta libreria utiliza las conexiones a la base de datos y además
# gestiona los scripts para ejecutarlos, las bases son invocadas desde el proyecto principal
# pip install colorama
import mysql.connector
from colorama import Fore
from colorama import Style

# Set cursor para cada base
def SetCursor(db):
    print(f"{Fore.YELLOW}{Style.BRIGHT}...poniendo el cursor en base :  {db.database}{Style.RESET_ALL}")
    # defino una variable que contendrá el cursor
    cursor = ""
    try :
        print(f"{Fore.YELLOW}...seteando cursor en la base de datos {db.database}..!{Style.RESET_ALL}")
        # ejecuto un cursor
        cursor = db.cursor()
    except :
        # si hay error en el cursor
        print(f"{Fore.RED}{Style.BRIGHT}...ERROR en (LibDBManager2.py --> SetCursor(db))... cursor no seteado para {db.database}{Style.RESET_ALL}")
    else :
        # en caso de no haber error, se devuelve un cursor
        print(f"{Fore.GREEN}{Style.BRIGHT}...CURSOR OK para la base {db.database}{Style.RESET_ALL}")
    return cursor

# verificar que la base de datos existe, en caso de que así sea devuelve un cursor (puntero) 
# y True o False en caso de que no se pudo conectar
def VerificarBD(db):
    # cuando hago la consulta para sabes si la base de datos existe, necesito guardarla en algun lugar
    resultado = ""
    # voy a devolver un cursor para cuando encuentr la base
    cursor = ""
    # devuelvo true o false por si se pudo conectar
    verifyOK = False
    # verifica que la base de datos seleccionada esté en el servidor
    try :
        print(f"{Fore.YELLOW}{Style.BRIGHT}...tratando de acceder a la base de datos {db.database}...{Style.RESET_ALL}")
        # seteo un cursor para esa base
        cursor = SetCursor(db)
        # me fijo si la base existe,..
        cursor.execute("SHOW DATABASES LIKE " + "'" + db.database + "'")
        # en caso de que exista, me va a traer un resultado
        resultado = cursor.fetchall()
    except :        
        # si el resiltado que trae no coincide con el nombre de la base de datos 
        # que he declarado en el módulo de la conexión, entonces se verifica un error
        # y devuelve false para la verificacion
        if str(resultado[0]) != str("('" + db.database + "'),"):
            print(f"{Fore.RED}{Style.BRIGHT}...ERROR en (LibDBManager2.py --> VerificarBD(db)) no se pudo acceder a la base de datos {db.database}...{Style.RESET_ALL}")
            verifyOK = False
            cursor = None
    else :
        # en caso de que haya encontrado la base que necesesito conectarme,..
        # devuelve un mensaje y me dice que la verificación es True
        if str(resultado[0]) == str("('" + db.database + "',)"):
            print(f"{Fore.GREEN}{Style.BRIGHT}...todo OK con la base de datos {db.database}...{Style.RESET_ALL}")
            verifyOK = True
    # devuelvo la verificación True o False y el cursor
    return cursor , verifyOK        

# verifica que la tabla exista dentro de la base de datos seleccionada
# devuelve un cursor y True o False en caso de que la tabla exista
def VerificarTabla(db , tabla):
    # verifica la existencia de una tabla dentro de una base de datos
    # que pasamos por parámteros
    # necesito el resultado para poder verificar que sea el valor que estoy buscando
    resultado = ""
    # un cursor para ejecutar el script
    cursor = ""
    # si se verifica que está, se devolverá true
    verifyOK = False
    try :
        print(f"{Fore.YELLOW}{Style.BRIGHT}...tratando de acceder a la tabla {tabla} de la base de datos {db.database}...{Style.RESET_ALL}")        
        cursor = SetCursor(db)        
        # compongo el nombre de la base de datos
        dbName = "'" + db.database + "'"
        # compongo el nombre de la tabla
        tableName = "'" + tabla + "'"
        # tengo el script para ejecutar contra la base de datos
        script = "SHOW TABLES LIKE " + tableName        
        # ejecuto el script
        cursor.execute(script)
        # ya tengo el resultado
        resultado = cursor.fetchall()
    except :
        # si el resultado es vacío, es porque la tabla no existe
        if str(resultado == ""):
            print(f"{Fore.RED}{Style.BRIGHT}...ERROR en (LibDBManager2.py --> VerificarTabla(db , tabla)) no se pudo acceder a la TABLA {tabla}...{Style.RESET_ALL}")
            verifyOK = False
            cursor = None
    else :
        # si el resultado trae el nombre de la tabla que estoy buscando, entonces es porque existe la tabla
        if str(resultado[0]) == str("(" + tableName + ",)"):
            print(f"{Fore.GREEN}{Style.BRIGHT}...todo OK con la TABLA {tabla}...{Style.RESET_ALL}")
            verifyOK = True
    return cursor , verifyOK

# verificar el tamaño de una tabla guardada con el tamaño generado por la consulta
# leyendo la cantidad de registros
# db es la base en la que está la tabla, tabla es la que queremos comparar, tamañoOriginal es un valor
# que tiene la cantidad de registros leidos originalmente
def VerificarTamañoDeLaTabla(db , tabla , tamañoOriginal):
    return True



def LimpiarTabla(db , cursor , tabla):
    print("...limpiando tabla : " + tabla)
    queryTruncate = "TRUNCATE TABLE " + tabla
    cursor.execute(queryTruncate)
    db.commit()
    return True

def CrearTablaEnBD(db , cursor , queryCrear):
    print(f"...creando tabla en base de datos {db.database}")
    cursor.execute(queryCrear)
    db.commit()
    return True

def CerrarBD(db):
    print("...cerrando conexión a : " + db.database)
    db.close()
    return True

def GuardarConsultaEnBD(db , cursor , scriptSelect):
    print("...guardando consulta en tabla {tabla} de la base de datos {db}")
    # debo verificar si la base existe
    # luego verifico que la tabla exista
    # si la tabla no existe, la creo
    # si la tabla ya existe, guardo los datos
    return True
""" ver si esto sirve 
def EjecutarScript(db , cursor , queryParajecutar):
    verifyOK = False
    resultado = ""
    try:
        print(f"...ejecutando un script en la base {db.database}")
        resultado = cursor.execute(queryParajecutar)
        db.commit()
    except:
        print(f"...script no ejecutado, revisar..!!")
        verifyOK = False
    else:
        print("...script ejecutado existosamente..!")
        verifyOK = True
    return resultado , verifyOK
"""
    
def InsertarDatos(db , cursor , resultado , scriptInsert):
    print("...ejecutando script INSERT contra : ", db.database)
    cursor.executemany(scriptInsert, resultado)
    db.commit()
##############################################################################################
def Leer(db , cursor , scriptSelect):
    try:
        print(f"{Fore.BLUE}{Style.BRIGHT}...leyendo datos de la base : {db.database} ...{Style.RESET_ALL}")    
        cursor.execute(scriptSelect)
        resultado = cursor.fetchall()
        #db.close()
    except:
        print(f"{Fore.RED}{Style.BRIGHT}...ERROR en (LibDBManager2.py --> Leer(db , cursor , scriptSelect)) no se pudo ejecutar el script...{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}{Style.BRIGHT}...datos leidos de la base {db.database}  ...{Style.RESET_ALL}")
    return resultado

def LeerYGuardarEnLocal(dbGEM , cursorGEM , scriptSelectGEM , dbLocal , cursorLocal , scriptInsertar):
    # hago la consulta al gem
    resultado = Leer(dbGEM , cursorGEM , scriptSelectGEM)
    # guardo el resultado en la base local
    InsertarDatos(dbLocal , cursorLocal , resultado , scriptInsertar)
    return resultado

def BorrarTabla(db , cursor , tabla):
    print(f"{Fore.BLUE}{Style.BRIGHT}...borrando tabla : {tabla} en {db.database} ...{Style.RESET_ALL}")
    return True

def CrearTabla(db , cursor , scriptCrear):
    print(f"{Fore.BLUE}{Style.BRIGHT}...creando tabla : en {db.database} ...{Style.RESET_ALL}")
    return True

def EliminarTabla(db , cursor , tabla):
    print(f"{Fore.BLUE}{Style.BRIGHT}...eliminando tabla : {tabla} en {db.database} ...{Style.RESET_ALL}")
    return True
##########################################################################################################
#print(f"{Fore.GREEN} verde {Fore.RED} rojo {Style.BRIGHT} brillante {Style.RESET_ALL} resetear todo")
