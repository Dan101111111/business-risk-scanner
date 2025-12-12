# Business Risk Scanner 📊

**Business Risk Scanner** es una aplicación web desarrollada en Streamlit que evalúa el riesgo financiero empresarial mediante el cálculo de ratios clave y el modelo Z-Score de Altman. La herramienta genera análisis visuales y una clasificación automática del nivel de riesgo para apoyar decisiones económicas informadas.

## 🎯 Características Principales

- **Análisis de Ratios Financieros**: Cálculo de 13 indicadores clave de liquidez, solvencia, rentabilidad y eficiencia
- **Z-Score de Altman**: Predicción de riesgo de quiebra empresarial
- **Clasificación de Riesgo**: Categorización automática del nivel de riesgo
- **Interfaz Intuitiva**: Aplicación web fácil de usar en Streamlit
- **Análisis Visual**: Gráficos y reportes interactivos

## 📦 Estructura del Proyecto

```
business-risk-scanner/
├── risk_engine/          # Motor de cálculo financiero
│   ├── ratios.py        # Funciones de ratios financieros
│   ├── zscore.py        # Cálculo del Z-Score de Altman
│   └── classification.py # Clasificación de riesgo
├── tests/               # Tests unitarios
│   ├── test_ratios.py
│   └── test_zscore.py
├── ui/                  # Interfaz de usuario
│   ├── forms.py
│   ├── layout.py
│   └── view_results.py
├── utils/               # Utilidades
│   ├── sample_data.py
│   └── validation.py
├── examples/            # Ejemplos de uso
│   └── ejemplo_uso_ratios.py
├── app.py              # Aplicación principal Streamlit
└── requirements.txt    # Dependencias
```

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior

### Pasos de Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/business-risk-scanner.git
cd business-risk-scanner

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## 💻 Uso

### Ejecutar la Aplicación Web

```bash
streamlit run app.py
```

### Usar el Módulo de Ratios

```python
from risk_engine.ratios import ratio_liquidez, roe, periodo_medio_cobro

# Calcular ratio de liquidez
activo_corriente = 400000
pasivo_corriente = 200000
liquidez = ratio_liquidez(activo_corriente, pasivo_corriente)
print(f"Ratio de Liquidez: {liquidez}")  # 2.0

# Calcular rentabilidad sobre patrimonio
utilidad_neta = 120000
patrimonio = 600000
rentabilidad = roe(utilidad_neta, patrimonio)
print(f"ROE: {rentabilidad * 100:.1f}%")  # 20.0%

# Calcular período medio de cobro
cuentas_por_cobrar = 100000
ventas_credito = 730000
dias_cobro = periodo_medio_cobro(cuentas_por_cobrar, ventas_credito)
print(f"Período de Cobro: {dias_cobro:.0f} días")  # 50 días

# Manejo de división entre cero
resultado = ratio_liquidez(100000, 0)
if resultado is None:
    print("Error: No se puede calcular (pasivo corriente es cero)")
```

## 📊 Módulo de Ratios Financieros

El módulo `risk_engine/ratios.py` contiene **13 funciones** para calcular indicadores financieros:

### Ratios de Liquidez (3)

- **`ratio_liquidez()`** - Mide la capacidad de pago a corto plazo
  - Fórmula: Activo Corriente / Pasivo Corriente
- **`ratio_prueba_acida()`** - Liquidez inmediata excluyendo inventarios
  - Fórmula: (Activo Corriente - Inventarios) / Pasivo Corriente
- **`ratio_tesoreria()`** - Disponibilidad de efectivo inmediata
  - Fórmula: (Caja + Bancos + Inversiones CP) / Pasivo Corriente

### Ratios de Solvencia (2)

- **`ratio_endeudamiento()`** - Proporción de deuda sobre activos totales
  - Fórmula: Pasivo Total / Activo Total
- **`ratio_apalancamiento()`** - Multiplicador de capital (leverage)
  - Fórmula: Activo Total / Patrimonio

### Ratios de Rentabilidad (3)

- **`margen_neto()`** - Porcentaje de ganancia sobre ventas
  - Fórmula: Utilidad Neta / Ventas
- **`roe()`** - Rentabilidad sobre patrimonio (Return on Equity)
  - Fórmula: Utilidad Neta / Patrimonio
- **`roa()`** - Rentabilidad sobre activos (Return on Assets)
  - Fórmula: Utilidad Neta / Activos Totales

### Ratios de Eficiencia Operativa (5)

- **`rotacion_activos()`** - Eficiencia en el uso de activos para generar ventas
  - Fórmula: Ventas / Activos Totales
- **`rotacion_inventarios()`** - Veces que rota el inventario en el período
  - Fórmula: Costo de Ventas / Inventario Promedio
- **`dias_inventario()`** - Días promedio que permanece el inventario
  - Fórmula: 365 × Inventario Promedio / Costo de Ventas
- **`periodo_medio_cobro()`** - Días promedio de cobranza a clientes
  - Fórmula: 365 × Cuentas por Cobrar / Ventas a Crédito
- **`periodo_medio_pago()`** - Días promedio de pago a proveedores
  - Fórmula: 365 × Cuentas por Pagar / Compras a Crédito

### Ciclo de Conversión de Efectivo

Puedes calcular el ciclo completo de efectivo combinando los ratios de eficiencia:

```python
from risk_engine.ratios import dias_inventario, periodo_medio_cobro, periodo_medio_pago

di = dias_inventario(costo_ventas, inventario_promedio)
pmc = periodo_medio_cobro(cuentas_por_cobrar, ventas_credito)
pmp = periodo_medio_pago(cuentas_por_pagar, compras_credito)

if di is not None and pmc is not None and pmp is not None:
    ciclo_efectivo = di + pmc - pmp
    print(f"Ciclo de Conversión: {ciclo_efectivo:.0f} días")
```

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

---

## 🧪 Tests

El proyecto incluye una suite completa de tests unitarios.

### Ejecutar Tests

```bash
# Activar entorno virtual
.\venv\Scripts\activate

# Ejecutar todos los tests
python -m unittest discover tests -v

# Ejecutar tests de ratios específicamente
python -m unittest tests.test_ratios -v

# Ejecutar doctests del módulo de ratios
python -m doctest risk_engine/ratios.py -v
```

### Cobertura de Tests

- **43 tests unitarios** para el módulo de ratios
- **39 doctests** integrados en las funciones
- Cobertura de casos normales, división entre cero y valores negativos

## 📈 Ejemplo Completo

Consulta el archivo `examples/ejemplo_uso_ratios.py` para ver un análisis completo de dos empresas:

```bash
python examples/ejemplo_uso_ratios.py
```

Este script demuestra:

- Cálculo de todos los ratios disponibles
- Interpretación de resultados
- Manejo de casos especiales
- Análisis comparativo entre empresa saludable y empresa en riesgo

## 🛡️ Características Técnicas

- **Funciones puras**: Sin efectos secundarios
- **Type hints**: Todas las funciones tienen anotaciones de tipo (`Optional[float]`)
- **Manejo de errores**: Retorna `None` cuando hay división entre cero
- **Sin dependencias externas**: El módulo de ratios usa solo Python estándar
- **Documentación completa**: Docstrings en español con ejemplos
- **Separación de responsabilidades**: Lógica de negocio separada de la interfaz

## 📊 Interpretación de Resultados

### Ratios de Liquidez

- **Ratio > 2.0**: Excelente capacidad de pago
- **Ratio 1.0 - 2.0**: Saludable
- **Ratio < 1.0**: Posibles problemas de liquidez

### Ratios de Endeudamiento

- **< 0.5**: Bajo endeudamiento (conservador)
- **0.5 - 0.7**: Moderado
- **> 0.7**: Alto riesgo financiero

### Ratios de Rentabilidad (ROE)

- **> 15%**: Excelente rentabilidad
- **10% - 15%**: Buena
- **< 10%**: Baja rentabilidad

## 🔮 Próximos Pasos

- [x] Implementar módulo de Z-Score de Altman
- [x] Completar módulo de clasificación de riesgo
- [ ] Desarrollar interfaz completa en Streamlit
- [ ] Añadir visualizaciones gráficas
- [ ] Generar reportes en PDF

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📧 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.

---

**Versión**: 2.0  
**Última actualización**: Diciembre 2025

