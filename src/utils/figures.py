import plotly_express as px 


def make_time_series(df):
    return px.line(df, x="Date", y="Value", title="Time Series")