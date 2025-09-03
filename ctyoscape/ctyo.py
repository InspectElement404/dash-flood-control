import dash
from dash import html
import dash_cytoscape as cyto
import pandas as pd

# Example dataset
data = {
    "ProjectID": ["P1", "P2", "P3"],
    "Province": ["PALAWAN", "PALAWAN", "PALAWAN"],
    "Contractor": ["AZARRAGA CONSTRUCTION", "F.F. GALANG CONSTRUCTION", "AZARRAGA CONSTRUCTION"]
}
df = pd.DataFrame(data)

elements = []

# Add contractor nodes
for contractor in df["Contractor"].unique():
    elements.append({"data": {"id": contractor, "label": contractor}, "classes": "contractor"})

# Build contractor-contractor edges (same province)
grouped = df.groupby("Province")["Contractor"].unique()

for province, contractors in grouped.items():
    contractors = list(contractors)
    for i in range(len(contractors)):
        for j in range(i+1, len(contractors)):
            elements.append({
                "data": {
                    "source": contractors[i],
                    "target": contractors[j],
                    "label": province
                }
            })

# App layout
app = dash.Dash(__name__)
app.layout = html.Div([
    cyto.Cytoscape(
        id="contractor-network",
        elements=elements,
        style={"width": "100%", "height": "600px"},
        layout={"name": "cose"},
        stylesheet=[
            {
                "selector": ".contractor",
                "style": {"background-color": "orange", "label": "data(label)", "shape": "ellipse"}
            },
            {
                "selector": "edge",
                "style": {"line-color": "#999", "label": "data(label)"}
            }
        ]
    )
])

if __name__ == "__main__":
    app.run(debug=True)
