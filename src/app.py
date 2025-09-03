from dash import Dash, html
import dash_bootstrap_components as dbc
from src.components.header import Header
from src.pages.home import HomePage, data
from src.callbacks.filter_callbacks import register_callbacks

fontawesome_stylesheet = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, fontawesome_stylesheet ])
register_callbacks(app, data['df2'])

app.layout = html.Div([
    Header(),      # top navbar
    HomePage()     # main page content
])

if __name__ == "__main__":
    app.run()
