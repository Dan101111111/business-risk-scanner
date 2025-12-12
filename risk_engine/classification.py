from typing import Optional

def classify_risk(z: Optional[float]) -> str:
    """
    Clasifica el nivel de riesgo financiero según el Z-Score de Altman.

    Args:
        z: Valor del Z-Score calculado. Puede ser None si no se pudo calcular.

    Returns:
        Cadena descriptiva del nivel de riesgo:
        - "Datos insuficientes" si z es None.
        - "⚠️ Alto riesgo (posible quiebra)" si z < 1.81.
        - "🔶 Riesgo moderado (zona gris)" si 1.81 <= z < 2.99.
        - "🟢 Bajo riesgo (empresa sana)" si z >= 2.99.
    """
    if z is None:
        return "Datos insuficientes"
    if z < 1.81:
        return "⚠️ Alto riesgo (posible quiebra)"
    elif z < 2.99:
        return "🔶 Riesgo moderado (zona gris)"
    else:
        return "🟢 Bajo riesgo (empresa sana)"
