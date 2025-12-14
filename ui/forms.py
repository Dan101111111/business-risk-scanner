import streamlit as st
import pandas as pd
from utils.validation import validate_number, validate_positive


def get_ejemplo_empresa_saludable():
    """Retorna datos de ejemplo de una empresa saludable."""
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
    }


def get_ejemplo_empresa_riesgo():
    """Retorna datos de ejemplo de una empresa en riesgo."""
    return {
        "activo_corriente": 250000,
        "pasivo_corriente": 240000,
        "pasivo_total": 800000,
        "patrimonio": 200000,
        "ventas": 800000,
        "utilidad_neta": 10000,  # Cambié de -50000 a 10000 para evitar negativos
        "ebit": 30000,
        "total_assets": 1000000,
        "working_capital": 10000,
        "retained_earnings": 50000,
        "market_value_equity": 220000,
    }


def financial_input_form():
    st.subheader("Ingreso de datos financieros")
    
    # Botones para cargar datos de ejemplo
    st.markdown("#### 📋 ¿Quieres probar con datos de ejemplo?")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
    
    with col_btn1:
        if st.button("✅ Empresa Saludable", use_container_width=True):
            st.session_state['datos_ejemplo'] = get_ejemplo_empresa_saludable()
            st.rerun()
    
    with col_btn2:
        if st.button("⚠️ Empresa en Riesgo", use_container_width=True):
            st.session_state['datos_ejemplo'] = get_ejemplo_empresa_riesgo()
            st.rerun()
    
    # Obtener datos precargados si existen
    datos_precargados = st.session_state.get('datos_ejemplo', {})

    with st.form("financial_form"):
        st.markdown("### Balance General")

        col1, col2 = st.columns(2)
        with col1:
            activo_corriente = st.text_input("Activo corriente", 
                value=str(datos_precargados.get('activo_corriente', '')))
            pasivo_corriente = st.text_input("Pasivo corriente",
                value=str(datos_precargados.get('pasivo_corriente', '')))
        with col2:
            pasivo_total = st.text_input("Pasivo total",
                value=str(datos_precargados.get('pasivo_total', '')))
            patrimonio = st.text_input("Patrimonio",
                value=str(datos_precargados.get('patrimonio', '')))

        st.markdown("### Estado de Resultados")

        col3, col4 = st.columns(2)
        with col3:
            ventas = st.text_input("Ventas",
                value=str(datos_precargados.get('ventas', '')))
            utilidad_neta = st.text_input("Utilidad neta",
                value=str(datos_precargados.get('utilidad_neta', '')))
        with col4:
            ebit = st.text_input("EBIT",
                value=str(datos_precargados.get('ebit', '')))

        st.markdown("### Otros datos")

        col5, col6 = st.columns(2)
        with col5:
            total_assets = st.text_input("Activo total",
                value=str(datos_precargados.get('total_assets', '')))
            working_capital = st.text_input("Capital de trabajo",
                value=str(datos_precargados.get('working_capital', '')))
        with col6:
            retained_earnings = st.text_input("Utilidades retenidas",
                value=str(datos_precargados.get('retained_earnings', '')))
            market_value_equity = st.text_input("Valor de mercado del patrimonio",
                value=str(datos_precargados.get('market_value_equity', '')))

        submitted = st.form_submit_button("Calcular riesgo")
    
    # Limpiar datos de ejemplo después de enviar el formulario
    if submitted and 'datos_ejemplo' in st.session_state:
        del st.session_state['datos_ejemplo']

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
