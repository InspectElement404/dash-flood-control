from dash import Input, Output

def register_callbacks(app, df):
    # Update province dropdown options when region changes
    @app.callback(
        Output("province-filter", "options"),
        Input("region-filter", "value")
    )
    def update_province_options(region):
       
        if not region or region == "All":
            provinces = df["Province"].unique()
        else:
            provinces = df[df["Region"] == region]["Province"].unique()
        return [{"label": p, "value": p} for p in sorted(provinces)]
    



