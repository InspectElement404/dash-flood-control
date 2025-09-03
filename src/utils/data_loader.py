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

def load_app_data():
    df2 = load_data()
    mini, maxi = get_range_infra(df2)
    regionals = get_region(df2)
    provincials = get_province(df2)
    kpi_data, total_fund = calculate_kpis(df2)

    return {
        "df2": df2,
        "mini": mini,
        "maxi": maxi,
        "regionals": regionals,
        "provincials": provincials,
        "kpi_data": kpi_data,
        "total_fund": total_fund,
    }
