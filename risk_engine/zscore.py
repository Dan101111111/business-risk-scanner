def z_score(working_capital, retained_earnings, ebit, market_value_equity, total_liabilities, sales, total_assets):
    try:
        z = (
            1.2 * (working_capital / total_assets) +
            1.4 * (retained_earnings / total_assets) +
            3.3 * (ebit / total_assets) +
            0.6 * (market_value_equity / total_liabilities) +
            1.0 * (sales / total_assets)
        )
        return round(z, 3)
    except ZeroDivisionError:
        return None
