from multiprocessing import connection
import LibConexiones
import LibDBScripts
import QuerysMatricula
import LibDBManager2
from colorama import Fore
from colorama import Style

try :
    # verificar base dbejemplo
    cursorDBEjemplo , verifyOkBDEjemplo = LibDBManager2.VerificarBD(LibConexiones.dbejemplo)    
    # OBLIGATORIO ESTO PARA PODE EJECUTAR CONSULTAS MUY GRANDES..!!!
    cursorDBEjemplo.execute('SET GLOBAL max_allowed_packet = 6710886400')
    cursorDBEjemplo.execute('SET GLOBAL connect_timeout = 360000')
    
    # verificar base GEM
    cursorGEM , verifyOkGEM = LibDBManager2.VerificarBD(LibConexiones.gem)
except :    
    print(f"{Fore.RED}{Style.BRIGHT}...ERROR en ProyectoMySQL_002.py ...{Style.RESET_ALL}")

resultado , accionExitosa = LibDBManager2.LeerYGuardarEnLocal(LibConexiones.gem , 
                                                cursorGEM , 
                                                QuerysMatricula.seleccionar_TABLA_INSTITUCIONAL_POR_CURSO_DIVISION , 
                                                LibConexiones.dbejemplo , 
                                                cursorDBEjemplo , 
                                                QuerysMatricula.insertar_TABLA_INSTITUCIONAL_POR_CURSO_DIVISION)

print("la accion de leer y guardar en local produjo un resultado : ",accionExitosa)