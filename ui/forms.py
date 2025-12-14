import streamlit as st
import pandas as pd
from utils.validation import validate_number, validate_positive


def financial_input_form():
    st.subheader("Ingreso de datos financieros")

    with st.form("financial_form"):
        st.markdown("### Balance General")

        activo_corriente = st.text_input("Activo corriente")
        pasivo_corriente = st.text_input("Pasivo corriente")
        pasivo_total = st.text_input("Pasivo total")
        patrimonio = st.text_input("Patrimonio")

        st.markdown("### Estado de Resultados")

        ventas = st.text_input("Ventas")
        utilidad_neta = st.text_input("Utilidad neta")
        ebit = st.text_input("EBIT")

        st.markdown("### Otros datos")

        total_assets = st.text_input("Activo total")
        working_capital = st.text_input("Capital de trabajo")
        retained_earnings = st.text_input("Utilidades retenidas")
        market_value_equity = st.text_input("Valor de mercado del patrimonio")

        submitted = st.form_submit_button("Calcular riesgo")

    if not submitted:
        return None

    # Validación
    fields = {
        "activo_corriente": activo_corriente,
        "pasivo_corriente": pasivo_corriente,
        "pasivo_total": pasivo_total,
        "patrimonio": patrimonio,
        "ventas": ventas,
        "utilidad_neta": utilidad_neta,
        "ebit": ebit,
        "total_assets": total_assets,
        "working_capital": working_capital,
        "retained_earnings": retained_earnings,
        "market_value_equity": market_value_equity,
    }

    data = {}

    for name, value in fields.items():
        value = validate_number(value, name)
        if value is None:
            return None
        value = validate_positive(value, name)
        if value is None:
            return None
        data[name] = value

    st.success("Datos validados correctamente")

    return data
