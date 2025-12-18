"""
Módulo de cálculo de ratios financieros.

Este módulo contiene funciones puras para calcular diversos indicadores financieros
de liquidez, solvencia, rentabilidad y eficiencia operativa.
"""

from typing import Optional


def ratio_liquidez(activo_corriente: float, pasivo_corriente: float) -> Optional[float]:
    """
    Calcula el ratio de liquidez corriente.
    
    Mide la capacidad de la empresa para cubrir sus obligaciones de corto plazo
    con sus activos corrientes.
    
    Fórmula: Activo Corriente / Pasivo Corriente
    
    Args:
        activo_corriente: Activos líquidos o convertibles a corto plazo
        pasivo_corriente: Obligaciones de corto plazo
    
    Returns:
        Ratio de liquidez o None si el pasivo corriente es cero
    
    Examples:
        >>> ratio_liquidez(100000, 50000)
        2.0
        >>> ratio_liquidez(75000, 100000)
        0.75
        >>> ratio_liquidez(100000, 0)
    """
    if pasivo_corriente == 0:
        return None
    return activo_corriente / pasivo_corriente


def ratio_prueba_acida(
    activo_corriente: float, 
    inventarios: float, 
    pasivo_corriente: float
) -> Optional[float]:
    """
    Calcula el ratio de prueba ácida (quick ratio).
    
    Mide la capacidad inmediata de pago excluyendo inventarios,
    ya que estos son menos líquidos.
    
    Fórmula: (Activo Corriente - Inventarios) / Pasivo Corriente
    
    Args:
        activo_corriente: Activos corrientes totales
        inventarios: Valor de inventarios
        pasivo_corriente: Obligaciones de corto plazo
    
    Returns:
        Ratio de prueba ácida o None si el pasivo corriente es cero
    
    Examples:
        >>> ratio_prueba_acida(100000, 30000, 50000)
        1.4
        >>> ratio_prueba_acida(80000, 20000, 60000)
        1.0
        >>> ratio_prueba_acida(100000, 30000, 0)
    """
    if pasivo_corriente == 0:
        return None
    return (activo_corriente - inventarios) / pasivo_corriente


def ratio_endeudamiento(pasivo_total: float, activo_total: float) -> Optional[float]:
    """
    Calcula el ratio de endeudamiento.
    
    Mide qué proporción de los activos está financiada con deuda.
    Un valor alto indica mayor riesgo financiero.
    
    Fórmula: Pasivo Total / Activo Total
    
    Args:
        pasivo_total: Total de deudas y obligaciones
        activo_total: Total de activos de la empresa
    
    Returns:
        Ratio de endeudamiento (0-1+) o None si el activo total es cero
    
    Examples:
        >>> ratio_endeudamiento(400000, 1000000)
        0.4
        >>> ratio_endeudamiento(700000, 1000000)
        0.7
        >>> ratio_endeudamiento(100000, 0)
    """
    if activo_total == 0:
        return None
    return pasivo_total / activo_total


def ratio_apalancamiento(activo_total: float, patrimonio: float) -> Optional[float]:
    """
    Calcula el ratio de apalancamiento financiero.
    
    Indica cuántas veces los activos superan al patrimonio.
    Mayor apalancamiento implica mayor uso de deuda.
    
    Fórmula: Activo Total / Patrimonio
    
    Args:
        activo_total: Total de activos
        patrimonio: Capital propio (activos - pasivos)
    
    Returns:
        Ratio de apalancamiento o None si el patrimonio es cero
    
    Examples:
        >>> ratio_apalancamiento(1000000, 600000)
        1.6666666666666667
        >>> ratio_apalancamiento(500000, 500000)
        1.0
        >>> ratio_apalancamiento(1000000, 0)
    """
    if patrimonio == 0:
        return None
    return activo_total / patrimonio


def margen_neto(utilidad_neta: float, ventas: float) -> Optional[float]:
    """
    Calcula el margen de utilidad neta.
    
    Indica qué porcentaje de las ventas se convierte en ganancia neta.
    
    Fórmula: Utilidad Neta / Ventas
    
    Args:
        utilidad_neta: Ganancia después de impuestos y gastos
        ventas: Ingresos totales por ventas
    
    Returns:
        Margen neto (decimal) o None si las ventas son cero
    
    Examples:
        >>> margen_neto(50000, 500000)
        0.1
        >>> margen_neto(75000, 1000000)
        0.075
        >>> margen_neto(50000, 0)
    """
    if ventas == 0:
        return None
    return utilidad_neta / ventas


def roe(utilidad_neta: float, patrimonio: float) -> Optional[float]:
    """
    Calcula el Return on Equity (ROE) - Rentabilidad sobre el Patrimonio.
    
    Mide la rentabilidad que obtienen los accionistas sobre su inversión.
    
    Fórmula: Utilidad Neta / Patrimonio
    
    Args:
        utilidad_neta: Ganancia neta del período
        patrimonio: Capital propio
    
    Returns:
        ROE (decimal) o None si el patrimonio es cero
    
    Examples:
        >>> roe(120000, 600000)
        0.2
        >>> roe(80000, 500000)
        0.16
        >>> roe(100000, 0)
    """
    if patrimonio == 0:
        return None
    return utilidad_neta / patrimonio


def roa(utilidad_neta: float, activos_totales: float) -> Optional[float]:
    """
    Calcula el Return on Assets (ROA) - Rentabilidad sobre los Activos.
    
    Mide la eficiencia con que la empresa utiliza sus activos para generar utilidades.
    
    Fórmula: Utilidad Neta / Activos Totales
    
    Args:
        utilidad_neta: Ganancia neta del período
        activos_totales: Total de activos
    
    Returns:
        ROA (decimal) o None si los activos totales son cero
    
    Examples:
        >>> roa(100000, 1000000)
        0.1
        >>> roa(50000, 800000)
        0.0625
        >>> roa(100000, 0)
    """
    if activos_totales == 0:
        return None
    return utilidad_neta / activos_totales


def rotacion_activos(ventas: float, activos_totales: float) -> Optional[float]:
    """
    Calcula el ratio de rotación de activos.
    
    Mide la eficiencia en el uso de activos para generar ventas.
    Un valor más alto indica mejor eficiencia operativa.
    
    Fórmula: Ventas / Activos Totales
    
    Args:
        ventas: Ingresos totales por ventas
        activos_totales: Total de activos
    
    Returns:
        Ratio de rotación o None si los activos totales son cero
    
    Examples:
        >>> rotacion_activos(2000000, 1000000)
        2.0
        >>> rotacion_activos(800000, 1000000)
        0.8
        >>> rotacion_activos(1000000, 0)
    """
    if activos_totales == 0:
        return None
    return ventas / activos_totales


def ratio_tesoreria(
    caja_bancos: float, 
    inversiones_cp: float, 
    pasivo_corriente: float
) -> Optional[float]:
    """
    Calcula el ratio de tesorería (ratio de disponibilidad inmediata).
    
    Mide la capacidad de la empresa para pagar sus deudas a corto plazo
    únicamente con sus recursos más líquidos (caja, bancos e inversiones 
    a corto plazo).
    
    Fórmula: (Caja y Bancos + Inversiones Corto Plazo) / Pasivo Corriente
    
    Args:
        caja_bancos: Efectivo en caja y depósitos bancarios
        inversiones_cp: Inversiones financieras a corto plazo
        pasivo_corriente: Obligaciones de corto plazo
    
    Returns:
        Ratio de tesorería o None si el pasivo corriente es cero
    
    Examples:
        >>> ratio_tesoreria(50000, 30000, 100000)
        0.8
        >>> ratio_tesoreria(60000, 40000, 80000)
        1.25
        >>> ratio_tesoreria(50000, 30000, 0)
    """
    if pasivo_corriente == 0:
        return None
    return (caja_bancos + inversiones_cp) / pasivo_corriente


def rotacion_inventarios(costo_ventas: float, inventario_promedio: float) -> Optional[float]:
    """
    Calcula el ratio de rotación de inventarios.
    
    Indica cuántas veces se renuevan los inventarios durante un período.
    Un valor más alto sugiere mejor gestión de inventarios.
    
    Fórmula: Costo de Ventas / Inventario Promedio
    
    Args:
        costo_ventas: Costo de los productos vendidos
        inventario_promedio: Promedio de inventarios en el período
    
    Returns:
        Número de rotaciones o None si el inventario promedio es cero
    
    Examples:
        >>> rotacion_inventarios(600000, 100000)
        6.0
        >>> rotacion_inventarios(480000, 120000)
        4.0
        >>> rotacion_inventarios(600000, 0)
    """
    if inventario_promedio == 0:
        return None
    return costo_ventas / inventario_promedio


def dias_inventario(costo_ventas: float, inventario_promedio: float) -> Optional[float]:
    """
    Calcula los días promedio de inventario.
    
    Indica cuántos días en promedio permanece el inventario en la empresa
    antes de ser vendido. Un valor más bajo indica mayor eficiencia.
    
    Fórmula: 365 * Inventario Promedio / Costo de Ventas
    
    Args:
        costo_ventas: Costo de los productos vendidos
        inventario_promedio: Promedio de inventarios en el período
    
    Returns:
        Número de días o None si el costo de ventas es cero
    
    Examples:
        >>> dias_inventario(365000, 100000)
        100.0
        >>> dias_inventario(730000, 100000)
        50.0
        >>> dias_inventario(0, 100000)
    """
    if costo_ventas == 0:
        return None
    return 365 * inventario_promedio / costo_ventas


def periodo_medio_cobro(
    cuentas_por_cobrar: float, 
    ventas_credito: float
) -> Optional[float]:
    """
    Calcula el período medio de cobro (días de cuentas por cobrar).
    
    Indica el número promedio de días que tarda la empresa en cobrar
    sus ventas a crédito. Un valor más bajo indica mejor gestión de cobranza.
    
    Fórmula: 365 * Cuentas por Cobrar / Ventas a Crédito
    
    Args:
        cuentas_por_cobrar: Saldo de cuentas por cobrar a clientes
        ventas_credito: Total de ventas realizadas a crédito
    
    Returns:
        Número de días o None si las ventas a crédito son cero
    
    Examples:
        >>> periodo_medio_cobro(100000, 730000)
        50.0
        >>> periodo_medio_cobro(150000, 1095000)
        50.0
        >>> periodo_medio_cobro(100000, 0)
    """
    if ventas_credito == 0:
        return None
    return 365 * cuentas_por_cobrar / ventas_credito


def periodo_medio_pago(
    cuentas_por_pagar: float, 
    compras_credito: float
) -> Optional[float]:
    """
    Calcula el período medio de pago (días de cuentas por pagar).
    
    Indica el número promedio de días que tarda la empresa en pagar
    a sus proveedores. Un valor más alto puede indicar mejor uso del
    crédito comercial o potenciales problemas de liquidez.
    
    Fórmula: 365 * Cuentas por Pagar / Compras a Crédito
    
    Args:
        cuentas_por_pagar: Saldo de cuentas por pagar a proveedores
        compras_credito: Total de compras realizadas a crédito
    
    Returns:
        Número de días o None si las compras a crédito son cero
    
    Examples:
        >>> periodo_medio_pago(80000, 584000)
        50.0
        >>> periodo_medio_pago(120000, 876000)
        50.0
        >>> periodo_medio_pago(80000, 0)
    """
    if compras_credito == 0:
        return None
    return 365 * cuentas_por_pagar / compras_credito
