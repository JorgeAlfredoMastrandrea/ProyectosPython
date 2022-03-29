# la idea es la de poder ejecutar un script contra GEM, extraer la tupla correspondiente
# y luego guardar el resultado del script y también el proceso de esa tabla en otra que
# refleje un resultado para poder genera al final un informe en PDF

# https://schedule.readthedocs.io/en/stable/
# https://www.geeksforgeeks.org/python-schedule-library/
# https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/    <----------- desempacar las tuplas en python

from multiprocessing import connection
import LibConexiones
import LibDBScripts
import LibDBScriptsMatricula
import LibDBManager2
from colorama import Fore
from colorama import Style

try :
    # verificar base dbejemplo
    cursorDBEjemplo , verifyOk = LibDBManager2.VerificarBD(LibConexiones.dbejemplo)    
    # OBLIGATORIO ESTO PARA PODE EJECUTAR CONSULTAS MUY GRANDES..!!!
    cursorDBEjemplo.execute('SET GLOBAL max_allowed_packet = 6710886400')
    cursorDBEjemplo.execute('SET GLOBAL connect_timeout = 360000')
    
    # verificar base GEM
    cursorGEM , verifyOkGEM = LibDBManager2.VerificarBD(LibConexiones.gem)
except :    
    print(f"{Fore.RED}{Style.BRIGHT}...ERROR en ProyectoMySQL_002.py ...{Style.RESET_ALL}")

resultado = LibDBManager2.Leer(LibConexiones.dbejemplo , cursorDBEjemplo , LibDBScriptsMatricula.leer_TABLA_INSTITUCIONAL)

#LibDBManager2.VerificarTabla(LibConexiones.dbejemplo , "tabla_institucional")

LibDBManager2.EjecutarScript(LibConexiones.dbejemplo , cursorDBEjemplo , LibDBScriptsMatricula.drop_TABLA_INSTITUCIONAL_POR_CURSO_SiExiste)
LibDBManager2.EjecutarScript(LibConexiones.dbejemplo , cursorDBEjemplo , LibDBScriptsMatricula.crear_TABLA_INSTITUCIONAL_POR_CURSO)
#resultadoConsulta_TABLA_INSTITUCIONAL_POR_CURSO_GEM = LibDBManager2.Leer(LibConexiones.gem , cursorGEM , LibDBScriptsMatricula.seleccionar_TABLA_INSTITUCIONAL_POR_CURSO)
#LibDBManager2.InsertarDatos(LibConexiones.dbejemplo , cursorDBEjemplo , resultadoConsulta_TABLA_INSTITUCIONAL_POR_CURSO_GEM , LibDBScriptsMatricula.insertar_TABLA_INSTITUCIONAL_POR_CURSO)
LibDBManager2.LeerYGuardar(LibConexiones.gem , cursorGEM , LibDBScriptsMatricula.seleccionar_TABLA_INSTITUCIONAL_POR_CURSO , LibConexiones.dbejemplo , cursorDBEjemplo , LibDBScriptsMatricula.insertar_TABLA_INSTITUCIONAL_POR_CURSO)


#for x in resultadoConsulta_TABLA_INSTITUCIONAL_POR_CURSO_GEM:
#    print(x)