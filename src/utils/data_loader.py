import os
import pandas as pd
import humanize

#load data
def load_data():
    file_path = os.path.join("src", "utils", "dataset", "flood_control_data.csv")
    return pd.read_csv(file_path)


def get_range_infra(df):
    min_range = df["InfraYear"].min()
    max_range = df["InfraYear"].max()
    return min_range, max_range

def get_region(df):
    reg = df["Region"].unique()
    return sorted(reg)

def get_province(df, region=None):
    if region is None or region == "All":
        prov = df["Province"].unique()
    else:
        prov = df[df["Region"] == region]["Province"].unique()
    return sorted(prov)

def calculate_kpis(df):
    total_fund  = df["ABC"].sum()
    df_kpi = pd.DataFrame({
        "Actual": [total_fund], 
        "Reference": [total_fund]
    }
    )
    return df_kpi, humanize.intword(total_fund)