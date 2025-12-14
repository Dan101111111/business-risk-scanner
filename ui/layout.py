"""
Módulo de layout y componentes visuales reutilizables.

Este módulo contiene funciones para configurar el diseño general de la aplicación,
estilos personalizados y componentes visuales reutilizables.
"""

import streamlit as st
from datetime import datetime
from typing import Optional, Literal


def configurar_pagina() -> None:
    """
    Configura los ajustes generales de la página de Streamlit.
    Debe ser llamada al inicio de la aplicación.
    """
    st.set_page_config(
        page_title="Business Risk Scanner",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://github.com/Dan101111111/business-risk-scanner',
            'Report a bug': 'https://github.com/Dan101111111/business-risk-scanner/issues',
            'About': """
            # Business Risk Scanner 📊
            **Versión:** 1.0.0
            
            Herramienta de análisis de riesgo financiero empresarial basada en ratios 
            financieros y el Z-Score de Altman.
            
            Desarrollado por: Daniel, Igor, Mario, D'Alessandro y Bruno
            """
        }
    )


def aplicar_estilos_personalizados() -> None:
    """
    Aplica estilos CSS personalizados a la aplicación para mejorar la apariencia visual.
    """
    st.markdown("""
        <style>
        /* Estilos generales */
        .main {
            padding-top: 2rem;
        }
        
        /* Header personalizado */
        .custom-header {
            background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .custom-header h1 {
            color: white;
            margin: 0;
            font-size: 2.5rem;
            font-weight: 700;
        }
        
        .custom-header p {
            color: #e0e7ff;
            margin: 0.5rem 0 0 0;
            font-size: 1.1rem;
        }
        
        /* Cards personalizadas */
        .info-card {
            background-color: #f8fafc;
            border-left: 4px solid #3b82f6;
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
        }
        
        .warning-card {
            background-color: #fef3c7;
            border-left: 4px solid #f59e0b;
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
        }
        
        .success-card {
            background-color: #d1fae5;
            border-left: 4px solid #10b981;
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
        }
        
        .danger-card {
            background-color: #fee2e2;
            border-left: 4px solid #ef4444;
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
        }
        
        /* Botones mejorados */
        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }
        
        /* Métricas mejoradas */
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #f8fafc;
        }
        
        /* Tablas */
        .dataframe {
            border-radius: 8px;
            overflow: hidden;
        }
        
        /* Footer */
        .custom-footer {
            text-align: center;
            padding: 2rem 0;
            color: #64748b;
            border-top: 1px solid #e2e8f0;
            margin-top: 3rem;
        }
        
        /* Animación de loading */
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        .loading {
            animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }
        
        /* Tooltips mejorados */
        .tooltip-icon {
            color: #3b82f6;
            cursor: help;
            margin-left: 0.5rem;
        }
        </style>
    """, unsafe_allow_html=True)


def mostrar_header(titulo: str = "Business Risk Scanner", 
                   subtitulo: str = "Análisis de Riesgo Financiero Empresarial") -> None:
    """
    Muestra un header personalizado con estilo profesional.
    
    Args:
        titulo: Título principal de la aplicación
        subtitulo: Subtítulo o descripción breve
    """
    st.markdown(f"""
        <div class="custom-header">
            <h1>📊 {titulo}</h1>
            <p>{subtitulo}</p>
        </div>
    """, unsafe_allow_html=True)


def mostrar_sidebar_navegacion() -> str:
    """
    Muestra la barra lateral con opciones de navegación.
    
    Returns:
        Opción seleccionada por el usuario
    """
    with st.sidebar:
        st.image("https://via.placeholder.com/150x50/1e3a8a/ffffff?text=BRS", 
                 use_container_width=True)
        
        st.markdown("### 🧭 Navegación")
        
        opcion = st.radio(
            "Selecciona una sección:",
            ["🏠 Inicio", "📝 Análisis de Empresa", "📚 Ayuda", "ℹ️ Acerca de"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        st.markdown("### 📋 Guía Rápida")
        st.markdown("""
        1. Ingresa los datos financieros
        2. Revisa los ratios calculados
        3. Analiza el Z-Score
        4. Exporta los resultados
        """)
        
        st.markdown("---")
        
        # Información adicional
        with st.expander("⚙️ Configuración"):
            tema = st.selectbox("Tema de gráficos", ["Claro", "Oscuro", "Automático"])
            decimales = st.slider("Decimales en resultados", 0, 4, 2)
            st.session_state['config_decimales'] = decimales
        
        st.markdown("---")
        
        # Footer del sidebar
        st.markdown("""
        <div style="text-align: center; color: #64748b; font-size: 0.8rem;">
            <p>v1.0.0</p>
            <p>© 2025 BRS Team</p>
        </div>
        """, unsafe_allow_html=True)
        
        return opcion


def crear_card(titulo: str, contenido: str, 
               tipo: Literal["info", "warning", "success", "danger"] = "info") -> None:
    """
    Crea una card informativa con estilo personalizado.
    
    Args:
        titulo: Título de la card
        contenido: Contenido o descripción
        tipo: Tipo de card (info, warning, success, danger)
    """
    clase = f"{tipo}-card"
    
    iconos = {
        "info": "ℹ️",
        "warning": "⚠️",
        "success": "✅",
        "danger": "❌"
    }
    
    icono = iconos.get(tipo, "ℹ️")
    
    st.markdown(f"""
        <div class="{clase}">
            <h4>{icono} {titulo}</h4>
            <p>{contenido}</p>
        </div>
    """, unsafe_allow_html=True)


def crear_seccion(titulo: str, icono: str = "📌") -> None:
    """
    Crea una sección visual separada con título y línea divisoria.
    
    Args:
        titulo: Título de la sección
        icono: Emoji o icono para el título
    """
    st.markdown(f"## {icono} {titulo}")
    st.markdown("---")


def mostrar_footer() -> None:
    """
    Muestra el footer de la aplicación con información del equipo.
    """
    st.markdown("""
        <div class="custom-footer">
            <p><strong>Business Risk Scanner</strong> - Herramienta de Análisis Financiero</p>
            <p>Desarrollado por: Daniel, Igor, Mario, D'Alessandro y Bruno</p>
            <p style="margin-top: 1rem;">
                <a href="https://github.com/Dan101111111/business-risk-scanner" target="_blank">
                    📂 GitHub
                </a> | 
                <a href="#" target="_blank">
                    📖 Documentación
                </a> | 
                <a href="#" target="_blank">
                    📧 Contacto
                </a>
            </p>
            <p style="font-size: 0.85rem; color: #94a3b8; margin-top: 1rem;">
                Última actualización: Diciembre 2025
            </p>
        </div>
    """, unsafe_allow_html=True)


def mostrar_breadcrumb(ruta: list[str]) -> None:
    """
    Muestra un breadcrumb de navegación.
    
    Args:
        ruta: Lista con los nombres de las secciones (ej: ["Inicio", "Análisis", "Resultados"])
    """
    breadcrumb = " → ".join(ruta)
    st.markdown(f"*{breadcrumb}*")
    st.markdown("")


def mostrar_loading(mensaje: str = "Procesando...") -> None:
    """
    Muestra un spinner de carga con mensaje personalizado.
    
    Args:
        mensaje: Mensaje a mostrar durante la carga
    """
    with st.spinner(mensaje):
        import time
        time.sleep(0.5)  # Simulación mínima


def crear_tabs_principales() -> tuple:
    """
    Crea las tabs principales de la aplicación.
    
    Returns:
        Tuple con los objetos tab de Streamlit
    """
    tabs = st.tabs([
        "📝 Entrada de Datos",
        "📊 Resultados",
        "📈 Gráficos",
        "📄 Reporte"
    ])
    
    return tabs


def mostrar_ayuda_contextual(titulo: str, contenido: str) -> None:
    """
    Muestra un widget de ayuda contextual expandible.
    
    Args:
        titulo: Título del panel de ayuda
        contenido: Contenido markdown de la ayuda
    """
    with st.expander(f"❓ {titulo}"):
        st.markdown(contenido)


def crear_columnas_responsive(num_cols: int = 3) -> list:
    """
    Crea columnas responsive según el número especificado.
    
    Args:
        num_cols: Número de columnas a crear
        
    Returns:
        Lista de objetos columna de Streamlit
    """
    return st.columns(num_cols)


def mostrar_banner_estado(mensaje: str, 
                         tipo: Literal["info", "success", "warning", "error"] = "info") -> None:
    """
    Muestra un banner de estado temporal.
    
    Args:
        mensaje: Mensaje a mostrar
        tipo: Tipo de banner
    """
    if tipo == "success":
        st.success(mensaje)
    elif tipo == "warning":
        st.warning(mensaje)
    elif tipo == "error":
        st.error(mensaje)
    else:
        st.info(mensaje)


def crear_grid_metricas(metricas: list[dict]) -> None:
    """
    Crea un grid de métricas visualmente atractivo.
    
    Args:
        metricas: Lista de diccionarios con 'label', 'value' y opcionalmente 'delta'
        
    Example:
        metricas = [
            {"label": "Liquidez", "value": "2.5", "delta": "Saludable"},
            {"label": "ROE", "value": "15%", "delta": "+2%"}
        ]
    """
    cols = st.columns(len(metricas))
    
    for col, metrica in zip(cols, metricas):
        with col:
            st.metric(
                label=metrica['label'],
                value=metrica['value'],
                delta=metrica.get('delta')
            )


def mostrar_separador(altura: int = 20) -> None:
    """
    Muestra un espacio vertical separador.
    
    Args:
        altura: Altura del separador en píxeles
    """
    st.markdown(f"<div style='height: {altura}px'></div>", unsafe_allow_html=True)


def crear_contenedor_central(ancho_maximo: str = "1200px") -> None:
    """
    Crea un contenedor central con ancho máximo para mejor legibilidad.
    
    Args:
        ancho_maximo: Ancho máximo del contenedor
    """
    st.markdown(f"""
        <style>
        .main .block-container {{
            max-width: {ancho_maximo};
            padding-left: 2rem;
            padding-right: 2rem;
        }}
        </style>
    """, unsafe_allow_html=True)


def mostrar_pagina_inicio() -> None:
    """
    Muestra la página de inicio con información general de la aplicación.
    """
    mostrar_header()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 ¿Qué es Business Risk Scanner?
        
        Es una herramienta profesional para el **análisis de riesgo financiero** de empresas,
        que utiliza:
        
        - 📊 **Ratios Financieros**: Liquidez, solvencia, rentabilidad y eficiencia
        - 📈 **Z-Score de Altman**: Predicción de probabilidad de quiebra
        - 🎨 **Visualizaciones**: Gráficos interactivos y reportes ejecutivos
        - 📥 **Exportación**: Descarga de resultados en formato CSV
        """)
        
        st.markdown("### 🚀 Comenzar es fácil:")
        st.markdown("""
        1. Ingresa los datos financieros de la empresa
        2. El sistema calculará automáticamente los ratios
        3. Obtendrás el Z-Score y clasificación de riesgo
        4. Visualiza gráficos y exporta resultados
        """)
    
    with col2:
        crear_card(
            "💡 Consejo",
            "Asegúrate de tener los estados financieros actualizados para un análisis preciso.",
            tipo="info"
        )
        
        crear_card(
            "📚 Recursos",
            "Consulta la sección de Ayuda para entender cada ratio e indicador.",
            tipo="success"
        )
    
    st.markdown("---")
    
    # Métricas de ejemplo
    st.markdown("### 📊 Indicadores que Analizamos")
    
    cols = st.columns(4)
    indicadores = [
        {"icono": "💧", "nombre": "Liquidez", "desc": "Capacidad de pago"},
        {"icono": "🏦", "nombre": "Solvencia", "desc": "Nivel de deuda"},
        {"icono": "💰", "nombre": "Rentabilidad", "desc": "Generación de utilidades"},
        {"icono": "⚙️", "nombre": "Eficiencia", "desc": "Uso de recursos"}
    ]
    
    for col, ind in zip(cols, indicadores):
        with col:
            st.markdown(f"""
            <div style="text-align: center; padding: 1rem;">
                <div style="font-size: 3rem;">{ind['icono']}</div>
                <h4>{ind['nombre']}</h4>
                <p style="color: #64748b;">{ind['desc']}</p>
            </div>
            """, unsafe_allow_html=True)


def mostrar_pagina_ayuda() -> None:
    """
    Muestra la página de ayuda con documentación y guías.
    """
    crear_seccion("Ayuda y Documentación", "📚")
    
    tab1, tab2, tab3 = st.tabs(["📊 Ratios Financieros", "📈 Z-Score", "❓ FAQ"])
    
    with tab1:
        st.markdown("""
        ### Ratios de Liquidez
        
        **Liquidez Corriente** = Activo Corriente / Pasivo Corriente
        - Mide la capacidad de pagar deudas de corto plazo
        - Valor ideal: > 1.5
        
        **Prueba Ácida** = (Activo Corriente - Inventarios) / Pasivo Corriente
        - Medida más conservadora de liquidez
        - Valor ideal: > 1.0
        
        ### Ratios de Solvencia
        
        **Endeudamiento** = Pasivo Total / Activo Total
        - Proporción de activos financiados con deuda
        - Valor ideal: < 0.5 (50%)
        
        **Apalancamiento** = Activo Total / Patrimonio
        - Grado de uso de deuda para financiar activos
        - Valor ideal: < 2.0
        
        ### Ratios de Rentabilidad
        
        **ROA** = Utilidad Neta / Activo Total
        - Rentabilidad sobre activos
        - Valor ideal: > 10%
        
        **ROE** = Utilidad Neta / Patrimonio
        - Rentabilidad sobre patrimonio
        - Valor ideal: > 15%
        """)
    
    with tab2:
        st.markdown("""
        ### Z-Score de Altman
        
        El Z-Score es un modelo estadístico que predice la probabilidad de quiebra:
        
        **Fórmula:**
        ```
        Z = 1.2×(WC/TA) + 1.4×(RE/TA) + 3.3×(EBIT/TA) + 0.6×(MVE/TL) + 1.0×(Sales/TA)
        ```
        
        **Interpretación:**
        - **Z < 1.81**: 🔴 Alto riesgo - Alta probabilidad de quiebra
        - **1.81 ≤ Z < 2.99**: 🟡 Zona gris - Riesgo moderado
        - **Z ≥ 2.99**: 🟢 Zona segura - Baja probabilidad de quiebra
        
        **Variables:**
        - WC = Capital de trabajo
        - RE = Utilidades retenidas
        - EBIT = Utilidad antes de intereses e impuestos
        - MVE = Valor de mercado del patrimonio
        - TL = Pasivo total
        - TA = Activo total
        - Sales = Ventas
        """)
    
    with tab3:
        st.markdown("""
        ### Preguntas Frecuentes
        
        **¿Qué datos necesito para el análisis?**
        - Estados financieros actualizados (Balance General y Estado de Resultados)
        
        **¿Con qué frecuencia debo hacer el análisis?**
        - Se recomienda al menos trimestral, o cuando haya cambios significativos
        
        **¿Qué hacer si mi empresa está en "zona gris"?**
        - Revisar ratios específicos, mejorar liquidez y reducir endeudamiento
        
        **¿Es aplicable a todo tipo de empresas?**
        - El Z-Score original es para empresas manufactureras, pero se puede adaptar
        """)


def mostrar_pagina_acerca_de() -> None:
    """
    Muestra la página "Acerca de" con información del proyecto y equipo.
    """
    crear_seccion("Acerca del Proyecto", "ℹ️")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🏢 Business Risk Scanner
        
        Herramienta profesional de análisis de riesgo financiero desarrollada como
        proyecto académico por un equipo multidisciplinario.
        
        ### 👥 Equipo de Desarrollo
        
        - **Daniel**: Arquitectura y motor de cálculos
        - **Igor**: Z-Score y clasificación de riesgo
        - **Mario**: Formularios y validación de datos
        - **D'Alessandro**: Resultados y visualizaciones
        - **Bruno**: Documentación y despliegue
        
        ### 🛠️ Tecnologías Utilizadas
        
        - **Python**: Lenguaje principal
        - **Streamlit**: Framework de UI
        - **Plotly**: Gráficos interactivos
        - **Pandas**: Manipulación de datos
        """)
    
    with col2:
        st.markdown("""
        ### 📊 Versión
        **v1.0.0**
        
        ### 📅 Fecha
        Diciembre 2025
        
        ### 📝 Licencia
        MIT License
        
        ### 🔗 Enlaces
        - [GitHub](https://github.com/Dan101111111/business-risk-scanner)
        - [Documentación](#)
        - [Reportar Bug](#)
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🙏 Agradecimientos
    
    Este proyecto fue desarrollado como parte de un curso de Análisis Financiero
    y programación. Agradecemos a los profesores y compañeros por su apoyo.
    """)