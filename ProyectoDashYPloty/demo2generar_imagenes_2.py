# https://plotly.com/python/v3/pdf-reports/#creating-pdf-reports-with-plotly-graphs-and-python
# https://plotly.com/python/static-image-export/#write-image-file

import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.express as px
# creamos und irectorio
import os
import csv

# leer los datos
# ES IMPORTANTE DECLARAR LOS SEPARADORES QUE SE VAN A USAR , DADO QUE SI PONEMOS ; O , PUEDE NO LEERSE
dF = pd.read_csv('datos/FLUIDEZ_POR_DIVISION__.csv' ,  sep=';', lineterminator='\n')
# maxima cantidad de filas a mostrar
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(dF)
# fig = px.line(df, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')
# fig.show()

if not os.path.exists("imagenes"):
    os.mkdir("imagenes")

# exportamos la imagen en formato PNG
# fig.write_image("imagenes/fig_2.png")

# otra forma de poder leer los datos y mandarlos a un data frame
# read the csv file
# csv_reader = csv.reader('datos/FLUIDEZ_POR_DIVISION__.csv')
# now we can use this csv files into the pandas
# df = pd.DataFrame([csv_reader], index = None)
# for val in list(df[1]):
#     print(val)

# seleccionar datos del data frame
# selecting rows based on condition
rslt_df = dF.loc[(dF['Operativo'] == "Operativo 2022 Instancia I")]
filterinfDataframe = dF[(dF['Operativo'] == "Operativo 2022 Instancia I") 
                        & 
                        (dF['escuela seleccionada'] == 'si')]
# rslt_df = rslt_df.loc[(rslt_df['escuela seleccionada'] == "no")]
print(filterinfDataframe)