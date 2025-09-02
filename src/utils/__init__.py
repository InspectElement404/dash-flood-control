import pandas as pd

#load data
def load_data():
    df = pd.read_csv("/dataset/flood_control_data.csv")
    return df 


def get_range_infra(df):
    min_range = df["InfraYear"].min()
    max_range = df["InfraYear"].max()
    return min_range, max_range