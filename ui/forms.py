import streamlit as st
import pandas as pd
from utils.validation import validate_number, validate_positive
from utils.sample_data import get_ejemplo_empresa_saludable, get_ejemplo_empresa_riesgo


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
            retained_earnings = st.text_input("Utilidades retenidas",
                value=str(datos_precargados.get('retained_earnings', '')))
            inventarios = st.text_input("Inventarios (saldo)",
                value=str(datos_precargados.get('inventarios', '')),
                help="Dejar vacío para estimar como 30% del activo corriente")
        with col6:
            market_value_equity = st.text_input("Valor de mercado del patrimonio",
                value=str(datos_precargados.get('market_value_equity', '')))
            inventario_promedio = st.text_input("Inventario promedio",
                value=str(datos_precargados.get('inventario_promedio', '')),
                help="Dejar vacío para usar inventarios como proxy")
            costo_ventas = st.text_input("Costo de ventas",
                value=str(datos_precargados.get('costo_ventas', '')),
                help="Dejar vacío para estimar como 60% de ventas")
            total_liabilities = st.text_input("Pasivo total (para Z-Score)",
                value=str(datos_precargados.get('total_liabilities', '')),
                help="Dejar vacío para usar pasivo_total")

        submitted = st.form_submit_button("Calcular riesgo")
    
    # Limpiar datos de ejemplo después de enviar el formulario
    if submitted and 'datos_ejemplo' in st.session_state:
        del st.session_state['datos_ejemplo']

    if not submitted:
        return None

    # Validación
    # Campos obligatorios
    campos_obligatorios = {
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
    
    # Campos opcionales (pueden estar vacíos)
    campos_opcionales = {
        "inventarios": inventarios,
        "inventario_promedio": inventario_promedio,
        "costo_ventas": costo_ventas,
        "total_liabilities": total_liabilities,
    }
    
    # Campos que NO pueden ser negativos (>=0)
    campos_no_negativos = {
        "activo_corriente", "pasivo_corriente", "pasivo_total", 
        "patrimonio", "ventas", "total_assets", "market_value_equity",
        "inventarios", "inventario_promedio", "costo_ventas", "total_liabilities"
    }
    
    # Campos que SÍ pueden ser negativos
    # (utilidad_neta, ebit, working_capital, retained_earnings)

    data = {}

    # Validar campos obligatorios
    for name, value in campos_obligatorios.items():
        value = validate_number(value, name)
        if value is None:
            return None
        # Solo validar positividad si el campo está en campos_no_negativos
        if name in campos_no_negativos:
            value = validate_positive(value, name)
            if value is None:
                return None
        data[name] = value
    
    # Validar campos opcionales (si están llenos)
    for name, value in campos_opcionales.items():
        if value and str(value).strip():  # Si el usuario ingresó algo
            value = validate_number(value, name)
            if value is None:
                return None
            # Solo validar positividad si el campo está en campos_no_negativos
            if name in campos_no_negativos:
                value = validate_positive(value, name)
                if value is None:
                    return None
            data[name] = value
        # Si está vacío, no agregarlo al diccionario (el backend usará aproximaciones)

    st.success("Datos validados correctamente")

    return data
