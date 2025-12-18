import unittest
from risk_engine.zscore import z_score
from risk_engine.classification import classify_risk

class TestZScore(unittest.TestCase):

    def test_zscore_normal(self):
        """Z-score con valores razonables."""
        z = z_score(
            working_capital=200000,
            retained_earnings=150000,
            ebit=120000,
            market_value_equity=500000,
            total_liabilities=300000,
            sales=800000,
            total_assets=1000000
        )
        # Z = 1.2×0.2 + 1.4×0.15 + 3.3×0.12 + 0.6×1.667 + 1.0×0.8
        # Z = 0.24 + 0.21 + 0.396 + 1.0 + 0.8 = 2.646
        self.assertAlmostEqual(z, 2.646, places=3)

    def test_zscore_low(self):
        """Z-score bajo, empresa en riesgo."""
        z = z_score(
            working_capital=10000,
            retained_earnings=5000,
            ebit=3000,
            market_value_equity=20000,
            total_liabilities=50000,
            sales=10000,
            total_assets=100000
        )
        # Z = 1.2×0.1 + 1.4×0.05 + 3.3×0.03 + 0.6×0.4 + 1.0×0.1
        # Z = 0.12 + 0.07 + 0.099 + 0.24 + 0.1 = 0.629
        self.assertAlmostEqual(z, 0.629, places=3)

    def test_zscore_zero_assets(self):
        """Si total_assets = 0 debe devolver None."""
        z = z_score(
            working_capital=10000,
            retained_earnings=5000,
            ebit=3000,
            market_value_equity=20000,
            total_liabilities=50000,
            sales=10000,
            total_assets=0
        )
        self.assertIsNone(z)

    def test_zscore_zero_liabilities(self):
        """Si total_liabilities = 0, evitar división por cero."""
        z = z_score(
            working_capital=200000,
            retained_earnings=150000,
            ebit=120000,
            market_value_equity=500000,
            total_liabilities=0,
            sales=800000,
            total_assets=1000000
        )
        self.assertIsNone(z)

    def test_zscore_negative_values(self):
        """Debe calcular aunque algunos valores sean negativos."""
        z = z_score(
            working_capital=-20000,
            retained_earnings=-50000,
            ebit=-10000,
            market_value_equity=50000,
            total_liabilities=30000,
            sales=20000,
            total_assets=150000
        )
        self.assertTrue(isinstance(z, float))


class TestZScoreClassification(unittest.TestCase):

    def test_high_risk_classification(self):
        self.assertEqual(
            classify_risk(1.5),
            "⚠️ Alto riesgo (posible quiebra)"
        )

    def test_medium_risk_classification(self):
        self.assertEqual(
            classify_risk(2.5),
            "🔶 Riesgo moderado (zona gris)"
        )

    def test_low_risk_classification(self):
        self.assertEqual(
            classify_risk(3.2),
            "🟢 Bajo riesgo (empresa sana)"
        )

    def test_classification_none(self):
        self.assertEqual(
            classify_risk(None),
            "Datos insuficientes"
        )


if __name__ == "__main__":
    unittest.main()
