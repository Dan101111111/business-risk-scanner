import streamlit as st
import pandas as pd
from utils.validation import validate_number, validate_positive


def financial_input_form():
    st.subheader("Ingreso de datos financieros")

    with st.form("financial_form"):
        st.markdown("### Balance General")

        col1, col2 = st.columns(2)
        with col1:
            activo_corriente = st.text_input("Activo corriente")
            pasivo_corriente = st.text_input("Pasivo corriente")
        with col2:
            pasivo_total = st.text_input("Pasivo total")
            patrimonio = st.text_input("Patrimonio")

        st.markdown("### Estado de Resultados")

        col3, col4 = st.columns(2)
        with col3:
            ventas = st.text_input("Ventas")
            utilidad_neta = st.text_input("Utilidad neta")
        with col4:
            ebit = st.text_input("EBIT")

        st.markdown("### Otros datos")

        col5, col6 = st.columns(2)
        with col5:
            total_assets = st.text_input("Activo total")
            working_capital = st.text_input("Capital de trabajo")
        with col6:
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
