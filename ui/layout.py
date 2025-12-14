"""
Módulo de visualización de resultados.

Este módulo contiene funciones para mostrar los resultados del análisis financiero
incluyendo ratios, Z-Score, clasificación de riesgo y gráficos interactivos.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, Optional


def mostrar_seccion_ratios(ratios: Dict[str, Optional[float]]) -> None:
    """
    Muestra los ratios financieros en una tabla organizada por categorías.
    
    Args:
        ratios: Diccionario con los ratios calculados
    """
    st.header("📊 Ratios Financieros Calculados")
    
    # Organizar ratios por categoría
    categorias = {
        "💧 Liquidez": {
            "Liquidez Corriente": ratios.get("liquidez"),
            "Prueba Ácida": ratios.get("prueba_acida"),
        },
        "🏦 Solvencia": {
            "Endeudamiento": ratios.get("endeudamiento"),
            "Apalancamiento": ratios.get("apalancamiento"),
        },
        "💰 Rentabilidad": {
            "ROA (Rentabilidad sobre Activos)": ratios.get("roa"),
            "ROE (Rentabilidad sobre Patrimonio)": ratios.get("roe"),
            "Margen de Utilidad": ratios.get("margen_utilidad"),
        },
        "⚙️ Eficiencia": {
            "Rotación de Activos": ratios.get("rotacion_activos"),
            "Rotación de Inventarios": ratios.get("rotacion_inventarios"),
        }
    }
    
    # Crear columnas para mejor distribución
    cols = st.columns(2)
    
    for idx, (categoria, items) in enumerate(categorias.items()):
        with cols[idx % 2]:
            st.subheader(categoria)
            
            # Crear DataFrame para cada categoría
            data = []
            for nombre, valor in items.items():
                if valor is not None:
                    # Formatear según el tipo de ratio
                    if "Margen" in nombre or "ROA" in nombre or "ROE" in nombre:
                        valor_str = f"{valor * 100:.2f}%"
                    elif "Endeudamiento" in nombre:
                        valor_str = f"{valor * 100:.2f}%"
                    else:
                        valor_str = f"{valor:.2f}"
                    
                    # Determinar color según valor
                    color = interpretar_ratio(nombre, valor)
                    data.append({"Indicador": nombre, "Valor": valor_str, "Estado": color})
                else:
                    data.append({"Indicador": nombre, "Valor": "N/A", "Estado": "⚪"})
            
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True, hide_index=True)


def interpretar_ratio(nombre: str, valor: float) -> str:
    """
    Interpreta el valor de un ratio y devuelve un indicador visual.
    
    Args:
        nombre: Nombre del ratio
        valor: Valor calculado del ratio
        
    Returns:
        Emoji indicador: 🟢 (bueno), 🟡 (aceptable), 🔴 (malo)
    """
    # Liquidez Corriente
    if "Liquidez Corriente" in nombre:
        if valor >= 2.0:
            return "🟢"
        elif valor >= 1.0:
            return "🟡"
        else:
            return "🔴"
    
    # Prueba Ácida
    if "Prueba Ácida" in nombre:
        if valor >= 1.0:
            return "🟢"
        elif valor >= 0.7:
            return "🟡"
        else:
            return "🔴"
    
    # Endeudamiento
    if "Endeudamiento" in nombre:
        if valor <= 0.5:
            return "🟢"
        elif valor <= 0.7:
            return "🟡"
        else:
            return "🔴"
    
    # Apalancamiento
    if "Apalancamiento" in nombre:
        if valor <= 2.0:
            return "🟢"
        elif valor <= 3.0:
            return "🟡"
        else:
            return "🔴"
    
    # Rentabilidad (ROA, ROE, Margen)
    if "ROA" in nombre or "ROE" in nombre or "Margen" in nombre:
        if valor >= 0.1:  # 10%
            return "🟢"
        elif valor >= 0.05:  # 5%
            return "🟡"
        else:
            return "🔴"
    
    # Rotación de Activos
    if "Rotación de Activos" in nombre:
        if valor >= 1.0:
            return "🟢"
        elif valor >= 0.5:
            return "🟡"
        else:
            return "🔴"
    
    # Rotación de Inventarios
    if "Rotación de Inventarios" in nombre:
        if valor >= 6.0:
            return "🟢"
        elif valor >= 3.0:
            return "🟡"
        else:
            return "🔴"
    
    return "⚪"


def mostrar_zscore(z_score: Optional[float], clasificacion: str) -> None:
    """
    Muestra el Z-Score de Altman y su clasificación de riesgo.
    
    Args:
        z_score: Valor del Z-Score calculado
        clasificacion: Clasificación de riesgo asociada
    """
    st.header("📈 Z-Score de Altman")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if z_score is not None:
            # Mostrar el valor del Z-Score en una métrica grande
            st.metric(label="Valor Z-Score", value=f"{z_score:.3f}")
        else:
            st.metric(label="Valor Z-Score", value="N/A")
    
    with col2:
        # Mostrar la clasificación con formato destacado
        st.markdown("### Clasificación de Riesgo")
        
        if "Alto riesgo" in clasificacion:
            st.error(clasificacion)
        elif "Riesgo moderado" in clasificacion:
            st.warning(clasificacion)
        elif "Bajo riesgo" in clasificacion:
            st.success(clasificacion)
        else:
            st.info(clasificacion)
    
    # Gráfico de gauge/medidor para el Z-Score
    if z_score is not None:
        crear_gauge_zscore(z_score)
    
    # Información adicional sobre la escala
    with st.expander("ℹ️ ¿Cómo interpretar el Z-Score?"):
        st.markdown("""
        El **Z-Score de Altman** es un modelo que predice la probabilidad de quiebra de una empresa:
        
        - **Z < 1.81**: 🔴 Alto riesgo - Alta probabilidad de quiebra
        - **1.81 ≤ Z < 2.99**: 🟡 Zona gris - Riesgo moderado
        - **Z ≥ 2.99**: 🟢 Zona segura - Baja probabilidad de quiebra
        
        **Componentes del Z-Score:**
        - Capital de trabajo / Activos totales (peso 1.2)
        - Utilidades retenidas / Activos totales (peso 1.4)
        - EBIT / Activos totales (peso 3.3)
        - Valor de mercado del patrimonio / Pasivo total (peso 0.6)
        - Ventas / Activos totales (peso 1.0)
        """)


def crear_gauge_zscore(z_score: float) -> None:
    """
    Crea un gráfico de tipo gauge (medidor) para visualizar el Z-Score.
    
    Args:
        z_score: Valor del Z-Score
    """
    # Determinar el color según la zona
    if z_score < 1.81:
        color = "red"
    elif z_score < 2.99:
        color = "orange"
    else:
        color = "green"
    
    # Crear el gráfico de gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=z_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Escala Z-Score", 'font': {'size': 20}},
        gauge={
            'axis': {'range': [None, 5], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 1.81], 'color': 'rgba(255, 0, 0, 0.2)'},
                {'range': [1.81, 2.99], 'color': 'rgba(255, 165, 0, 0.2)'},
                {'range': [2.99, 5], 'color': 'rgba(0, 255, 0, 0.2)'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 2.99
            }
        }
    ))
    
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)


def crear_grafico_barras_ratios(ratios: Dict[str, Optional[float]]) -> None:
    """
    Crea un gráfico de barras comparando los ratios calculados.
    
    Args:
        ratios: Diccionario con los ratios calculados
    """
    st.header("📊 Visualización de Ratios")
    
    # Filtrar ratios no nulos y organizarlos
    ratios_validos = {k: v for k, v in ratios.items() if v is not None}
    
    if not ratios_validos:
        st.warning("No hay ratios disponibles para visualizar.")
        return
    
    # Crear tabs para diferentes categorías
    tab1, tab2, tab3, tab4 = st.tabs(["💧 Liquidez", "🏦 Solvencia", "💰 Rentabilidad", "⚙️ Eficiencia"])
    
    with tab1:
        liquidez_data = {
            "Liquidez Corriente": ratios.get("liquidez"),
            "Prueba Ácida": ratios.get("prueba_acida"),
        }
        crear_barras_categoria(liquidez_data, "Ratios de Liquidez", referencia=1.5)
    
    with tab2:
        solvencia_data = {
            "Endeudamiento": ratios.get("endeudamiento"),
            "Apalancamiento": ratios.get("apalancamiento"),
        }
        crear_barras_categoria(solvencia_data, "Ratios de Solvencia")
    
    with tab3:
        rentabilidad_data = {
            "ROA": ratios.get("roa"),
            "ROE": ratios.get("roe"),
            "Margen de Utilidad": ratios.get("margen_utilidad"),
        }
        crear_barras_categoria(rentabilidad_data, "Ratios de Rentabilidad (%)", multiplicar_100=True)
    
    with tab4:
        eficiencia_data = {
            "Rotación de Activos": ratios.get("rotacion_activos"),
            "Rotación de Inventarios": ratios.get("rotacion_inventarios"),
        }
        crear_barras_categoria(eficiencia_data, "Ratios de Eficiencia")


def crear_barras_categoria(data: Dict[str, Optional[float]], titulo: str, 
                           referencia: Optional[float] = None, 
                           multiplicar_100: bool = False) -> None:
    """
    Crea un gráfico de barras para una categoría específica de ratios.
    
    Args:
        data: Diccionario con los ratios de la categoría
        titulo: Título del gráfico
        referencia: Línea de referencia opcional
        multiplicar_100: Si se debe multiplicar valores por 100 (para porcentajes)
    """
    # Filtrar valores nulos
    data_validos = {k: v for k, v in data.items() if v is not None}
    
    if not data_validos:
        st.info("No hay datos disponibles para esta categoría.")
        return
    
    # Preparar datos
    nombres = list(data_validos.keys())
    valores = list(data_validos.values())
    
    if multiplicar_100:
        valores = [v * 100 for v in valores]
    
    # Crear gráfico de barras
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=nombres,
        y=valores,
        marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'][:len(nombres)],
        text=[f'{v:.2f}' for v in valores],
        textposition='auto',
    ))
    
    # Agregar línea de referencia si se especifica
    if referencia is not None:
        fig.add_hline(y=referencia, line_dash="dash", line_color="red", 
                      annotation_text=f"Referencia: {referencia}")
    
    fig.update_layout(
        title=titulo,
        xaxis_title="Indicador",
        yaxis_title="Valor",
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)


def crear_radar_chart(ratios: Dict[str, Optional[float]]) -> None:
    """
    Crea un gráfico de radar para visualizar todos los ratios de forma comparativa.
    
    Args:
        ratios: Diccionario con todos los ratios calculados
    """
    st.header("🎯 Radar de Indicadores Financieros")
    
    # Seleccionar ratios principales y normalizarlos
    ratios_radar = {
        "Liquidez": ratios.get("liquidez"),
        "Prueba Ácida": ratios.get("prueba_acida"),
        "Endeudamiento": ratios.get("endeudamiento"),
        "ROA": ratios.get("roa"),
        "ROE": ratios.get("roe"),
        "Rotación Activos": ratios.get("rotacion_activos"),
    }
    
    # Filtrar valores nulos
    ratios_validos = {k: v for k, v in ratios_radar.items() if v is not None}
    
    if len(ratios_validos) < 3:
        st.warning("Se necesitan al menos 3 ratios para crear el gráfico de radar.")
        return
    
    # Normalizar valores para el radar (escala 0-10)
    categorias = list(ratios_validos.keys())
    valores = list(ratios_validos.values())
    
    # Normalización simple (puedes ajustar según necesites)
    valores_norm = []
    for cat, val in zip(categorias, valores):
        if "Liquidez" in cat or "Prueba" in cat:
            valores_norm.append(min(val * 5, 10))  # Máx esperado ~2
        elif "Endeudamiento" in cat:
            valores_norm.append(max(10 - val * 10, 0))  # Invertir (menor es mejor)
        elif "ROA" in cat or "ROE" in cat:
            valores_norm.append(min(val * 50, 10))  # Máx esperado ~0.2 (20%)
        elif "Rotación" in cat:
            valores_norm.append(min(val * 5, 10))  # Máx esperado ~2
        else:
            valores_norm.append(min(val, 10))
    
    # Crear gráfico de radar
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=valores_norm,
        theta=categorias,
        fill='toself',
        name='Empresa'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        showlegend=False,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **Nota:** Los valores están normalizados en una escala de 0 a 10 para facilitar la comparación visual.")


def mostrar_resumen_ejecutivo(ratios: Dict[str, Optional[float]], 
                              z_score: Optional[float], 
                              clasificacion: str) -> None:
    """
    Muestra un resumen ejecutivo con los indicadores clave.
    
    Args:
        ratios: Diccionario con los ratios calculados
        z_score: Valor del Z-Score
        clasificacion: Clasificación de riesgo
    """
    st.header("📋 Resumen Ejecutivo")
    
    # Crear 4 columnas para métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        liquidez = ratios.get("liquidez")
        if liquidez is not None:
            delta_color = "normal" if liquidez >= 1.5 else "inverse"
            st.metric("Liquidez", f"{liquidez:.2f}", delta="Saludable" if liquidez >= 1.5 else "Bajo")
        else:
            st.metric("Liquidez", "N/A")
    
    with col2:
        endeudamiento = ratios.get("endeudamiento")
        if endeudamiento is not None:
            st.metric("Endeudamiento", f"{endeudamiento*100:.1f}%", 
                     delta="Bajo" if endeudamiento <= 0.5 else "Alto",
                     delta_color="normal" if endeudamiento <= 0.5 else "inverse")
        else:
            st.metric("Endeudamiento", "N/A")
    
    with col3:
        roe = ratios.get("roe")
        if roe is not None:
            st.metric("ROE", f"{roe*100:.1f}%",
                     delta="Bueno" if roe >= 0.1 else "Bajo",
                     delta_color="normal" if roe >= 0.1 else "inverse")
        else:
            st.metric("ROE", "N/A")
    
    with col4:
        if z_score is not None:
            st.metric("Z-Score", f"{z_score:.2f}",
                     delta="Seguro" if z_score >= 2.99 else "Riesgo",
                     delta_color="normal" if z_score >= 2.99 else "inverse")
        else:
            st.metric("Z-Score", "N/A")
    
    # Conclusión general
    st.markdown("---")
    st.subheader("🎯 Conclusión General")
    
    conclusion = generar_conclusion(ratios, z_score, clasificacion)
    
    if "saludable" in conclusion.lower():
        st.success(conclusion)
    elif "moderado" in conclusion.lower() or "gris" in conclusion.lower():
        st.warning(conclusion)
    else:
        st.error(conclusion)


def generar_conclusion(ratios: Dict[str, Optional[float]], 
                      z_score: Optional[float], 
                      clasificacion: str) -> str:
    """
    Genera una conclusión textual basada en los indicadores calculados.
    
    Args:
        ratios: Diccionario con los ratios
        z_score: Valor del Z-Score
        clasificacion: Clasificación de riesgo
        
    Returns:
        Texto con la conclusión del análisis
    """
    puntos_fuertes = []
    puntos_debiles = []
    
    # Analizar liquidez
    liquidez = ratios.get("liquidez")
    if liquidez is not None:
        if liquidez >= 2.0:
            puntos_fuertes.append("excelente liquidez")
        elif liquidez < 1.0:
            puntos_debiles.append("problemas de liquidez")
    
    # Analizar endeudamiento
    endeudamiento = ratios.get("endeudamiento")
    if endeudamiento is not None:
        if endeudamiento <= 0.5:
            puntos_fuertes.append("bajo endeudamiento")
        elif endeudamiento > 0.7:
            puntos_debiles.append("alto endeudamiento")
    
    # Analizar rentabilidad
    roe = ratios.get("roe")
    if roe is not None:
        if roe >= 0.15:
            puntos_fuertes.append("alta rentabilidad")
        elif roe < 0.05:
            puntos_debiles.append("baja rentabilidad")
    
    # Construir conclusión
    if "Alto riesgo" in clasificacion:
        conclusion = "⚠️ **La empresa presenta indicadores de alto riesgo financiero.** "
    elif "Riesgo moderado" in clasificacion:
        conclusion = "🔶 **La empresa se encuentra en una zona de riesgo moderado.** "
    elif "Bajo riesgo" in clasificacion:
        conclusion = "🟢 **La empresa muestra una situación financiera saludable.** "
    else:
        conclusion = "ℹ️ **No hay suficientes datos para emitir una conclusión definitiva.** "
    
    if puntos_fuertes:
        conclusion += f"Destaca por su {', '.join(puntos_fuertes)}. "
    
    if puntos_debiles:
        conclusion += f"Se recomienda atención en: {', '.join(puntos_debiles)}. "
    
    return conclusion


def mostrar_resultados_completos(ratios: Dict[str, Optional[float]], 
                                z_score: Optional[float], 
                                clasificacion: str) -> None:
    """
    Función principal que orquesta la visualización completa de resultados.
    
    Args:
        ratios: Diccionario con todos los ratios calculados
        z_score: Valor del Z-Score de Altman
        clasificacion: Clasificación de riesgo asociada al Z-Score
    """
    # Título principal con estilo
    st.title("🏢 Análisis de Riesgo Financiero - Resultados")
    st.markdown("---")
    
    # Resumen ejecutivo al inicio
    mostrar_resumen_ejecutivo(ratios, z_score, clasificacion)
    
    st.markdown("---")
    
    # Z-Score y clasificación de riesgo
    mostrar_zscore(z_score, clasificacion)
    
    st.markdown("---")
    
    # Ratios detallados
    mostrar_seccion_ratios(ratios)
    
    st.markdown("---")
    
    # Gráficos de barras por categorías
    crear_grafico_barras_ratios(ratios)
    
    st.markdown("---")
    
    # Radar chart
    crear_radar_chart(ratios)
    
    st.markdown("---")
    
    # Sección de descarga de reporte
    st.header("📥 Exportar Resultados")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Preparar datos para CSV
        datos_export = preparar_datos_exportacion(ratios, z_score, clasificacion)
        csv = datos_export.to_csv(index=False)
        st.download_button(
            label="📄 Descargar CSV",
            data=csv,
            file_name="analisis_financiero.csv",
            mime="text/csv"
        )
    
    with col2:
        st.info("💡 Puedes descargar los resultados en formato CSV para análisis posterior.")


def preparar_datos_exportacion(ratios: Dict[str, Optional[float]], 
                               z_score: Optional[float], 
                               clasificacion: str) -> pd.DataFrame:
    """
    Prepara un DataFrame con todos los datos para exportación.
    
    Args:
        ratios: Diccionario con los ratios
        z_score: Valor del Z-Score
        clasificacion: Clasificación de riesgo
        
    Returns:
        DataFrame con los datos organizados
    """
    datos = []
    
    # Agregar ratios
    for nombre, valor in ratios.items():
        datos.append({
            "Categoría": "Ratio",
            "Indicador": nombre,
            "Valor": valor if valor is not None else "N/A"
        })
    
    # Agregar Z-Score
    datos.append({
        "Categoría": "Z-Score",
        "Indicador": "Valor Z-Score",
        "Valor": z_score if z_score is not None else "N/A"
    })
    
    datos.append({
        "Categoría": "Z-Score",
        "Indicador": "Clasificación",
        "Valor": clasificacion
    })
    
    return pd.DataFrame(datos)