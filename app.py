# app.py
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Datos de ejemplo
df = pd.DataFrame({
    "Fruit": ["Manzanas", "Naranjas", "Plátanos", "Manzanas", "Naranjas", "Plátanos"],
    "Cantidad": [4, 1, 2, 2, 4, 5],
    "Ciudad": ["SF", "SF", "SF", "NYC", "NYC", "NYC"]
})

# Gráfico de Plotly
fig = px.bar(df, x="Fruit", y="Cantidad", color="Ciudad", barmode="group")

# Layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Dashboard de Frutas'),
    dcc.Graph(id='example-graph', figure=fig)
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)