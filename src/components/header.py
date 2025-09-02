from dash import html
import dash
def Header():
    return html.Div([
        # Left: logo + title
        html.Div([
            html.Img(src=dash.get_asset_url('dpwh.png'), alt="dpwh-logo"),
            html.H3("Flood Control Projects Analytics", style={"margin": 0})
        ], className="left-side"),

        # Center menu
        html.Div([
            html.Div("Overview"),
            html.Div("Project"),
            html.Div("Contractors")
        ], className="center-side")
    ], className="top-block")
