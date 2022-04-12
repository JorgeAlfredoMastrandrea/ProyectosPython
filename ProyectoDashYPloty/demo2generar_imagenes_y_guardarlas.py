# va a genera una imagen y la va a mandar a un diretorio
# la idea es que la genere, las guarde y luego la podamos
# incluir en el pdf

# https://plotly.com/python/v3/pdf-reports/#creating-pdf-reports-with-plotly-graphs-and-python
# https://plotly.com/python/static-image-export/#write-image-file

import plotly.graph_objects as go
import numpy as np
np.random.seed(1)

# creamos und irectorio
import os

if not os.path.exists("imagenes"):
    os.mkdir("imagenes")


N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sz = np.random.rand(N) * 30

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="markers",
    marker=go.scatter.Marker(
        size=sz,
        color=colors,
        opacity=0.6,
        colorscale="Viridis"
    )
))

fig.show()

# exportamos la imagen en formato PNG
fig.write_image("imagenes/fig1.png")