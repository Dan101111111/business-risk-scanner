import streamlit as st
from ui.forms import financial_input_form

st.set_page_config(
    page_title="Business Risk Scanner",
    layout="centered"
)

st.title("Business Risk Scanner")
st.markdown("Ingrese los datos financieros de la empresa")

data = financial_input_form()

if data:
    st.divider()
    st.subheader("Datos listos para análisis")

    st.json(data)

    st.info(
        "Los cálculos de ratios, Z-Score y gráficos se mostrarán aquí en las "
        "siguientes etapas del proyecto (Moreno has tu chamba pe)."
    )
