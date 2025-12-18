"""
Módulo de layout y componentes visuales reutilizables.

Este módulo contiene funciones para configurar el diseño general de la aplicación,
estilos personalizados y componentes visuales reutilizables.
"""

import streamlit as st
from typing import Literal


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


def mostrar_sidebar_navegacion() -> str:
    with st.sidebar:
        st.markdown("## 📊 BRS")
        opcion = st.radio(
            "Navegación",
            ["🏠 Inicio", "📝 Análisis de Empresa", "📚 Ayuda", "ℹ️ Acerca de"],
            label_visibility="collapsed"
        )
        return opcion


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

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Ratios Financieros", "📈 Z-Score de Altman", "💡 Cómo Usar", "❓ Preguntas Frecuentes"])

    with tab1:
        st.markdown("""
        ### 📊 Ratios Financieros - Guía Completa
        
        #### 🔵 **Ratios de Liquidez**
        
        **1. Ratio de Liquidez Corriente**
        - **Fórmula:** Activo Corriente / Pasivo Corriente
        - **Interpretación:**
          - > 2.0: Excelente capacidad de pago
          - 1.5 - 2.0: Buena situación financiera
          - 1.0 - 1.5: Aceptable, requiere monitoreo
          - < 1.0: Problemas de liquidez, riesgo de insolvencia
        - **Ejemplo:** Si tienes $400,000 en activos corrientes y $200,000 en pasivos corrientes, tu ratio es 2.0 (muy saludable)
        
        **2. Prueba Ácida (Quick Ratio)**
        - **Fórmula:** (Activo Corriente - Inventarios) / Pasivo Corriente
        - **Interpretación:**
          - > 1.0: Excelente liquidez inmediata
          - 0.7 - 1.0: Aceptable
          - < 0.7: Dependencia excesiva de inventarios
        - **¿Por qué excluir inventarios?** Los inventarios pueden tardar en convertirse en efectivo
        
        **3. Ratio de Tesorería**
        - **Fórmula:** (Caja + Bancos + Inversiones CP) / Pasivo Corriente
        - **Interpretación:** Mide disponibilidad inmediata de efectivo
        
        ---
        
        #### 🟢 **Ratios de Solvencia**
        
        **1. Ratio de Endeudamiento**
        - **Fórmula:** Pasivo Total / Activo Total
        - **Interpretación:**
          - < 0.5 (50%): Bajo endeudamiento, estructura conservadora
          - 0.5 - 0.7 (50-70%): Moderado, nivel aceptable
          - > 0.7 (70%): Alto riesgo financiero
        - **Nota:** Indica qué % de los activos están financiados con deuda
        
        **2. Ratio de Apalancamiento**
        - **Fórmula:** Activo Total / Patrimonio
        - **Interpretación:**
          - 1.0 - 2.0: Bajo apalancamiento
          - 2.0 - 3.0: Moderado
          - > 3.0: Alto uso de deuda
        
        ---
        
        #### 💰 **Ratios de Rentabilidad**
        
        **1. ROA (Return on Assets)**
        - **Fórmula:** Utilidad Neta / Activos Totales
        - **Interpretación:**
          - > 15%: Excelente eficiencia
          - 10-15%: Buena
          - 5-10%: Aceptable
          - < 5%: Baja rentabilidad
        - **Significado:** ¿Cuánto genera cada peso invertido en activos?
        
        **2. ROE (Return on Equity)**
        - **Fórmula:** Utilidad Neta / Patrimonio
        - **Interpretación:**
          - > 20%: Excelente rentabilidad para accionistas
          - 15-20%: Muy buena
          - 10-15%: Aceptable
          - < 10%: Baja, considerar alternativas
        - **Significado:** Rendimiento sobre la inversión de los accionistas
        
        **3. Margen Neto**
        - **Fórmula:** Utilidad Neta / Ventas
        - **Interpretación:**
          - > 10%: Excelente margen
          - 5-10%: Bueno
          - 2-5%: Ajustado
          - < 2%: Muy bajo, revisar costos
        
        ---
        
        #### ⚙️ **Ratios de Eficiencia Operativa**
        
        **1. Rotación de Activos**
        - **Fórmula:** Ventas / Activos Totales
        - **Interpretación:** Cuántas veces se "renuevan" los activos vía ventas
        - Mayor valor = Mayor eficiencia
        
        **2. Rotación de Inventarios**
        - **Fórmula:** Costo de Ventas / Inventario Promedio
        - **Interpretación:**
          - Alto: Buena gestión, rápida rotación
          - Bajo: Inventario estancado, riesgo de obsolescencia
        
        **3. Días de Inventario**
        - **Fórmula:** 365 × Inventario Promedio / Costo de Ventas
        - **Interpretación:** Días promedio que el inventario permanece en stock
        
        **4. Período Medio de Cobro**
        - **Fórmula:** 365 × Cuentas por Cobrar / Ventas a Crédito
        - **Interpretación:**
          - < 30 días: Excelente gestión de cobranza
          - 30-60 días: Aceptable
          - > 60 días: Problemas de cobranza
        
        **5. Período Medio de Pago**
        - **Fórmula:** 365 × Cuentas por Pagar / Compras a Crédito
        - **Interpretación:** Días promedio para pagar a proveedores
        
        ---
        
        #### 🔄 **Ciclo de Conversión de Efectivo**
        - **Fórmula:** Días Inventario + Período Cobro - Período Pago
        - **Interpretación:**
          - Negativo: La empresa cobra antes de pagar (¡excelente!)
          - 0-30 días: Muy bueno
          - 30-60 días: Aceptable
          - > 60 días: Requiere atención
        """)

    with tab2:
        st.markdown("""
        ### 📈 Z-Score de Altman - Predicción de Quiebra
        
        #### 📖 **Historia y Contexto**
        El Z-Score fue desarrollado por **Edward Altman en 1968** en la Universidad de Nueva York. 
        Es uno de los modelos más conocidos para predecir la probabilidad de quiebra empresarial.
        
        #### 🧮 **Fórmula Completa**
        ```
        Z = 1.2 × (Capital de Trabajo / Activo Total) +
            1.4 × (Utilidades Retenidas / Activo Total) +
            3.3 × (EBIT / Activo Total) +
            0.6 × (Valor de Mercado del Patrimonio / Pasivo Total) +
            1.0 × (Ventas / Activo Total)
        ```
        
        #### 📊 **Interpretación de Resultados**
        
        | Rango de Z-Score | Clasificación | Probabilidad de Quiebra | Acción Recomendada |
        |------------------|---------------|------------------------|-------------------|
        | **Z < 1.81** | 🔴 **Alto Riesgo** | > 80% en 2 años | Reestructuración urgente |
        | **1.81 ≤ Z < 2.99** | 🟡 **Zona Gris** | 35-50% en 2 años | Monitoreo continuo |
        | **Z ≥ 2.99** | 🟢 **Zona Segura** | < 10% en 2 años | Situación saludable |
        
        #### 🔍 **Componentes del Z-Score**
        
        **1. Capital de Trabajo / Activo Total (Coef: 1.2)**
        - Mide liquidez y eficiencia operativa
        - Valor positivo indica capacidad para cubrir obligaciones
        
        **2. Utilidades Retenidas / Activo Total (Coef: 1.4)**
        - Refleja la edad y rentabilidad acumulada
        - Empresas maduras tienen mayor valor
        
        **3. EBIT / Activo Total (Coef: 3.3)**
        - Rentabilidad operativa (el más importante)
        - Mide eficiencia en generación de utilidades
        
        **4. Valor de Mercado / Pasivo Total (Coef: 0.6)**
        - Capacidad de los activos para cubrir deudas
        - Para empresas no cotizadas, usar valor en libros
        
        **5. Ventas / Activo Total (Coef: 1.0)**
        - Eficiencia en uso de activos
        - Generación de ingresos
        
        #### ⚠️ **Limitaciones del Z-Score**
        
        - **Diseñado para:** Empresas manufactureras que cotizan en bolsa
        - **No aplicable a:**
          - Bancos y empresas financieras
          - Empresas de servicios sin activos físicos
          - Empresas en sectores muy específicos
        
        #### 💡 **Versiones del Z-Score**
        
        1. **Z-Score Original (1968):** Empresas manufactureras públicas
        2. **Z'-Score (1983):** Empresas privadas manufactureras
        3. **Z''-Score (1995):** Empresas no manufactureras
        
        *Nuestra aplicación usa el Z-Score original*
        
        #### 📈 **Ejemplos Prácticos**
        
        **Empresa Saludable (Z = 2.65):**
        - Capital de trabajo positivo
        - Rentabilidad consistente
        - Bajo endeudamiento
        - Generación sólida de ventas
        → **Resultado:** Baja probabilidad de quiebra
        
        **Empresa en Riesgo (Z = 0.63):**
        - Capital de trabajo negativo
        - Pérdidas acumuladas
        - Alto endeudamiento
        - Baja generación de ventas
        → **Resultado:** Alta probabilidad de quiebra
        """)

    with tab3:
        st.markdown("""
        ### 💡 Cómo Usar Business Risk Scanner
        
        #### 🚀 **Paso a Paso**
        
        **1. Recopilar Información Financiera**
        
        Necesitarás los siguientes datos de tus estados financieros:
        
        📋 **Balance General:**
        - ✅ Activo Corriente
        - ✅ Pasivo Corriente
        - ✅ Pasivo Total
        - ✅ Patrimonio
        - ✅ Activo Total
        - 🔹 Inventarios (opcional)
        
        📋 **Estado de Resultados:**
        - ✅ Ventas Totales
        - ✅ Utilidad Neta
        - ✅ EBIT (Utilidad antes de intereses e impuestos)
        - 🔹 Costo de Ventas (opcional)
        
        📋 **Otros Datos:**
        - ✅ Capital de Trabajo
        - ✅ Utilidades Retenidas
        - ✅ Valor de Mercado del Patrimonio
        - 🔹 Inventario Promedio (opcional)
        
        ---
        
        **2. Ingresar los Datos en el Formulario**
        
        - Puedes usar **comas** en los números: `1,000,000`
        - Puedes usar **espacios**: `100 000`
        - Los campos marcados como **opcionales** pueden dejarse vacíos
        - **Valores negativos** permitidos en:
          - Utilidad Neta (pérdidas)
          - EBIT (pérdidas operativas)
          - Capital de Trabajo (pasivos > activos corrientes)
          - Utilidades Retenidas (pérdidas acumuladas)
        
        ---
        
        **3. Usar Datos de Ejemplo**
        
        Si quieres probar la aplicación primero, usa los botones:
        - 🟢 **Empresa Saludable:** Ver cómo luce un buen análisis
        - 🔴 **Empresa en Riesgo:** Ver alertas y señales de peligro
        
        ---
        
        **4. Revisar los Resultados**
        
        La aplicación generará automáticamente:
        
        ✅ **Tabla de Ratios:** Con valores calculados y categorización
        ✅ **Gráficos de Barras:** Visualización por categoría
        ✅ **Radar Chart:** Comparación visual de todos los indicadores
        ✅ **Z-Score:** Predicción de riesgo de quiebra
        ✅ **Clasificación:** Alto, Moderado o Bajo riesgo
        ✅ **Resumen Ejecutivo:** Interpretación automática
        
        ---
        
        **5. Exportar Resultados**
        
        📥 **Descargar CSV:**
        - Formato optimizado para Excel
        - Separador: punto y coma (`;`)
        - Decimales: coma (`,`)
        - Codificación: UTF-8 con BOM
        - Incluye categorías y valores formateados
        
        ---
        
        #### 🎯 **Consejos de Uso**
        
        ✅ **Actualiza regularmente:** Haz el análisis trimestral o semestral
        ✅ **Compara periodos:** Guarda los CSVs para ver evolución
        ✅ **Revisa tendencias:** Un ratio aislado no cuenta toda la historia
        ✅ **Compara con sector:** Cada industria tiene estándares diferentes
        ✅ **Actúa sobre alertas:** Si detectas riesgos, toma medidas correctivas
        
        #### ⚙️ **Campos Opcionales - Aproximaciones**
        
        Si dejas campos opcionales vacíos, el sistema usa:
        - **Inventarios:** 30% del Activo Corriente
        - **Inventario Promedio:** Igual a Inventarios
        - **Costo de Ventas:** 60% de Ventas
        - **Pasivo Total (Z-Score):** Igual a Pasivo Total del balance
        
        *Nota: Para mayor precisión, ingresa los valores reales*
        """)

    with tab4:
        st.markdown("""
        ### ❓ Preguntas Frecuentes (FAQ)
        
        #### 🔷 **General**
        
        **¿Con qué frecuencia debo hacer el análisis financiero?**
        - **Mínimo:** Trimestral
        - **Recomendado:** Mensual para empresas en crecimiento
        - **Crítico:** Semanal si detectas señales de alerta
        
        **¿Es aplicable a todo tipo de empresas?**
        - **Ideal para:** Empresas manufactureras
        - **Adaptable a:** Comercio y servicios (con ajustes)
        - **NO aplicable a:** Bancos, aseguradoras, empresas financieras
        
        **¿Necesito ser experto en finanzas?**
        - No, la aplicación interpreta automáticamente los resultados
        - Sin embargo, recomendamos entender conceptos básicos
        - La sección de Ayuda explica cada ratio
        
        ---
        
        #### 🔷 **Sobre los Datos**
        
        **¿De dónde obtengo los datos financieros?**
        - Estados financieros auditados o internos
        - Software contable (SAP, QuickBooks, etc.)
        - Reportes del departamento de contabilidad
        
        **¿Puedo usar datos no auditados?**
        - Sí, pero la precisión depende de la calidad de los datos
        - Recomendamos validar con un contador
        
        **¿Qué hago si no tengo ciertos datos?**
        - Deja los campos opcionales vacíos
        - El sistema usará estimaciones conservadoras
        - Para mayor precisión, obtén los datos reales
        
        ---
        
        #### 🔷 **Interpretación de Resultados**
        
        **Mi Z-Score es bajo, ¿significa quiebra segura?**
        - No necesariamente, es una **probabilidad estadística**
        - Considera otros factores: sector, economía, gestión
        - Úsalo como señal de alerta para tomar acción
        
        **¿Un ratio malo significa que la empresa va mal?**
        - No siempre, analiza el **contexto completo**
        - Compara con periodos anteriores
        - Compara con empresas similares del sector
        
        **¿Cuántos ratios deben estar en rojo para preocuparse?**
        - **1-2 ratios:** Monitorear y mejorar
        - **3-4 ratios:** Atención, plan de acción
        - **5+ ratios:** Situación crítica, reestructuración urgente
        
        ---
        
        #### 🔷 **Acciones Correctivas**
        
        **Mi liquidez es baja, ¿qué hago?**
        1. Acelerar cobranza a clientes
        2. Negociar plazos más largos con proveedores
        3. Vender inventario obsoleto
        4. Buscar líneas de crédito de corto plazo
        
        **Mi endeudamiento es alto, ¿qué hago?**
        1. Aumentar capital (nuevos socios/inversionistas)
        2. Refinanciar deuda a plazos más largos
        3. Vender activos no productivos
        4. Retener más utilidades (menos dividendos)
        
        **Mi rentabilidad es baja, ¿qué hago?**
        1. Revisar estructura de costos
        2. Optimizar precios
        3. Mejorar eficiencia operativa
        4. Eliminar productos/servicios no rentables
        
        ---
        
        #### 🔷 **Aspectos Técnicos**
        
        **¿Los datos quedan guardados?**
        - No, todo se procesa en tiempo real
        - No almacenamos información de tu empresa
        - Para guardar resultados, descarga el CSV
        
        **¿Puedo usar la aplicación sin conexión?**
        - No, Streamlit requiere conexión
        - Puedes instalarla localmente para uso privado
        
        **¿El análisis es confidencial?**
        - Sí, los datos no se almacenan
        - No se comparten con terceros
        - Procesamiento local en tu navegador
        
        ---
        
        #### 🔷 **Soporte y Contacto**
        
        **¿Dónde reporto errores o problemas?**
        - Sección "Acerca de" tiene información del equipo
        - Repositorio GitHub para issues técnicos
        
        **¿Puedo solicitar nuevas funcionalidades?**
        - Sí, estamos abiertos a sugerencias
        - Contacta al equipo de desarrollo
        
        **¿Hay documentación técnica?**
        - Sí, revisa el README.md del repositorio
        - Documentación de API en el código fuente
        """)


def mostrar_pagina_acerca_de() -> None:
    mostrar_header("Acerca de", "Conoce nuestro sistema de análisis financiero")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ## 🎯 Business Risk Scanner
        
        ### 📌 **¿Qué es?**
        
        Business Risk Scanner es una **aplicación web avanzada** diseñada para realizar análisis financiero 
        integral de empresas mediante:
        
        - **Cálculo automatizado** de 15+ ratios financieros
        - **Predicción de riesgo** usando el Z-Score de Altman
        - **Visualizaciones interactivas** con gráficos dinámicos
        - **Exportación de datos** en formato CSV compatible con Excel
        - **Interpretación automática** de resultados financieros
        
        ---
        
        ### 🎯 **Objetivo del Proyecto**
        
        Democratizar el análisis financiero empresarial, proporcionando una herramienta:
        - ✅ **Accesible:** Interfaz intuitiva sin necesidad de conocimientos avanzados
        - ✅ **Precisa:** Cálculos basados en metodologías reconocidas internacionalmente
        - ✅ **Práctica:** Resultados accionables con recomendaciones claras
        - ✅ **Rápida:** Análisis completo en segundos
        - ✅ **Gratuita:** Software de código abierto
        
        ---
        
        ### 🌟 **Características Principales**
        
        #### 📊 **Análisis de Ratios Financieros**
        - **Liquidez:** Ratio corriente, prueba ácida, tesorería
        - **Solvencia:** Endeudamiento, apalancamiento
        - **Rentabilidad:** ROA, ROE, margen neto
        - **Eficiencia:** Rotación de activos, inventarios, cuentas por cobrar/pagar
        - **Ciclo de Conversión de Efectivo**
        
        #### 📈 **Z-Score de Altman**
        - Modelo predictivo de probabilidad de quiebra
        - Desarrollado por Edward Altman (1968)
        - Precisión del 80-90% en predicciones a 2 años
        - Clasificación en zonas: segura, gris, riesgo
        
        #### 📉 **Visualizaciones Dinámicas**
        - Gráficos de barras por categoría de ratio
        - Radar chart multidimensional
        - Indicadores visuales de riesgo
        - Adaptación automática a modo claro/oscuro
        
        #### 💾 **Exportación y Reportes**
        - Formato CSV optimizado para Excel español
        - Valores formateados con 4 decimales
        - Nombres descriptivos de ratios
        - Categorización automática
        
        ---
        
        ### 👥 **Equipo de Desarrollo**
        
        | Nombre | Rol | Contribución |
        |--------|-----|-------------|
        | **Daniel** | Lead Developer | Arquitectura, backend, validaciones |
        | **Igor** | Frontend Engineer | UI/UX, Streamlit, visualizaciones |
        | **Mario** | Data Analyst | Algoritmos, fórmulas, Z-Score |
        | **D'Alessandro** | QA Engineer | Testing, validación de cálculos |
        | **Bruno** | DevOps | Deployment, documentación |
        
        ---
        
        ### 🛠️ **Stack Tecnológico**
        
        #### 🐍 **Backend**
        - **Python 3.13:** Lenguaje de programación principal
        - **NumPy 2.3.3:** Computación numérica y operaciones matriciales
        - **Pandas 2.3.3:** Manipulación y análisis de datos tabulares
        
        #### 🎨 **Frontend**
        - **Streamlit 1.50.0:** Framework web interactivo para Python
        - **Plotly 6.3.1:** Gráficos interactivos (radar, barras, scatter)
        - **Seaborn:** Visualizaciones estadísticas complementarias
        
        #### 🧪 **Testing & Quality**
        - **unittest:** Framework de testing nativo de Python
        - **62 tests unitarios:** Cobertura de ratios, validaciones, Z-Score
        - **Validaciones en tiempo real:** Control de tipos y rangos
        
        #### 📦 **Gestión de Dependencias**
        ```
        streamlit >= 1.50.0
        pandas >= 2.3.0
        numpy >= 2.3.0
        matplotlib >= 3.10.0
        seaborn >= 0.13.2
        plotly >= 6.0.0
        ```
        
        ---
        
        ### 📚 **Fundamentos Académicos**
        
        #### 📖 **Referencias Bibliográficas**
        
        1. **Altman, E. I. (1968).** "Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy." 
           *The Journal of Finance*, 23(4), 589-609.
        
        2. **Brigham, E. F., & Houston, J. F. (2021).** "Fundamentals of Financial Management." 
           *Cengage Learning* (16th Edition).
        
        3. **Ross, S. A., Westerfield, R. W., & Jaffe, J. (2019).** "Corporate Finance." 
           *McGraw-Hill Education* (12th Edition).
        
        4. **Gitman, L. J., & Zutter, C. J. (2019).** "Principles of Managerial Finance." 
           *Pearson* (15th Edition).
        
        #### 🎓 **Metodologías Aplicadas**
        - **Análisis de Ratios:** Estándares internacionales de contabilidad (IFRS/GAAP)
        - **Z-Score:** Modelo Altman original (1968) para empresas manufactureras
        - **Clasificación de Riesgo:** Umbrales estadísticamente validados
        
        ---
        
        ### 📋 **Versión y Licencia**
        
        - **Versión Actual:** 1.0.0 (2025)
        - **Licencia:** MIT License (Open Source)
        - **Repositorio:** GitHub - business-risk-scanner
        - **Última Actualización:** Diciembre 2025
        
        #### 📄 **Términos de Uso**
        
        Esta herramienta se proporciona "tal cual" para fines educativos y de análisis. 
        Los resultados deben ser:
        - ✅ Validados por profesionales contables/financieros
        - ✅ Complementados con análisis cualitativo
        - ✅ Contextualizados según industria y economía
        
        **Descargo de Responsabilidad:**
        No nos hacemos responsables de decisiones financieras tomadas 
        exclusivamente con base en los resultados de esta aplicación.
        
        ---
        
        ### 🚀 **Roadmap Futuro**
        
        #### 🔜 **Próximas Funcionalidades**
        - [ ] Comparación multi-periodo (análisis de tendencias)
        - [ ] Benchmarking por sector industrial
        - [ ] Análisis de sensibilidad (what-if scenarios)
        - [ ] Exportación a PDF con gráficos
        - [ ] Dashboard ejecutivo personalizable
        - [ ] Integración con APIs contables (QuickBooks, Xero)
        - [ ] Modo multi-empresa (comparaciones)
        - [ ] Alertas automáticas vía email
        
        #### 🎯 **Mejoras Planificadas**
        - [ ] Z-Score adaptado para empresas de servicios
        - [ ] Machine Learning para predicciones personalizadas
        - [ ] Módulo de análisis de flujo de efectivo
        - [ ] Indicadores ESG (Environmental, Social, Governance)
        
        ---
        
        ### 📞 **Contacto y Soporte**
        
        #### 💬 **Reportar Problemas**
        - **GitHub Issues:** Para bugs técnicos y solicitudes de funcionalidades
        - **Email:** [Configurar según el equipo]
        
        #### 🤝 **Contribuciones**
        ¡Las contribuciones son bienvenidas!
        1. Fork del repositorio
        2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
        3. Commit de cambios (`git commit -m 'Agrega nueva funcionalidad'`)
        4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
        5. Abre un Pull Request
        
        #### ⭐ **Agradecimientos**
        - A la comunidad de Streamlit por el excelente framework
        - A Edward Altman por el modelo Z-Score
        - A todos los contribuidores y usuarios beta-testers
        
        ---
        
        ### 🏆 **Reconocimientos**
        
        Este proyecto fue desarrollado como parte de:
        - 📚 Proyecto académico de análisis financiero
        - 💼 Iniciativa de democratización de herramientas empresariales
        - 🌍 Contribución al software libre en español
        """)

    with col2:
        st.info("""
        ### 📊 Estadísticas
        
        **Métricas del Proyecto:**
        - ✅ 62 Tests Unitarios
        - ✅ 15+ Ratios Calculados
        - ✅ 100% Python
        - ✅ Open Source
        
        ---
        
        ### 🔗 Enlaces Rápidos
        
        - [📖 Documentación](https://github.com/Dan101111111/business-risk-scanner#readme)
        - [💻 GitHub](https://github.com/Dan101111111/business-risk-scanner)
        - [🐛 Reportar Bug](https://github.com/Dan101111111/business-risk-scanner/issues)
        - [💡 Sugerencias](https://github.com/Dan101111111/business-risk-scanner/issues/new)
        
        ---
        
        ### 📈 Versión
        
        **v1.0.0**  
        *Diciembre 2025*
        
        ---
        
        ### 🌟 Tech Stack
        
        - 🐍 Python 3.13
        - 🎨 Streamlit 1.50
        - 📊 Plotly 6.3
        - 🔢 NumPy 2.3
        - 📑 Pandas 2.3
        """)

        st.success("""
        ### ✅ Calidad Garantizada
        
        - Fórmulas validadas
        - Testing automatizado
        - Código documentado
        - Actualizaciones regulares
        """)

