from vizro.figures.library import kpi_card, kpi_card_reference
from dash import html


def get_kpi(df_map):
    """
    { kpi_title: df}
    
    """
    total_fund = 1000

    total_funds_kpi = html.Div(kpi_card_reference(
                            data_frame=df_map["total_funds_kpi"],
                            value_column="ABC",
                            reference_column="ABC",
                            icon="money_bag",
                            title="Total Allocated Funds",
                            value_format=f"₱{total_fund}" 
                            ),className="kpi-card")
    
    total_projects_kpi = html.Div(kpi_card_reference(
                        data_frame=df_map["total_projects_kpi"],
                        value_column="ABC",
                        reference_column="ABC",
                        icon="money_bag",
                        title="Total Allocated Funds",
                        value_format=f"₱{total_fund}" 
                        ),className="kpi-card")
    
    avg_contr_cost = html.Div(kpi_card_reference(
                    data_frame=df_map["avg_contr_cost"],
                    value_column="ABC",
                    reference_column="ABC",
                    icon="money_bag",
                    title="Total Allocated Funds",
                    value_format=f"₱{total_fund}" 
                    ),className="kpi-card")
    
    other_cards = html.Div(kpi_card_reference(
                data_frame=df_map["other_cards"],
                value_column="ABC",
                reference_column="ABC",
                icon="money_bag",
                title="Total Allocated Funds",
                value_format=f"₱{total_fund}" 
                ),className="kpi-card")
    
    return [total_funds_kpi, total_projects_kpi, other_cards, avg_contr_cost]