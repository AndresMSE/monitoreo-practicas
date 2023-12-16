import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os

# Cargar datos
model_metrics = pd.read_csv(os.path.abspath('./data/model_metrics.csv')) # Cambiar la ruta

# Inicializar la aplicación Dash
app = dash.Dash(__name__)


# Diseño del layout
app.layout = html.Div([html.H1("Dashboard de Monitoreo de Modelos de Datos"),
                       dcc.Graph(id='precision-plot',figure=px.line(model_metrics, x='Fecha', y='Precision', title='Precisión a lo largo del tiempo')),
                       dcc.Graph(id='recall-plot',figure=px.line(model_metrics, x='Fecha', y='Recall', title='Recall a lo largo del tiempo')),
                       dcc.Graph(id='accuracy-plot',figure=px.line(model_metrics, x='Fecha', y='Exactitud', title='Exactitud a lo largo del tiempo')),
                       ])
# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)