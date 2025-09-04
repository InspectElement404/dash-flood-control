import plotly_express as px

def generate_plot_timeseries(df,kin,x, y):
    func = getattr(px, kin)
    figma = func(df,x=x,y=y)
    return figma
