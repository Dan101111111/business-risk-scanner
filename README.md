# Business Risk Scanner

Business Risk Scanner es una aplicación en Streamlit que evalúa el riesgo financiero empresarial mediante el cálculo de ratios clave y el modelo Z-Score de Altman, generando análisis visuales y una clasificación automática del nivel de riesgo para apoyar decisiones económicas.

---

## 🧮 Módulo de Análisis de Riesgo Financiero: Z-Score de Altman

El proyecto incluye un módulo especializado para calcular el **Z-Score de Altman**, una métrica ampliamente utilizada para evaluar la probabilidad de quiebra en empresas. Además, incorpora un sistema de clasificación automática basado en dicho valor.

### 1. Cálculo del Z-Score

La fórmula utilizada es:

```
Z = 1.2 * (WC / TA) +
    1.4 * (RE / TA) +
    3.3 * (EBIT / TA) +
    0.6 * (MVE / TL) +
    1.0 * (Sales / TA)
```

**Donde:**

* WC = Capital de trabajo
* RE = Utilidades retenidas
* EBIT = Utilidad antes de intereses e impuestos
* MVE = Valor de mercado del patrimonio
* TL = Pasivo total
* TA = Activo total
* Sales = Ventas netas

El módulo retorna el Z-Score con tres decimales o `None` si existe división entre cero.

---

### 2. Clasificación del Riesgo

| Z-Score         | Clasificación       | Interpretación                    |
| --------------- | ------------------- | --------------------------------- |
| z < 1.81        | ⚠️ Alto riesgo      | Alta probabilidad de quiebra      |
| 1.81 ≤ z < 2.99 | 🔶 Riesgo moderado  | Zona gris                         |
| z ≥ 2.99        | 🟢 Bajo riesgo      | Empresa financieramente saludable |
| None            | Datos insuficientes | Cálculo inválido                  |

---

### 3. Ejemplo de uso

```python
from risk_engine.zscore import z_score
from risk_engine.classification import classify_risk

z = z_score(
    working_capital=200000,
    retained_earnings=150000,
    ebit=120000,
    market_value_equity=500000,
    total_liabilities=300000,
    sales=800000,
    total_assets=1000000
)

clasificacion = classify_risk(z)

print("Z-Score:", z)
print("Clasificación:", clasificacion)
```

---

### 4. Tests unitarios incluidos

El archivo `tests/test_zscore.py` valida:

* Cálculo correcto del Z-Score
* Manejo de divisiones entre cero
* Funcionamiento con valores negativos
* Clasificación del riesgo en sus tres niveles
* Respuesta correcta cuando el cálculo retorna `None`

