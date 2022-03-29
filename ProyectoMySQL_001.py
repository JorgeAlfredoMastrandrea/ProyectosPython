# la idea es la de poder ejecutar un script contra GEM, extraer la tupla correspondiente
# y luego guardar el resultado del script y también el proceso de esa tabla en otra que
# refleje un resultado para poder genera al final un informe en PDF

# https://schedule.readthedocs.io/en/stable/
# https://www.geeksforgeeks.org/python-schedule-library/
# https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/    <----------- desempacar las tuplas en python

from multiprocessing import connection
import LibDBManager
import LibConexiones
import LibDBScripts
import LibDBScriptsMatricula
import LibDBManager2

#cursorGEM       = LibDBManager2.SetCursor(LibConexiones.gem)
#cursorDBEjemplo = LibDBManager2.SetCursor(LibConexiones.dbejemplo)

# cursorDBEjemplo = LibDBManager2.SetCursor(LibConexiones.dbejemplo)

cursorDBEjemplo , verifyOk = LibDBManager2.VerificarBD(LibConexiones.dbejemplo)

# OBLIGATORIO ESTO PARA PODE EJECUTAR CONSULTAS MUY GRANDES..!!!
cursorDBEjemplo.execute('SET GLOBAL max_allowed_packet = 6710886400')
cursorDBEjemplo.execute('SET GLOBAL connect_timeout = 360000')


"""
LibDBManager.LimpiarTabla(LibConexiones.dbejemplo , cursorDBEjemplo , "resultado")
resultadoConsultaGEM = LibDBManager.SeleccionarDatos(LibConexiones.gem , cursorGEM , LibDBScripts.seleccionarTablaNivel)
LibDBManager.InsertarDatos(LibConexiones.dbejemplo , cursorDBEjemplo , resultadoConsultaGEM , LibDBScripts.insertarEnTablaResultado)
#LibDBManager.CerrarBase(LibConexiones.dbejemplo)

LibDBManager.EjecutarScript(LibConexiones.dbejemplo , cursorDBEjemplo , LibDBScripts.dropTabla_MATRICULA_NOMINAL_SiExiste)
LibDBManager.CrearTabla(LibConexiones.dbejemplo , cursorDBEjemplo , LibDBScripts.crearTablaMatriculaNominal)
resultadoConsultaMatricula_Nominal_GEM = LibDBManager.SeleccionarDatos(LibConexiones.gem , cursorGEM , LibDBScripts.matriculaNominalCicloLectivoActual)

#for registro in resultadoConsultaMatricula_Nominal_GEM:
#    print(registro)

LibDBManager.InsertarDatos(LibConexiones.dbejemplo , cursorDBEjemplo , resultadoConsultaMatricula_Nominal_GEM , LibDBScripts.insertarEnTabla_MATRICULA_NOMINAL)

resultadoConsultaGEM = LibDBManager.SeleccionarDatos(LibConexiones.gem , cursorGEM , LibDBScriptsMatricula.consultaTablaInstitucional)
for registro in resultadoConsultaGEM:
    print(registro)
"""
"""
LibDBManager.EjecutarScript(LibConexiones.dbejemplo , cursorDBEjemplo , LibDBScriptsMatricula.drop_TABLA_INSTITUCIONAL_SiExiste)
LibDBManager.EjecutarScript(LibConexiones.dbejemplo , cursorDBEjemplo , LibDBScriptsMatricula.crear_TABLA_INSTITUCIONAL)
resultadoConsulta_TABLA_INSTITUCIONAL_GEM = LibDBManager.SeleccionarDatos(LibConexiones.gem , cursorGEM , LibDBScriptsMatricula.consulta_TABLA_INSTITUCIONAL)
LibDBManager.InsertarDatos(LibConexiones.dbejemplo , cursorDBEjemplo , resultadoConsulta_TABLA_INSTITUCIONAL_GEM , LibDBScriptsMatricula.insertar_TABLA_INSTITUCIONAL)
"""

