from vizro.figures.library import kpi_card, kpi_card_reference


def get_kpi(df_map):
    """
    { kpi_title: df}
    
    """
    total_fund = 1000

    total_funds_kpi = kpi_card_reference(
                            data_frame=df_map["total_funds_kpi"],
                            value_column="ABC",
                            reference_column="ABC",
                            icon="money_bag",
                            title="Total Allocated Funds",
                            value_format=f"₱{total_fund}" 
                            )
    
    total_projects_kpi = kpi_card_reference(
                        data_frame=df_map["total_projects_kpi"],
                        value_column="ABC",
                        reference_column="ABC",
                        icon="money_bag",
                        title="Total Allocated Funds",
                        value_format=f"₱{total_fund}" 
                        )
    
    avg_contr_cost = kpi_card_reference(
                    data_frame=df_map["avg_contr_cost"],
                    value_column="ABC",
                    reference_column="ABC",
                    icon="money_bag",
                    title="Total Allocated Funds",
                    value_format=f"₱{total_fund}" 
                    )
    
    other_cards = kpi_card_reference(
                data_frame=df_map["other_cards"],
                value_column="ABC",
                reference_column="ABC",
                icon="money_bag",
                title="Total Allocated Funds",
                value_format=f"₱{total_fund}" 
                )
    
    return [total_funds_kpi, total_projects_kpi, other_cards, avg_contr_cost]