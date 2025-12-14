"""
Tests unitarios para el módulo de ratios financieros.
"""

import unittest
from risk_engine.ratios import (
    ratio_liquidez,
    ratio_prueba_acida,
    ratio_endeudamiento,
    ratio_apalancamiento,
    margen_neto,
    roe,
    roa,
    rotacion_activos,
    ratio_tesoreria,
    rotacion_inventarios,
    dias_inventario,
    periodo_medio_cobro,
    periodo_medio_pago
)


class TestRatiosLiquidez(unittest.TestCase):
    """Tests para ratios de liquidez."""
    
    def test_ratio_liquidez_normal(self):
        """Prueba ratio de liquidez con valores normales."""
        resultado = ratio_liquidez(100000, 50000)
        self.assertEqual(resultado, 2.0)
    
    def test_ratio_liquidez_menor_uno(self):
        """Prueba cuando activos son menores que pasivos."""
        resultado = ratio_liquidez(75000, 100000)
        self.assertEqual(resultado, 0.75)
    
    def test_ratio_liquidez_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = ratio_liquidez(100000, 0)
        self.assertIsNone(resultado)
    
    def test_prueba_acida_normal(self):
        """Prueba ratio de prueba ácida con valores normales."""
        resultado = ratio_prueba_acida(100000, 30000, 50000)
        self.assertEqual(resultado, 1.4)
    
    def test_prueba_acida_exacto(self):
        """Prueba cuando activos líquidos igualan pasivos."""
        resultado = ratio_prueba_acida(80000, 20000, 60000)
        self.assertEqual(resultado, 1.0)
    
    def test_prueba_acida_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = ratio_prueba_acida(100000, 30000, 0)
        self.assertIsNone(resultado)


class TestRatiosSolvencia(unittest.TestCase):
    """Tests para ratios de solvencia y endeudamiento."""
    
    def test_ratio_endeudamiento_bajo(self):
        """Prueba endeudamiento bajo (saludable)."""
        resultado = ratio_endeudamiento(400000, 1000000)
        self.assertEqual(resultado, 0.4)
    
    def test_ratio_endeudamiento_alto(self):
        """Prueba endeudamiento alto (mayor riesgo)."""
        resultado = ratio_endeudamiento(700000, 1000000)
        self.assertEqual(resultado, 0.7)
    
    def test_ratio_endeudamiento_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = ratio_endeudamiento(100000, 0)
        self.assertIsNone(resultado)
    
    def test_ratio_apalancamiento_normal(self):
        """Prueba apalancamiento con valores normales."""
        resultado = ratio_apalancamiento(1000000, 600000)
        self.assertAlmostEqual(resultado, 1.6666666666666667)
    
    def test_ratio_apalancamiento_sin_deuda(self):
        """Prueba cuando no hay deuda (activos = patrimonio)."""
        resultado = ratio_apalancamiento(500000, 500000)
        self.assertEqual(resultado, 1.0)
    
    def test_ratio_apalancamiento_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = ratio_apalancamiento(1000000, 0)
        self.assertIsNone(resultado)


class TestRatiosRentabilidad(unittest.TestCase):
    """Tests para ratios de rentabilidad."""
    
    def test_margen_neto_normal(self):
        """Prueba margen neto con valores normales."""
        resultado = margen_neto(50000, 500000)
        self.assertEqual(resultado, 0.1)  # 10%
    
    def test_margen_neto_bajo(self):
        """Prueba margen neto bajo."""
        resultado = margen_neto(75000, 1000000)
        self.assertEqual(resultado, 0.075)  # 7.5%
    
    def test_margen_neto_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = margen_neto(50000, 0)
        self.assertIsNone(resultado)
    
    def test_roe_normal(self):
        """Prueba ROE con valores normales."""
        resultado = roe(120000, 600000)
        self.assertEqual(resultado, 0.2)  # 20%
    
    def test_roe_bajo(self):
        """Prueba ROE bajo."""
        resultado = roe(80000, 500000)
        self.assertEqual(resultado, 0.16)  # 16%
    
    def test_roe_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = roe(100000, 0)
        self.assertIsNone(resultado)
    
    def test_roa_normal(self):
        """Prueba ROA con valores normales."""
        resultado = roa(100000, 1000000)
        self.assertEqual(resultado, 0.1)  # 10%
    
    def test_roa_bajo(self):
        """Prueba ROA bajo."""
        resultado = roa(50000, 800000)
        self.assertEqual(resultado, 0.0625)  # 6.25%
    
    def test_roa_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = roa(100000, 0)
        self.assertIsNone(resultado)


class TestRatiosEficiencia(unittest.TestCase):
    """Tests para ratios de eficiencia operativa."""
    
    def test_rotacion_activos_alta(self):
        """Prueba rotación alta (eficiencia)."""
        resultado = rotacion_activos(2000000, 1000000)
        self.assertEqual(resultado, 2.0)
    
    def test_rotacion_activos_baja(self):
        """Prueba rotación baja."""
        resultado = rotacion_activos(800000, 1000000)
        self.assertEqual(resultado, 0.8)
    
    def test_rotacion_activos_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = rotacion_activos(1000000, 0)
        self.assertIsNone(resultado)


class TestValoresNegativos(unittest.TestCase):
    """Tests para validar comportamiento con valores negativos."""
    
    def test_utilidad_negativa_margen_neto(self):
        """Prueba margen neto con pérdidas."""
        resultado = margen_neto(-50000, 500000)
        self.assertEqual(resultado, -0.1)
    
    def test_utilidad_negativa_roe(self):
        """Prueba ROE con pérdidas."""
        resultado = roe(-30000, 600000)
        self.assertEqual(resultado, -0.05)
    
    def test_utilidad_negativa_roa(self):
        """Prueba ROA con pérdidas."""
        resultado = roa(-40000, 1000000)
        self.assertEqual(resultado, -0.04)


class TestRatioTesoreria(unittest.TestCase):
    """Tests para ratio de tesorería."""
    
    def test_ratio_tesoreria_normal(self):
        """Prueba ratio de tesorería con valores normales."""
        resultado = ratio_tesoreria(50000, 30000, 100000)
        self.assertEqual(resultado, 0.8)
    
    def test_ratio_tesoreria_mayor_uno(self):
        """Prueba cuando el disponible supera el pasivo corriente."""
        resultado = ratio_tesoreria(60000, 40000, 80000)
        self.assertEqual(resultado, 1.25)
    
    def test_ratio_tesoreria_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = ratio_tesoreria(50000, 30000, 0)
        self.assertIsNone(resultado)
    
    def test_ratio_tesoreria_sin_inversiones(self):
        """Prueba cuando solo hay caja y bancos."""
        resultado = ratio_tesoreria(80000, 0, 100000)
        self.assertEqual(resultado, 0.8)


class TestRotacionInventarios(unittest.TestCase):
    """Tests para rotación de inventarios."""
    
    def test_rotacion_inventarios_alta(self):
        """Prueba rotación alta de inventarios."""
        resultado = rotacion_inventarios(600000, 100000)
        self.assertEqual(resultado, 6.0)
    
    def test_rotacion_inventarios_baja(self):
        """Prueba rotación baja de inventarios."""
        resultado = rotacion_inventarios(480000, 120000)
        self.assertEqual(resultado, 4.0)
    
    def test_rotacion_inventarios_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = rotacion_inventarios(600000, 0)
        self.assertIsNone(resultado)


class TestDiasInventario(unittest.TestCase):
    """Tests para días promedio de inventario."""
    
    def test_dias_inventario_normal(self):
        """Prueba cálculo de días de inventario."""
        resultado = dias_inventario(365000, 100000)
        self.assertEqual(resultado, 100.0)
    
    def test_dias_inventario_rapida_rotacion(self):
        """Prueba con rotación rápida (menos días)."""
        resultado = dias_inventario(730000, 100000)
        self.assertEqual(resultado, 50.0)
    
    def test_dias_inventario_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = dias_inventario(0, 100000)
        self.assertIsNone(resultado)


class TestPeriodoMedioCobro(unittest.TestCase):
    """Tests para período medio de cobro."""
    
    def test_periodo_medio_cobro_normal(self):
        """Prueba cálculo de período medio de cobro."""
        resultado = periodo_medio_cobro(100000, 730000)
        self.assertEqual(resultado, 50.0)
    
    def test_periodo_medio_cobro_alto(self):
        """Prueba con período de cobro alto."""
        resultado = periodo_medio_cobro(150000, 1095000)
        self.assertAlmostEqual(resultado, 50.0, places=1)
    
    def test_periodo_medio_cobro_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = periodo_medio_cobro(100000, 0)
        self.assertIsNone(resultado)


class TestPeriodoMedioPago(unittest.TestCase):
    """Tests para período medio de pago."""
    
    def test_periodo_medio_pago_normal(self):
        """Prueba cálculo de período medio de pago."""
        resultado = periodo_medio_pago(80000, 584000)
        self.assertAlmostEqual(resultado, 50.0, places=1)
    
    def test_periodo_medio_pago_alto(self):
        """Prueba con período de pago alto."""
        resultado = periodo_medio_pago(120000, 876000)
        self.assertAlmostEqual(resultado, 50.0, places=1)
    
    def test_periodo_medio_pago_division_cero(self):
        """Prueba división entre cero retorna None."""
        resultado = periodo_medio_pago(80000, 0)
        self.assertIsNone(resultado)


if __name__ == '__main__':
    unittest.main()
