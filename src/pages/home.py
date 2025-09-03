from dash import html, dcc
import plotly.express as px
import pandas as pd
from vizro.figures.library import kpi_card_reference, kpi_card
from src.utils.data_loader import load_data, get_range_infra, get_region, get_province, calculate_kpis, load_app_data
from src.components.cards import get_kpi
from src.components.slicer import get_infra_slider, get_province_dropdown, get_region_dropdown
import humanize
import dash_bootstrap_components as dbc

#loading all app related data
data= load_app_data()

#populating the slicer
infra_slider = get_infra_slider(data['mini'], data['maxi'])
region_dropdown = get_region_dropdown(data['regionals'])
province_dropdown = get_province_dropdown(data['provincials'])

#populating the main cards kpi
card_list = get_kpi(
    {
        "total_funds_kpi": data['df2'] ,
        "total_projects_kpi": data['df2'], 
        "other_cards": data['df2'],
        "avg_contr_cost": data['df2'], 
    }
)


def HomePage():
    return html.Div([
        # Two-column section
        html.Div([
            html.Div(html.Div(card_list, className="first-row"),
                     className="left-column"
                     ), 
            html.Div([ 
                html.Label("Infra Year:"),
                infra_slider,
                html.Label("Region:"),
                region_dropdown,
                html.Label("Province:"),
                province_dropdown], className="right-column column")], className="columns-container")
                ])
