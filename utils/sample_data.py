"""
Datos de ejemplo para testing y demostración.
"""

def get_ejemplo_empresa_saludable():
    """
    Retorna datos de ejemplo de una empresa financieramente saludable.
    
    Returns:
        dict: Datos financieros de una empresa saludable
    """
    return {
        "activo_corriente": 400000,
        "pasivo_corriente": 200000,
        "pasivo_total": 400000,
        "patrimonio": 600000,
        "ventas": 2000000,
        "utilidad_neta": 150000,
        "ebit": 250000,
        "total_assets": 1000000,
        "working_capital": 200000,
        "retained_earnings": 300000,
        "market_value_equity": 650000,
        # Nuevos campos
        "inventarios": 120000,
        "inventario_promedio": 100000,
        "costo_ventas": 1200000,
        "total_liabilities": 400000,
    }


def get_ejemplo_empresa_riesgo():
    """
    Retorna datos de ejemplo de una empresa en riesgo financiero.
    Incluye utilidad neta negativa como caso real.
    
    Returns:
        dict: Datos financieros de una empresa en riesgo
    """
    return {
        "activo_corriente": 250000,
        "pasivo_corriente": 240000,
        "pasivo_total": 800000,
        "patrimonio": 200000,
        "ventas": 800000,
        "utilidad_neta": -50000,  # Empresa en pérdidas (ahora permitido)
        "ebit": 30000,
        "total_assets": 1000000,
        "working_capital": 10000,
        "retained_earnings": 50000,
        "market_value_equity": 220000,
        # Nuevos campos
        "inventarios": 100000,
        "inventario_promedio": 95000,
        "costo_ventas": 500000,
        "total_liabilities": 800000,
    }