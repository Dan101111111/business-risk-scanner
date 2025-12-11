"""
Ejemplo de uso del módulo de ratios financieros.
Demuestra cómo calcular todos los ratios disponibles.
"""

from risk_engine.ratios import (
    ratio_liquidez,
    ratio_prueba_acida,
    ratio_tesoreria,
    ratio_endeudamiento,
    ratio_apalancamiento,
    margen_neto,
    roe,
    roa,
    rotacion_activos,
    rotacion_inventarios,
    dias_inventario,
    periodo_medio_cobro,
    periodo_medio_pago
)


def imprimir_ratio(nombre: str, valor: float | None, unidad: str = ""):
    """Imprime un ratio de forma formateada."""
    if valor is None:
        print(f"  {nombre}: No se puede calcular (división entre cero)")
    elif unidad == "%":
        print(f"  {nombre}: {valor * 100:.2f}%")
    elif unidad == "veces":
        print(f"  {nombre}: {valor:.2f} veces")
    elif unidad == "días":
        print(f"  {nombre}: {valor:.0f} días")
    else:
        print(f"  {nombre}: {valor:.2f}")


def ejemplo_empresa_saludable():
    """Ejemplo de análisis de una empresa con buenos indicadores."""
    print("\n" + "=" * 70)
    print("ANÁLISIS FINANCIERO - EMPRESA SALUDABLE S.A.")
    print("=" * 70)
    
    # Datos del Balance General
    print("\n📊 BALANCE GENERAL:")
    activo_total = 1000000
    activo_corriente = 400000
    caja_bancos = 80000
    inversiones_cp = 70000
    inventarios = 100000
    pasivo_total = 400000
    pasivo_corriente = 200000
    patrimonio = 600000
    
    print(f"  Activo Total: ${activo_total:,.0f}")
    print(f"  Activo Corriente: ${activo_corriente:,.0f}")
    print(f"  Pasivo Total: ${pasivo_total:,.0f}")
    print(f"  Patrimonio: ${patrimonio:,.0f}")
    
    # Datos del Estado de Resultados
    print("\n📈 ESTADO DE RESULTADOS:")
    ventas = 2000000
    ventas_credito = 1500000
    costo_ventas = 1200000
    utilidad_neta = 150000
    
    print(f"  Ventas: ${ventas:,.0f}")
    print(f"  Costo de Ventas: ${costo_ventas:,.0f}")
    print(f"  Utilidad Neta: ${utilidad_neta:,.0f}")
    
    # Otros datos
    cuentas_por_cobrar = 205479  # Aprox. 50 días
    inventario_promedio = 100000
    cuentas_por_pagar = 164384  # Aprox. 50 días
    compras_credito = 1200000
    
    # RATIOS DE LIQUIDEZ
    print("\n💧 RATIOS DE LIQUIDEZ:")
    imprimir_ratio(
        "Ratio de Liquidez Corriente",
        ratio_liquidez(activo_corriente, pasivo_corriente)
    )
    imprimir_ratio(
        "Ratio de Prueba Ácida",
        ratio_prueba_acida(activo_corriente, inventarios, pasivo_corriente)
    )
    imprimir_ratio(
        "Ratio de Tesorería",
        ratio_tesoreria(caja_bancos, inversiones_cp, pasivo_corriente)
    )
    
    # RATIOS DE SOLVENCIA
    print("\n🏦 RATIOS DE SOLVENCIA:")
    imprimir_ratio(
        "Ratio de Endeudamiento",
        ratio_endeudamiento(pasivo_total, activo_total),
        "%"
    )
    imprimir_ratio(
        "Ratio de Apalancamiento",
        ratio_apalancamiento(activo_total, patrimonio),
        "veces"
    )
    
    # RATIOS DE RENTABILIDAD
    print("\n💰 RATIOS DE RENTABILIDAD:")
    imprimir_ratio(
        "Margen Neto",
        margen_neto(utilidad_neta, ventas),
        "%"
    )
    imprimir_ratio(
        "ROE (Rentabilidad sobre Patrimonio)",
        roe(utilidad_neta, patrimonio),
        "%"
    )
    imprimir_ratio(
        "ROA (Rentabilidad sobre Activos)",
        roa(utilidad_neta, activo_total),
        "%"
    )
    
    # RATIOS DE EFICIENCIA
    print("\n⚡ RATIOS DE EFICIENCIA OPERATIVA:")
    imprimir_ratio(
        "Rotación de Activos",
        rotacion_activos(ventas, activo_total),
        "veces"
    )
    imprimir_ratio(
        "Rotación de Inventarios",
        rotacion_inventarios(costo_ventas, inventario_promedio),
        "veces"
    )
    imprimir_ratio(
        "Días de Inventario",
        dias_inventario(costo_ventas, inventario_promedio),
        "días"
    )
    
    # CICLO DE CONVERSIÓN DE EFECTIVO
    print("\n🔄 CICLO DE CONVERSIÓN DE EFECTIVO:")
    pmc = periodo_medio_cobro(cuentas_por_cobrar, ventas_credito)
    pmp = periodo_medio_pago(cuentas_por_pagar, compras_credito)
    di = dias_inventario(costo_ventas, inventario_promedio)
    
    imprimir_ratio("Período Medio de Cobro", pmc, "días")
    imprimir_ratio("Período Medio de Pago", pmp, "días")
    
    if pmc is not None and pmp is not None and di is not None:
        ciclo_efectivo = di + pmc - pmp
        imprimir_ratio("Ciclo de Conversión de Efectivo", ciclo_efectivo, "días")
    
    print("\n✅ INTERPRETACIÓN:")
    print("  • Liquidez: EXCELENTE (ratio > 2.0)")
    print("  • Endeudamiento: SALUDABLE (40%)")
    print("  • Rentabilidad: BUENA (ROE 25%, Margen 7.5%)")
    print("  • Eficiencia: ALTA (rotación de activos 2x)")


def ejemplo_empresa_con_problemas():
    """Ejemplo de análisis de una empresa con problemas financieros."""
    print("\n" + "=" * 70)
    print("ANÁLISIS FINANCIERO - EMPRESA EN RIESGO S.A.")
    print("=" * 70)
    
    # Datos del Balance General
    print("\n📊 BALANCE GENERAL:")
    activo_total = 1000000
    activo_corriente = 250000
    caja_bancos = 20000
    inversiones_cp = 10000
    inventarios = 150000
    pasivo_total = 800000
    pasivo_corriente = 240000
    patrimonio = 200000
    
    print(f"  Activo Total: ${activo_total:,.0f}")
    print(f"  Activo Corriente: ${activo_corriente:,.0f}")
    print(f"  Pasivo Total: ${pasivo_total:,.0f}")
    print(f"  Patrimonio: ${patrimonio:,.0f}")
    
    # Datos del Estado de Resultados
    print("\n📈 ESTADO DE RESULTADOS:")
    ventas = 800000
    utilidad_neta = -50000  # Pérdida
    
    print(f"  Ventas: ${ventas:,.0f}")
    print(f"  Utilidad Neta: ${utilidad_neta:,.0f} (PÉRDIDA)")
    
    # RATIOS DE LIQUIDEZ
    print("\n💧 RATIOS DE LIQUIDEZ:")
    imprimir_ratio(
        "Ratio de Liquidez Corriente",
        ratio_liquidez(activo_corriente, pasivo_corriente)
    )
    imprimir_ratio(
        "Ratio de Prueba Ácida",
        ratio_prueba_acida(activo_corriente, inventarios, pasivo_corriente)
    )
    imprimir_ratio(
        "Ratio de Tesorería",
        ratio_tesoreria(caja_bancos, inversiones_cp, pasivo_corriente)
    )
    
    # RATIOS DE SOLVENCIA
    print("\n🏦 RATIOS DE SOLVENCIA:")
    imprimir_ratio(
        "Ratio de Endeudamiento",
        ratio_endeudamiento(pasivo_total, activo_total),
        "%"
    )
    imprimir_ratio(
        "Ratio de Apalancamiento",
        ratio_apalancamiento(activo_total, patrimonio),
        "veces"
    )
    
    # RATIOS DE RENTABILIDAD
    print("\n💰 RATIOS DE RENTABILIDAD:")
    imprimir_ratio(
        "Margen Neto",
        margen_neto(utilidad_neta, ventas),
        "%"
    )
    imprimir_ratio(
        "ROE (Rentabilidad sobre Patrimonio)",
        roe(utilidad_neta, patrimonio),
        "%"
    )
    imprimir_ratio(
        "ROA (Rentabilidad sobre Activos)",
        roa(utilidad_neta, activo_total),
        "%"
    )
    
    # RATIOS DE EFICIENCIA
    print("\n⚡ RATIOS DE EFICIENCIA OPERATIVA:")
    imprimir_ratio(
        "Rotación de Activos",
        rotacion_activos(ventas, activo_total),
        "veces"
    )
    
    print("\n⚠️ INTERPRETACIÓN:")
    print("  • Liquidez: CRÍTICA (ratio apenas > 1.0)")
    print("  • Endeudamiento: MUY ALTO (80% - RIESGO EXTREMO)")
    print("  • Rentabilidad: NEGATIVA (pérdidas)")
    print("  • Tesorería: INSUFICIENTE (0.13)")
    print("  • Apalancamiento: EXCESIVO (5x)")


if __name__ == "__main__":
    ejemplo_empresa_saludable()
    ejemplo_empresa_con_problemas()
    
    print("\n" + "=" * 70)
    print("📚 Estos ejemplos demuestran el uso completo del módulo de ratios")
    print("=" * 70 + "\n")
