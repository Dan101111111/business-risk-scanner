def classify_risk(z):
    if z is None:
        return "Datos insuficientes"
    if z < 1.81:
        return "⚠️ Alto riesgo (posible quiebra)"
    elif z < 2.99:
        return "🔶 Riesgo moderado (zona gris)"
    else:
        return "🟢 Bajo riesgo (empresa sana)"
