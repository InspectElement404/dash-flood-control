import plotly_express as px 


def generate_plot_timeseries(df,kin,x, y):
    func = getattr(px, kin)
    figma = func(df,x=x,y=y)
    return figma

def make_project_trend(data):
    project_fig = generate_plot_timeseries(data,"line","StartDate", "count")
    project_fig.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=50,r=50,t=0,b=50),
    annotations = [dict
        (
            text="Anomaly",
            x=  "2022-03-24",
            y=206,
            arrowhead=2,
            showarrow=True,
            font=dict(size=12),
            bgcolor="white"
        )])
    return project_fig

def output_figure(data):
    #project_trend fig
    project_trend = make_project_trend(data)
    return {
        "project_trend": project_trend
    }

