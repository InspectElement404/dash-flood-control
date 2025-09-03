from dash import html, dcc

def get_infra_slider(mini, maxi):
    infra_range = dcc.RangeSlider( mini,maxi, 1, 
                            value=[mini, maxi], 
                            id='my-range-slider',
                            marks={year: str(year) for year in range(mini, maxi)})
    return infra_range


def get_region_dropdown(regionals):
    regions = dcc.Dropdown(id="region-filter",
                           options=[{"label": "All", "value": "All"}] +[{"label": r, "value": r} for r in regionals],
                           value="All",  # default = All regions
                           clearable=False,
                           className="dash-dropdown"
                            )
    return regions


def get_province_dropdown(provincials):
    provinces = dcc.Dropdown(
                            id="province-filter",
                            options=[{"label": "All", "value": "All"}] +
                                    [{"label": p, "value": p} for p in provincials],
                            value="All",  # default = All provinces
                            clearable=False,
                            className="dash-dropdown"
                        )
    return provinces