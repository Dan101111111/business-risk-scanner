"""
Módulo de layout y componentes visuales reutilizables.

Este módulo contiene funciones para configurar el diseño general de la aplicación,
estilos personalizados y componentes visuales reutilizables.
"""

import streamlit as st
from typing import Literal


# --------------------------------------------------
# CONFIGURACIÓN GENERAL
# --------------------------------------------------

def configurar_pagina() -> None:
    st.set_page_config(
        page_title="Business Risk Scanner",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Get Help": "https://github.com/Dan101111111/business-risk-scanner",
            "Report a bug": "https://github.com/Dan101111111/business-risk-scanner/issues",
            "About": """
            # Business Risk Scanner 📊
            **Versión:** 1.0.0
            
            Herramienta de análisis de riesgo financiero empresarial basada en ratios 
            financieros y el Z-Score de Altman.
            
            Desarrollado por: Daniel, Igor, Mario, D'Alessandro y Bruno
            """
        }
    )


# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

def aplicar_estilos_personalizados() -> None:
    dark_mode = st.session_state.get("dark_mode", True)

    if dark_mode:
        bg_color = "#0e1117"
        text_color = "#fafafa"
        card_bg = "#1e293b"
        secondary_bg = "#262730"
        border_color = "#374151"
    else:
        bg_color = "#ffffff"
        text_color = "#1f2937"
        card_bg = "#f8fafc"
        secondary_bg = "#f1f5f9"
        border_color = "#e5e7eb"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
        }}

        .custom-header {{
            background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }}

        .info-card, .warning-card, .success-card, .danger-card {{
            background-color: {card_bg};
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
            color: {text_color};
        }}

        .info-card {{ border-left: 4px solid #3b82f6; }}
        .warning-card {{ border-left: 4px solid #f59e0b; }}
        .success-card {{ border-left: 4px solid #10b981; }}
        .danger-card {{ border-left: 4px solid #ef4444; }}

        .custom-footer {{
            text-align: center;
            padding: 2rem 0;
            border-top: 1px solid {border_color};
            margin-top: 3rem;
            color: #64748b;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# COMPONENTES VISUALES
# --------------------------------------------------

def mostrar_header(
    titulo: str = "Business Risk Scanner",
    subtitulo: str = "Análisis de Riesgo Financiero Empresarial"
) -> None:
    st.markdown(
        f"""
        <div class="custom-header">
            <h1>📊 {titulo}</h1>
            <p>{subtitulo}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def mostrar_separador(altura: int = 20) -> None:
    """
    Muestra un espacio vertical separador.
    
    Args:
        altura: Altura del separador en píxeles
    """
    st.markdown(
        f"<div style='height: {altura}px'></div>",
        unsafe_allow_html=True
    )

def crear_card(
    titulo: str,
    contenido: str,
    tipo: Literal["info", "warning", "success", "danger"] = "info"
) -> None:
    iconos = {
        "info": "ℹ️",
        "warning": "⚠️",
        "success": "✅",
        "danger": "❌"
    }

    st.markdown(
        f"""
        <div class="{tipo}-card">
            <h4>{iconos.get(tipo, "ℹ️")} {titulo}</h4>
            <p>{contenido}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def crear_seccion(titulo: str, icono: str = "📌") -> None:
    st.markdown(f"## {icono} {titulo}")
    st.markdown("---")


def mostrar_footer() -> None:
    st.markdown(
        """
        <div class="custom-footer">
            <p><strong>Business Risk Scanner</strong></p>
            <p>Desarrollado por: Daniel, Igor, Mario, D'Alessandro y Bruno</p>
            <p style="font-size: 0.85rem;">Última actualización: Diciembre 2025</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

def mostrar_sidebar_navegacion() -> str:
    with st.sidebar:
        st.markdown("## 📊 BRS")
        opcion = st.radio(
            "Navegación",
            ["🏠 Inicio", "📝 Análisis de Empresa", "📚 Ayuda", "ℹ️ Acerca de"],
            label_visibility="collapsed"
        )
        return opcion


# --------------------------------------------------
# PÁGINAS
# --------------------------------------------------

def mostrar_pagina_inicio() -> None:
    mostrar_header()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            """
            ### 🎯 ¿Qué es Business Risk Scanner?
            Herramienta profesional para analizar el **riesgo financiero empresarial** 
            mediante ratios financieros y el **Z-Score de Altman**.
            
            ### 🚀 Comenzar es fácil:
            1. Ve a **Análisis de Empresa** en el menú lateral
            2. Usa los botones de **datos de ejemplo** o ingresa tus propios datos
            3. Obtén ratios financieros y Z-Score automáticamente
            4. Visualiza gráficos interactivos y exporta resultados
            """
        )

    with col2:
        crear_card(
            "💡 Consejo",
            "Utiliza estados financieros actualizados para un análisis preciso.",
            "info"
        )
        
        crear_card(
            "🎯 Prueba Rápida",
            "Usa los datos de ejemplo para ver las visualizaciones inmediatamente.",
            "success"
        )

    st.markdown("---")
    
    st.markdown("### 📊 Indicadores Analizados")

    indicadores = [
        {"icono": "💧", "nombre": "Liquidez", "desc": "Capacidad de pago"},
        {"icono": "🏦", "nombre": "Solvencia", "desc": "Nivel de deuda"},
        {"icono": "💰", "nombre": "Rentabilidad", "desc": "Utilidades"},
        {"icono": "⚙️", "nombre": "Eficiencia", "desc": "Uso de recursos"},
    ]

    cols = st.columns(4)
    for col, ind in zip(cols, indicadores):
        with col:
            st.markdown(
                f"""
                <div class="info-card" style="text-align:center">
                    <h3>{ind['icono']} {ind['nombre']}</h3>
                    <p>{ind['desc']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    
    st.markdown("---")
    
    # Sección de comparación de ejemplos
    st.markdown("### 📈 Ejemplos de Análisis")
    st.markdown("Ve cómo el sistema evalúa diferentes empresas:")
    
    col_ej1, col_ej2 = st.columns(2)
    
    with col_ej1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
                    padding: 1.5rem; border-radius: 10px; color: white;">
            <h4>✅ Empresa Saludable</h4>
            <ul style="color: white;">
                <li>Liquidez: <strong>2.0</strong> (Excelente)</li>
                <li>Endeudamiento: <strong>40%</strong> (Saludable)</li>
                <li>ROE: <strong>25%</strong> (Muy bueno)</li>
                <li>Z-Score: <strong>~3.5</strong> (Zona segura)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_ej2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); 
                    padding: 1.5rem; border-radius: 10px; color: white;">
            <h4>⚠️ Empresa en Riesgo</h4>
            <ul style="color: white;">
                <li>Liquidez: <strong>1.04</strong> (Crítico)</li>
                <li>Endeudamiento: <strong>80%</strong> (Muy alto)</li>
                <li>ROE: <strong>5%</strong> (Bajo)</li>
                <li>Z-Score: <strong>~1.2</strong> (Alto riesgo)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


def mostrar_pagina_ayuda() -> None:
    mostrar_header("Ayuda y Documentación", "Guía completa del sistema")

    tab1, tab2, tab3 = st.tabs(["📊 Ratios", "📈 Z-Score", "❓ FAQ"])

    with tab1:
        st.markdown("### Ratios Financieros\n- Liquidez\n- Solvencia\n- Rentabilidad")

    with tab2:
        st.markdown(
            """
            ### Z-Score de Altman
            - Z < 1.81: 🔴 Alto riesgo  
            - 1.81 ≤ Z < 2.99: 🟡 Riesgo medio  
            - Z ≥ 2.99: 🟢 Bajo riesgo
            """
        )

    with tab3:
        st.markdown(
            """
            ### Preguntas Frecuentes

            **¿Con qué frecuencia debo hacer el análisis?**  
            - Al menos trimestral.

            **¿Es aplicable a todo tipo de empresas?**  
            - Principalmente manufactureras, con adaptaciones.
            """
        )


def mostrar_pagina_acerca_de() -> None:
    crear_seccion("Acerca del Proyecto", "ℹ️")

    st.markdown(
        """
        ### 👥 Equipo
        - Daniel  
        - Igor  
        - Mario  
        - D'Alessandro  
        - Bruno  

        ### 🛠️ Tecnologías
        - Python
        - Streamlit
        - Pandas
        - Plotly
        """
    )
