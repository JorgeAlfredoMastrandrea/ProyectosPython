# acá dejamos establecidas las bases de datos con las que nos vamos a conectar
import mysql.connector
from colorama import Fore
from colorama import Style

miConector = mysql.connector.connect

try:
  print("...iniciando conector a DB GEM...")
  gem = miConector(
    host="gemdbrep1.mendoza.gob.ar",
    user="jmastrandrea",
    password="C*1cuZRvsr",
    database="gem"
)
except:
  print(f"{Fore.RED}{Style.BRIGHT}...ERROR en LibConexiones.py --> en el conector de GEM reviselo...{Style.RESET_ALL}")
else :
  print(f"{Fore.GREEN}{Style.BRIGHT}...conector GEM OK...{Style.RESET_ALL}") 
  


try:
  print("...iniciando conector a DB dbejemplo...")
  dbejemplo = miConector(
    host="127.0.0.1",
    user="root",
    password="Margarita90",
    database="dbejemplo"
  )
except :
  print(f"{Fore.RED}{Style.BRIGHT}...ERROR en LibConexiones.py --> en el conector dbejemplo reviselo...{Style.RESET_ALL}")
else :
  print(f"{Fore.GREEN}{Style.BRIGHT}...conector OK...{Style.RESET_ALL}")  