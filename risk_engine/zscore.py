from typing import Optional

def z_score(
    working_capital: float,
    retained_earnings: float,
    ebit: float,
    market_value_equity: float,
    total_liabilities: float,
    sales: float,
    total_assets: float,
) -> Optional[float]:
    """
    Calcula el Z-Score de Altman para empresas manufactureras.

    Fórmula:
        Z = 1.2 * (WC / TA) +
            1.4 * (RE / TA) +
            3.3 * (EBIT / TA) +
            0.6 * (MVE / TL) +
            1.0 * (Sales / TA)

    Donde:
        WC  = Capital de trabajo
        RE  = Utilidades retenidas
        EBIT = Utilidad antes de intereses e impuestos
        MVE = Valor de mercado del patrimonio
        TL  = Pasivo total
        TA  = Activo total

    Retorna:
        Z-Score redondeado a 3 decimales, o None si no es posible calcular
        por denominadores en cero.
    """
    if total_assets == 0 or total_liabilities == 0:
        return None

    z = (
        1.2 * (working_capital / total_assets) +
        1.4 * (retained_earnings / total_assets) +
        3.3 * (ebit / total_assets) +
        0.6 * (market_value_equity / total_liabilities) +
        1.0 * (sales / total_assets)
    )
    return round(z, 3)
