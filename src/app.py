from dash import Dash, html
from src.components.header import Header
from src.pages.home import HomePage, df2
from src.callbacks.filter_callbacks import register_callbacks

app = Dash(__name__)
register_callbacks(app, df2)

app.layout = html.Div([
    Header(),      # top navbar
    HomePage()     # main page content
])

if __name__ == "__main__":
    app.run()
