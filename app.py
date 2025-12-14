"""
Business Risk Scanner - Aplicación Principal

Herramienta de análisis de riesgo financiero empresarial basada en ratios
financieros y el Z-Score de Altman.
"""

import streamlit as st
from ui.forms import financial_input_form
from ui.layout import (
    configurar_pagina,
    aplicar_estilos_personalizados,
    mostrar_header,
    mostrar_sidebar_navegacion,
    mostrar_footer,
    mostrar_pagina_inicio,
    mostrar_pagina_ayuda,
    mostrar_pagina_acerca_de,
    crear_seccion,
    crear_card,
    mostrar_separador
)
from ui.view_results import mostrar_resultados_completos
from risk_engine.ratios import (
    ratio_liquidez,
    ratio_prueba_acida,
    ratio_endeudamiento,
    ratio_apalancamiento,
    roa,
    roe,
    margen_neto,
    rotacion_activos,
    rotacion_inventarios
)
from risk_engine.zscore import z_score
from risk_engine.classification import classify_risk

# Configurar página (debe ser lo primero)
configurar_pagina()

# Aplicar estilos personalizados
aplicar_estilos_personalizados()

# Inicializar estado de sesión
if 'datos_calculados' not in st.session_state:
    st.session_state['datos_calculados'] = None


def calcular_ratios(data: dict) -> dict:
    """
    Calcula todos los ratios financieros a partir de los datos ingresados.
    
    Args:
        data: Diccionario con los datos financieros
        
    Returns:
        Diccionario con todos los ratios calculados
    """
    ratios = {}
    
    # Mapear campos del formulario
    activo_total = data.get('total_assets', data.get('activo_total', 0))
    
    # Ratios de liquidez
    ratios['liquidez'] = ratio_liquidez(
        data['activo_corriente'],
        data['pasivo_corriente']
    )
    
    # Calcular inventarios si no están (asumimos 30% del activo corriente)
    inventarios = data.get('inventarios', data['activo_corriente'] * 0.3)
    
    ratios['prueba_acida'] = ratio_prueba_acida(
        data['activo_corriente'],
        inventarios,
        data['pasivo_corriente']
    )
    
    # Ratios de solvencia
    ratios['endeudamiento'] = ratio_endeudamiento(
        data['pasivo_total'],
        activo_total
    )
    
    ratios['apalancamiento'] = ratio_apalancamiento(
        activo_total,
        data['patrimonio']
    )
    
    # Ratios de rentabilidad
    ratios['roa'] = roa(
        data['utilidad_neta'],
        activo_total
    )
    
    ratios['roe'] = roe(
        data['utilidad_neta'],
        data['patrimonio']
    )
    
    ratios['margen_utilidad'] = margen_neto(
        data['utilidad_neta'],
        data['ventas']
    )
    
    # Ratios de eficiencia
    ratios['rotacion_activos'] = rotacion_activos(
        data['ventas'],
        activo_total
    )
    
    # Calcular costo de ventas si no está (asumimos 60% de ventas)
    costo_ventas = data.get('costo_ventas', data['ventas'] * 0.6)
    
    ratios['rotacion_inventarios'] = rotacion_inventarios(
        costo_ventas,
        inventarios
    )
    
    return ratios


def calcular_zscore(data: dict) -> float:
    """
    Calcula el Z-Score de Altman a partir de los datos ingresados.
    
    Args:
        data: Diccionario con los datos financieros
        
    Returns:
        Valor del Z-Score
    """
    # Mapear campos del formulario a los esperados por z_score
    activo_total = data.get('total_assets', data.get('activo_total', 0))
    working_capital = data.get('working_capital', data['activo_corriente'] - data['pasivo_corriente'])
    retained_earnings = data.get('retained_earnings', data.get('utilidades_retenidas', 0))
    market_value_equity = data.get('market_value_equity', data.get('valor_mercado_patrimonio', data['patrimonio']))
    
    return z_score(
        working_capital=working_capital,
        retained_earnings=retained_earnings,
        ebit=data['ebit'],
        market_value_equity=market_value_equity,
        total_liabilities=data['pasivo_total'],
        sales=data['ventas'],
        total_assets=activo_total
    )


def main():
    """Función principal de la aplicación."""
    
    # Mostrar sidebar y obtener navegación
    opcion = mostrar_sidebar_navegacion()
    
    # Navegar según la opción seleccionada
    if opcion == "🏠 Inicio":
        mostrar_pagina_inicio()
        
    elif opcion == "📝 Análisis de Empresa":
        # Página principal de análisis
        mostrar_header()
        
        crear_seccion("Ingreso de Datos Financieros", "📝")
        
        # Formulario de entrada
        data = financial_input_form()
        
        # Si hay datos, procesarlos inmediatamente
        if data:
            with st.spinner("Calculando ratios y análisis de riesgo..."):
                try:
                    # Calcular ratios
                    ratios = calcular_ratios(data)
                    
                    # Calcular Z-Score
                    zscore_valor = calcular_zscore(data)
                    
                    # Obtener clasificación de riesgo
                    clasificacion = classify_risk(zscore_valor)
                    
                    # Guardar en sesión
                    st.session_state['datos_calculados'] = {
                        'ratios': ratios,
                        'zscore': zscore_valor,
                        'clasificacion': clasificacion,
                        'datos_originales': data
                    }
                    
                    st.success("✅ ¡Análisis completado exitosamente!")
                    
                except Exception as e:
                    st.error(f"❌ Error al calcular: {str(e)}")
                    st.session_state['datos_calculados'] = None
        
        # Mostrar resultados si están disponibles
        if st.session_state.get('datos_calculados') is not None:
            mostrar_separador(40)
            
            # Mostrar resultados completos
            mostrar_resultados_completos(
                ratios=st.session_state['datos_calculados']['ratios'],
                z_score=st.session_state['datos_calculados']['zscore'],
                clasificacion=st.session_state['datos_calculados']['clasificacion']
            )
        elif data is None:
            # Mostrar mensaje informativo si no hay datos
            crear_card(
                "💡 Instrucciones",
                "Complete el formulario con los datos financieros de su empresa para comenzar el análisis. "
                "Todos los campos son obligatorios para obtener resultados precisos.",
                tipo="info"
            )
    
    elif opcion == "📚 Ayuda":
        mostrar_pagina_ayuda()
    
    elif opcion == "ℹ️ Acerca de":
        mostrar_pagina_acerca_de()
    
    # Mostrar footer al final
    mostrar_separador(50)
    mostrar_footer()


if __name__ == "__main__":
    main()
