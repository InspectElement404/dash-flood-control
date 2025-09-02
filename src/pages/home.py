from dash import html, dcc
import plotly.express as px
import pandas as pd
from vizro.figures.library import kpi_card_reference
from src.utils.data_loader import load_data, get_range_infra, get_region, get_province, calculate_kpis
import humanize


# Prepare dataset
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Revenue": [1000, 1500, 1300, 1700]
})
# KPI dataset
df_kpi = pd.DataFrame({"Actual": [100, 200, 700], "Reference": [100, 300, 500]})

df2 = load_data()
mini, maxi = get_range_infra(df2)
regionals = get_region(df2)
provincials = get_province(df2)

kpi_data, total_fund = calculate_kpis(df2)

fig = px.line(df, x="Month", y="Revenue", title="Monthly Revenue")

ptx = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
       "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
       "when an unknown printer took a galley of type and scrambled it to make a type specimen book.")

def HomePage():
    return html.Div([
        # Two-column section
        html.Div([
            # Left column with graph + text
            html.Div([
                html.Div(
                kpi_card_reference(
                    data_frame=kpi_data,
                    value_column="Actual",
                    reference_column="Reference",
                    icon="money_bag",
                    title="Total Allocated Funds",
                 value_format=f"₱{total_fund}" ,
                   
                ),

              className="kpi-card"
            ),  html.Div(
                kpi_card_reference(
                    data_frame=df_kpi,
                    value_column="Actual",
                    reference_column="Reference",
                    icon="cases",
                    title="Total Projects",
                    value_format="{value}€",
                   
                ),
                 className="kpi-card"
            ),html.Div(
                kpi_card_reference(
                    data_frame=df_kpi,
                    value_column="Actual",
                    reference_column="Reference",
                    icon="engineering",
                    title="Total Contractors",
                    value_format="{value}€",
                  
                ),
                 className="kpi-card"
            ),
            html.Div(
                kpi_card_reference(
                    data_frame=df_kpi,
                    value_column="Actual",
                    reference_column="Reference",
                    icon="currency_ruble",
                    title="Avg Cost/Contractor",
                    value_format="{value}€",
                   
                ),
                 className="kpi-card"
            ),
            
            ], className="left-column "),

            # Right column placeholder
            html.Div([
    html.Label("Infra Year:"),
   dcc.RangeSlider(
    mini, maxi, 1,
    value=[mini, maxi],
    id='my-range-slider',
    marks={year: str(year) for year in range(mini, maxi)},  # show full years

),
   html.Label("Region:"),
dcc.Dropdown(
    id="region-filter",
    options=[{"label": "All", "value": "All"}] +
            [{"label": r, "value": r} for r in regionals],
    value="All",  # default = All regions
    clearable=False,
    className="dash-dropdown"
),

html.Label("Province:"),
dcc.Dropdown(
    id="province-filter",
    options=[{"label": "All", "value": "All"}] +
            [{"label": p, "value": p} for p in provincials],
    value="All",  # default = All provinces
    clearable=False,
    className="dash-dropdown"
)
  
], className="right-column column")

        ], className="columns-container")
    ])
